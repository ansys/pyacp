import importlib.metadata

from ._client import Client
from ._server import DirectLaunchConfig, DockerComposeLaunchConfig, LaunchMode, launch_acp
from ._tree_objects import (
    CylindricalSelectionRule,
    EdgeSet,
    EdgeSetType,
    ElementalDataType,
    ElementSet,
    Fabric,
    FabricWithAngle,
    Material,
    Model,
    ModelingGroup,
    ModelingPly,
    NodalDataType,
    OrientedSelectionSet,
    ProductionPly,
    ParallelSelectionRule,
    Rosette,
    SphericalSelectionRule,
    TubeSelectionRule,
    Stackup,
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
    "ParallelSelectionRule",
    "CylindricalSelectionRule",
    "SphericalSelectionRule",
    "TubeSelectionRule",
    "OrientedSelectionSet",
    "ModelingGroup",
    "ModelingPly",
    "ProductionPly",
    "UnitSystemType",
    "Stackup",
    "FabricWithAngle",
    "ElementalDataType",
    "NodalDataType",
]
