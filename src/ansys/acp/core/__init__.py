try:
    import importlib.metadata as importlib_metadata  # type: ignore
except ModuleNotFoundError:
    import importlib_metadata  # type: ignore

from ._client import Client
from ._server import (
    LocalAcpServer,
    RemoteAcpServer,
    check_server,
    launch_acp,
    launch_acp_docker,
    launch_acp_docker_compose,
    shutdown_server,
    wait_for_server,
)
from ._tree_objects import (
    ElementSet,
    Fabric,
    Material,
    Model,
    ModelingGroup,
    ModelingPly,
    OrientedSelectionSet,
    Rosette,
)

__version__ = importlib_metadata.version(__name__.replace(".", "-"))


__all__ = [
    "__version__",
    "launch_acp",
    "launch_acp_docker",
    "launch_acp_docker_compose",
    "check_server",
    "wait_for_server",
    "shutdown_server",
    "LocalAcpServer",
    "RemoteAcpServer",
    "Client",
    "Model",
    "Material",
    "Fabric",
    "ElementSet",
    "Rosette",
    "OrientedSelectionSet",
    "ModelingGroup",
    "ModelingPly",
]
