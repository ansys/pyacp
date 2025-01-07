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

from ansys.api.acp.v0 import (
    cut_off_geometry_pb2,
    cut_off_material_pb2,
    cutoff_selection_rule_pb2,
    drop_off_material_pb2,
    edge_set_pb2,
    enum_types_pb2,
    extrusion_guide_pb2,
    geometrical_selection_rule_pb2,
    imported_modeling_ply_pb2,
    layup_mapping_object_pb2,
    lookup_table_3d_pb2,
    lookup_table_column_type_pb2,
    mesh_query_pb2,
    modeling_ply_pb2,
    ply_material_pb2,
    rosette_pb2,
    section_cut_pb2,
    sensor_pb2,
    snap_to_geometry_pb2,
    solid_model_pb2,
    unit_system_pb2,
    virtual_geometry_pb2,
)

from ._grpc_helpers.enum_wrapper import wrap_to_string_enum

__all__ = [
    "ArrowType",
    "BaseElementMaterialHandling",
    "BooleanOperationType",
    "CutOffGeometryOrientationType",
    "CutOffMaterialHandling",
    "CutOffRuleType",
    "DrapingMaterialModel",
    "DrapingType",
    "DropOffMaterialHandling",
    "DropOffType",
    "EdgeSetType",
    "ElementalDataType",
    "ElementTechnology",
    "ExtrusionGuideType",
    "ExtrusionMethod",
    "ExtrusionType",
    "GeometricalRuleType",
    "ImportedPlyDrapingType",
    "ImportedPlyOffsetType",
    "ImportedPlyThicknessType",
    "IntersectionType",
    "LookUpTable3DInterpolationAlgorithm",
    "LookUpTableColumnValueType",
    "NodalDataType",
    "OffsetType",
    "PhysicalDimension",
    "PlyCutOffType",
    "PlyGeometryExportFormat",
    "PlyType",
    "ReinforcingBehavior",
    "RosetteSelectionMethod",
    "RosetteType",
    "SectionCutType",
    "SensorType",
    "SnapToGeometryOrientationType",
    "SolidModelExportFormat",
    "SolidModelOffsetDirectionType",
    "SolidModelSkinExportFormat",
    "Status",
    "StressStateType",
    "SymmetryType",
    "ThicknessFieldType",
    "ThicknessType",
    "UnitSystemType",
    "VirtualGeometryDimension",
]

(Status, status_type_to_pb, status_type_from_pb) = wrap_to_string_enum(
    "Status",
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
    CutOffMaterialHandling,
    cut_off_material_type_to_pb,
    cut_off_material_type_from_pb,
) = wrap_to_string_enum(
    "CutOffMaterialHandling",
    cut_off_material_pb2.MaterialHandlingType,
    module=__name__,
    doc="Options for how cut-off material is selected.",
)

(
    DropOffMaterialHandling,
    drop_off_material_type_to_pb,
    drop_off_material_type_from_pb,
) = wrap_to_string_enum(
    "DropOffMaterialHandling",
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
    ImportedPlyDrapingType,
    imported_ply_draping_type_to_pb,
    imported_ply_draping_type_from_pb,
) = wrap_to_string_enum(
    "ImportedPlyDrapingType",
    ply_material_pb2.DrapingType,
    module=__name__,
    doc="Options for the draping algorithm used.",
    explicit_value_list=(
        ply_material_pb2.DrapingType.NO_DRAPING,
        ply_material_pb2.DrapingType.TABULAR_VALUES,
    ),
)

(
    DrapingMaterialModel,
    draping_material_type_to_pb,
    draping_material_type_from_pb,
) = wrap_to_string_enum(
    "DrapingMaterialModel",
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

(OffsetType, offset_type_to_pb, _) = wrap_to_string_enum(
    "OffsetType",
    enum_types_pb2.OffsetType,
    module=__name__,
    doc="Options for the ply offset type.",
)

(ArrowType, arrow_type_to_pb, _) = wrap_to_string_enum(
    "ArrowType",
    enum_types_pb2.ArrowType,
    module=__name__,
    doc="Options for the type of arrow to be created for directions in the ply geometry export.",
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
    # When loading from a file, the value 'from_file' is more descriptive than 'undefined',
    # so we add an alias for it.
    extra_aliases={"undefined": ("FROM_FILE", "from_file")},
)

(
    PhysicalDimension,
    physical_dimension_to_pb,
    physical_dimension_from_pb,
) = wrap_to_string_enum(
    "PhysicalDimension",
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
    CutOffRuleType,
    cut_off_rule_type_to_pb,
    cut_off_rule_type_from_pb,
) = wrap_to_string_enum(
    "CutOffRuleType",
    cutoff_selection_rule_pb2.CutoffRuleType,
    module=__name__,
    doc="Options for how a cut off rule is defined.",
)

(
    PlyCutOffType,
    ply_cut_off_type_to_pb,
    ply_cut_off_type_from_pb,
) = wrap_to_string_enum(
    "PlyCutOffType",
    cutoff_selection_rule_pb2.PlyCutoffType,
    module=__name__,
    doc="Options for how ply cut-off is computed.",
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
    ImportedPlyThicknessType,
    imported_ply_thickness_type_to_pb,
    imported_ply_thickness_type_from_pb,
) = wrap_to_string_enum(
    "ImportedPlyThicknessType",
    modeling_ply_pb2.ThicknessType,
    module=__name__,
    doc="Options for how ply thickness is defined.",
    explicit_value_list=(
        modeling_ply_pb2.ThicknessType.NOMINAL,
        modeling_ply_pb2.ThicknessType.FROM_TABLE,
    ),
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

(PlyGeometryExportFormat, ply_geometry_export_format_to_pb, _) = wrap_to_string_enum(
    "PlyGeometryExportFormat",
    enum_types_pb2.FileFormat,
    module=__name__,
    doc="Options for the file format of the ply geometry export.",
    explicit_value_list=(
        enum_types_pb2.FileFormat.STEP,
        enum_types_pb2.FileFormat.IGES,
        enum_types_pb2.FileFormat.STL,
    ),
)

(
    ImportedPlyOffsetType,
    imported_ply_offset_type_to_pb,
    imported_ply_offset_type_from_pb,
) = wrap_to_string_enum(
    "ImportedPlyOffsetType",
    enum_types_pb2.OffsetType,
    module=__name__,
    doc="Options for the definition of the offset.",
    explicit_value_list=(
        enum_types_pb2.OffsetType.MIDDLE_OFFSET,
        enum_types_pb2.OffsetType.BOTTOM_OFFSET,
        enum_types_pb2.OffsetType.TOP_OFFSET,
    ),
)

(
    MeshImportType,
    mesh_import_type_to_pb,
    mesh_import_type_from_pb,
) = wrap_to_string_enum(
    "MeshImportType",
    imported_modeling_ply_pb2.MeshImportType,
    module=__name__,
    doc="Options for the definition of the source of the imported mesh.",
)

(ExtrusionType, extrusion_type_to_pb, extrusion_type_from_pb) = wrap_to_string_enum(
    "ExtrusionType",
    section_cut_pb2.ExtrusionType,
    module=__name__,
    doc="Extrusion method used in a section cut.",
)

(SectionCutType, section_cut_type_to_pb, section_cut_type_from_pb) = wrap_to_string_enum(
    "SectionCutType",
    section_cut_pb2.SectionCutType,
    module=__name__,
    doc="Determines whether the section cut is extruded by modeling ply, production ply, or analysis ply.",
)

(IntersectionType, intersection_type_to_pb, intersection_type_from_pb) = wrap_to_string_enum(
    "IntersectionType",
    section_cut_pb2.IntersectionType,
    module=__name__,
    doc="Determines how the intersection is computed for wireframe section cuts.",
)

(ExtrusionMethod, extrusion_method_type_to_pb, extrusion_method_type_from_pb) = wrap_to_string_enum(
    "ExtrusionMethod",
    solid_model_pb2.ExtrusionMethodType,
    module=__name__,
    doc="Extrusion method used in a solid model.",
)

(ExtrusionGuideType, extrusion_guide_type_to_pb, extrusion_guide_type_from_pb) = (
    wrap_to_string_enum(
        "ExtrusionGuideType",
        extrusion_guide_pb2.ExtrusionGuideType,
        module=__name__,
        doc="Extrusion guide type used in an extrusion guide (solid model).",
    )
)

(SolidModelOffsetDirectionType, offset_direction_type_to_pb, offset_direction_type_from_pb) = (
    wrap_to_string_enum(
        "SolidModelOffsetDirectionType",
        solid_model_pb2.OffsetDirectionType,
        module=__name__,
        doc=(
            "Determines how the offset direction is evaluated in a solid model. With "
            "``SURFACE_NORMAL``, the offset direction is re-evaluated based on the "
            "surface of the solid. With ``SHELL_NORMAL``, the direction is based on the "
            "shell surface."
        ),
    )
)
(DropOffType, drop_off_type_to_pb, drop_off_type_from_pb) = wrap_to_string_enum(
    "DropOffType",
    solid_model_pb2.DropOffType,
    module=__name__,
    doc="Determines whether the drop off in solid models is inside or outside the ply boundary.",
)

SolidModelExportFormat, solid_model_export_format_to_pb, _ = wrap_to_string_enum(
    "SolidModelExportFormat",
    enum_types_pb2.FileFormat,
    module=__name__,
    value_converter=lambda val: val.lower().replace("_", ":"),
    doc="Options for the export format of solid models.",
    explicit_value_list=(
        enum_types_pb2.FileFormat.ANSYS_H5,
        enum_types_pb2.FileFormat.ANSYS_CDB,
    ),
)

SolidModelSkinExportFormat, solid_model_skin_export_format_to_pb, _ = wrap_to_string_enum(
    "SolidModelSkinExportFormat",
    enum_types_pb2.FileFormat,
    module=__name__,
    value_converter=lambda val: val.lower().replace("_", ":"),
    doc="Options for the export format of solid model skins.",
    explicit_value_list=(
        enum_types_pb2.FileFormat.ANSYS_CDB,
        enum_types_pb2.FileFormat.STEP,
        enum_types_pb2.FileFormat.IGES,
        enum_types_pb2.FileFormat.STL,
    ),
)


def _prefix_undefined(value: str) -> str:
    if value == "UNDEFINED":
        return "_UNDEFINED"
    return value


(
    SnapToGeometryOrientationType,
    snap_to_geometry_orientation_type_to_pb,
    snap_to_geometry_orientation_type_from_pb,
) = wrap_to_string_enum(
    "SnapToGeometryOrientationType",
    snap_to_geometry_pb2.OrientationType,
    module=__name__,
    key_converter=_prefix_undefined,
    value_converter=lambda val: _prefix_undefined(val).lower(),
    doc=(
        "Determines which layup face a snap-to geometry is applies to. Note that the "
        "``_UNDEFINED`` option should not be used. It is equivalent to using "
        "``BOTTOM``, and included only for compatibility with existing models."
    ),
)
(
    CutOffGeometryOrientationType,
    cut_off_geometry_orientation_type_to_pb,
    cut_off_geometry_orientation_type_from_pb,
) = wrap_to_string_enum(
    "CutOffGeometryOrientationType",
    cut_off_geometry_pb2.OrientationType,
    module=__name__,
    doc="Determines the orientation of a cut-off geometry.",
)

ElementTechnology, element_technology_to_pb, element_technology_from_pb = wrap_to_string_enum(
    "ElementTechnology",
    layup_mapping_object_pb2.ElementTechnology,
    module=__name__,
    doc=("Options for the element technology used in a layup mapping object."),
)

ReinforcingBehavior, reinforcing_behavior_to_pb, reinforcing_behavior_from_pb = wrap_to_string_enum(
    "ReinforcingBehavior",
    layup_mapping_object_pb2.ReinforcingBehavior,
    module=__name__,
    doc=(
        "Specifies whether the reinforcing elements carry tension and compression load, or only one of them."
    ),
)

(
    BaseElementMaterialHandling,
    base_element_material_handling_to_pb,
    base_element_material_handling_from_pb,
) = wrap_to_string_enum(
    "BaseElementMaterialHandling",
    layup_mapping_object_pb2.BaseElementMaterialHandlingType,
    module=__name__,
    doc=(
        "Determines how the base material is handled where it intersects with a reinforcing element."
    ),
)
StressStateType, stress_state_type_to_pb, stress_state_type_from_pb = wrap_to_string_enum(
    "StressStateType",
    layup_mapping_object_pb2.StressStateType,
    module=__name__,
    doc="Specifies if the reinforcing elements should behave like a link, membrane, or shell "
    "element (with or without bending).",
)
