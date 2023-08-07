import importlib.metadata

from ._client import Client
from ._server import DirectLaunchConfig, DockerComposeLaunchConfig, LaunchMode, launch_acp
from ._tree_objects import (
    BooleanSelectionRule,
    CylindricalSelectionRule,
    EdgeSet,
    EdgeSetType,
    ElementalDataType,
    ElementSet,
    Fabric,
    FabricWithAngle,
    LinkedSelectionRule,
    Material,
    Model,
    ModelingGroup,
    ModelingPly,
    NodalDataType,
    OrientedSelectionSet,
    ParallelSelectionRule,
    ProductionPly,
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
    "BooleanSelectionRule",
    "LinkedSelectionRule",
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
