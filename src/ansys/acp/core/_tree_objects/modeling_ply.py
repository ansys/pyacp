from __future__ import annotations

import dataclasses
from typing import Container, Iterable

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0 import modeling_ply_pb2, modeling_ply_pb2_grpc

from ._grpc_helpers.linked_object_list import define_linked_object_list
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from ._mesh_data import ElementalData, NodalData, elemental_data_property, nodal_data_property
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .fabric import Fabric
from .object_registry import register
from .oriented_selection_set import OrientedSelectionSet

__all__ = ["ModelingPly", "ModelingPlyElementalData", "ModelingPlyNodalData"]


@dataclasses.dataclass
class ModelingPlyElementalData(ElementalData):
    """Represents elemental data for a Modeling Ply."""

    normal: npt.NDArray[np.float64]
    orientation: npt.NDArray[np.float64]
    reference_direction: npt.NDArray[np.float64]
    fiber_direction: npt.NDArray[np.float64]
    draped_fiber_direction: npt.NDArray[np.float64]
    transverse_direction: npt.NDArray[np.float64]
    draped_transverse_direction: npt.NDArray[np.float64]
    thickness: npt.NDArray[np.float64]
    relative_thickness_correction: npt.NDArray[np.float64]
    design_angle: npt.NDArray[np.float64]
    shear_angle: npt.NDArray[np.float64]
    draped_fiber_angle: npt.NDArray[np.float64]
    draped_transverse_angle: npt.NDArray[np.float64]
    area: npt.NDArray[np.float64]
    price: npt.NDArray[np.float64]
    volume: npt.NDArray[np.float64]
    mass: npt.NDArray[np.float64]
    offset: npt.NDArray[np.float64]
    cog: npt.NDArray[np.float64]


@dataclasses.dataclass
class ModelingPlyNodalData(NodalData):
    """Represents nodal data for a Modeling Ply."""

    ply_offset: npt.NDArray[np.float64]


@mark_grpc_properties
@register
class ModelingPly(CreatableTreeObject, IdTreeObject):
    """Instantiate an Oriented Selection Set.

    Parameters
    ----------
    name :
        The name of the ModelingPly
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "modeling_plies"
    OBJECT_INFO_TYPE = modeling_ply_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = modeling_ply_pb2.CreateRequest

    def __init__(
        self,
        name: str = "ModelingPly",
        ply_material: Fabric | None = None,
        oriented_selection_sets: Container[OrientedSelectionSet] = (),
        ply_angle: float = 0.0,
        number_of_layers: int = 1,
        active: bool = True,
        # Backend will automatically assign a consistent global_ply_nr
        # if global_ply_nr == 0
        global_ply_nr: int = 0,
    ):
        super().__init__(name=name)

        self.oriented_selection_sets = oriented_selection_sets
        self.ply_material = ply_material
        self.ply_angle = ply_angle
        self.number_of_layers = number_of_layers
        self.active = active
        self.global_ply_nr = global_ply_nr

    def _create_stub(self) -> modeling_ply_pb2_grpc.ObjectServiceStub:
        return modeling_ply_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    ply_material = grpc_link_property("properties.ply_material")

    oriented_selection_sets = define_linked_object_list(
        "properties.oriented_selection_sets", OrientedSelectionSet
    )

    ply_angle = grpc_data_property("properties.ply_angle")
    number_of_layers = grpc_data_property("properties.number_of_layers")
    active = grpc_data_property("properties.active")
    global_ply_nr = grpc_data_property("properties.global_ply_nr")

    elemental_data = elemental_data_property(ModelingPlyElementalData)
    nodal_data = nodal_data_property(ModelingPlyNodalData)
