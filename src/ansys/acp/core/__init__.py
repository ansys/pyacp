# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyACP: Ansys Composite PrepPost (ACP) module for Python.

PyACP enables you to design and analyze layered composite structures.
"""

import importlib.metadata

from . import mesh_data

from . import material_property_sets
from ._model_printer import get_model_tree, print_model
from ._plotter import get_directions_plotter
from ._recursive_copy import LinkedObjectHandling, recursive_copy
from ._server import (
    ACPInstance,
    ConnectLaunchConfig,
    DirectLaunchConfig,
    DockerComposeLaunchConfig,
    LaunchMode,
    launch_acp,
)
from ._tree_objects import (
    AnalysisPly,
    ArrowType,
    BaseElementMaterialHandling,
    BooleanOperationType,
    BooleanSelectionRule,
    ButtJointSequence,
    CADComponent,
    CADGeometry,
    CoordinateTransformation,
    CutOffGeometry,
    CutOffGeometryOrientationType,
    CutoffMaterialHandling,
    CutoffRuleType,
    CutoffSelectionRule,
    CylindricalSelectionRule,
    DimensionType,
    DrapingMaterialModel,
    DrapingType,
    DropoffMaterialHandling,
    DropOffSettings,
    DropOffType,
    EdgeSet,
    EdgeSetType,
    ElementalDataType,
    ElementSet,
    ElementTechnology,
    ExtrusionGuide,
    ExtrusionGuideType,
    ExtrusionMethod,
    ExtrusionType,
    Fabric,
    FabricWithAngle,
    FeFormat,
    FieldDefinition,
    GeometricalRuleType,
    GeometricalSelectionRule,
    HDF5CompositeCAEImportMode,
    HDF5CompositeCAEProjectionMode,
    IgnorableEntity,
    ImportedAnalysisPly,
    ImportedModelingGroup,
    ImportedModelingPly,
    ImportedPlyDrapingType,
    ImportedPlyOffsetType,
    ImportedPlyThicknessType,
    ImportedProductionPly,
    ImportedSolidModel,
    ImportedSolidModelExportSettings,
    InterfaceLayer,
    IntersectionType,
    Lamina,
    LayupMappingObject,
    LayupMappingRosetteSelectionMethod,
    LinkedSelectionRule,
    LookUpTable1D,
    LookUpTable1DColumn,
    LookUpTable3D,
    LookUpTable3DColumn,
    LookUpTable3DInterpolationAlgorithm,
    LookUpTableColumnValueType,
    Material,
    MeshImportType,
    Model,
    ModelingGroup,
    ModelingPly,
    NodalDataType,
    OffsetType,
    OrientedSelectionSet,
    ParallelSelectionRule,
    PlyCutoffType,
    PlyGeometryExportFormat,
    PlyType,
    PrimaryPly,
    ProductionPly,
    ReinforcingBehavior,
    Rosette,
    RosetteSelectionMethod,
    RosetteType,
    SamplingPoint,
    SectionCut,
    SectionCutType,
    Sensor,
    SensorType,
    ShellMappingProperties,
    SnapToGeometry,
    SnapToGeometryOrientationType,
    SolidElementSet,
    SolidMappingProperties,
    SolidModel,
    SolidModelExportFormat,
    SolidModelExportSettings,
    SolidModelImportFormat,
    SolidModelOffsetDirectionType,
    SolidModelSkinExportFormat,
    SphericalSelectionRule,
    Stackup,
    Status,
    StressStateType,
    SubLaminate,
    SubShape,
    SymmetryType,
    TaperEdge,
    ThicknessFieldType,
    ThicknessType,
    TubeSelectionRule,
    UnitSystemType,
    VariableOffsetSelectionRule,
    VirtualGeometry,
    VirtualGeometryDimension,
)
from ._workflow import ACPWorkflow, get_composite_post_processing_files, get_dpf_unit_system

__version__ = importlib.metadata.version(__name__.replace(".", "-"))


__all__ = [
    "__version__",
    "ACPInstance",
    "ACPWorkflow",
    "AnalysisPly",
    "ArrowType",
    "BaseElementMaterialHandling",
    "BooleanOperationType",
    "BooleanSelectionRule",
    "ButtJointSequence",
    "CADComponent",
    "CADGeometry",
    "ConnectLaunchConfig",
    "CoordinateTransformation",
    "CutOffGeometry",
    "CutOffGeometryOrientationType",
    "CutoffMaterialHandling",
    "CutoffRuleType",
    "CutoffSelectionRule",
    "CylindricalSelectionRule",
    "DimensionType",
    "DirectLaunchConfig",
    "DockerComposeLaunchConfig",
    "DrapingMaterialModel",
    "DrapingType",
    "DropoffMaterialHandling",
    "DropOffSettings",
    "DropOffType",
    "EdgeSet",
    "EdgeSetType",
    "ElementalDataType",
    "ElementSet",
    "ElementTechnology",
    "ExportSettings",
    "ExtrusionGuide",
    "ExtrusionGuideType",
    "ExtrusionMethod",
    "ExtrusionType",
    "Fabric",
    "FabricWithAngle",
    "FeFormat",
    "FieldDefinition",
    "GeometricalRuleType",
    "GeometricalSelectionRule",
    "get_composite_post_processing_files",
    "get_directions_plotter",
    "get_dpf_unit_system",
    "get_model_tree",
    "HDF5CompositeCAEImportMode",
    "HDF5CompositeCAEProjectionMode",
    "IgnorableEntity",
    "ImportedAnalysisPly",
    "ImportedModelingGroup",
    "ImportedModelingPly",
    "ImportedPlyDrapingType",
    "ImportedPlyOffsetType",
    "ImportedPlyThicknessType",
    "ImportedProductionPly",
    "ImportedSolidModel",
    "ImportedSolidModelExportSettings",
    "InterfaceLayer",
    "IntersectionType",
    "Lamina",
    "launch_acp",
    "LaunchMode",
    "LayupMappingObject",
    "LayupMappingRosetteSelectionMethod",
    "LinkedObjectHandling",
    "LinkedSelectionRule",
    "LookUpTable1D",
    "LookUpTable1DColumn",
    "LookUpTable3D",
    "LookUpTable3DColumn",
    "LookUpTable3DInterpolationAlgorithm",
    "LookUpTableColumnValueType",
    "material_property_sets",
    "Material",
    "MeshImportType",
    "Model",
    "ModelingGroup",
    "ModelingPly",
    "NodalDataType",
    "SolidModelOffsetDirectionType",
    "OffsetType",
    "OrientedSelectionSet",
    "ParallelSelectionRule",
    "PlyCutoffType",
    "PlyGeometryExportFormat",
    "PlyType",
    "PrimaryPly",
    "print_model",
    "ProductionPly",
    "recursive_copy",
    "ReinforcingBehavior",
    "Rosette",
    "RosetteSelectionMethod",
    "RosetteType",
    "SamplingPoint",
    "SectionCut",
    "SectionCutType",
    "Sensor",
    "SensorType",
    "ShellMappingProperties",
    "SnapToGeometry",
    "SnapToGeometryOrientationType",
    "SolidElementSet",
    "SolidMappingProperties",
    "SolidModel",
    "SolidModelExportFormat",
    "SolidModelExportSettings",
    "SolidModelImportFormat",
    "SolidModelSkinExportFormat",
    "SphericalSelectionRule",
    "Stackup",
    "Status",
    "StressStateType",
    "SubLaminate",
    "SubShape",
    "SymmetryType",
    "TaperEdge",
    "ThicknessFieldType",
    "ThicknessType",
    "TubeSelectionRule",
    "UnitSystemType",
    "VariableOffsetSelectionRule",
    "VirtualGeometry",
    "VirtualGeometryDimension",
    "mesh_data",
]
