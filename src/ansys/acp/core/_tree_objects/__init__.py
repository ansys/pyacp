# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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

from ._elemental_or_nodal_data import ScalarData, VectorData
from ._mesh_data import MeshData
from .analysis_ply import AnalysisPly, AnalysisPlyElementalData, AnalysisPlyNodalData
from .boolean_selection_rule import (
    BooleanSelectionRule,
    BooleanSelectionRuleElementalData,
    BooleanSelectionRuleNodalData,
)
from .butt_joint_sequence import ButtJointSequence, PrimaryPly
from .cad_component import CADComponent
from .cad_geometry import CADGeometry, TriangleMesh
from .cut_off_geometry import CutOffGeometry
from .cut_off_selection_rule import (
    CutOffSelectionRule,
    CutOffSelectionRuleElementalData,
    CutOffSelectionRuleNodalData,
)
from .cylindrical_selection_rule import (
    CylindricalSelectionRule,
    CylindricalSelectionRuleElementalData,
    CylindricalSelectionRuleNodalData,
)
from .edge_set import EdgeSet
from .element_set import ElementSet, ElementSetElementalData, ElementSetNodalData
from .enums import (
    ArrowType,
    BaseElementMaterialHandling,
    BooleanOperationType,
    CutOffGeometryOrientationType,
    CutOffMaterialHandling,
    CutOffRuleType,
    DrapingMaterialModel,
    DrapingType,
    DropOffMaterialHandling,
    DropOffType,
    EdgeSetType,
    ElementalDataType,
    ElementTechnology,
    ExtrusionGuideType,
    ExtrusionMethod,
    ExtrusionType,
    GeometricalRuleType,
    ImportedPlyDrapingType,
    ImportedPlyOffsetType,
    ImportedPlyThicknessType,
    IntersectionType,
    LookUpTable3DInterpolationAlgorithm,
    LookUpTableColumnValueType,
    MeshImportType,
    NodalDataType,
    OffsetType,
    PhysicalDimension,
    PlyCutOffType,
    PlyGeometryExportFormat,
    PlyType,
    ReinforcingBehavior,
    RosetteSelectionMethod,
    RosetteType,
    SectionCutType,
    SensorType,
    SnapToGeometryOrientationType,
    SolidModelExportFormat,
    SolidModelOffsetDirectionType,
    SolidModelSkinExportFormat,
    Status,
    StressStateType,
    SymmetryType,
    ThicknessFieldType,
    ThicknessType,
    UnitSystemType,
    VirtualGeometryDimension,
)
from .extrusion_guide import ExtrusionGuide
from .fabric import Fabric
from .field_definition import FieldDefinition
from .geometrical_selection_rule import (
    GeometricalSelectionRule,
    GeometricalSelectionRuleElementalData,
    GeometricalSelectionRuleNodalData,
)
from .imported_analysis_ply import ImportedAnalysisPly
from .imported_modeling_group import ImportedModelingGroup
from .imported_modeling_ply import ImportedModelingPly
from .imported_production_ply import ImportedProductionPly
from .imported_solid_model import (
    ImportedSolidModel,
    ImportedSolidModelElementalData,
    ImportedSolidModelExportSettings,
    ImportedSolidModelNodalData,
    SolidModelImportFormat,
)
from .interface_layer import InterfaceLayer
from .layup_mapping_object import LayupMappingObject, LayupMappingRosetteSelectionMethod
from .linked_selection_rule import LinkedSelectionRule
from .lookup_table_1d import LookUpTable1D
from .lookup_table_1d_column import LookUpTable1DColumn
from .lookup_table_3d import LookUpTable3D
from .lookup_table_3d_column import LookUpTable3DColumn
from .material import Material
from .model import (
    FeFormat,
    HDF5CompositeCAEImportMode,
    HDF5CompositeCAEProjectionMode,
    IgnorableEntity,
    Model,
    ModelElementalData,
    ModelNodalData,
    ShellMappingProperties,
    SolidMappingProperties,
)
from .modeling_group import ModelingGroup
from .modeling_ply import ModelingPly, ModelingPlyElementalData, ModelingPlyNodalData, TaperEdge
from .oriented_selection_set import (
    OrientedSelectionSet,
    OrientedSelectionSetElementalData,
    OrientedSelectionSetNodalData,
)
from .parallel_selection_rule import (
    ParallelSelectionRule,
    ParallelSelectionRuleElementalData,
    ParallelSelectionRuleNodalData,
)
from .production_ply import ProductionPly, ProductionPlyElementalData, ProductionPlyNodalData
from .rosette import Rosette
from .sampling_point import SamplingPoint
from .section_cut import SectionCut
from .sensor import Sensor
from .snap_to_geometry import SnapToGeometry
from .solid_element_set import (
    SolidElementSet,
    SolidElementSetElementalData,
    SolidElementSetNodalData,
)
from .solid_model import (
    DropOffSettings,
    SolidModel,
    SolidModelElementalData,
    SolidModelExportSettings,
    SolidModelNodalData,
)
from .spherical_selection_rule import (
    SphericalSelectionRule,
    SphericalSelectionRuleElementalData,
    SphericalSelectionRuleNodalData,
)
from .stackup import FabricWithAngle, Stackup
from .sublaminate import Lamina, SubLaminate
from .tube_selection_rule import (
    TubeSelectionRule,
    TubeSelectionRuleElementalData,
    TubeSelectionRuleNodalData,
)
from .utils import CoordinateTransformation
from .variable_offset_selection_rule import (
    VariableOffsetSelectionRule,
    VariableOffsetSelectionRuleElementalData,
    VariableOffsetSelectionRuleNodalData,
)
from .virtual_geometry import SubShape, VirtualGeometry

__all__ = [
    "AnalysisPly",
    "AnalysisPlyElementalData",
    "AnalysisPlyNodalData",
    "ArrowType",
    "BaseElementMaterialHandling",
    "BooleanOperationType",
    "BooleanSelectionRule",
    "BooleanSelectionRuleElementalData",
    "BooleanSelectionRuleNodalData",
    "ButtJointSequence",
    "CADComponent",
    "CADGeometry",
    "CoordinateTransformation",
    "CutOffGeometry",
    "CutOffGeometryOrientationType",
    "CutOffMaterialHandling",
    "CutOffRuleType",
    "CutOffSelectionRule",
    "CutOffSelectionRuleElementalData",
    "CutOffSelectionRuleNodalData",
    "CylindricalSelectionRule",
    "CylindricalSelectionRuleElementalData",
    "CylindricalSelectionRuleNodalData",
    "DrapingMaterialModel",
    "DrapingType",
    "DropOffMaterialHandling",
    "DropOffSettings",
    "DropOffType",
    "EdgeSet",
    "EdgeSetType",
    "ElementalDataType",
    "ElementSet",
    "ElementSetElementalData",
    "ElementSetNodalData",
    "ElementTechnology",
    "ExtrusionGuide",
    "ExtrusionGuideType",
    "ExtrusionMethod",
    "ExtrusionType",
    "Fabric",
    "FabricWithAngle",
    "FeFormat",
    "FieldDefinition",
    "FieldVariable",
    "GeometricalRuleType",
    "GeometricalSelectionRule",
    "GeometricalSelectionRuleElementalData",
    "GeometricalSelectionRuleNodalData",
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
    "ImportedSolidModelElementalData",
    "ImportedSolidModelExportSettings",
    "ImportedSolidModelNodalData",
    "InterfaceLayer",
    "InterpolationOptions",
    "IntersectionType",
    "Lamina",
    "LayupMappingObject",
    "LayupMappingRosetteSelectionMethod",
    "LinkedSelectionRule",
    "LookUpTable1D",
    "LookUpTable1DColumn",
    "LookUpTable3D",
    "LookUpTable3DColumn",
    "LookUpTable3DInterpolationAlgorithm",
    "LookUpTableColumnValueType",
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
    "OffsetType",
    "OrientedSelectionSet",
    "OrientedSelectionSetElementalData",
    "OrientedSelectionSetNodalData",
    "ParallelSelectionRule",
    "ParallelSelectionRuleElementalData",
    "ParallelSelectionRuleNodalData",
    "PhysicalDimension",
    "PlyCutOffType",
    "PlyGeometryExportFormat",
    "PlyType",
    "PrimaryPly",
    "ProductionPly",
    "ProductionPlyElementalData",
    "ProductionPlyNodalData",
    "PuckMaterialType",
    "ReinforcingBehavior",
    "Rosette",
    "RosetteSelectionMethod",
    "RosetteType",
    "SamplingPoint",
    "ScalarData",
    "SectionCut",
    "SectionCutType",
    "Sensor",
    "SensorType",
    "ShellMappingProperties",
    "SnapToGeometry",
    "SnapToGeometryOrientationType",
    "SolidElementSet",
    "SolidElementSetElementalData",
    "SolidElementSetNodalData",
    "SolidMappingProperties",
    "SolidModel",
    "SolidModelElementalData",
    "SolidModelExportFormat",
    "SolidModelExportSettings",
    "SolidModelImportFormat",
    "SolidModelNodalData",
    "SolidModelOffsetDirectionType",
    "SolidModelSkinExportFormat",
    "SphericalSelectionRule",
    "SphericalSelectionRuleElementalData",
    "SphericalSelectionRuleNodalData",
    "Stackup",
    "Status",
    "StressStateType",
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
