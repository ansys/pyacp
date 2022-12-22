try:
    import importlib.metadata as importlib_metadata  # type: ignore
except ModuleNotFoundError:
    import importlib_metadata  # type: ignore

from ._client import Client
from ._server import (
    DirectLaunchConfig,
    DockerComposeLaunchConfig,
    DockerLaunchConfig,
    LaunchMode,
    launch_acp,
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
    UnitSystemType,
)

__version__ = importlib_metadata.version(__name__.replace(".", "-"))


__all__ = [
    "__version__",
    "launch_acp",
    "LaunchMode",
    "DirectLaunchConfig",
    "DockerLaunchConfig",
    "DockerComposeLaunchConfig",
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
