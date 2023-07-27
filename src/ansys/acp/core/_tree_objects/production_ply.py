from __future__ import annotations

from typing import Iterable

from ansys.api.acp.v0 import production_ply_pb2, production_ply_pb2_grpc

from ._grpc_helpers.property_helper import (
    grpc_data_property_read_only,
    grpc_link_property_read_only,
    mark_grpc_properties,
)
from .base import IdTreeObject, ReadOnlyTreeObject
from .enums import status_type_from_pb
from .object_registry import register

__all__ = ["ProductionPly"]


@mark_grpc_properties
@register
class ProductionPly(ReadOnlyTreeObject, IdTreeObject):
    """Instantiate a Production Ply.

    Parameters
    ----------
    name :
        The name of the ProductionPly
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "production_plies"
    OBJECT_INFO_TYPE = production_ply_pb2.ObjectInfo

    def _create_stub(self) -> production_ply_pb2_grpc.ObjectServiceStub:
        return production_ply_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    material = grpc_link_property_read_only("properties.material")
    angle = grpc_data_property_read_only("properties.angle")
