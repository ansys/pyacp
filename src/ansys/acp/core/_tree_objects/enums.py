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

from ansys.api.acp.v0 import (
    cut_off_material_pb2,
    cutoff_selection_rule_pb2,
    drop_off_material_pb2,
    edge_set_pb2,
    enum_types_pb2,
    geometrical_selection_rule_pb2,
    lookup_table_3d_pb2,
    lookup_table_column_type_pb2,
    mesh_query_pb2,
    modeling_ply_pb2,
    ply_material_pb2,
    rosette_pb2,
    sensor_pb2,
    unit_system_pb2,
    virtual_geometry_pb2,
)

from ._grpc_helpers.enum_wrapper import wrap_to_string_enum

__all__ = [
    "StatusType",
    "RosetteSelectionMethod",
    "CutoffMaterialType",
    "DropoffMaterialType",
    "DrapingType",
    "DrapingMaterialType",
    "SymmetryType",
    "EdgeSetType",
    "PlyType",
    "BooleanOperationType",
    "UnitSystemType",
    "DimensionType",
    "ElementalDataType",
    "NodalDataType",
    "LookUpTableColumnValueType",
    "LookUpTable3DInterpolationAlgorithm",
    "RosetteType",
    "SensorType",
    "VirtualGeometryDimension",
    "CutoffRuleType",
    "PlyCutoffType",
    "GeometricalRuleType",
    "ThicknessType",
    "ThicknessFieldType",
]

(StatusType, status_type_to_pb, status_type_from_pb) = wrap_to_string_enum(
    "StatusType",
    enum_types_pb2.StatusType,
    module=__name__,
    value_converter=lambda val: val,
    doc="Options for the update status of an object.",
)
(
    RosetteSelectionMethod,
    rosette_selection_method_to_pb,
    rosette_selection_method_from_pb,
) = wrap_to_string_enum(
    "RosetteSelectionMethod",
    enum_types_pb2.RosetteSelectionMethod,
    module=__name__,
    doc="Options for how the rosette is selected in oriented selection sets.",
)

(
    CutoffMaterialType,
    cut_off_material_type_to_pb,
    cut_off_material_type_from_pb,
) = wrap_to_string_enum(
    "CutoffMaterialType",
    cut_off_material_pb2.MaterialHandlingType,
    module=__name__,
    doc="Options for how cut-off material is selected.",
)

(
    DropoffMaterialType,
    drop_off_material_type_to_pb,
    drop_off_material_type_from_pb,
) = wrap_to_string_enum(
    "DropoffMaterialType",
    drop_off_material_pb2.MaterialHandlingType,
    module=__name__,
    doc="Options for how drop-off material is selected.",
)

(
    DrapingType,
    draping_type_to_pb,
    draping_type_from_pb,
) = wrap_to_string_enum(
    "DrapingType",
    ply_material_pb2.DrapingType,
    module=__name__,
    doc="Options for the draping algorithm used.",
)

(
    DrapingMaterialType,
    draping_material_type_to_pb,
    draping_material_type_from_pb,
) = wrap_to_string_enum(
    "DrapingMaterialType",
    ply_material_pb2.DrapingMaterialType,
    module=__name__,
    doc="Options for the material type used in the draping algorithm.",
)

(
    SymmetryType,
    symmetry_type_to_pb,
    symmetry_type_from_pb,
) = wrap_to_string_enum(
    "SymmetryType",
    ply_material_pb2.SymmetryType,
    module=__name__,
    doc="Options for the symmetry of stackups or sublaminates.",
)

(
    EdgeSetType,
    edge_set_type_to_pb,
    edge_set_type_from_pb,
) = wrap_to_string_enum(
    "EdgeSetType",
    edge_set_pb2.EdgeSetType,
    module=__name__,
    doc="Options for how an edge set is defined.",
)

(
    RosetteType,
    rosette_type_to_pb,
    rosette_type_from_pb,
) = wrap_to_string_enum(
    "RosetteType",
    rosette_pb2.Type,
    module=__name__,
    doc="Options for the type of a rosette.",
)

(
    PlyType,
    ply_type_to_pb,
    ply_type_from_pb,
) = wrap_to_string_enum(
    "PlyType",
    enum_types_pb2.PlyType,
    module=__name__,
    doc="Options for the material type of a ply.",
)

(
    BooleanOperationType,
    boolean_operation_type_to_pb,
    boolean_operation_type_from_pb,
) = wrap_to_string_enum(
    "BooleanOperationType",
    enum_types_pb2.BooleanOperationType,
    module=__name__,
    doc="Options for combining selection rules.",
)

(
    UnitSystemType,
    unit_system_type_to_pb,
    unit_system_type_from_pb,
) = wrap_to_string_enum(
    "UnitSystemType",
    unit_system_pb2.UnitSystemType,
    module=__name__,
    doc="Available choices for the unit system.",
)

(
    DimensionType,
    dimension_type_to_pb,
    dimension_type_from_pb,
) = wrap_to_string_enum(
    "DimensionType",
    unit_system_pb2.DimensionType,
    module=__name__,
    doc="Options for the dimension (time, length, currency, ...) of data.",
)

(
    ElementalDataType,
    elemental_data_type_to_pb,
    elemental_data_type_from_pb,
) = wrap_to_string_enum(
    "ElementalDataType",
    mesh_query_pb2.ElementalDataType,
    module=__name__,
    # The enum value names in the '.proto' definition are prefixed with 'ELEMENT_',
    # since they must be unique within the 'mesh_query.proto' file and would
    # otherwise conflict with the 'NodalDataType' enum.
    # For the Python enum, we remove the prefix and convert the values to
    # lowercase.
    key_converter=lambda val: val.split("_", 1)[1],
    value_converter=lambda val: val.split("_", 1)[1].lower(),
    doc="Options for the type of per-element data.",
)
(
    NodalDataType,
    nodal_data_type_to_pb,
    nodal_data_type_from_pb,
) = wrap_to_string_enum(
    "NodalDataType",
    mesh_query_pb2.NodalDataType,
    module=__name__,
    # The enum value names in the '.proto' definition are prefixed with 'NODE_',
    # since they must be unique within the 'mesh_query.proto' file and would
    # otherwise conflict with the 'ElementalDataType' enum.
    # For the Python enum, we remove the prefix and convert the values to
    # lowercase.
    key_converter=lambda val: val.split("_", 1)[1],
    value_converter=lambda val: val.split("_", 1)[1].lower(),
    doc="Options for the type of per-node data.",
)

(
    LookUpTableColumnValueType,
    lookup_table_column_value_type_to_pb,
    lookup_table_column_value_type_from_pb,
) = wrap_to_string_enum(
    "LookUpTableColumnValueType",
    lookup_table_column_type_pb2.ValueType,
    module=__name__,
    doc=(
        "Options for the column type (data location, scalar data, directional data) "
        "of look-up table columns."
    ),
)
(
    LookUpTable3DInterpolationAlgorithm,
    lookup_table_3d_interpolation_algorithm_to_pb,
    lookup_table_3d_interpolation_algorithm_from_pb,
) = wrap_to_string_enum(
    "LookUpTable3DInterpolationAlgorithm",
    lookup_table_3d_pb2.InterpolationAlgorithm,
    module=__name__,
    doc="Options for the interpolation algorithm used for 3D look-up tables.",
)
(
    SensorType,
    sensor_type_to_pb,
    sensor_type_from_pb,
) = wrap_to_string_enum(
    "SensorType", sensor_pb2.SensorType, module=__name__, doc="Options for the type of sensor."
)

(
    VirtualGeometryDimension,
    virtual_geometry_dimension_to_pb,
    virtual_geometry_dimension_from_pb,
) = wrap_to_string_enum(
    "VirtualGeometryDimension",
    virtual_geometry_pb2.Dimension,
    module=__name__,
    doc="Options for the dimension of a virtual geometry.",
)

(
    CutoffRuleType,
    cutoff_rule_type_to_pb,
    cutoff_rule_type_from_pb,
) = wrap_to_string_enum(
    "CutoffRuleType",
    cutoff_selection_rule_pb2.CutoffRuleType,
    module=__name__,
    doc="Options for how a cutoff rule is defined.",
)

(
    PlyCutoffType,
    ply_cutoff_type_to_pb,
    ply_cutoff_type_from_pb,
) = wrap_to_string_enum(
    "PlyCutoffType",
    cutoff_selection_rule_pb2.PlyCutoffType,
    module=__name__,
    doc="Options for how ply cutoff is computed.",
)

(
    GeometricalRuleType,
    geometrical_rule_type_to_pb,
    geometrical_rule_type_from_pb,
) = wrap_to_string_enum(
    "GeometricalRuleType",
    geometrical_selection_rule_pb2.GeometricalRuleType,
    module=__name__,
    doc="Options for how a geometrical selection rule is defined.",
)
(
    ThicknessType,
    thickness_type_to_pb,
    thickness_type_from_pb,
) = wrap_to_string_enum(
    "ThicknessType",
    modeling_ply_pb2.ThicknessType,
    module=__name__,
    doc="Options for how ply thickness is defined.",
)

(
    ThicknessFieldType,
    thickness_field_type_to_pb,
    thickness_field_type_from_pb,
) = wrap_to_string_enum(
    "ThicknessFieldType",
    modeling_ply_pb2.ThicknessFieldType,
    module=__name__,
    doc="Options for how thickness from a table is defined.",
)
