from __future__ import annotations

from typing import Protocol

import grpc

from .._typing_helper import StrEnum

__all__ = ["LaunchMode"]


class ServerKey(StrEnum):  # type: ignore
    MAIN = "main"
    FILE_TRANSFER = "file_transfer"


class LaunchMode(StrEnum):  # type: ignore
    """Available launch modes for ACP."""

    DIRECT = "direct"
    DOCKER_COMPOSE = "docker_compose"
    CONNECT = "connect"


class ServerProtocol(Protocol):
    """Interface definition for ACP gRPC servers."""

    @property
    def channels(self) -> dict[str, grpc.Channel]:
        ...

    def check(self, timeout: float | None = None) -> bool:
        ...

    def wait(self, timeout: float) -> None:
        ...


class ControllableServerProtocol(ServerProtocol, Protocol):
    """Interface definition for ACP servers which can be remotely started / stopped."""

    def start(self) -> None:
        ...

    def stop(self, *, timeout: float | None = None) -> None:
        ...

    def restart(self, *, stop_timeout: float | None = None) -> None:
        ...
