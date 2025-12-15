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

from ansys.tools.common.launcher.grpc_transport import (
    InsecureOptions,
    MTLSOptions,
    TransportOptionsType,
    UDSOptions,
    WNUAOptions,
)
from ansys.tools.common.launcher.helpers.grpc import check_grpc_health
from ansys.tools.common.launcher.interface import (
    METADATA_KEY_DOC,
    LauncherProtocol,
    ServerType,
)

from .common import ServerKey

__all__ = ["ConnectLaunchConfig", "ConnectLocalLaunchConfig"]


@dataclasses.dataclass(kw_only=True)
class ConnectLaunchConfig:
    """Configuration options for attaching to an existing ACP server."""

    acp_transport_mode: str = dataclasses.field(
        default="mtls",
        metadata={
            METADATA_KEY_DOC: "Specifies the gRPC transport mode to use for the main ACP server. "
            "Possible values: 'mtls' (default), 'uds' (Unix only), 'wnua' (Windows only), 'insecure'."
        },
    )
    """Specifies the gRPC transport mode to use for the main ACP server.

    Possible values are:

    - ``"mtls"`` : Mutual TLS (default)
    - ``"uds"`` : Unix Domain Sockets (unsupported on Windows)
    - ``"wnua"`` : Windows Named User Authentication (unsupported on Unix)
    - ``"insecure"`` : Insecure TCP connection (not recommended)
    """

    acp_host: str = dataclasses.field(
        default="localhost",
        metadata={
            METADATA_KEY_DOC: "Hostname or IP address to connect to for the main ACP server."
        },
    )
    """Hostname or IP address to connect to for the main ACP server."""

    acp_port: int = dataclasses.field(
        default=50555,
        metadata={METADATA_KEY_DOC: "Port number to connect to for the main ACP server."},
    )
    """Port number to connect to for the main ACP server."""

    acp_uds_dir: str | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: (
                "Directory path for UDS socket files used by the main ACP server (default: ~/.conn). "
                "Only used if acp_transport_mode is 'uds'."
            )
        },
    )
    """
    Directory path for UDS socket files used by the main ACP server.

    Defaults to ``~/.conn``. Only used if ``acp_transport_mode`` is ``"uds"``.
    """

    acp_uds_id: str | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: "Optional ID for UDS socket file naming for the main ACP server "
            "(acp_grpcserver-<id>.sock). Only used if acp_transport_mode is 'uds'."
        },
    )
    """
    Optional ID for UDS socket file naming for the main ACP server (acp_grpcserver-<id>.sock).
    Only used if ``acp_transport_mode`` is ``"uds"``.
    """

    acp_certs_dir: str | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: "Directory path for mTLS certificate files for the main ACP server. "
            "Only used if acp_transport_mode is 'mtls'."
        },
    )
    """Directory path for mTLS certificate files for the main ACP server.

    Defaults to the ``ANSYS_GRPC_CERTIFICATES`` environment variable, or ``certs`` if the variable is not set.
    Only used if ``acp_transport_mode`` is ``"mtls"``.
    """

    acp_allow_remote_host: bool = dataclasses.field(
        default=False,
        metadata={
            METADATA_KEY_DOC: "Whether to allow connecting to a remote host for the main ACP server."
        },
    )
    """Whether to allow connecting to a remote host for the main ACP server."""

    filetransfer_transport_mode: str = dataclasses.field(
        default="mtls",
        metadata={
            METADATA_KEY_DOC: "Specifies the gRPC transport mode to use. "
            "Possible values: 'mtls' (default), 'uds', 'insecure'."
        },
    )
    """Specifies the gRPC transport mode to use for the file transfer server.

    Possible values are:

    - ``"mtls"`` : Mutual TLS (default)
    - ``"uds"`` : Unix Domain Sockets (unsupported on Windows)
    - ``"insecure"`` : Insecure TCP connection (not recommended)
    """

    filetransfer_host: str = dataclasses.field(
        default="localhost",
        metadata={METADATA_KEY_DOC: "Host to connect to for the file transfer server."},
    )
    """Hostname or IP address to connect to for the file transfer server."""

    filetransfer_port: int = dataclasses.field(
        default=50556,
        metadata={METADATA_KEY_DOC: "Port to connect to for the file transfer server."},
    )
    """Port number to connect to for the file transfer server."""

    filetransfer_uds_dir: str | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: (
                "Directory path for UDS socket files used by the filetransfer server (default: ~/.conn). "
                "Only used if acp_transport_mode is 'uds'."
            )
        },
    )
    """
    Directory path for UDS socket files used by the filetransfer server.

    Defaults to ``~/.conn``. Only used if ``filetransfer_transport_mode`` is ``"uds"``.
    """

    filetransfer_uds_id: str | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: "Optional ID for UDS socket file naming for the filetransfer server "
            "(filetransfer_grpcserver-<id>.sock). Only used if filetransfer_transport_mode is 'uds'."
        },
    )
    """
    Optional ID for UDS socket file naming for the filetransfer server (filetransfer_grpcserver-<id>.sock).
    Only used if ``filetransfer_transport_mode`` is ``"uds"``.
    """

    filetransfer_certs_dir: str | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: "Directory containing TLS certificates for file transfer. "
            "Only used if filetransfer_transport_mode is 'mtls'."
        },
    )
    """Directory path for mTLS certificate files for the filetransfer server.

    Defaults to the ``ANSYS_GRPC_CERTIFICATES`` environment variable, or ``certs`` if the variable is not set.
    Only used if ``filetransfer_transport_mode`` is ``"mtls"``.
    """

    filetransfer_allow_remote_host: bool = dataclasses.field(
        default=False,
        metadata={
            METADATA_KEY_DOC: "Whether to allow connecting to a remote host for the file transfer server."
        },
    )
    """Whether to allow connecting to a remote host for the filetransfer server."""


class ConnectLauncher(LauncherProtocol[ConnectLaunchConfig]):
    CONFIG_MODEL = ConnectLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC, ServerKey.FILE_TRANSFER: ServerType.GRPC}

    def __init__(self, *, config: ConnectLaunchConfig):
        self._config = config

        if self._config.acp_transport_mode == "uds":
            acp_transport_options: TransportOptionsType = UDSOptions(
                uds_service="acp_grpcserver",
                uds_dir=self._config.acp_uds_dir,
                uds_id=self._config.acp_uds_id,
            )
        elif self._config.acp_transport_mode == "wnua":
            acp_transport_options = WNUAOptions(
                port=self._config.acp_port,
            )
        elif self._config.acp_transport_mode == "mtls":
            acp_transport_options = MTLSOptions(
                certs_dir=self._config.acp_certs_dir,
                host=self._config.acp_host,
                port=self._config.acp_port,
                allow_remote_host=self._config.acp_allow_remote_host,
            )
        elif self._config.acp_transport_mode == "insecure":
            acp_transport_options = InsecureOptions(
                host=self._config.acp_host,
                port=self._config.acp_port,
                allow_remote_host=self._config.acp_allow_remote_host,
            )
        else:
            raise ValueError(f"Invalid transport mode for ACP: {self._config.acp_transport_mode}")

        if self._config.filetransfer_transport_mode == "uds":
            filetransfer_transport_options: UDSOptions | MTLSOptions | InsecureOptions = UDSOptions(
                uds_service="filetransfer_grpcserver",
                uds_dir=self._config.filetransfer_uds_dir,
                uds_id=self._config.filetransfer_uds_id,
            )
        elif self._config.filetransfer_transport_mode == "mtls":
            filetransfer_transport_options = MTLSOptions(
                certs_dir=self._config.filetransfer_certs_dir,
                host=self._config.filetransfer_host,
                port=self._config.filetransfer_port,
                allow_remote_host=self._config.filetransfer_allow_remote_host,
            )
        elif self._config.filetransfer_transport_mode == "insecure":
            filetransfer_transport_options = InsecureOptions(
                host=self._config.filetransfer_host,
                port=self._config.filetransfer_port,
                allow_remote_host=self._config.filetransfer_allow_remote_host,
            )
        else:
            raise ValueError(
                f"Invalid transport mode for filetransfer: {self._config.filetransfer_transport_mode}"
            )

        self._acp_transport_options = acp_transport_options
        self._filetransfer_transport_options = filetransfer_transport_options

    def start(self) -> None:
        # Since this launcher simply connects to an existing server, we don't need to start it.
        return

    def stop(self, *, timeout: float | None = None) -> None:
        # Since this launcher simply connects to an existing server, we don't need to stop it.
        return

    def check(self, timeout: float | None = None) -> bool:
        for transport_opt in self.transport_options.values():
            channel = transport_opt.create_channel()
            if not check_grpc_health(channel=channel, timeout=timeout):
                return False
        return True

    @property
    def transport_options(self) -> dict[str, TransportOptionsType]:
        return {
            ServerKey.MAIN: self._acp_transport_options,
            ServerKey.FILE_TRANSFER: self._filetransfer_transport_options,
        }


@dataclasses.dataclass
class ConnectLocalLaunchConfig:
    """Configuration options for attaching to an existing ACP server without filetransfer."""

    transport_mode: str = dataclasses.field(
        default="mtls",
        metadata={
            METADATA_KEY_DOC: "Specifies the gRPC transport mode to use."
            "Possible values: 'mtls' (default), 'uds' (Unix only), 'wnua' (Windows only), 'insecure'."
        },
    )
    """Specifies the gRPC transport mode to use.

    Possible values are:
    - ``"mtls"`` : Mutual TLS (default)
    - ``"uds"`` : Unix Domain Sockets (unsupported on Windows)
    - ``"wnua"`` : Windows Named User Authentication (unsupported on Unix)
    - ``"insecure"`` : Insecure TCP connection (not recommended)
    """

    host: str = dataclasses.field(
        default="localhost",
        metadata={METADATA_KEY_DOC: "Hostname or IP to connect to."},
    )
    """Hostname or IP to connect to."""

    port: int = dataclasses.field(
        default=50555,
        metadata={METADATA_KEY_DOC: "Port number to connect to."},
    )
    """Port number to connect to."""

    uds_dir: str | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: (
                "Directory path for UDS socket files (default: ~/.conn). "
                "Only used if transport_mode is 'uds'."
            )
        },
    )
    """Directory path for UDS socket files.

    Defaults to ``~/.conn``. Only used if ``transport_mode`` is ``"uds"``.
    """

    uds_id: str | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: "Optional ID for UDS socket file naming (acp_grpcserver-<id>.sock). "
            "Only used if transport_mode is 'uds'."
        },
    )
    """
    Optional ID for UDS socket file naming (acp_grpcserver-<id>.sock).
    Only used if ``transport_mode`` is ``"uds"``.
    """

    certs_dir: str | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: "Directory path for mTLS certificate files. "
            "Only used if transport_mode is 'mtls'."
        },
    )
    """Directory path for mTLS certificate files.

    Defaults to the ``ANSYS_GRPC_CERTIFICATES`` environment variable, or ``certs`` if the variable is not set.
    Only used if ``transport_mode`` is ``"mtls"``.
    """

    allow_remote_host: bool = dataclasses.field(
        default=False,
        metadata={METADATA_KEY_DOC: "Whether to allow connecting to a remote host."},
    )
    """Whether to allow connecting to a remote host."""


class ConnectLocalLauncher(LauncherProtocol[ConnectLocalLaunchConfig]):
    CONFIG_MODEL = ConnectLocalLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC}

    def __init__(self, *, config: ConnectLocalLaunchConfig):
        self._config = config
        if self._config.transport_mode == "uds":
            acp_transport_options: TransportOptionsType = UDSOptions(
                uds_service="acp_grpcserver",
                uds_dir=self._config.uds_dir,
                uds_id=self._config.uds_id,
            )
        elif self._config.transport_mode == "wnua":
            acp_transport_options = WNUAOptions(
                port=self._config.port,
            )
        elif self._config.transport_mode == "mtls":
            acp_transport_options = MTLSOptions(
                certs_dir=self._config.certs_dir,
                host=self._config.host,
                port=self._config.port,
                allow_remote_host=self._config.allow_remote_host,
            )
        elif self._config.transport_mode == "insecure":
            acp_transport_options = InsecureOptions(
                host=self._config.host,
                port=self._config.port,
                allow_remote_host=self._config.allow_remote_host,
            )
        else:
            raise ValueError(f"Invalid transport mode for ACP: {self._config.transport_mode}")

        self._acp_transport_options = acp_transport_options

    def start(self) -> None:
        # Since this launcher simply connects to an existing server, we don't need to start it.
        return

    def stop(self, *, timeout: float | None = None) -> None:
        # Since this launcher simply connects to an existing server, we don't need to stop it.
        return

    def check(self, timeout: float | None = None) -> bool:
        for transport_opt in self.transport_options.values():
            channel = transport_opt.create_channel()
            if not check_grpc_health(channel=channel, timeout=timeout):
                return False
        return True

    @property
    def transport_options(self) -> dict[str, TransportOptionsType]:
        return {
            ServerKey.MAIN: self._acp_transport_options,
        }
