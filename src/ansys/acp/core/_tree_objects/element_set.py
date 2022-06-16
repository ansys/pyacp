from __future__ import annotations

from functools import lru_cache
from typing import Collection

from ansys.api.acp.v0.element_set_pb2 import ElementSetReply
from ansys.api.acp.v0.element_set_pb2_grpc import ElementSetStub

from .._grpc_helpers.property_helper import grpc_data_property, grpc_data_property_read_only
from ..utils.array_conversions import to_1D_int_array, to_list_from_int_array
from ..utils.enum_conversions import status_type_to_string
from .base import TreeObject

__all__ = ["ElementSet"]


class ElementSet(TreeObject):
    COLLECTION_LABEL = "element_sets"
    OBJECT_INFO_TYPE = ElementSetReply

    def __init__(
        self,
        name: str = "ElementSet",
        middle_offset: bool = False,
        element_labels: Collection[int] = (),
    ):
        if element_labels is None:
            element_labels = []
        super().__init__(name=name)

        self.middle_offset = middle_offset
        self.element_labels = element_labels

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_to_string)
    id = grpc_data_property_read_only("info.id")

    element_labels = grpc_data_property(
        "properties.element_labels",
        from_protobuf=to_list_from_int_array,
        to_protobuf=to_1D_int_array,
    )

    # Mypy doesn't like this being a property, see https://github.com/python/mypy/issues/1362
    @lru_cache(maxsize=1)
    def _get_stub(self) -> ElementSetStub:
        return ElementSetStub(self._channel)
