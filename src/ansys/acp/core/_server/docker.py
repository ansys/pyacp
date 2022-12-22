import dataclasses
import os
import pathlib
import sys
import time
from typing import Dict, Optional
import uuid

import docker
import grpc

from ansys.tools.local_product_launcher.helpers.grpc import check_grpc_health
from ansys.tools.local_product_launcher.interface import (
    DOC_METADATA_KEY,
    LauncherProtocol,
    ServerType,
)

from .common import ServerKey


# TODO: move to common location; maybe into helpers module
def _get_default_license_server() -> str:
    try:
        return os.environ["ANSYSLMD_LICENSE_FILE"]
    except KeyError:
        return ""


@dataclasses.dataclass
class DockerLaunchConfig:
    """Configuration options for launching ACP as a docker container."""

    image_name: str = dataclasses.field(
        default="ghcr.io/pyansys/pyacp-private:latest",
        metadata={DOC_METADATA_KEY: "Docker image running the ACP gRPC server."},
    )
    license_server: str = dataclasses.field(
        default=_get_default_license_server(),
        metadata={
            DOC_METADATA_KEY: (
                "License server passed to the container as "
                "'ANSYSLMD_LICENSE_FILE' environment variable."
            )
        },
    )
    mount_directories: Dict[str, str] = dataclasses.field(
        default_factory=dict,
        metadata={
            DOC_METADATA_KEY: (
                'A mapping \'{"<LOCAL_DIRECTORY>": "<DIRECTORY_IN_CONTAINER>"}\' of '
                "directories to mount into the container."
            )
        },
    )
    keep_container: bool = dataclasses.field(
        default=False,
        metadata={DOC_METADATA_KEY: "If true, keep the container after it is stopped."},
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
        self._container = self._docker_client.containers.run(
            **self._common_run_kwargs, ports={"50051/tcp": None}
        )
        for _ in range(600):
            self._container.reload()
            if (self._container.status != "created") and (self._container.ports["50051/tcp"]):
                break
            time.sleep(0.1)
        else:
            raise RuntimeError("Container initialization did not succeed.")
        if self._container.status != "running":
            raise RuntimeError(
                f"Container did not start successfully; current status: {self._container.status}"
            )
        port = self._container.ports["50051/tcp"][0]["HostPort"]
        self._url = f"localhost:{port}"

    def stop(self) -> None:
        self._container.stop()

    def check(self, timeout: Optional[float] = None) -> bool:
        self._container.reload()
        if self._container.status != "running":
            return False
        channel = grpc.insecure_channel(self.urls[ServerKey.MAIN])
        return check_grpc_health(channel=channel, timeout=timeout)

    @property
    def urls(self) -> Dict[str, str]:
        return {ServerKey.MAIN: self._url}
