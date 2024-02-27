# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import dataclasses
import os
import subprocess
from typing import Optional, TextIO, Union

import grpc

from ansys.tools.local_product_launcher.helpers.grpc import check_grpc_health
from ansys.tools.local_product_launcher.helpers.ports import find_free_ports
from ansys.tools.local_product_launcher.interface import (
    METADATA_KEY_DOC,
    LauncherProtocol,
    ServerType,
)
from ansys.tools.path import get_available_ansys_installations

from .common import ServerKey

__all__ = ["DirectLaunchConfig"]


def _get_latest_ansys_installation() -> str:
    """Get the latest installed Ansys installation."""

    installations = get_available_ansys_installations()
    if not installations:
        raise ValueError("No Ansys installation found.")

    def sort_key(version_nr: int) -> Union[int, float]:
        # prefer regular over student installs
        if version_nr < 0:
            return abs(version_nr) - 0.5
        return version_nr

    latest_key = max(installations, key=sort_key)
    return installations[latest_key]


def _get_default_binary_path() -> str:
    try:
        ans_root = _get_latest_ansys_installation()
        binary_path = os.path.join(ans_root, "ACP", "acp_grpcserver")
        if os.name == "nt":
            binary_path += ".exe"
        return binary_path
    except (ValueError, FileNotFoundError):
        return ""


@dataclasses.dataclass
class DirectLaunchConfig:
    """Configuration options for launching ACP as a sub-process."""

    binary_path: str = dataclasses.field(
        default=_get_default_binary_path(),
        metadata={METADATA_KEY_DOC: "Path to the ACP gRPC server executable."},
    )
    stdout_file: str = dataclasses.field(
        default=os.devnull,
        metadata={METADATA_KEY_DOC: "File in which the server stdout is stored."},
    )
    stderr_file: str = dataclasses.field(
        default=os.devnull,
        metadata={METADATA_KEY_DOC: "File in which the server stderr is stored."},
    )


class DirectLauncher(LauncherProtocol[DirectLaunchConfig]):
    CONFIG_MODEL = DirectLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC}

    def __init__(self, *, config: DirectLaunchConfig):
        self._config = config
        self._url: str
        self._process: subprocess.Popen[str]
        self._stdout: TextIO
        self._stderr: TextIO

    def start(self) -> None:
        # TODO: implement patterns
        stdout_file = self._config.stdout_file
        stderr_file = self._config.stderr_file

        port = find_free_ports()[0]
        self._url = f"localhost:{port}"
        self._stdout = open(stdout_file, mode="w", encoding="utf-8")
        self._stderr = open(stderr_file, mode="w", encoding="utf-8")
        self._process = subprocess.Popen(
            [
                self._config.binary_path,
                f"--server-address=0.0.0.0:{port}",
            ],
            stdout=self._stdout,
            stderr=self._stderr,
            text=True,
        )

    def stop(self, *, timeout: Optional[float] = None) -> None:
        self._process.terminate()
        try:
            self._process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            self._process.kill()
            self._process.wait()
        self._stdout.close()
        self._stderr.close()

    def check(self, timeout: Optional[float] = None) -> bool:
        channel = grpc.insecure_channel(self.urls[ServerKey.MAIN])
        return check_grpc_health(channel=channel, timeout=timeout)

    @property
    def urls(self) -> dict[str, str]:
        return {ServerKey.MAIN: self._url}
