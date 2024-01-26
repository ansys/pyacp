from __future__ import annotations

from collections.abc import Iterable
import dataclasses

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0 import analysis_ply_pb2_grpc, production_ply_pb2, production_ply_pb2_grpc

from .._utils.property_protocols import ReadOnlyProperty
from ._grpc_helpers.mapping import get_read_only_collection_property
from ._grpc_helpers.property_helper import (
    grpc_data_property_read_only,
    grpc_link_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import ElementalData, NodalData, elemental_data_property, nodal_data_property
from .analysis_ply import AnalysisPly
from .base import IdTreeObject, ReadOnlyTreeObject
from .enums import status_type_from_pb
from .object_registry import register

__all__ = ["ProductionPly", "ProductionPlyElementalData", "ProductionPlyNodalData"]


@dataclasses.dataclass
class ProductionPlyElementalData(ElementalData):
    """Represents elemental data for a Production Ply."""

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
class ProductionPlyNodalData(NodalData):
    """Represents nodal data for a Production Ply."""

    ply_offset: npt.NDArray[np.float64]


@mark_grpc_properties
@register
class ProductionPly(ReadOnlyTreeObject, IdTreeObject):
    """Instantiate a Production Ply.

    Parameters
    ----------
    name: str
        The name of the ProductionPly.
    material: Material
        Material of the production ply.
    angle: float
        Angle of the production ply in degrees.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "production_plies"
    OBJECT_INFO_TYPE = production_ply_pb2.ObjectInfo

    def _create_stub(self) -> production_ply_pb2_grpc.ObjectServiceStub:
        return production_ply_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    material = grpc_link_property_read_only("properties.material")
    angle: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.angle")
    elemental_data = elemental_data_property(ProductionPlyElementalData)
    nodal_data = nodal_data_property(ProductionPlyNodalData)

    analysis_plies = get_read_only_collection_property(
        AnalysisPly, analysis_ply_pb2_grpc.ObjectServiceStub
    )
