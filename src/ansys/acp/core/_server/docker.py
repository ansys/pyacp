import os
import pathlib
import sys
from typing import Dict, Optional, Union
import uuid

import docker
import grpc
import pydantic

from ansys.tools.local_product_launcher.helpers.grpc import check_grpc_health
from ansys.tools.local_product_launcher.helpers.ports import find_free_ports
from ansys.tools.local_product_launcher.interface import LauncherProtocol, ServerType

from .common import ServerKey


def _get_default_license_server() -> Union[str, pydantic.fields.UndefinedType]:
    try:
        return os.environ["ANSYSLMD_LICENSE_FILE"]
    except KeyError:
        return pydantic.fields.Undefined


class DockerLaunchConfig(pydantic.BaseModel):
    image_name: str = pydantic.Field(
        default="ghcr.io/pyansys/pyacp-private:latest",
        description="Docker image used to run the ACP gRPC server.",
    )
    license_server: str = pydantic.Field(
        default=_get_default_license_server(),
        description="License server passed to the container as 'ANSYSLMD_LICENSE_FILE' environment variable.",
    )
    mount_directories: Dict[str, str] = pydantic.Field(
        default={},
        description=(
            'A mapping \'{"<LOCAL_DIRECTORY>": "<DIRECTORY_IN_CONTAINER>"}\' of '
            "directories to mount into the container."
        ),
    )
    keep_container: bool = pydantic.Field(
        default=False, description="If true, keep the container after it is stopped."
    )


class DockerLauncher(LauncherProtocol[DockerLaunchConfig]):
    CONFIG_MODEL = DockerLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC}

    def __init__(self, *, config: DockerLaunchConfig):
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
        channel = grpc.insecure_channel(self.urls[ServerKey.MAIN])
        return check_grpc_health(channel=channel, timeout=timeout)

    @property
    def urls(self) -> Dict[str, str]:
        return {ServerKey.MAIN: self._url}
