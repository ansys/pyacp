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
import pathlib

import grpc

from ansys.tools.local_product_launcher.helpers.grpc import check_grpc_health
from ansys.tools.local_product_launcher.interface import (
    METADATA_KEY_DOC,
    LauncherProtocol,
    ServerType,
)
from ansys.tools.local_product_launcher.grpc_transport import TransportOptions, UDSOptions, WNUAOptions, MTLSOptions, InsecureOptions

from .common import ServerKey

__all__ = ["ConnectLaunchConfig", "ConnectLocalLaunchConfig"]


@dataclasses.dataclass(kw_only=True)
class ConnectLaunchConfig:
    """Configuration options for attaching to an existing ACP server."""
    acp_transport_mode: str = dataclasses.field(
        default="mtls",
        metadata={METADATA_KEY_DOC: "gRPC transport mode to use."},
    )
    acp_host: str = dataclasses.field(
        default="localhost",
        metadata={METADATA_KEY_DOC: "Host to connect to for the main ACP server."},
    )
    acp_port: int = dataclasses.field(
        default=50555,
        metadata={METADATA_KEY_DOC: "Port to connect to for the main ACP server."
    },
    )
    acp_uds_dir: str | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={METADATA_KEY_DOC: "Directory for Unix Domain Sockets to connect to ACP. Only used if acp_transport_mode is 'uds'."},
    )
    acp_uds_id : str | None = dataclasses.field(
        default=None,
        metadata={METADATA_KEY_DOC: "Identifier for the Unix Domain Socket to connect to ACP. Only used if acp_transport_mode is 'uds'."},
    )
    acp_certs_dir: str  | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={METADATA_KEY_DOC: "Directory containing TLS certificates for ACP. Only used if acp_transport_mode is 'mtls'."},
    )
    acp_allow_remote_host: bool = dataclasses.field(
        default=False,
        metadata={METADATA_KEY_DOC: "Whether to allow connecting to a remote host for the main ACP server."},
    )

    filetransfer_transport_mode: str = dataclasses.field(
        default="mtls",
        metadata={METADATA_KEY_DOC: "gRPC transport mode to use for file transfer."},
    )
    filetransfer_host: str = dataclasses.field(
        default="localhost",
        metadata={METADATA_KEY_DOC: "Host to connect to for the file transfer server."},
    )
    filetransfer_port: int = dataclasses.field(
        default=50556,
        metadata={METADATA_KEY_DOC: "Port to connect to for the file transfer server."},
    )
    filetransfer_uds_dir: str | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={METADATA_KEY_DOC: "Directory for Unix Domain Sockets to connect to file transfer. Only used if filetransfer_transport_mode is 'uds'."},
    )
    filetransfer_uds_id: str | None = dataclasses.field(
        default=None,
        metadata={METADATA_KEY_DOC: "Identifier for the Unix Domain Socket to connect to file transfer. Only used if filetransfer_transport_mode is 'uds'."},
    )
    filetransfer_certs_dir: str  | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={METADATA_KEY_DOC: "Directory containing TLS certificates for file transfer. Only used if filetransfer_transport_mode is 'mtls'."},
    )
    filetransfer_allow_remote_host: bool = dataclasses.field(
        default=False,
        metadata={METADATA_KEY_DOC: "Whether to allow connecting to a remote host for the file transfer server."},
    )


class ConnectLauncher(LauncherProtocol[ConnectLaunchConfig]):
    CONFIG_MODEL = ConnectLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC, ServerKey.FILE_TRANSFER: ServerType.GRPC}

    def __init__(self, *, config: ConnectLaunchConfig):
        self._config = config

        if self._config.acp_transport_mode == "uds":
            acp_options = UDSOptions(
                uds_service="acp_grpcserver",
                uds_dir=self._config.acp_uds_dir,
                uds_id=self._config.acp_uds_id,
            )
        elif self._config.acp_transport_mode == "wnua":
            acp_options = WNUAOptions(
                port=self._config.acp_port,
            )
        elif self._config.acp_transport_mode == "mtls":
            acp_options = MTLSOptions(
                certs_dir=self._config.acp_certs_dir,
                host=self._config.acp_host,
                port=self._config.acp_port,
                allow_remote_host=self._config.acp_allow_remote_host,
            )
        elif self._config.acp_transport_mode == "insecure":
            acp_options = InsecureOptions(
                host=self._config.acp_host,
                port=self._config.acp_port,
                allow_remote_host=self._config.acp_allow_remote_host,
            )
        else:
            raise ValueError(f"Invalid transport mode for ACP: {self._config.acp_transport_mode}")

        if self._config.filetransfer_transport_mode == "uds":
            filetransfer_options = UDSOptions(
                uds_service="filetransfer_grpcserver",
                uds_dir=self._config.filetransfer_uds_dir,
                uds_id=self._config.filetransfer_uds_id,
            )
        elif self._config.filetransfer_transport_mode == "mtls":
            filetransfer_options = MTLSOptions(
                certs_dir=self._config.filetransfer_certs_dir,
                host=self._config.filetransfer_host,
                port=self._config.filetransfer_port,
                allow_remote_host=self._config.filetransfer_allow_remote_host,
            )
        elif self._config.filetransfer_transport_mode == "insecure":
            filetransfer_options = InsecureOptions(
                host=self._config.filetransfer_host,
                port=self._config.filetransfer_port,
                allow_remote_host=self._config.filetransfer_allow_remote_host,
            )
        else:
            raise ValueError(f"Invalid transport mode for filetransfer: {self._config.filetransfer_transport_mode}")

        self._acp_transport_options = TransportOptions(
            mode=self._config.acp_transport_mode,
            options=acp_options,
        )
        self._filetransfer_transport_options = TransportOptions(
            mode=self._config.filetransfer_transport_mode,
            options=filetransfer_options,
        )


    def start(self) -> None:
        # Since this launcher simply connects to an existing server, we don't need to start it.
        return

    def stop(self, *, timeout: float | None = None) -> None:
        # Since this launcher simply connects to an existing server, we don't need to stop it.
        return

    def check(self, timeout: float | None = None) -> bool:
        for transport_opt in self.transport_options.values():
            channel = transport_opt.to_channel()
            if not check_grpc_health(channel=channel, timeout=timeout):
                return False
        return True

    @property
    def transport_options(self) -> dict[str, TransportOptions]:
        return {
            ServerKey.MAIN: self._acp_transport_options,
            ServerKey.FILE_TRANSFER: self._filetransfer_transport_options,
        }


@dataclasses.dataclass
class ConnectLocalLaunchConfig:
    """Configuration options for attaching to an existing ACP server without filetransfer."""

    url_acp: str = dataclasses.field(
        metadata={METADATA_KEY_DOC: "URL to connect to for the main ACP server."},
    )


class ConnectLocalLauncher(LauncherProtocol[ConnectLocalLaunchConfig]):
    CONFIG_MODEL = ConnectLocalLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC}

    def __init__(self, *, config: ConnectLocalLaunchConfig):
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
        }
