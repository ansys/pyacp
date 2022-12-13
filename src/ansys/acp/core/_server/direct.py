import os
import subprocess
from typing import Dict, Optional, TextIO, Union

import grpc
import pydantic

from ansys.tools.local_product_launcher.helpers.ansys_root import get_ansys_root
from ansys.tools.local_product_launcher.helpers.direct import DirectLauncherBase
from ansys.tools.local_product_launcher.helpers.grpc import check_grpc_health
from ansys.tools.local_product_launcher.helpers.ports import find_free_ports
from ansys.tools.local_product_launcher.interface import ServerType

from .common import ServerKey


def _get_default_binary_path() -> Union[str, pydantic.fields.UndefinedType]:
    try:
        ans_root = get_ansys_root()
        binary_path = os.path.join(ans_root, "ACP", "acp_grpcserver")
        if os.name == "nt":
            binary_path += ".exe"
        return binary_path
    except (RuntimeError, FileNotFoundError):
        return pydantic.fields.Undefined


class DirectLaunchConfig(pydantic.BaseModel):
    binary_path: str = pydantic.Field(
        default=_get_default_binary_path(), description="Path to the ACP gRPC server executable."
    )
    stdout_file: str = pydantic.Field(
        default=os.devnull, description="File in which the server stdout is stored."
    )
    stderr_file: str = pydantic.Field(
        default=os.devnull, description="File in which the server stderr is stored."
    )


class DirectLauncher(DirectLauncherBase[DirectLaunchConfig]):
    CONFIG_MODEL = DirectLaunchConfig
    SERVER_SPEC = {ServerKey.MAIN: ServerType.GRPC}

    def __init__(self, *, config: DirectLaunchConfig):
        self._config = config
        self._url: str
        self._process: subprocess.Popen[str]
        self._stdout: TextIO
        self._stderr: TextIO

    def start(self) -> None:
        # TODO: fix
        stdout_file = self._config.stdout_file
        stderr_file = self._config.stderr_file

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
        channel = grpc.insecure_channel(self.urls[ServerKey.MAIN])
        return check_grpc_health(channel=channel, timeout=timeout)

    @property
    def urls(self) -> Dict[str, str]:
        return {ServerKey.MAIN: self._url}
