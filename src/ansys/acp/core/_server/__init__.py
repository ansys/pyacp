from .common import LaunchMode, ServerKey, ServerProtocol
from .direct import DirectLaunchConfig
from .docker import DockerLaunchConfig
from .launch import launch_acp

__all__ = [
    "launch_acp",
    "LaunchMode",
    "ServerKey",
    "ServerProtocol",
    "DirectLaunchConfig",
    "DockerLaunchConfig",
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


# def launch_acp_docker_compose(
#     *,
#     image_name_pyacp: str = "ghcr.io/pyansys/pyacp-private:latest",
#     image_name_filetransfer: str = "ghcr.io/ansys/utilities-filetransfer:latest",
#     license_server: str,
#     port_pyacp: Optional[int] = None,
#     port_filetransfer: Optional[int] = None,
#     stdout_file: _PATH = os.devnull,
#     stderr_file: _PATH = os.devnull,
# ) -> Tuple[ServerProtocol, ServerProtocol]:
#     try:
#         import ansys.utilities.filetransfer
#     except ImportError as err:
#         raise ImportError(
#             "The 'ansys.utilities.filetransfer' module is needed to launch ACP via docker-compose."
#         ) from err

#     with importlib.resources.path(__name__, "docker-compose.yaml") as compose_file:
#         tmp_port_pyacp, tmp_port_filetransfer = find_free_ports(num_ports=2)
#         if port_pyacp is None:
#             port_pyacp = tmp_port_pyacp
#         if port_filetransfer is None:
#             port_filetransfer = tmp_port_filetransfer

#         stdout = open(stdout_file, mode="w", encoding="utf-8")
#         stderr = open(stderr_file, mode="w", encoding="utf-8")
#         cmd = ["docker-compose", "-f", str(compose_file.resolve()), "up"]
#         env = copy.copy(os.environ)
#         env.update(
#             dict(
#                 IMAGE_NAME_PYACP=image_name_pyacp,
#                 IMAGE_NAME_FILETRANSFER=image_name_filetransfer,
#                 ANSYSLMD_LICENSE_FILE=license_server,
#                 PORT_FILETRANSFER=str(port_filetransfer),
#                 PORT_PYACP=str(port_pyacp),
#             )
#         )
#         process = subprocess.Popen(
#             cmd,
#             stdout=stdout,
#             stderr=stderr,
#             env=env,
#             text=True,
#         )
#         server_pyacp = LocalAcpServer(
#             process=process,
#             port=port_pyacp,
#             stdout=stdout,
#             stderr=stderr,
#         )
#         server_filetransfer = RemoteAcpServer(hostname="localhost", port=port_filetransfer)

#         # The compose_file may be temporary, in particular if the package is a zipfile.
#         # To avoid it being deleted before docker-compose has read it, we wait for the
#         # filetransfer server (which is faster since it doesn't need to check out a
#         # license) to start.
#         wait_for_server(server_filetransfer, timeout=10)
#         return (server_pyacp, server_filetransfer)
