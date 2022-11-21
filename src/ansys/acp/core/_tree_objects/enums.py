from ansys.api.acp.v0 import (
    model_pb2,
    cut_off_material_pb2,
    drop_off_material_pb2,
    enum_types_pb2,
    ply_material_pb2,
    unit_system_pb2,
)

from .._grpc_helpers.enum_wrapper import wrap_to_string_enum

__all__ = [
    "StatusType",
    "RosetteSelectionMethod",
    "CutoffMaterialType",
    "DropoffMaterialType",
    "DrapingMaterialType",
    "PlyType",
    "UnitSystemType"
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
    PlyType,
    ply_type_to_pb,
    ply_type_from_pb,
) = wrap_to_string_enum("PlyType", enum_types_pb2.PlyType, module=__name__)

(
    UnitSystemType,
    unit_system_type_to_pb,
    unit_system_type_from_pb,
) = wrap_to_string_enum("UnitSystemType", unit_system_pb2.UnitSystemType, module=__name__)
