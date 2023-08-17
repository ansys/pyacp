from __future__ import annotations

import dataclasses
from typing import Container, Iterable

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0 import modeling_ply_pb2, modeling_ply_pb2_grpc, production_ply_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from ._grpc_helpers.edge_property_list import define_edge_property_list
from ._grpc_helpers.linked_object_list import define_linked_object_list
from ._grpc_helpers.mapping import get_read_only_collection_property
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from ._mesh_data import ElementalData, NodalData, elemental_data_property, nodal_data_property
from .base import CreatableTreeObject, IdTreeObject
from .enums import DrapingType, draping_type_from_pb, draping_type_to_pb, status_type_from_pb
from .fabric import Fabric
from .linked_selection_rule import LinkedSelectionRule
from .lookup_table_1d_column import LookUpTable1DColumn
from .lookup_table_3d_column import LookUpTable3DColumn
from .object_registry import register
from .oriented_selection_set import OrientedSelectionSet
from .production_ply import ProductionPly

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
    """Instantiate an Modeling Ply.

    Parameters
    ----------
    name :
        The name of the ModelingPly
    ply_material :
        The material (fabric, stackup or sub-laminate) of the ply.
    ply_angle :
        Design angle between the reference direction and the ply fiber direction.
    number_of_layers :
        Number of times the plies are generated.
    active :
        Inactive plies are ignored in ACP and the downstream analysis.
    global_ply_nr :
        Defines the global ply order.
    selection_rules :
        Selection Rules which may limit the extent of the ply.
    draping :
        Chooses between different draping formulations.
    draping_seed_point :
        Starting point of the draping algorithm.
    auto_draping_direction :
        If ``True``, the fiber direction of the production ply at the draping
         seed point is used as draping direction.
    draping_direction :
        Set the primary draping direction for the draping algorithm. Only used if
        ``auto_draping_direction`` is ``False``.
    draping_mesh_size :
        Defines the mesh size for the draping algorithm.
    draping_thickness_correction :
        Enables the thickness correction of draped plies based on the draping
        shear angle.
    draping_angle_1_field :
        Correction angle between the fiber and draped fiber directions, in degree.
    draping_angle_2_field :
        Correction angle between the transverse and draped transverse directions,
        in degree. Optional, uses the same values as ``draping_angle_1_field``
        (no shear) by default.
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
        selection_rules: Iterable[LinkedSelectionRule] = (),
        draping: DrapingType = DrapingType.NO_DRAPING,
        draping_seed_point: tuple[float, float, float] = (0.0, 0.0, 0.0),
        auto_draping_direction: bool = True,
        draping_direction: tuple[float, float, float] = (1.0, 0.0, 0.0),
        draping_mesh_size: float | None = None,  # let the backend choose the default value
        draping_thickness_correction: bool = True,
        draping_angle_1_field: LookUpTable1DColumn | LookUpTable3DColumn | None = None,
        draping_angle_2_field: LookUpTable1DColumn | LookUpTable3DColumn | None = None,
    ):
        super().__init__(name=name)

        self.oriented_selection_sets = oriented_selection_sets
        self.ply_material = ply_material
        self.ply_angle = ply_angle
        self.number_of_layers = number_of_layers
        self.active = active
        self.global_ply_nr = global_ply_nr
        self.selection_rules = selection_rules
        self.draping = draping
        self.draping_seed_point = draping_seed_point
        self.auto_draping_direction = auto_draping_direction
        self.draping_direction = draping_direction
        if draping_mesh_size is not None:
            self.draping_mesh_size = draping_mesh_size
        self.draping_thickness_correction = draping_thickness_correction
        self.draping_angle_1_field = draping_angle_1_field
        self.draping_angle_2_field = draping_angle_2_field

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

    draping = grpc_data_property(
        "properties.draping", from_protobuf=draping_type_from_pb, to_protobuf=draping_type_to_pb
    )
    draping_seed_point = grpc_data_property(
        "properties.draping_seed_point",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    auto_draping_direction = grpc_data_property("properties.auto_draping_direction")
    draping_direction = grpc_data_property(
        "properties.draping_direction",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    draping_mesh_size = grpc_data_property("properties.draping_mesh_size")
    draping_thickness_correction = grpc_data_property("properties.draping_thickness_correction")
    draping_angle_1_field = grpc_link_property("properties.draping_angle_1_field")
    draping_angle_2_field = grpc_link_property("properties.draping_angle_2_field")

    selection_rules = define_edge_property_list("properties.selection_rules", LinkedSelectionRule)

    production_plies = property(
        get_read_only_collection_property(ProductionPly, production_ply_pb2_grpc.ObjectServiceStub)
    )

    elemental_data = elemental_data_property(ModelingPlyElementalData)
    nodal_data = nodal_data_property(ModelingPlyNodalData)
