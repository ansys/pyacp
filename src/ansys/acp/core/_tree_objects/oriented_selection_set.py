from __future__ import annotations

import dataclasses
from typing import Iterable, Sequence

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0 import oriented_selection_set_pb2, oriented_selection_set_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from ._grpc_helpers.linked_object_list import define_linked_object_list
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import ElementalData, NodalData, elemental_data_property, nodal_data_property
from .base import CreatableTreeObject, IdTreeObject
from .element_set import ElementSet
from .enums import (
    RosetteSelectionMethod,
    rosette_selection_method_from_pb,
    rosette_selection_method_to_pb,
    status_type_from_pb,
)
from .object_registry import register
from .rosette import Rosette

__all__ = [
    "OrientedSelectionSet",
    "OrientedSelectionSetElementalData",
    "OrientedSelectionSetNodalData",
]


@dataclasses.dataclass
class OrientedSelectionSetElementalData(ElementalData):
    """Represents elemental data for an Oriented Selection Set."""

    normal: npt.NDArray[np.float64]
    orientation: npt.NDArray[np.float64]
    reference_direction: npt.NDArray[np.float64]


@dataclasses.dataclass
class OrientedSelectionSetNodalData(NodalData):
    """Represents nodal data for an Oriented Selection Set."""


@mark_grpc_properties
@register
class OrientedSelectionSet(CreatableTreeObject, IdTreeObject):
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

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "oriented_selection_sets"
    OBJECT_INFO_TYPE = oriented_selection_set_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = oriented_selection_set_pb2.CreateRequest

    def __init__(
        self,
        name: str = "OrientedSelectionSet",
        element_sets: Sequence[ElementSet] = tuple(),
        orientation_point: tuple[float, ...] = (0.0, 0.0, 0.0),
        orientation_direction: tuple[float, ...] = (0.0, 0.0, 0.0),
        rosettes: Sequence[Rosette] = tuple(),
        rosette_selection_method: RosetteSelectionMethod = "minimum_angle",
    ):
        super().__init__(name=name)
        self.element_sets = element_sets
        self.orientation_point = orientation_point
        self.orientation_direction = orientation_direction
        self.rosettes = rosettes
        self.rosette_selection_method = RosetteSelectionMethod(rosette_selection_method)

    def _create_stub(self) -> oriented_selection_set_pb2_grpc.ObjectServiceStub:
        return oriented_selection_set_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

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

    elemental_data = elemental_data_property(OrientedSelectionSetElementalData)
    nodal_data = nodal_data_property(OrientedSelectionSetNodalData)
