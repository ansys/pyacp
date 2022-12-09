import os
import pathlib
import sys
from typing import Dict, Optional
import uuid

import docker
import grpc
import pydantic

from ansys.utilities.local_instancemanager_server.helpers.grpc import check_grpc_health
from ansys.utilities.local_instancemanager_server.helpers.ports import find_free_ports
from ansys.utilities.local_instancemanager_server.interface import LauncherProtocol, ServerType

from .common import AcpServerKey


class DockerAcpConfig(pydantic.BaseModel):
    image_name: str = "ghcr.io/pyansys/pyacp-private:latest"
    license_server: str
    mount_directories: Dict[str, str]
    keep_container: bool = False


class DockerAcpLauncher(LauncherProtocol[DockerAcpConfig]):
    CONFIG_MODEL = DockerAcpConfig
    SERVER_SPEC = {AcpServerKey.MAIN: ServerType.GRPC}

    def __init__(self, *, config: DockerAcpConfig):
        self._docker_client = docker.from_env()
        self._url: str
        self._container: docker.containers.Container

        self._common_run_kwargs = {
            "image": self._docker_client.images.get(config.image_name),
            "name": f"pyacp_{uuid.uuid4().hex}",
            "environment": dict(ANSYSLMD_LICENSE_FILE=config.license_server),
            "remove": not config.keep_container,
            "detach": True,
        }
        volumes = []
        for source_dir, target_dir in config.mount_directories.items():
            volumes.append(
                f"/{pathlib.Path(source_dir).resolve().as_posix().replace(':', '')}:{target_dir}",
            )
        if volumes:
            self._common_run_kwargs["volumes"] = volumes

        if sys.platform == "linux":
            self._common_run_kwargs["user"] = f"{os.getuid()}:{os.getgid()}"

    def start(self) -> None:
        port = find_free_ports()[0]
        self._url = f"localhost:{port}"
        self._container = self._docker_client.containers.run(
            **self._common_run_kwargs, ports={"50051/tcp": port}
        )

    def stop(self) -> None:
        self._container.stop()

    def check(self, timeout: Optional[float] = None) -> bool:
        channel = grpc.insecure_channel(self.urls[AcpServerKey.MAIN])
        return check_grpc_health(channel=channel, timeout=timeout)

    @property
    def urls(self) -> Dict[str, str]:
        return {AcpServerKey.MAIN: self._url}
