from ansys.api.acp.v0 import enum_types_pb2

from .._grpc_helpers.enum_wrapper import wrap_to_string_enum

__all__ = ["RosetteSelectionMethod"]

(
    RosetteSelectionMethod,
    rosette_selection_method_to_pb,
    rosette_selection_method_from_pb,
) = wrap_to_string_enum(
    "RosetteSelectionMethod", enum_types_pb2.RosetteSelectionMethod, module=__name__
)
