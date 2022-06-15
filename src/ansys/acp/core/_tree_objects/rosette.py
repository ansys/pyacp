from __future__ import annotations

from functools import lru_cache
from typing import Tuple

from ansys.api.acp.v0.base_pb2 import CollectionPath
from ansys.api.acp.v0.rosette_pb2 import CreateRosetteRequest, RosetteReply
from ansys.api.acp.v0.rosette_pb2_grpc import RosetteStub

from .._grpc_helpers.property_helper import grpc_data_property, grpc_data_property_read_only
from .._resource_paths import join as _rp_join
from ..utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from ..utils.enum_conversions import status_type_to_string
from .base import TreeObjectBase

__all__ = ["Rosette"]


class Rosette(TreeObjectBase):
    COLLECTION_LABEL = "rosettes"
    OBJECT_INFO_TYPE = RosetteReply

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

    # Mypy doesn't like this being a property, see https://github.com/python/mypy/issues/1362
    @lru_cache(maxsize=1)
    def _get_stub(self) -> RosetteStub:
        return RosetteStub(self._channel)

    def store(self, parent: TreeObjectBase) -> None:
        self._channel_store = parent._channel

        collection_path = CollectionPath(
            value=_rp_join(parent._resource_path.value, self.COLLECTION_LABEL)
        )
        request = CreateRosetteRequest(
            collection_path=collection_path,
            name=self._pb_object.info.name,
            # TODO: Remove the 'type: ignore' statement after .protos are harmonized
            # and all ObjectInfo types have a '.properties' attribute.
            properties=self._pb_object.properties,  # type: ignore
        )
        self._pb_object = self._get_stub().Create(request)

    id = grpc_data_property_read_only("info.id")

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_to_string)
    origin = grpc_data_property(
        "properties.origin", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    dir1 = grpc_data_property(
        "properties.dir1", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    dir2 = grpc_data_property(
        "properties.dir2", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
