import importlib.metadata

from ._client import Client
from ._server import DirectLaunchConfig, DockerComposeLaunchConfig, LaunchMode, launch_acp
from ._tree_objects import (
    EdgeSet,
    EdgeSetType,
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

__version__ = importlib.metadata.version(__name__.replace(".", "-"))


__all__ = [
    "__version__",
    "launch_acp",
    "LaunchMode",
    "DirectLaunchConfig",
    "DockerComposeLaunchConfig",
    "Client",
    "Model",
    "Material",
    "Fabric",
    "ElementSet",
    "EdgeSet",
    "EdgeSetType",
    "Rosette",
    "OrientedSelectionSet",
    "ModelingGroup",
    "ModelingPly",
    "UnitSystemType",
]
