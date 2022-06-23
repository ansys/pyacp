from __future__ import annotations

from ansys.api.acp.v0 import oriented_selection_set_pb2, oriented_selection_set_pb2_grpc

from .._grpc_helpers.linked_object_list import define_linked_object_list
from .._grpc_helpers.property_helper import grpc_data_property_read_only
from .._utils.enum_conversions import status_type_to_string
from .base import CreatableTreeObject
from .element_set import ElementSet
from .object_registry import register

__all__ = ["OrientedSelectionSet"]


@register
class OrientedSelectionSet(CreatableTreeObject):
    """Instantiate an Oriented Selection Set.

    Parameters
    ----------
    name :
        The name of the Oriented Selection Set.
    """

    COLLECTION_LABEL = "oriented_selection_sets"
    OBJECT_INFO_TYPE = oriented_selection_set_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = oriented_selection_set_pb2.CreateRequest

    def __init__(
        self,
        name: str = "OrientedSelectionSet",
    ):
        super().__init__(name=name)

    def _create_stub(self) -> oriented_selection_set_pb2_grpc.ObjectServiceStub:
        return oriented_selection_set_pb2_grpc.ObjectServiceStub(self._channel)

    id = grpc_data_property_read_only("info.id")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_to_string)

    element_sets = define_linked_object_list("properties.element_sets", ElementSet)
