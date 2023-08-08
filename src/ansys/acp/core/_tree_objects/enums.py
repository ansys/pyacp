from ansys.api.acp.v0 import (
    cut_off_material_pb2,
    drop_off_material_pb2,
    edge_set_pb2,
    enum_types_pb2,
    mesh_query_pb2,
    ply_material_pb2,
    unit_system_pb2,
)

from ._grpc_helpers.enum_wrapper import wrap_to_string_enum

__all__ = [
    "StatusType",
    "RosetteSelectionMethod",
    "CutoffMaterialType",
    "DropoffMaterialType",
    "DrapingMaterialType",
    "PlyType",
    "UnitSystemType",
    "ElementalDataType",
    "NodalDataType",
]

(StatusType, status_type_to_pb, status_type_from_pb) = wrap_to_string_enum(
    "StatusType", enum_types_pb2.StatusType, module=__name__, value_converter=lambda val: val
)
(
    RosetteSelectionMethod,
    rosette_selection_method_to_pb,
    rosette_selection_method_from_pb,
) = wrap_to_string_enum(
    "RosetteSelectionMethod", enum_types_pb2.RosetteSelectionMethod, module=__name__
)

(
    CutoffMaterialType,
    cut_off_material_type_to_pb,
    cut_off_material_type_from_pb,
) = wrap_to_string_enum(
    "CutoffMaterialType", cut_off_material_pb2.MaterialHandlingType, module=__name__
)

(
    DropoffMaterialType,
    drop_off_material_type_to_pb,
    drop_off_material_type_from_pb,
) = wrap_to_string_enum(
    "DropoffMaterialType", drop_off_material_pb2.MaterialHandlingType, module=__name__
)

(
    DrapingMaterialType,
    draping_material_type_to_pb,
    draping_material_type_from_pb,
) = wrap_to_string_enum(
    "DrapingMaterialType", ply_material_pb2.DrapingMaterialType, module=__name__
)

(
    SymmetryType,
    symmetry_type_to_pb,
    symmetry_type_from_pb,
) = wrap_to_string_enum("SymmetryType", ply_material_pb2.SymmetryType, module=__name__)

(
    EdgeSetType,
    edge_set_type_to_pb,
    edge_set_type_from_pb,
) = wrap_to_string_enum("EdgeSetType", edge_set_pb2.EdgeSetType, module=__name__)

(
    PlyType,
    ply_type_to_pb,
    ply_type_from_pb,
) = wrap_to_string_enum("PlyType", enum_types_pb2.PlyType, module=__name__)

(
    UnitSystemType,
    unit_system_type_to_pb,
    unit_system_type_from_pb,
) = wrap_to_string_enum("UnitSystemType", unit_system_pb2.UnitSystemType, module=__name__)

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
)
