"""PyACP: Ansys Composite PrepPost (ACP) module for Python.

PyACP enables you to design and analyze layered composite structures.
"""

import importlib.metadata

from . import example_helpers, material_property_sets
from ._model_printer import get_model_tree, print_model
from ._plotter import get_directions_plotter
from ._server import (
    ACP,
    ConnectLaunchConfig,
    DirectLaunchConfig,
    DockerComposeLaunchConfig,
    LaunchMode,
    launch_acp,
)
from ._tree_objects import (
    AnalysisPly,
    AnalysisPlyElementalData,
    AnalysisPlyNodalData,
    BooleanOperationType,
    BooleanSelectionRule,
    BooleanSelectionRuleElementalData,
    BooleanSelectionRuleNodalData,
    CADComponent,
    CADGeometry,
    CutoffMaterialType,
    CutoffRuleType,
    CutoffSelectionRule,
    CutoffSelectionRuleElementalData,
    CutoffSelectionRuleNodalData,
    CylindricalSelectionRule,
    CylindricalSelectionRuleElementalData,
    CylindricalSelectionRuleNodalData,
    DimensionType,
    DrapingMaterialType,
    DrapingType,
    DropoffMaterialType,
    EdgeSet,
    EdgeSetType,
    ElementalDataType,
    ElementSet,
    ElementSetElementalData,
    ElementSetNodalData,
    Fabric,
    FabricWithAngle,
    FeFormat,
    GeometricalRuleType,
    GeometricalSelectionRule,
    GeometricalSelectionRuleElementalData,
    GeometricalSelectionRuleNodalData,
    IgnorableEntity,
    Lamina,
    LinkedSelectionRule,
    LookUpTable1D,
    LookUpTable1DColumn,
    LookUpTable3D,
    LookUpTable3DColumn,
    LookUpTable3DInterpolationAlgorithm,
    LookUpTableColumnValueType,
    Material,
    MeshData,
    Model,
    ModelElementalData,
    ModelingGroup,
    ModelingPly,
    ModelingPlyElementalData,
    ModelingPlyNodalData,
    ModelNodalData,
    NodalDataType,
    OrientedSelectionSet,
    OrientedSelectionSetElementalData,
    OrientedSelectionSetNodalData,
    ParallelSelectionRule,
    ParallelSelectionRuleElementalData,
    ParallelSelectionRuleNodalData,
    PlyCutoffType,
    PlyType,
    ProductionPly,
    ProductionPlyElementalData,
    ProductionPlyNodalData,
    Rosette,
    RosetteSelectionMethod,
    ScalarData,
    Sensor,
    SensorType,
    SphericalSelectionRule,
    SphericalSelectionRuleElementalData,
    SphericalSelectionRuleNodalData,
    Stackup,
    StatusType,
    SubLaminate,
    SubShape,
    SymmetryType,
    TaperEdge,
    ThicknessFieldType,
    ThicknessType,
    TubeSelectionRule,
    TubeSelectionRuleElementalData,
    TubeSelectionRuleNodalData,
    UnitSystemType,
    VariableOffsetSelectionRule,
    VariableOffsetSelectionRuleElementalData,
    VariableOffsetSelectionRuleNodalData,
    VectorData,
    VirtualGeometry,
    VirtualGeometryDimension,
)
from ._workflow import ACPWorkflow, get_composite_post_processing_files, get_dpf_unit_system

__version__ = importlib.metadata.version(__name__.replace(".", "-"))


__all__ = [
    "__version__",
    "ACP",
    "ACPWorkflow",
    "AnalysisPly",
    "AnalysisPlyElementalData",
    "AnalysisPlyNodalData",
    "BooleanOperationType",
    "BooleanSelectionRule",
    "BooleanSelectionRuleElementalData",
    "BooleanSelectionRuleNodalData",
    "CADComponent",
    "CADGeometry",
    "ConnectLaunchConfig",
    "CutoffMaterialType",
    "CutoffRuleType",
    "CutoffSelectionRule",
    "CutoffSelectionRuleElementalData",
    "CutoffSelectionRuleNodalData",
    "CylindricalSelectionRule",
    "CylindricalSelectionRuleElementalData",
    "CylindricalSelectionRuleNodalData",
    "DimensionType",
    "DirectLaunchConfig",
    "DockerComposeLaunchConfig",
    "DrapingMaterialType",
    "DrapingType",
    "DropoffMaterialType",
    "EdgeSet",
    "EdgeSetType",
    "ElementalDataType",
    "ElementSet",
    "ElementSetElementalData",
    "ElementSetNodalData",
    "example_helpers",
    "Fabric",
    "FabricWithAngle",
    "FeFormat",
    "GeometricalRuleType",
    "GeometricalSelectionRule",
    "GeometricalSelectionRuleElementalData",
    "GeometricalSelectionRuleNodalData",
    "get_composite_post_processing_files",
    "get_dpf_unit_system",
    "get_model_tree",
    "IgnorableEntity",
    "Lamina",
    "launch_acp",
    "LaunchMode",
    "LinkedSelectionRule",
    "LookUpTable1D",
    "LookUpTable1DColumn",
    "LookUpTable3D",
    "LookUpTable3DColumn",
    "LookUpTable3DInterpolationAlgorithm",
    "LookUpTableColumnValueType",
    "material_property_sets",
    "Material",
    "MeshData",
    "Model",
    "ModelElementalData",
    "ModelingGroup",
    "ModelingPly",
    "ModelingPlyElementalData",
    "ModelingPlyNodalData",
    "ModelNodalData",
    "NodalDataType",
    "OrientedSelectionSet",
    "OrientedSelectionSetElementalData",
    "OrientedSelectionSetNodalData",
    "ParallelSelectionRule",
    "ParallelSelectionRuleElementalData",
    "ParallelSelectionRuleNodalData",
    "PlyCutoffType",
    "PlyType",
    "print_model",
    "ProductionPly",
    "ProductionPlyElementalData",
    "ProductionPlyNodalData",
    "Rosette",
    "RosetteSelectionMethod",
    "ScalarData",
    "Sensor",
    "SensorType",
    "SphericalSelectionRule",
    "SphericalSelectionRuleElementalData",
    "SphericalSelectionRuleNodalData",
    "Stackup",
    "StatusType",
    "SubLaminate",
    "SubShape",
    "SymmetryType",
    "TaperEdge",
    "ThicknessFieldType",
    "ThicknessType",
    "TubeSelectionRule",
    "TubeSelectionRuleElementalData",
    "TubeSelectionRuleNodalData",
    "UnitSystemType",
    "VariableOffsetSelectionRule",
    "VariableOffsetSelectionRuleElementalData",
    "VariableOffsetSelectionRuleNodalData",
    "VectorData",
    "VirtualGeometry",
    "VirtualGeometryDimension",
    "get_directions_plotter",
]
