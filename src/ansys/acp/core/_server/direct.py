# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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
import pathlib
import subprocess  # nosec B404
from typing import TextIO
import uuid

from ansys.tools.local_product_launcher.helpers.grpc import check_grpc_health
from ansys.tools.local_product_launcher.helpers.ports import find_free_ports
from ansys.tools.local_product_launcher.interface import (
    METADATA_KEY_DOC,
    LauncherProtocol,
    ServerType,
)
from ansys.tools.local_product_launcher.grpc_transport import TransportOptions, UDSOptions, WNUAOptions, MTLSOptions, InsecureOptions
from ansys.tools.path import get_latest_ansys_installation

from .common import ServerKey

__all__ = ["DirectLaunchConfig"]

_GRPC_MAX_MESSAGE_LENGTH = 256 * 1024**2  # 256 MB


def _get_default_binary_path() -> str:
    try:
        _, ans_root = get_latest_ansys_installation()
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
    transport_mode: str = dataclasses.field(
        default="wnua" if os.name == "nt" else "uds",
        metadata={METADATA_KEY_DOC: "gRPC transport mode to use."},
    )
    uds_dir: str | None = dataclasses.field(
        default=None,
        metadata={METADATA_KEY_DOC: "Directory for Unix Domain Sockets. Only used if transport_mode is 'uds'."},
    )
    certs_dir: str | None = dataclasses.field(
        default=None,
        metadata={METADATA_KEY_DOC: "Directory containing TLS certificates. Only used if transport_mode is 'mtls'."},
    )


class DirectLauncher(LauncherProtocol[DirectLaunchConfig]):
    CONFIG_MODEL = DirectLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC}

    def __init__(self, *, config: DirectLaunchConfig):
        self._config = config
        self._process: subprocess.Popen[str] | None = None
        self._stdout: TextIO
        self._stderr: TextIO
        self._url: str
        self._transport_options: TransportOptions

    def start(self) -> None:
        # TODO: implement patterns
        stdout_file = self._config.stdout_file
        stderr_file = self._config.stderr_file

        binary = pathlib.Path(self._config.binary_path)
        if not binary.exists():
            raise FileNotFoundError(f"Binary not found: '{binary}'")

        if self._config.transport_mode == "uds":
            if os.name == "nt":
                raise RuntimeError("UDS transport mode is not supported on Windows.")
            uds_id = uuid.uuid4().hex
            transport_args = [
                "--transport-mode=uds",
                f"--uds-id={uds_id}",
            ]
            if self._config.uds_dir is not None:
                transport_args.append(f"--uds-dir={self._config.uds_dir}")

            self._transport_options = TransportOptions(
                mode="uds",
                options=UDSOptions(
                    uds_service="acp_grpcserver",
                    uds_dir=self._config.uds_dir,
                    uds_id=uds_id,
                ),
            )
        else:
            port = find_free_ports()[0]
            if self._config.transport_mode == "wnua":
                if os.name != "nt":
                    raise RuntimeError("WNUA transport mode is only supported on Windows.")
                transport_args = [
                    "--transport-mode=wnua",
                    f"--port={port}",
                ]
                self._transport_options = TransportOptions(
                    mode="wnua",
                    options=WNUAOptions(
                        port=port
                    ),
                )
            elif self._config.transport_mode == "mtls":
                transport_args = [
                    "--transport-mode=mtls",
                    "--host=localhost",
                    f"--port={port}",
                ]
                if self._config.certs_dir is not None:
                    transport_args.extend(["--certs-dir", self._config.certs_dir])
                self._transport_options = TransportOptions(
                    mode="mtls",
                    options=MTLSOptions(
                        certs_dir=self._config.certs_dir,
                        host="localhost",
                        port=port,
                        allow_remote_host=False,
                    ),
                )
            elif self._config.transport_mode == "insecure":
                transport_args = [
                    "--transport-mode=insecure",
                    "--host=localhost",
                    f"--port={port}",
                ]
                self._transport_options = TransportOptions(
                    mode="insecure",
                    options=InsecureOptions(
                        host="localhost",
                        port=port,
                    ),
                )


        self._stdout = open(stdout_file, mode="w", encoding="utf-8")
        self._stderr = open(stderr_file, mode="w", encoding="utf-8")
        self._process = subprocess.Popen(  # nosec B603: documented in 'security_considerations.rst'
            [
                self._config.binary_path,
            ] + transport_args,
            stdout=self._stdout,
            stderr=self._stderr,
            text=True,
        )

    def stop(self, *, timeout: float | None = None) -> None:
        if self._process is None:
            # The process has not been started, and therefore doesn't need to be stopped
            return
        self._process.terminate()
        try:
            self._process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            self._process.kill()
            self._process.wait()
        self._stdout.close()
        self._stderr.close()

    def check(self, timeout: float | None = None) -> bool:
        channel = self._transport_options.to_channel()
        return check_grpc_health(channel=channel, timeout=timeout)

    @property
    def transport_options(self) -> TransportOptions:
        return {ServerKey.MAIN: self._transport_options}
