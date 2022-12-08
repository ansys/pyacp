import enum
from typing import Dict, Protocol

import grpc


class AcpServerKey(str, enum.Enum):
    MAIN = "main"
    FILE_TRANSFER = "file_transfer"


class AcpLaunchMode(str, enum.Enum):
    DIRECT = "direct"
    DOCKER = "docker"
    DOCKER_COMPOSE = "docker_compose"


class ServerProtocol(Protocol):
    """Interface definition for ACP gRPC servers."""

    @property
    def channels(self) -> Dict[str, grpc.Channel]:
        ...

    # TODO: Remove what doesn't make sense with remote servers

    def wait(self, timeout: float) -> None:
        ...

    def restart(self) -> None:
        ...
