from __future__ import annotations

import os
import pathlib
import socket
import subprocess
import weakref
from contextlib import closing
from typing import Any
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

__all__ = ["launch_acp", "LocalAcpServer"]

_FILE = Union[str, pathlib.Path]


class ServerProtocol(Protocol):
    def __enter__(self) -> ServerProtocol:
        ...

    def __exit__(self, *exc: Any) -> None:
        ...

    def close(self) -> None:
        ...

    @property
    def closed(self) -> bool:
        ...

    def check(self, timeout: Optional[float] = None) -> bool:
        ...

    @property
    def channel(self) -> grpc.Channel:
        ...


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

    def check(self, timeout: Optional[float] = None) -> bool:
        try:
            res = HealthStub(self.channel).Check(
                request=HealthCheckRequest(),
                timeout=timeout,
            )
            if res.status == HealthCheckResponse.ServingStatus.SERVING:
                return True
        except grpc.RpcError:
            pass
        return False

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
    server = LocalAcpServer(process=process, port=port, stdout=stdout, stderr=stderr)
    return server


def _find_free_port() -> int:
    """Find a free port on localhost.

    Note that there is a race condition between finding the free port
    here, and binding to it from the gRPC server.
    """
    with closing(socket.socket()) as sock:
        sock.bind(("", 0))  # bind to a free port
        return sock.getsockname()[1]  # type: ignore
