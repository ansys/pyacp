# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import collections
from collections.abc import Iterator
import contextlib
import copy
import dataclasses
import importlib.resources
import math
import os
import pathlib
import subprocess  # nosec B404
import uuid

from packaging.version import parse as parse_version

from ansys.tools.local_product_launcher.grpc_transport import (
    InsecureOptions,
    MTLSOptions,
)
from ansys.tools.local_product_launcher.helpers.grpc import check_grpc_health
from ansys.tools.local_product_launcher.helpers.ports import find_free_ports
from ansys.tools.local_product_launcher.interface import (
    METADATA_KEY_DOC,
    METADATA_KEY_NOPROMPT,
    LauncherProtocol,
    ServerType,
)

from .common import ServerKey

__all__ = ["DockerComposeLaunchConfig"]

TransportOptionsType = (
    InsecureOptions | MTLSOptions
)  # UDS and WNUA are not supported for docker-compose


def _get_default_license_server() -> str:
    try:
        return os.environ["ANSYSLMD_LICENSE_FILE"]
    except KeyError:
        return ""


@dataclasses.dataclass
class DockerComposeLaunchConfig:
    """Configuration options for launching ACP through docker compose."""

    image_name_acp: str = dataclasses.field(
        default="ghcr.io/ansys/acp:latest",
        metadata={METADATA_KEY_DOC: "Docker image running the ACP gRPC server."},
    )
    image_name_filetransfer: str = dataclasses.field(
        default="ghcr.io/ansys/tools-filetransfer:latest",
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
        metadata={METADATA_KEY_DOC: "If true, keep the volume after docker compose is stopped."},
    )
    compose_file: str | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: (
                "Docker compose file used to start the services. Uses the "
                "compose files shipped with PyACP by default."
            ),
            METADATA_KEY_NOPROMPT: True,
        },
    )
    environment_variables: dict[str, str] = dataclasses.field(
        default_factory=dict,
        metadata={
            METADATA_KEY_DOC: (
                "Additional environment variables passed to docker compose. These take "
                "precedence over environment variables defined through another configuration "
                "option (for example 'license_server' which defines 'ANSYSLMD_LICENSE_FILE') "
                "or the pre-existing environment variables."
            ),
            METADATA_KEY_NOPROMPT: True,
        },
    )
    transport_mode: str = dataclasses.field(
        default="mtls",
        metadata={
            METADATA_KEY_DOC: "gRPC transport mode to use. Only 'mtls' and 'insecure' are supported."
        },
    )
    certs_dir: str | pathlib.Path | None = dataclasses.field(
        default=None,
        metadata={
            METADATA_KEY_DOC: "Directory containing TLS certificates. Only used if transport_mode is 'mtls'."
        },
    )


class DockerComposeLauncher(LauncherProtocol[DockerComposeLaunchConfig]):
    CONFIG_MODEL = DockerComposeLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC, ServerKey.FILE_TRANSFER: ServerType.GRPC}

    def __init__(self, *, config: DockerComposeLaunchConfig):
        self._compose_name = f"pyacp_compose_{uuid.uuid4().hex}"
        self._config = config
        self._transport_options: dict[str, TransportOptionsType] = {}

        try:
            import ansys.tools.filetransfer  # noqa
        except ImportError as err:
            raise ImportError(
                "The 'ansys.tools.filetransfer' module is needed to launch ACP via docker-compose."
            ) from err

        if self._config.transport_mode == "mtls" and self._config.certs_dir is None:
            # The default 'certs_dir' needs to be implemented explicitly here
            # since it needs to be mounted into the docker container.
            self._config.certs_dir = os.environ.get("ANSYS_GRPC_CERTIFICATES")
            if self._config.certs_dir is None:
                self._config.certs_dir = pathlib.Path.cwd() / "certs"

        self._env = copy.deepcopy(os.environ)
        self._env.update(
            IMAGE_NAME_ACP=self._config.image_name_acp,
            IMAGE_NAME_FILETRANSFER=self._config.image_name_filetransfer,
            ANSYSLMD_LICENSE_FILE=self._config.license_server,
        )
        self._env.update(self._config.environment_variables)
        if self._config.transport_mode == "mtls":
            assert self._config.certs_dir is not None
            self._env["CERTS_DIR"] = str(pathlib.Path(self._config.certs_dir).resolve())

        self._keep_volume = config.keep_volume

        if config.compose_file is not None:
            self._compose_file: pathlib.Path | None = pathlib.Path(config.compose_file)
        else:
            self._compose_file = None

        try:
            self._compose_version = parse_version(
                subprocess.check_output(  # nosec B603, B607: documented in 'security_considerations.rst'
                    ["docker", "compose", "version", "--short"], text=True
                ).replace(
                    "-", "+"
                )
            )
            self._compose_cmds = ["docker", "compose"]
        except subprocess.CalledProcessError:
            # If 'docker compose does not work, try 'docker-compose' instead.
            self._compose_version = parse_version(
                subprocess.check_output(  # nosec B603, B607: documented in 'security_considerations.rst'
                    ["docker-compose", "version", "--short"], text=True
                ).replace(
                    "-", "+"
                )
            )
            self._compose_cmds = ["docker-compose"]

    @contextlib.contextmanager
    def _get_compose_file(self) -> Iterator[pathlib.Path]:
        if self._compose_file is not None:
            yield self._compose_file
        else:
            compose_filename = f"docker-compose-{self._config.transport_mode}.yaml"
            with importlib.resources.path(__package__, compose_filename) as compose_file:
                yield compose_file

    def start(self) -> None:
        with self._get_compose_file() as compose_file:
            port_acp, port_ft = find_free_ports(2)

            if self._config.transport_mode == "mtls":
                assert self._config.certs_dir is not None
                self._transport_options = {
                    ServerKey.MAIN: MTLSOptions(
                        host="localhost",
                        port=port_acp,
                        certs_dir=pathlib.Path(self._config.certs_dir),
                        allow_remote_host=False,
                    ),
                    ServerKey.FILE_TRANSFER: MTLSOptions(
                        host="localhost",
                        port=port_ft,
                        certs_dir=pathlib.Path(self._config.certs_dir),
                        allow_remote_host=False,
                    ),
                }
            elif self._config.transport_mode == "insecure":
                self._transport_options = {
                    ServerKey.MAIN: InsecureOptions(
                        host="localhost",
                        port=port_acp,
                        allow_remote_host=False,
                    ),
                    ServerKey.FILE_TRANSFER: InsecureOptions(
                        host="localhost",
                        port=port_ft,
                        allow_remote_host=False,
                    ),
                }
            else:
                raise ValueError(
                    f"Unsupported transport mode '{self._config.transport_mode}'. "
                    "Only 'mtls' and 'insecure' are supported."
                )

            env = collections.ChainMap(
                {"PORT_ACP": str(port_acp), "PORT_FILETRANSFER": str(port_ft)}, self._env
            )

            # The compose_file may be temporary, in particular if the package is a zipfile.
            # To avoid it being deleted before docker compose has read it, we use the '--wait'
            # flag for 'docker compose'.
            cmd = self._compose_cmds + [
                "-f",
                str(compose_file.resolve()),
                "--project-name",
                self._compose_name,
                "up",
                "--detach",
            ]
            if self._compose_version >= parse_version("2.1.1"):
                # The '--wait' flag is only available from version >= 2.1.1 of docker compose:
                # https://github.com/docker/compose/commit/72e4519cbfb6cdfc600e6ebfa377ce4b8e162c78
                cmd.append("--wait")
            proc_res = subprocess.run(  # nosec B603: documented in 'security_considerations.rst'
                cmd, env=env, capture_output=True, text=True
            )
            if proc_res.returncode != 0:
                raise RuntimeError(f"Docker compose failed to start:\n{proc_res.stderr}")

    def stop(self, *, timeout: float | None = None) -> None:
        # The compose file needs to be passed for all commands with docker-compose 1.X.
        # With docker-compose 2.X, this no longer seems to be necessary.
        with self._get_compose_file() as compose_file:
            cmd = self._compose_cmds + [
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
            subprocess.check_call(  # nosec B603: documented in 'security_considerations.rst'
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

    def check(self, timeout: float | None = None) -> bool:
        for transport_options in self.transport_options.values():
            channel = transport_options.create_channel()
            if not check_grpc_health(channel=channel, timeout=timeout):
                return False
        return True

    @property
    def transport_options(self) -> dict[str, TransportOptionsType]:  # type: ignore[override]
        return self._transport_options
