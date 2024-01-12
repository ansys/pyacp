from __future__ import annotations

from collections.abc import Iterable

from ansys.api.acp.v0 import cad_component_pb2, cad_component_pb2_grpc

from ._grpc_helpers.property_helper import grpc_data_property_read_only, mark_grpc_properties
from .base import IdTreeObject, ReadOnlyTreeObject
from .enums import status_type_from_pb
from .object_registry import register


@mark_grpc_properties
@register
class CADComponent(ReadOnlyTreeObject, IdTreeObject):
    """Instantiate a CAD Component.

    Parameters
    ----------
    name :
        Name of the CAD component.
    path :
        Path of the CAD component.
    """

    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "cad_components"
    OBJECT_INFO_TYPE = cad_component_pb2.ObjectInfo

    def _create_stub(self) -> cad_component_pb2_grpc.ObjectServiceStub:
        return cad_component_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    path = grpc_data_property_read_only("properties.path")
