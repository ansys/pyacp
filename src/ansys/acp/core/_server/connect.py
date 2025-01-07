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

from __future__ import annotations

import dataclasses

import grpc

from ansys.tools.local_product_launcher.helpers.grpc import check_grpc_health
from ansys.tools.local_product_launcher.interface import (
    METADATA_KEY_DOC,
    LauncherProtocol,
    ServerType,
)

from .common import ServerKey

__all__ = ["ConnectLaunchConfig"]


@dataclasses.dataclass
class ConnectLaunchConfig:
    """Configuration options for attaching to an existing ACP server."""

    url_acp: str = dataclasses.field(
        default="localhost:50555",
        metadata={METADATA_KEY_DOC: "URL to connect to for the main ACP server."},
    )
    url_filetransfer: str = dataclasses.field(
        default="localhost:50556",
        metadata={METADATA_KEY_DOC: "URL to connect to for the file transfer server."},
    )


class ConnectLauncher(LauncherProtocol[ConnectLaunchConfig]):
    CONFIG_MODEL = ConnectLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC, ServerKey.FILE_TRANSFER: ServerType.GRPC}

    def __init__(self, *, config: ConnectLaunchConfig):
        self._config = config

    def start(self) -> None:
        # Since this launcher simply connects to an existing server, we don't need to start it.
        return

    def stop(self, *, timeout: float | None = None) -> None:
        # Since this launcher simply connects to an existing server, we don't need to stop it.
        return

    def check(self, timeout: float | None = None) -> bool:
        channel = grpc.insecure_channel(self.urls[ServerKey.MAIN])
        return check_grpc_health(channel=channel, timeout=timeout)

    @property
    def urls(self) -> dict[str, str]:
        return {
            ServerKey.MAIN: self._config.url_acp,
            ServerKey.FILE_TRANSFER: self._config.url_filetransfer,
        }
