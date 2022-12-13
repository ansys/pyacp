import collections
import copy
import importlib.resources
import os
import subprocess
from typing import Dict, Optional
import uuid

import grpc
import pydantic

from ansys.tools.local_product_launcher.helpers.grpc import check_grpc_health
from ansys.tools.local_product_launcher.helpers.ports import find_free_ports
from ansys.tools.local_product_launcher.interface import LauncherProtocol, ServerType

from .common import ServerKey


class DockerComposeLaunchConfig(pydantic.BaseModel):
    image_name_pyacp: str = "ghcr.io/pyansys/pyacp-private:latest"
    image_name_filetransfer: str = "ghcr.io/ansys/utilities-filetransfer:latest"
    license_server: str = os.environ.get("ANSYSLMD_LICENSE_FILE", "")  # TODO: validate non-empty
    keep_volume: bool = False


class DockerComposeLauncher(LauncherProtocol[DockerComposeLaunchConfig]):
    CONFIG_MODEL = DockerComposeLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC, ServerKey.FILE_TRANSFER: ServerType.GRPC}

    def __init__(self, *, config: DockerComposeLaunchConfig):
        self._compose_name = f"pyacp_compose_{uuid.uuid4().hex}"
        self._urls: Dict[str, str]

        try:
            import ansys.utilities.filetransfer  # noqa
        except ImportError as err:
            raise ImportError(
                "The 'ansys.utilities.filetransfer' module is needed to launch ACP via docker-compose."
            ) from err

        self._env = copy.copy(os.environ)
        self._env.update(
            IMAGE_NAME_PYACP=config.image_name_pyacp,
            IMAGE_NAME_FILETRANSFER=config.image_name_filetransfer,
            ANSYSLMD_LICENSE_FILE=config.license_server,
        )
        self._keep_volume = config.keep_volume

    def start(self) -> None:
        with importlib.resources.path(__package__, "docker-compose.yaml") as compose_file:
            port_acp, port_ft = find_free_ports(2)
            self._urls = {
                ServerKey.MAIN: f"localhost:{port_acp}",
                ServerKey.FILE_TRANSFER: f"localhost:{port_ft}",
            }

            env = collections.ChainMap(
                {"PORT_PYACP": str(port_acp), "PORT_FILETRANSFER": str(port_ft)}, self._env
            )

            # The compose_file may be temporary, in particular if the package is a zipfile.
            # To avoid it being deleted before docker-compose has read it, we use the '--wait'
            # flag for 'docker-compose'.
            cmd = [
                "docker-compose",
                "-f",
                str(compose_file.resolve()),
                "--project-name",
                self._compose_name,
                "up",
                "--detach",
                "--wait",
            ]
            subprocess.check_call(cmd, env=env)

    def stop(self) -> None:
        cmd = ["docker-compose", "--project-name", self._compose_name, "down"]
        if not self._keep_volume:
            cmd.append("--volumes")
        subprocess.check_call(cmd)

    def check(self, timeout: Optional[float] = None) -> bool:
        for url in self.urls.values():
            channel = grpc.insecure_channel(url)
            if not check_grpc_health(channel=channel, timeout=timeout):
                return False
        return True

    @property
    def urls(self) -> Dict[str, str]:
        return self._urls
