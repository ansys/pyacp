try:
    import importlib.metadata as importlib_metadata  # type: ignore
except ModuleNotFoundError:
    import importlib_metadata  # type: ignore

from ._client import Client
from ._model import Model
from ._modeling_group import ModelingGroup
from ._server import (
    LocalAcpServer,
    RemoteAcpServer,
    check_server,
    launch_acp,
    launch_acp_docker,
    shutdown_server,
    wait_for_server,
)

__version__ = importlib_metadata.version(__name__.replace(".", "-"))


__all__ = [
    "__version__",
    "launch_acp",
    "launch_acp_docker",
    "check_server",
    "wait_for_server",
    "shutdown_server",
    "LocalAcpServer",
    "RemoteAcpServer",
    "Model",
    "ModelingGroup",
    "Client",
]
