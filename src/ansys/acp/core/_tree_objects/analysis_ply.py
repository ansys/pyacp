from __future__ import annotations

from typing import Iterable

from ansys.api.acp.v0 import analysis_ply_pb2, analysis_ply_pb2_grpc

from ._grpc_helpers.property_helper import (
    grpc_data_property_read_only,
    grpc_link_property_read_only,
    mark_grpc_properties,
)
from .base import IdTreeObject, ReadOnlyTreeObject
from .enums import status_type_from_pb
from .object_registry import register

__all__ = ["AnalysisPly"]


@mark_grpc_properties
@register
class AnalysisPly(ReadOnlyTreeObject, IdTreeObject):
    """Instantiate an Analysis Ply.

    Parameters
    ----------
    name :
        The name of the AnalysisPly
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "analysis_plies"
    OBJECT_INFO_TYPE = analysis_ply_pb2.ObjectInfo

    def _create_stub(self) -> analysis_ply_pb2_grpc.ObjectServiceStub:
        return analysis_ply_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    material = grpc_link_property_read_only("properties.material")
    angle = grpc_data_property_read_only("properties.angle")
    active_in_post_mode = grpc_data_property_read_only("properties.active_in_post_mode")
