import os
import pathlib
import subprocess
import sys
from typing import Dict, Optional, TextIO

import grpc
import pydantic

from ansys.utilities.local_instancemanager_server.helpers.direct import DirectLauncherBase
from ansys.utilities.local_instancemanager_server.helpers.grpc import check_grpc_health
from ansys.utilities.local_instancemanager_server.helpers.ports import find_free_ports
from ansys.utilities.local_instancemanager_server.interface import ServerType

from .common import AcpServerKey


class DockerAcpConfig(pydantic.BaseModel):
    image_name: str = "ghcr.io/pyansys/pyacp-private:latest"
    license_server: str
    mount_directories: Dict[str, str]
    # port: Optional[int] = None,
    stdout_file: str = os.devnull
    stderr_file: str = os.devnull


class DockerAcpLauncher(DirectLauncherBase[DockerAcpConfig]):
    CONFIG_MODEL = DockerAcpConfig
    SERVER_SPEC = {AcpServerKey.MAIN: ServerType.GRPC}

    def __init__(self, *, config: DockerAcpConfig):
        self._config = config
        self._url: str
        self._process: subprocess.Popen[str]
        self._stdout: TextIO
        self._stderr: TextIO

    def start(self) -> None:
        stdout_file = self._config.stdout_file
        stderr_file = self._config.stderr_file
        mount_directories = self._config.mount_directories
        license_server = self._config.license_server
        image_name = self._config.image_name

        port = find_free_ports()[0]
        self._url = f"localhost:{port}"
        stdout = open(stdout_file, mode="w", encoding="utf-8")
        stderr = open(stderr_file, mode="w", encoding="utf-8")
        cmd = ["docker", "run"]
        for source_dir, target_dir in mount_directories.items():
            cmd += [
                "-v",
                f"/{pathlib.Path(source_dir).resolve().as_posix().replace(':', '')}:{target_dir}",
            ]
        if sys.platform == "linux":
            cmd += ["-u", f"{os.getuid()}:{os.getgid()}"]
        cmd += [
            "-p",
            f"{port}:50051/tcp",
            "-e",
            f"ANSYSLMD_LICENSE_FILE={license_server}",
            "-e",
            "HOME=/home/container",
            image_name,
        ]
        process = subprocess.Popen(
            cmd,
            stdout=stdout,
            stderr=stderr,
            text=True,
        )
        super()._start(
            process=process,
            stdout=stdout,
            stderr=stderr,
        )

    def check(self, timeout: Optional[float] = None) -> bool:
        channel = grpc.insecure_channel(self.urls[AcpServerKey.MAIN])
        return check_grpc_health(channel=channel, timeout=timeout)

    @property
    def urls(self) -> Dict[str, str]:
        return {AcpServerKey.MAIN: self._url}
