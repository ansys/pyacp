from __future__ import annotations

from contextlib import ExitStack, closing
import copy
import importlib.resources
import os
import pathlib
import socket
import subprocess
import sys
import tempfile
import time
from types import MappingProxyType
from typing import Any, List, Mapping, Optional, TextIO, Tuple
import weakref

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore

import grpc
from grpc_health.v1.health_pb2 import HealthCheckRequest, HealthCheckResponse
from grpc_health.v1.health_pb2_grpc import HealthStub
import pydantic

from ansys.api.acp.v0.base_pb2 import Empty
from ansys.api.acp.v0.control_pb2_grpc import ControlStub
from ansys.utilities.local_instancemanager_server.helpers.direct import DirectLauncherBase
from ansys.utilities.local_instancemanager_server.helpers.grpc import check_grpc_health
from ansys.utilities.local_instancemanager_server.helpers.ports import find_free_ports
from ansys.utilities.local_instancemanager_server.interface import (
    LAUNCHER_CONFIG_T,
    LauncherProtocol,
)

from .._typing_helper import PATH as _PATH

__all__ = [
    "launch_acp",
    "launch_acp_docker",
    "launch_acp_docker_compose",
    "check_server",
    "shutdown_server",
    "wait_for_server",
    "LocalAcpServer",
    "RemoteAcpServer",
]


class ServerProtocol(Protocol):
    """Interface definition for ACP gRPC servers."""

    @property
    def channel(self) -> grpc.Channel:
        ...


class ServerHandleWrapper(ServerProtocol):
    def __init__(self, handle: LauncherProtocol[LAUNCHER_CONFIG_T]):
        self._handle = handle
        self._channel = grpc.insecure_channel(handle.url)

    @property
    def channel(self) -> grpc.Channel:
        return self._channel


def check_server(server: ServerProtocol, timeout: Optional[float] = None) -> bool:
    """Check if the server responds to health check requests.

    Send a single health check request to the server, and check if it
    responds.

    Parameters
    ----------
    server :
        The server to which the request is sent.
    timeout :
        Optional time in seconds to allow for the server to respond.

    Returns
    -------
    :
        If the server responds, ``True``, otherwise ``False``.
    """
    # try:
    #     res = HealthStub(server.channel).Check(
    #         request=HealthCheckRequest(),
    #         timeout=timeout,
    #     )
    #     if res.status == HealthCheckResponse.ServingStatus.SERVING:
    #         return True
    # except grpc.RpcError:
    #     pass
    # return False


def wait_for_server(server: ServerProtocol, timeout: float) -> None:
    """Wait for the server to respond.

    Repeatedly sends a health check request to the server, returning
    as soon as the server responds.

    Parameters
    ----------
    server :
        The server to which the requests are sent.
    timeout :
        Wait time before raising an exception.

    Raises
    ------
    RuntimeError :
        In case the server still has not responded after ``timeout`` seconds.
    """
    start_time = time.time()
    while time.time() - start_time <= timeout:
        if check_server(server, timeout=timeout / 3.0):
            break
        else:
            # Try again until the timeout is reached. We add a small
            # delay s.t. the server isn't bombarded with requests.
            time.sleep(timeout / 100)
    else:
        raise RuntimeError(f"The gRPC server is not serving requests after {timeout}s.")


def shutdown_server(server: ServerProtocol) -> None:
    """Shut down an ACP server via its Control interface.

    Parameters
    ----------
    server :
        The server to shut down.
    """
    ControlStub(server.channel).ShutdownServer(request=Empty())


# NOTE: Currently unused, but could be used with manually starting a server.
class RemoteAcpServer:
    def __init__(self, hostname: str, port: int):
        self._hostname = hostname
        self._port = port
        self._channel = None

    @property
    def channel(self) -> grpc.Channel:
        # TODO: implement secure channel
        if self._channel is None:
            self._channel = grpc.insecure_channel(f"{self._hostname}:{self._port}")
        return self._channel


class LocalAcpServer:
    """Manages an ACP server running on the local machine.

    Wrapper for ACP servers which run as a process on the local machine.
    This class takes care of terminating the process when the object is
    either destroyed, or before Python exits (unless it is a hard crash
    / kill).
    Can be used as a context manager, to terminate the process when
    exiting the context.

    Parameters
    ----------
    process :
        The process which is executing the ACP server.
    port :
        The port (on localhost) on which the ACP server listens to requests.
    stdout :
        Open file handle to which the process output is being written.
    stderr :
        Open file handle to which the process error is being written.
    """

    def __init__(
        self,
        process: subprocess.Popen[str],
        port: int,
        stdout: TextIO,
        stderr: TextIO,
    ):
        self._process = process
        self._port = port
        self._stdout = stdout
        self._stderr = stderr
        self._channel: Optional[grpc.Channel] = None

        self._finalizer = weakref.finalize(
            self,
            self._finalize_impl,
            process=self._process,
            stdout=self._stdout,
            stderr=self._stderr,
        )

    @staticmethod
    def _finalize_impl(process: subprocess.Popen[str], stdout: TextIO, stderr: TextIO) -> None:
        process.terminate()
        process.wait()
        stdout.close()
        stderr.close()

    def __enter__(self) -> LocalAcpServer:
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def close(self) -> None:
        self._finalizer()

    @property
    def closed(self) -> bool:
        return not self._finalizer.alive

    @property
    def channel(self) -> grpc.Channel:
        if self.closed:
            raise RuntimeError(
                "Cannot open channel to the server, since it has already been closed."
            )
        if self._channel is not None:
            return self._channel
        self._channel = grpc.insecure_channel(f"localhost:{self._port}")
        return self._channel


def launch_acp(
    binary_path: _PATH,
    port: Optional[int] = None,
    stdout_file: _PATH = os.devnull,
    stderr_file: _PATH = os.devnull,
) -> ServerProtocol:
    """Launch a local ACP server.

    Launch the ``acp_grpcserver`` executable on the local machine.

    Parameters
    ----------
    binary_path :
        Path to the ``acp_grpcserver`` executable.
    port :
        Port on which the server should listen to gRPC calls. If no port
        is given, a free port will be chosen automatically.
    stdout_file :
        Path of the file to which the server output is written.
    stderr_file :
        Path of the file to which the server error log is written.

    Returns
    -------
    :
        Server object which can be used to control the server, and
        instantiate objects on the server.
    """
    return ServerHandleWrapper(DirectAcpLauncher(config=DirectAcpConfig(binary_path=binary_path)))


class DirectAcpConfig(pydantic.BaseModel):
    binary_path: str


class DirectAcpLauncher(DirectLauncherBase[DirectAcpConfig]):
    CONFIG_MODEL = DirectAcpConfig

    def __init__(self, *, config: DirectAcpConfig):
        # TODO: fix
        port = None
        stdout_file = os.devnull
        stderr_file = os.devnull

        if port is None:
            port = find_free_ports()[0]

        stdout = open(stdout_file, mode="w", encoding="utf-8")
        stderr = open(stderr_file, mode="w", encoding="utf-8")
        process = subprocess.Popen(
            [
                config.binary_path,
                f"--server-address=0.0.0.0:{port}",
            ],
            stdout=stdout,
            stderr=stderr,
            text=True,
        )
        self._url = f"localhost:{port}"
        super().__init__(
            process=process,
            # port=port,
            stdout=stdout,
            stderr=stderr,
        )

    def check(self) -> bool:
        channel = grpc.insecure_channel(self.url)
        return check_grpc_health(
            channel=channel,
        )

    @property
    def url(self) -> str:
        return self._url


def launch_acp_docker(
    *,
    image_name: str = "ghcr.io/pyansys/pyacp-private:latest",
    license_server: str,
    mount_directories: Mapping[str, str] = MappingProxyType({}),
    port: Optional[int] = None,
    stdout_file: _PATH = os.devnull,
    stderr_file: _PATH = os.devnull,
) -> ServerProtocol:
    """Launch an ACP server locally in a Docker container.

    Use ``docker run`` to locally start an ACP Docker container.

    Parameters
    ----------
    image_name :
        The name of the Docker image to launch.
    license_server :
        The ``ANSYSLMD_LICENSE_FILE`` environment variable that is passed
        to the Docker container.
    mount_directories :
        Local directories which should be mounted to the Docker container.
        The keys contain the path in the context of the host, and the
        values are the paths as they should appear inside the container.
    stdout_file :
        Path (on the host) to which the output of ``docker run`` is redirected.
    stderr_file :
        Path (on the host) where the standard error of ``docker run`` is
        redirected.

    Returns
    -------
    :
        Server object which can be used to control the server, and
        instantiate objects on the server.
    """
    if port is None:
        port = find_free_ports()[0]
    stdout = open(stdout_file, mode="w", encoding="utf-8")
    stderr = open(stderr_file, mode="w", encoding="utf-8")
    cmd = ["docker", "run"]
    for source_dir, target_dir in mount_directories.items():
        cmd += [
            "-v",
            f"/{pathlib.Path(source_dir).resolve().as_posix().replace(':', '')}:{target_dir}",
        ]
    if sys.platform == "linux":
        cmd += ["-u", f"{os.getuid()}:{os.getgid()}"]
    cmd += [
        "-p",
        f"{port}:50051/tcp",
        "-e",
        f"ANSYSLMD_LICENSE_FILE={license_server}",
        "-e",
        "HOME=/home/container",
        image_name,
    ]
    process = subprocess.Popen(
        cmd,
        stdout=stdout,
        stderr=stderr,
        text=True,
    )
    return LocalAcpServer(process=process, port=port, stdout=stdout, stderr=stderr)


def launch_acp_docker_compose(
    *,
    image_name_pyacp: str = "ghcr.io/pyansys/pyacp-private:latest",
    image_name_filetransfer: str = "ghcr.io/ansys/utilities-filetransfer:latest",
    license_server: str,
    port_pyacp: Optional[int] = None,
    port_filetransfer: Optional[int] = None,
    stdout_file: _PATH = os.devnull,
    stderr_file: _PATH = os.devnull,
) -> Tuple[ServerProtocol, ServerProtocol]:
    try:
        import ansys.utilities.filetransfer
    except ImportError as err:
        raise ImportError(
            "The 'ansys.utilities.filetransfer' module is needed to launch ACP via docker-compose."
        ) from err

    with importlib.resources.path(__name__, "docker-compose.yaml") as compose_file:
        tmp_port_pyacp, tmp_port_filetransfer = find_free_ports(num_ports=2)
        if port_pyacp is None:
            port_pyacp = tmp_port_pyacp
        if port_filetransfer is None:
            port_filetransfer = tmp_port_filetransfer

        stdout = open(stdout_file, mode="w", encoding="utf-8")
        stderr = open(stderr_file, mode="w", encoding="utf-8")
        cmd = ["docker-compose", "-f", str(compose_file.resolve()), "up"]
        env = copy.copy(os.environ)
        env.update(
            dict(
                IMAGE_NAME_PYACP=image_name_pyacp,
                IMAGE_NAME_FILETRANSFER=image_name_filetransfer,
                ANSYSLMD_LICENSE_FILE=license_server,
                PORT_FILETRANSFER=str(port_filetransfer),
                PORT_PYACP=str(port_pyacp),
            )
        )
        process = subprocess.Popen(
            cmd,
            stdout=stdout,
            stderr=stderr,
            env=env,
            text=True,
        )
        server_pyacp = LocalAcpServer(
            process=process,
            port=port_pyacp,
            stdout=stdout,
            stderr=stderr,
        )
        server_filetransfer = RemoteAcpServer(hostname="localhost", port=port_filetransfer)

        # The compose_file may be temporary, in particular if the package is a zipfile.
        # To avoid it being deleted before docker-compose has read it, we wait for the
        # filetransfer server (which is faster since it doesn't need to check out a
        # license) to start.
        wait_for_server(server_filetransfer, timeout=10)
        return (server_pyacp, server_filetransfer)
