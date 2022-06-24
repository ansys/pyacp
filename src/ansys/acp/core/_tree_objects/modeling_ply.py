from __future__ import annotations

from typing import Container, Union

from ansys.api.acp.v0 import modeling_ply_pb2, modeling_ply_pb2_grpc

from .._grpc_helpers.linked_object_list import define_linked_object_list
from .._grpc_helpers.property_helper import grpc_data_property_read_only, grpc_link_property
from .._utils.enum_conversions import status_type_to_string
from .base import CreatableTreeObject
from .fabric import Fabric
from .object_registry import register
from .oriented_selection_set import OrientedSelectionSet

__all__ = ["ModelingPly"]


@register
class ModelingPly(CreatableTreeObject):
    """Instantiate an Oriented Selection Set.

    Parameters
    ----------
    name :
        The name of the ModelingPly
    """

    COLLECTION_LABEL = "modeling_plies"
    OBJECT_INFO_TYPE = modeling_ply_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = modeling_ply_pb2.CreateRequest

    def __init__(
        self,
        name: str = "ModelingPly",
        ply_material: Union[Fabric, None] = None,
        oriented_selection_sets: Container[OrientedSelectionSet] = (),
        ply_angle: float = 0.0,
        number_of_layers: int = 1,
        active: bool = True,
        # Todo: Think about a way to get a default for the global_ply_nr
        global_ply_nr: int = 1,
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

    id = grpc_data_property_read_only("info.id")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_to_string)

    ply_material = grpc_link_property("properties.ply_material")

    oriented_selection_sets = define_linked_object_list(
        "properties.oriented_selection_sets", OrientedSelectionSet
    )
