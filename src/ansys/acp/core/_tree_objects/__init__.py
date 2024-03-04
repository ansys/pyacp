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

from ._mesh_data import ScalarData, VectorData
from .analysis_ply import AnalysisPly, AnalysisPlyElementalData, AnalysisPlyNodalData
from .boolean_selection_rule import (
    BooleanSelectionRule,
    BooleanSelectionRuleElementalData,
    BooleanSelectionRuleNodalData,
)
from .cad_component import CADComponent
from .cad_geometry import CADGeometry, TriangleMesh
from .cutoff_selection_rule import (
    CutoffSelectionRule,
    CutoffSelectionRuleElementalData,
    CutoffSelectionRuleNodalData,
)
from .cylindrical_selection_rule import (
    CylindricalSelectionRule,
    CylindricalSelectionRuleElementalData,
    CylindricalSelectionRuleNodalData,
)
from .edge_set import EdgeSet
from .element_set import ElementSet, ElementSetElementalData, ElementSetNodalData
from .enums import (
    BooleanOperationType,
    CutoffMaterialType,
    CutoffRuleType,
    DimensionType,
    DrapingMaterialType,
    DrapingType,
    DropoffMaterialType,
    EdgeSetType,
    ElementalDataType,
    GeometricalRuleType,
    LookUpTable3DInterpolationAlgorithm,
    LookUpTableColumnValueType,
    NodalDataType,
    PlyCutoffType,
    PlyType,
    RosetteSelectionMethod,
    RosetteType,
    SensorType,
    StatusType,
    SymmetryType,
    ThicknessFieldType,
    ThicknessType,
    UnitSystemType,
    VirtualGeometryDimension,
)
from .fabric import Fabric
from .geometrical_selection_rule import (
    GeometricalSelectionRule,
    GeometricalSelectionRuleElementalData,
    GeometricalSelectionRuleNodalData,
)
from .linked_selection_rule import LinkedSelectionRule
from .lookup_table_1d import LookUpTable1D
from .lookup_table_1d_column import LookUpTable1DColumn
from .lookup_table_3d import LookUpTable3D
from .lookup_table_3d_column import LookUpTable3DColumn
from .material import Material
from .model import FeFormat, IgnorableEntity, MeshData, Model, ModelElementalData, ModelNodalData
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
from .sensor import Sensor
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
    "BooleanOperationType",
    "BooleanSelectionRule",
    "BooleanSelectionRuleElementalData",
    "BooleanSelectionRuleNodalData",
    "CADComponent",
    "CADGeometry",
    "CutoffMaterialType",
    "CutoffRuleType",
    "CutoffSelectionRule",
    "CutoffSelectionRuleElementalData",
    "CutoffSelectionRuleNodalData",
    "CylindricalSelectionRule",
    "CylindricalSelectionRuleElementalData",
    "CylindricalSelectionRuleNodalData",
    "DimensionType",
    "DrapingMaterialType",
    "DrapingType",
    "DropoffMaterialType",
    "EdgeSet",
    "EdgeSetType",
    "ElementalDataType",
    "ElementSet",
    "ElementSetElementalData",
    "ElementSetNodalData",
    "Fabric",
    "FabricWithAngle",
    "FeFormat",
    "FieldVariable",
    "GeometricalRuleType",
    "GeometricalSelectionRule",
    "GeometricalSelectionRuleElementalData",
    "GeometricalSelectionRuleNodalData",
    "IgnorableEntity",
    "InterpolationOptions",
    "Lamina",
    "LinkedSelectionRule",
    "LookUpTable1D",
    "LookUpTable1DColumn",
    "LookUpTable3D",
    "LookUpTable3DColumn",
    "LookUpTable3DInterpolationAlgorithm",
    "LookUpTableColumnValueType",
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
    "ProductionPly",
    "ProductionPlyElementalData",
    "ProductionPlyNodalData",
    "PuckMaterialType",
    "Rosette",
    "RosetteSelectionMethod",
    "RosetteType",
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
