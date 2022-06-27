from __future__ import annotations

from typing import Iterable, Tuple

from ansys.api.acp.v0 import rosette_pb2, rosette_pb2_grpc

from .._grpc_helpers.property_helper import grpc_data_property, grpc_data_property_read_only
from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .base import CreatableTreeObject
from .enums import status_type_from_pb
from .object_registry import register

__all__ = ["Rosette"]


@register
class Rosette(CreatableTreeObject):
    """Instantiate a Rosette.

    Parameters
    ----------
    name :
        Name of the Rosette.
    origin :
        Coordinates of the Rosette origin.
    dir1 :
        Direction 1 (x-direction) vector of the Rosette.
    dir2 :
        Direction 2 (y-direction) vector of the Rosette.
    """

    __slots__: Iterable[str] = tuple()

    COLLECTION_LABEL = "rosettes"
    OBJECT_INFO_TYPE = rosette_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = rosette_pb2.CreateRequest

    def __init__(
        self,
        name: str = "Rosette",
        origin: Tuple[float, ...] = (0.0, 0.0, 0.0),
        dir1: Tuple[float, ...] = (1.0, 0.0, 0.0),
        dir2: Tuple[float, ...] = (0.0, 1.0, 0.0),
    ):
        super().__init__(name=name)

        self.origin = origin
        self.dir1 = dir1
        self.dir2 = dir2

    def _create_stub(self) -> rosette_pb2_grpc.ObjectServiceStub:
        return rosette_pb2_grpc.ObjectServiceStub(self._channel)

    id = grpc_data_property_read_only("info.id")

    locked = grpc_data_property_read_only("properties.locked")
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
