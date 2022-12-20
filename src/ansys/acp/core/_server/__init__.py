from .common import ControllableServerProtocol, LaunchMode, ServerKey, ServerProtocol
from .direct import DirectLaunchConfig
from .docker import DockerLaunchConfig
from .docker_compose import DockerComposeLaunchConfig
from .launch import launch_acp

__all__ = [
    "launch_acp",
    "LaunchMode",
    "ServerKey",
    "ServerProtocol",
    "ControllableServerProtocol",
    "DirectLaunchConfig",
    "DockerLaunchConfig",
    "DockerComposeLaunchConfig",
]

# # NOTE: Currently unused, but could be used with manually starting a server.
# class RemoteAcpServer:
#     def __init__(self, hostname: str, port: int):
#         self._hostname = hostname
#         self._port = port
#         self._channel = None

#     @property
#     def channel(self) -> grpc.Channel:
#         # TODO: implement secure channel
#         if self._channel is None:
#             self._channel = grpc.insecure_channel(f"{self._hostname}:{self._port}")
#         return self._channel
