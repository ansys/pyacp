from __future__ import annotations

from typing import Iterable

from ansys.api.acp.v0 import edge_set_pb2, edge_set_pb2_grpc

from .._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .._utils.array_conversions import to_1D_double_array, to_1D_int_array, to_tuple_from_1D_array
from .base import CreatableTreeObject
from .enums import edge_set_type_from_pb, edge_set_type_to_pb
from .object_registry import register


@mark_grpc_properties
@register
class EdgeSet(CreatableTreeObject):
    __slots__: Iterable[str] = tuple()
    COLLECTION_LABEL = "edge_sets"
    OBJECT_INFO_TYPE = edge_set_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = edge_set_pb2.CreateRequest

    def __init__(self, name: str = "EdgeSet"):
        super().__init__(name=name)
        ...

    def _create_stub(self) -> edge_set_pb2_grpc.ObjectServiceStub:
        return edge_set_pb2_grpc.ObjectServiceStub(self._channel)

    id = grpc_data_property("info.id")

    locked = grpc_data_property_read_only("properties.locked")

    edge_set_type = grpc_data_property(
        "properties.edge_set_type",
        from_protobuf=edge_set_type_from_pb,
        to_protobuf=edge_set_type_to_pb,
    )
    defining_node_labels = grpc_data_property(
        "properties.defining_node_labels",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_int_array,
    )
    element_set = grpc_link_property("properties.element_set")
    limit_angle = grpc_data_property("properties.limit_angle")
    origin = grpc_data_property(
        "properties.origin", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
