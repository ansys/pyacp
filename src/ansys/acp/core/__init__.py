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

from . import example_helpers, material_property_sets
from ._model_printer import get_model_tree, print_model
from ._plotter import get_directions_plotter
from ._recursive_copy import LinkedObjectHandling, recursive_copy
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
    ArrowType,
    BooleanOperationType,
    BooleanSelectionRule,
    BooleanSelectionRuleElementalData,
    BooleanSelectionRuleNodalData,
    ButtJointSequence,
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
    DropOffSettings,
    DropOffType,
    EdgeSet,
    EdgeSetType,
    ElementalDataType,
    ElementSet,
    ElementSetElementalData,
    ElementSetNodalData,
    ExportSettings,
    ExtrusionMethodType,
    ExtrusionType,
    Fabric,
    FabricWithAngle,
    FeFormat,
    GeometricalRuleType,
    GeometricalSelectionRule,
    GeometricalSelectionRuleElementalData,
    GeometricalSelectionRuleNodalData,
    IgnorableEntity,
    ImportedAnalysisPly,
    ImportedModelingGroup,
    ImportedModelingPly,
    ImportedPlyDrapingType,
    ImportedPlyOffsetType,
    ImportedPlyThicknessType,
    ImportedProductionPly,
    InterfaceLayer,
    IntersectionType,
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
    MeshImportType,
    Model,
    ModelElementalData,
    ModelingGroup,
    ModelingPly,
    ModelingPlyElementalData,
    ModelingPlyNodalData,
    ModelNodalData,
    NodalDataType,
    OffsetDirectionType,
    OffsetType,
    OrientationType,
    OrientedSelectionSet,
    OrientedSelectionSetElementalData,
    OrientedSelectionSetNodalData,
    ParallelSelectionRule,
    ParallelSelectionRuleElementalData,
    ParallelSelectionRuleNodalData,
    PlyCutoffType,
    PlyGeometryExportFormat,
    PlyType,
    PrimaryPly,
    ProductionPly,
    ProductionPlyElementalData,
    ProductionPlyNodalData,
    Rosette,
    RosetteSelectionMethod,
    RosetteType,
    SamplingPoint,
    ScalarData,
    SectionCut,
    SectionCutType,
    Sensor,
    SensorType,
    SnapToGeometry,
    SolidModel,
    SolidModelExportFormat,
    SolidModelSkinExportFormat,
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
    TriangleMesh,
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
    "ArrowType",
    "BooleanOperationType",
    "BooleanSelectionRule",
    "BooleanSelectionRuleElementalData",
    "BooleanSelectionRuleNodalData",
    "ButtJointSequence",
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
    "DropOffSettings",
    "DropOffType",
    "EdgeSet",
    "EdgeSetType",
    "ElementalDataType",
    "ElementSet",
    "ElementSetElementalData",
    "ElementSetNodalData",
    "example_helpers",
    "ExportSettings",
    "ExtrusionMethodType",
    "ExtrusionType",
    "Fabric",
    "FabricWithAngle",
    "FeFormat",
    "GeometricalRuleType",
    "GeometricalSelectionRule",
    "GeometricalSelectionRuleElementalData",
    "GeometricalSelectionRuleNodalData",
    "get_composite_post_processing_files",
    "get_directions_plotter",
    "get_dpf_unit_system",
    "get_model_tree",
    "IgnorableEntity",
    "ImportedAnalysisPly",
    "ImportedProductionPly",
    "ImportedModelingPly",
    "ImportedModelingGroup",
    "ImportedPlyDrapingType",
    "ImportedPlyOffsetType",
    "ImportedPlyThicknessType",
    "InterfaceLayer",
    "IntersectionType",
    "Lamina",
    "launch_acp",
    "LaunchMode",
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
    "MeshData",
    "MeshImportType",
    "Model",
    "ModelElementalData",
    "ModelingGroup",
    "ModelingPly",
    "ModelingPlyElementalData",
    "ModelingPlyNodalData",
    "ModelNodalData",
    "NodalDataType",
    "OffsetDirectionType",
    "OffsetType",
    "OrientationType",
    "OrientedSelectionSet",
    "OrientedSelectionSetElementalData",
    "OrientedSelectionSetNodalData",
    "ParallelSelectionRule",
    "ParallelSelectionRuleElementalData",
    "ParallelSelectionRuleNodalData",
    "PlyCutoffType",
    "PlyGeometryExportFormat",
    "PlyType",
    "PrimaryPly",
    "print_model",
    "ProductionPly",
    "ProductionPlyElementalData",
    "ProductionPlyNodalData",
    "recursive_copy",
    "Rosette",
    "RosetteSelectionMethod",
    "RosetteType",
    "SamplingPoint",
    "ScalarData",
    "SectionCut",
    "SectionCutType",
    "Sensor",
    "SensorType",
    "SnapToGeometry",
    "SolidModel",
    "SolidModelExportFormat",
    "SolidModelSkinExportFormat",
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
    "TriangleMesh",
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
]
