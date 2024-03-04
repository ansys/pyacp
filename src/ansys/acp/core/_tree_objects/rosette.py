from __future__ import annotations

from collections.abc import Iterable

from ansys.api.acp.v0 import rosette_pb2, rosette_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadOnlyProperty
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .edge_set import EdgeSet
from .enums import RosetteType, rosette_type_from_pb, rosette_type_to_pb, status_type_from_pb
from .object_registry import register

__all__ = ["Rosette"]


@mark_grpc_properties
@register
class Rosette(CreatableTreeObject, IdTreeObject):
    """Instantiate a Rosette.

    Parameters
    ----------
    name :
        Name of the rosette.
    rosette_type :
        Type of the rosette.
    origin :
        Coordinates of the rosette origin.
    dir1 :
        Direction 1 (x-direction) vector of the Rosette.
    dir2 :
        Direction 2 (y-direction) vector of the Rosette.
    edge_set :
        Edge Set used for the Rosettes with type :attr:`RosetteType.EDGE_WISE`.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "rosettes"
    OBJECT_INFO_TYPE = rosette_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = rosette_pb2.CreateRequest

    def __init__(
        self,
        *,
        name: str = "Rosette",
        rosette_type: RosetteType = RosetteType.PARALLEL,
        origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
        dir1: tuple[float, float, float] = (1.0, 0.0, 0.0),
        dir2: tuple[float, float, float] = (0.0, 1.0, 0.0),
        edge_set: EdgeSet | None = None,
    ):
        super().__init__(name=name)

        self.rosette_type = rosette_type
        self.origin = origin
        self.dir1 = dir1
        self.dir2 = dir2
        self.edge_set = edge_set

    def _create_stub(self) -> rosette_pb2_grpc.ObjectServiceStub:
        return rosette_pb2_grpc.ObjectServiceStub(self._channel)

    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    origin = grpc_data_property(
        "properties.origin", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    dir1 = grpc_data_property(
        "properties.dir1", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    dir2 = grpc_data_property(
        "properties.dir2", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )

    rosette_type = grpc_data_property(
        "properties.rosette_type",
        from_protobuf=rosette_type_from_pb,
        to_protobuf=rosette_type_to_pb,
    )

    edge_set = grpc_link_property("properties.edge_set", allowed_types=EdgeSet)
