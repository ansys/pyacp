import enum
from typing import Dict

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore

import grpc


class ServerKey(str, enum.Enum):
    MAIN = "main"
    FILE_TRANSFER = "file_transfer"


class LaunchMode(str, enum.Enum):
    DIRECT = "direct"
    DOCKER = "docker"
    DOCKER_COMPOSE = "docker_compose"


class ServerProtocol(Protocol):
    """Interface definition for ACP gRPC servers."""

    @property
    def channels(self) -> Dict[str, grpc.Channel]:
        ...

    def wait(self, timeout: float) -> None:
        ...

    # def restart(self) -> None:
    #     ...


class ControllableServerProtocol(ServerProtocol):
    def restart(self) -> None:
        ...