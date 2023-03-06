from __future__ import annotations

from typing import Container, Iterable

from ansys.api.acp.v0 import element_set_pb2, element_set_pb2_grpc

from .._utils.array_conversions import to_1D_int_array, to_tuple_from_1D_array
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .object_registry import register

__all__ = ["ElementSet"]


@mark_grpc_properties
@register
class ElementSet(CreatableTreeObject, IdTreeObject):
    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "element_sets"
    OBJECT_INFO_TYPE = element_set_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = element_set_pb2.CreateRequest

    def __init__(
        self,
        name: str = "ElementSet",
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

    def _create_stub(self) -> element_set_pb2_grpc.ObjectServiceStub:
        return element_set_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    locked = grpc_data_property_read_only("properties.locked")
    middle_offset = grpc_data_property("properties.middle_offset")
    element_labels = grpc_data_property(
        "properties.element_labels",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_int_array,
    )
