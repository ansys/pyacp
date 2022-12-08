from .common import AcpLaunchMode, AcpServerKey, ServerProtocol
from .direct import DirectAcpConfig
from .launch import launch_acp

__all__ = ["launch_acp", "AcpLaunchMode", "AcpServerKey", "ServerProtocol", "DirectAcpConfig"]

# from __future__ import annotations

# import copy
# import enum
# import importlib.resources
# import os
# import pathlib
# import subprocess
# import sys
# import time
# from types import MappingProxyType
# from typing import Any, Dict, List, Mapping, Optional, TextIO, Tuple
# import weakref

# try:
#     from typing import Protocol
# except ImportError:
#     from typing_extensions import Protocol  # type: ignore

# import grpc
# from grpc_health.v1.health_pb2 import HealthCheckRequest, HealthCheckResponse
# from grpc_health.v1.health_pb2_grpc import HealthStub
# import pydantic

# from ansys.api.acp.v0.base_pb2 import Empty
# from ansys.api.acp.v0.control_pb2_grpc import ControlStub
# from ansys.utilities.local_instancemanager_server.helpers.direct import DirectLauncherBase
# from ansys.utilities.local_instancemanager_server.helpers.grpc import check_grpc_health
# from ansys.utilities.local_instancemanager_server.helpers.ports import find_free_ports
# from ansys.utilities.local_instancemanager_server.interface import LAUNCHER_CONFIG_T, ServerType
# from ansys.utilities.local_instancemanager_server.launch import launch_product

# from .._typing_helper import PATH as _PATH


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


# def launch_acp_docker(
#     *,
#     image_name: str = "ghcr.io/pyansys/pyacp-private:latest",
#     license_server: str,
#     mount_directories: Mapping[str, str] = MappingProxyType({}),
#     port: Optional[int] = None,
#     stdout_file: _PATH = os.devnull,
#     stderr_file: _PATH = os.devnull,
# ) -> ServerProtocol:
#     """Launch an ACP server locally in a Docker container.

#     Use ``docker run`` to locally start an ACP Docker container.

#     Parameters
#     ----------
#     image_name :
#         The name of the Docker image to launch.
#     license_server :
#         The ``ANSYSLMD_LICENSE_FILE`` environment variable that is passed
#         to the Docker container.
#     mount_directories :
#         Local directories which should be mounted to the Docker container.
#         The keys contain the path in the context of the host, and the
#         values are the paths as they should appear inside the container.
#     stdout_file :
#         Path (on the host) to which the output of ``docker run`` is redirected.
#     stderr_file :
#         Path (on the host) where the standard error of ``docker run`` is
#         redirected.

#     Returns
#     -------
#     :
#         Server object which can be used to control the server, and
#         instantiate objects on the server.
#     """
#     if port is None:
#         port = find_free_ports()[0]
#     stdout = open(stdout_file, mode="w", encoding="utf-8")
#     stderr = open(stderr_file, mode="w", encoding="utf-8")
#     cmd = ["docker", "run"]
#     for source_dir, target_dir in mount_directories.items():
#         cmd += [
#             "-v",
#             f"/{pathlib.Path(source_dir).resolve().as_posix().replace(':', '')}:{target_dir}",
#         ]
#     if sys.platform == "linux":
#         cmd += ["-u", f"{os.getuid()}:{os.getgid()}"]
#     cmd += [
#         "-p",
#         f"{port}:50051/tcp",
#         "-e",
#         f"ANSYSLMD_LICENSE_FILE={license_server}",
#         "-e",
#         "HOME=/home/container",
#         image_name,
#     ]
#     process = subprocess.Popen(
#         cmd,
#         stdout=stdout,
#         stderr=stderr,
#         text=True,
#     )
#     return LocalAcpServer(process=process, port=port, stdout=stdout, stderr=stderr)


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
