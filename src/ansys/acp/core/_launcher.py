from __future__ import annotations

import os
import pathlib
import socket
import subprocess
from contextlib import closing
from dataclasses import dataclass
from functools import lru_cache
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
    def close(self) -> None:
        ...

    @property
    def channel(self) -> grpc.Channel:
        ...

    def __enter__(self) -> ServerProtocol:
        ...

    def __exit__(self, *exc: Any) -> None:
        ...

    def check(self, timeout: Optional[float] = None) -> bool:
        ...


@dataclass(frozen=True)
class LocalAcpServer:
    process: subprocess.Popen[str]
    port: int
    stdout: TextIO
    stderr: TextIO

    def close(self) -> None:
        self.process.terminate()
        self.process.wait()
        self.stdout.close()
        self.stderr.close()

    # Can be replaced by 'cached_property' for Python 3.8+
    @property  # type: ignore
    @lru_cache(maxsize=1)
    def channel(self) -> grpc.Channel:
        return grpc.insecure_channel(f"localhost:{self.port}")

    def __enter__(self) -> LocalAcpServer:
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

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

    def __del__(self) -> None:
        self.close()


def launch_acp(
    binary_path: _FILE,
    port: Optional[int] = None,
    stdout_file: _FILE = os.devnull,
    stderr_file: _FILE = os.devnull,
) -> LocalAcpServer:
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


def _find_free_port() -> int:
    """Find a free port on localhost.

    Note that there is a race condition between finding the free port
    here, and binding to it from the gRPC server.
    """
    with closing(socket.socket()) as sock:
        sock.bind(("", 0))  # bind to a free port
        return sock.getsockname()[1]  # type: ignore
