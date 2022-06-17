from __future__ import annotations

from functools import lru_cache
from typing import Container

from ansys.api.acp.v0.element_set_pb2 import CreateElementSetRequest, ElementSetInfo
from ansys.api.acp.v0.element_set_pb2_grpc import ElementSetStub

from .._grpc_helpers.property_helper import grpc_data_property, grpc_data_property_read_only
from .._utils.array_conversions import to_1D_int_array, to_tuple_from_1D_array
from .base import CreatableTreeObject

__all__ = ["ElementSet"]


class ElementSet(CreatableTreeObject):
    COLLECTION_LABEL = "element_sets"
    OBJECT_INFO_TYPE = ElementSetInfo
    CREATE_REQUEST_TYPE = CreateElementSetRequest

    def __init__(
        self,
        name: str = "Element Set",
        middle_offset: bool = False,
        element_labels: Container[int] = tuple(),
    ):
        """Instantiate an Element Set.

        Parameters
        ----------
        name :
            The name of the Element Set.
        middle_offset :
            TODO
        element_labels :
            TODO
        """
        super().__init__(name=name)
        self.middle_offset = middle_offset
        self.element_labels = element_labels

    # Mypy doesn't like this being a property, see https://github.com/python/mypy/issues/1362
    @lru_cache(maxsize=1)
    def _get_stub(self) -> ElementSetStub:
        return ElementSetStub(self._channel)

    id = grpc_data_property("info.id")

    locked = grpc_data_property_read_only("properties.locked")
    middle_offset = grpc_data_property("properties.middle_offset")
    element_labels = grpc_data_property(
        "properties.element_labels",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_int_array,
    )
