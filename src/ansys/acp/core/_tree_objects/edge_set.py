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
from .base import CreatableTreeObject, IdTreeObject
from .element_set import ElementSet
from .enums import EdgeSetType, edge_set_type_from_pb, edge_set_type_to_pb, status_type_from_pb
from .object_registry import register


@mark_grpc_properties
@register
class EdgeSet(CreatableTreeObject, IdTreeObject):
    """Instantiate an Edge Set.

    Parameters
    ----------
    name :
        Name of the Edge Set.
    edge_set_type :
        Determines how the Edge Set is defined. Can be either :attr:`.EdgeSetType.BY_NODES`
        or :attr:`.EdgeSetType.BY_REFERENCE`.
    defining_node_labels :
        Labels of the nodes in the Edge Set.
        Only applies when ``edge_set_type`` is :attr:`.EdgeSetType.BY_NODES`.
    element_set :
        Element Set whose boundary the Edge Set follows.
        Only applies when ``edge_set_type`` is :attr:`.EdgeSetType.BY_REFERENCE`.
    limit_angle :
        Maximum angle above which the remaining Element Set boundary is no
        longer considered connected to the Edge Set.
        Only applies when ``edge_set_type`` is :attr:`.EdgeSetType.BY_REFERENCE`.
    origin :
        Defines the starting point of the Edge Set.
        Only applies when ``edge_set_type`` is :attr:`.EdgeSetType.BY_REFERENCE`.
    """

    __slots__: Iterable[str] = tuple()
    COLLECTION_LABEL = "edge_sets"
    OBJECT_INFO_TYPE = edge_set_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = edge_set_pb2.CreateRequest

    def __init__(
        self,
        name: str = "EdgeSet",
        edge_set_type: EdgeSetType = EdgeSetType.BY_NODES,
        defining_node_labels: Iterable[int] = tuple(),
        element_set: ElementSet | None = None,
        limit_angle: float = -1.0,
        origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
    ):
        super().__init__(
            name=name,
        )
        self.edge_set_type = edge_set_type
        self.defining_node_labels = defining_node_labels
        self.element_set = element_set
        self.limit_angle = limit_angle
        self.origin = origin

    def _create_stub(self) -> edge_set_pb2_grpc.ObjectServiceStub:
        return edge_set_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
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
