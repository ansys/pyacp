import os
import subprocess
from typing import Dict, Optional, TextIO

import grpc
import pydantic

from ansys.utilities.local_instancemanager_server.helpers.direct import DirectLauncherBase
from ansys.utilities.local_instancemanager_server.helpers.grpc import check_grpc_health
from ansys.utilities.local_instancemanager_server.helpers.ports import find_free_ports
from ansys.utilities.local_instancemanager_server.interface import ServerType

from .common import AcpServerKey


class DirectAcpConfig(pydantic.BaseModel):
    binary_path: str
    stdout_file: str = os.devnull
    stderr_file: str = os.devnull


class DirectAcpLauncher(DirectLauncherBase[DirectAcpConfig]):
    CONFIG_MODEL = DirectAcpConfig
    SERVER_SPEC = {AcpServerKey.MAIN: ServerType.GRPC}

    def __init__(self, *, config: DirectAcpConfig):
        self._config = config
        self._url: str
        self._process: subprocess.Popen[str]
        self._stdout: TextIO
        self._stderr: TextIO

    def start(self) -> None:
        # TODO: fix
        port = None
        stdout_file = self._config.stdout_file
        stderr_file = self._config.stderr_file

        if port is None:
            port = find_free_ports()[0]

        stdout = open(stdout_file, mode="w", encoding="utf-8")
        stderr = open(stderr_file, mode="w", encoding="utf-8")
        process = subprocess.Popen(
            [
                self._config.binary_path,
                f"--server-address=0.0.0.0:{port}",
            ],
            stdout=stdout,
            stderr=stderr,
            text=True,
        )
        self._url = f"localhost:{port}"
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
