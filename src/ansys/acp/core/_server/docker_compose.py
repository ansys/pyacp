import collections
import contextlib
import copy
import dataclasses
import importlib.resources
import math
import os
import pathlib
import subprocess
from typing import Dict, Iterator, Optional
import uuid

import grpc
from packaging.version import parse as parse_version

from ansys.tools.local_product_launcher.helpers.grpc import check_grpc_health
from ansys.tools.local_product_launcher.helpers.ports import find_free_ports
from ansys.tools.local_product_launcher.interface import (
    METADATA_KEY_DOC,
    METADATA_KEY_NOPROMPT,
    LauncherProtocol,
    ServerType,
)

from .common import ServerKey


def _get_default_license_server() -> str:
    try:
        return os.environ["ANSYSLMD_LICENSE_FILE"]
    except KeyError:
        return ""


_COMPOSE_FILE_DEFAULT_KEY = "default"


@dataclasses.dataclass
class DockerComposeLaunchConfig:
    """Configuration options for launching ACP through docker-compose."""

    image_name_pyacp: str = dataclasses.field(
        default="ghcr.io/ansys-internal/pyacp:latest",
        metadata={METADATA_KEY_DOC: "Docker image running the ACP gRPC server."},
    )
    image_name_filetransfer: str = dataclasses.field(
        default="ghcr.io/ansys-internal/tools-filetransfer:latest",
        metadata={METADATA_KEY_DOC: "Docker image running the file transfer service."},
    )
    license_server: str = dataclasses.field(
        default=_get_default_license_server(),
        metadata={
            METADATA_KEY_DOC: (
                "License server passed to the container as "
                "'ANSYSLMD_LICENSE_FILE' environment variable."
            )
        },
    )
    keep_volume: bool = dataclasses.field(
        default=False,
        metadata={METADATA_KEY_DOC: "If true, keep the volume after docker-compose is stopped."},
    )
    compose_file: Optional[str] = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: (
                "Docker compose file used to start the services. Uses the "
                "'docker-compose.yaml' shipped with PyACP by default."
            ),
            METADATA_KEY_NOPROMPT: True,
        },
    )
    environment_variables: Dict[str, str] = dataclasses.field(
        default_factory=dict,
        metadata={
            METADATA_KEY_DOC: (
                "Additional environment variables passed to docker-compose. These take "
                "precedence over environment variables defined through another configuration "
                "option (for example 'license_server' which defines 'ANSYSLMD_LICENSE_FILE') "
                "or the pre-existing environment variables."
            ),
            METADATA_KEY_NOPROMPT: True,
        },
    )


class DockerComposeLauncher(LauncherProtocol[DockerComposeLaunchConfig]):
    CONFIG_MODEL = DockerComposeLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC, ServerKey.FILE_TRANSFER: ServerType.GRPC}

    def __init__(self, *, config: DockerComposeLaunchConfig):
        self._compose_name = f"pyacp_compose_{uuid.uuid4().hex}"
        self._urls: Dict[str, str]

        try:
            import ansys.tools.filetransfer  # noqa
        except ImportError as err:
            raise ImportError(
                "The 'ansys.tools.filetransfer' module is needed to launch ACP via docker-compose."
            ) from err

        self._env = copy.deepcopy(os.environ)
        self._env.update(
            IMAGE_NAME_PYACP=config.image_name_pyacp,
            IMAGE_NAME_FILETRANSFER=config.image_name_filetransfer,
            ANSYSLMD_LICENSE_FILE=config.license_server,
        )
        self._env.update(config.environment_variables)
        self._keep_volume = config.keep_volume

        if config.compose_file is not None:
            self._compose_file: Optional[pathlib.Path] = pathlib.Path(config.compose_file)
        else:
            self._compose_file = None

        self._compose_version = parse_version(
            subprocess.check_output(["docker-compose", "version", "--short"], text=True)
        )

    @contextlib.contextmanager
    def _get_compose_file(self) -> Iterator[pathlib.Path]:
        if self._compose_file is not None:
            yield self._compose_file
        else:
            with importlib.resources.path(__package__, "docker-compose.yaml") as compose_file:
                yield compose_file

    def start(self) -> None:
        with self._get_compose_file() as compose_file:
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
            ]
            if self._compose_version >= parse_version("2.1.1"):
                # The '--wait' flag is only available from version >= 2.1.1 of docker-compose:
                # https://github.com/docker/compose/commit/72e4519cbfb6cdfc600e6ebfa377ce4b8e162c78
                cmd.append("--wait")
            subprocess.check_call(
                cmd, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )

    def stop(self, *, timeout: Optional[float] = None) -> None:
        # The compose file needs to be passed for all commands with docker-compose 1.X.
        # With docker-compose 2.X, this no longer seems to be necessary.
        with self._get_compose_file() as compose_file:
            cmd = [
                "docker-compose",
                "-f",
                str(compose_file),
                "--project-name",
                self._compose_name,
                "down",
            ]
            if timeout is not None:
                # --timeout must be an integer, so we round up.
                cmd.extend(["--timeout", str(math.ceil(timeout))])
            if not self._keep_volume:
                cmd.append("--volumes")
            subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def check(self, timeout: Optional[float] = None) -> bool:
        for url in self.urls.values():
            channel = grpc.insecure_channel(url)
            if not check_grpc_health(channel=channel, timeout=timeout):
                return False
        return True

    @property
    def urls(self) -> Dict[str, str]:
        return self._urls
