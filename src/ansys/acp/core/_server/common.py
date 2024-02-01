from __future__ import annotations

import enum
from typing import Protocol

import grpc

try:
    from enum import StrEnum  # type: ignore
except ImportError:
    # For Python 3.10 and below, emulate the behavior of StrEnum by
    # inheriting from str and enum.Enum.
    # Note that this does *not* work on Python 3.11+, since the default
    # Enum format method has changed and will not return the value of
    # the enum member.
    class StrEnum(str, enum.Enum):  # type: ignore
        pass


__all__ = ["LaunchMode"]


class ServerKey(StrEnum):  # type: ignore
    MAIN = "main"
    FILE_TRANSFER = "file_transfer"


class LaunchMode(StrEnum):  # type: ignore
    """Available launch modes for ACP."""

    DIRECT = "direct"
    DOCKER_COMPOSE = "docker_compose"


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
