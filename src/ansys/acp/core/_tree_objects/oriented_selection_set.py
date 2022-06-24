from __future__ import annotations

from typing import Sequence, Tuple

from ansys.api.acp.v0 import oriented_selection_set_pb2, oriented_selection_set_pb2_grpc

from .._grpc_helpers.linked_object_list import define_linked_object_list
from .._grpc_helpers.property_helper import grpc_data_property, grpc_data_property_read_only
from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.enum_conversions import status_type_to_string
from .base import CreatableTreeObject
from .element_set import ElementSet
from .enums import (
    RosetteSelectionMethod,
    rosette_selection_method_from_pb,
    rosette_selection_method_to_pb,
)
from .rosette import Rosette

__all__ = ["OrientedSelectionSet"]


class OrientedSelectionSet(CreatableTreeObject):
    """Instantiate an Oriented Selection Set.

    Parameters
    ----------
    name :
        The name of the Oriented Selection Set.
    element_sets :
        Element Sets on which the Oriented Selection Set is defined.
    orientation_point :
        The Orientation Point of the Oriented Selection Set.
    orientation_direction :
        The Orientation Direction of the Oriented Element set.
    rosettes :
        Rosettes of the Oriented Selection Set.
    rosette_selection_method :
        Selection Method for Rosettes of the Oriented Selection Set.
    """

    COLLECTION_LABEL = "oriented_selection_sets"
    OBJECT_INFO_TYPE = oriented_selection_set_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = oriented_selection_set_pb2.CreateRequest

    def __init__(
        self,
        name: str = "OrientedSelectionSet",
        element_sets: Sequence[ElementSet] = tuple(),
        orientation_point: Tuple[float, ...] = (0.0, 0.0, 0.0),
        orientation_direction: Tuple[float, ...] = (0.0, 0.0, 0.0),
        rosettes: Sequence[Rosette] = tuple(),
        rosette_selection_method: RosetteSelectionMethod = RosetteSelectionMethod.MINIMUM_ANGLE,
    ):
        super().__init__(name=name)
        self.element_sets = element_sets
        self.orientation_point = orientation_point
        self.orientation_direction = orientation_direction
        self.rosettes = rosettes
        self.rosette_selection_method = RosetteSelectionMethod(rosette_selection_method)

    def _create_stub(self) -> oriented_selection_set_pb2_grpc.ObjectServiceStub:
        return oriented_selection_set_pb2_grpc.ObjectServiceStub(self._channel)

    id = grpc_data_property_read_only("info.id")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_to_string)

    element_sets = define_linked_object_list("properties.element_sets", ElementSet)

    orientation_point = grpc_data_property(
        "properties.orientation_point",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    orientation_direction = grpc_data_property(
        "properties.orientation_direction",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )

    rosettes = define_linked_object_list("properties.rosettes", Rosette)
    rosette_selection_method = grpc_data_property(
        "properties.rosette_selection_method",
        from_protobuf=rosette_selection_method_from_pb,
        to_protobuf=rosette_selection_method_to_pb,
    )
