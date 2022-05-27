from __future__ import annotations

import os
import pathlib
import socket
import subprocess
import sys
import time
import weakref
from contextlib import closing
from types import MappingProxyType
from typing import Any
from typing import Mapping
from typing import Optional
from typing import TextIO
from typing import Union

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore

import grpc
from grpc_health.v1.health_pb2 import HealthCheckRequest
from grpc_health.v1.health_pb2 import HealthCheckResponse
from grpc_health.v1.health_pb2_grpc import HealthStub

from ansys.api.acp.v0.base_pb2 import Empty
from ansys.api.acp.v0.control_pb2_grpc import ControlStub

__all__ = [
    "launch_acp",
    "launch_acp_docker",
    "check_server",
    "shutdown_server",
    "wait_for_server" "LocalAcpServer",
    "RemoteAcpServer",
]

_FILE = Union[str, pathlib.Path]


class ServerProtocol(Protocol):
    @property
    def channel(self) -> grpc.Channel:
        ...


def check_server(server: ServerProtocol, timeout: Optional[float] = None) -> bool:
    try:
        res = HealthStub(server.channel).Check(
            request=HealthCheckRequest(),
            timeout=timeout,
        )
        if res.status == HealthCheckResponse.ServingStatus.SERVING:
            return True
    except grpc.RpcError:
        pass
    return False


def wait_for_server(server: ServerProtocol, timeout: float) -> None:
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
    ControlStub(server.channel).ShutdownServer(request=Empty())


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
    def __init__(self, process: subprocess.Popen[str], port: int, stdout: TextIO, stderr: TextIO):
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
    binary_path: _FILE,
    port: Optional[int] = None,
    stdout_file: _FILE = os.devnull,
    stderr_file: _FILE = os.devnull,
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
    if port is None:
        port = _find_free_port()
    stdout = open(stdout_file, mode="w", encoding="utf-8")
    stderr = open(stderr_file, mode="w", encoding="utf-8")
    process = subprocess.Popen(
        [
            binary_path,
            f"--server-address=0.0.0.0:{port}",
        ],
        stdout=stdout,
        stderr=stderr,
        text=True,
    )
    return LocalAcpServer(process=process, port=port, stdout=stdout, stderr=stderr)


def launch_acp_docker(
    *,
    image_name: str = "ghcr.io/pyansys/pyacp-private:latest",
    license_server: str,
    mount_directories: Mapping[str, str] = MappingProxyType({}),
    port: Optional[int] = None,
    stdout_file: _FILE = os.devnull,
    stderr_file: _FILE = os.devnull,
) -> ServerProtocol:
    """Launch an ACP server locally in a Docker container."""
    if port is None:
        port = _find_free_port()
    stdout = open(stdout_file, mode="w", encoding="utf-8")
    stderr = open(stderr_file, mode="w", encoding="utf-8")
    cmd = ["docker", "run"]
    for source_dir, target_dir in mount_directories.items():
        cmd += ["-v", f"/{pathlib.Path(source_dir).as_posix().replace(':', '')}:{target_dir}"]
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


def _find_free_port() -> int:
    """Find a free port on localhost.

    .. note::

        There is no guarantee that the port is *still* free when it is
        used by the calling code.
    """
    with closing(socket.socket()) as sock:
        sock.bind(("", 0))  # bind to a free port
        return sock.getsockname()[1]  # type: ignore
