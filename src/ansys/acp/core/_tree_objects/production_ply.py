from __future__ import annotations

from collections.abc import Iterable
import dataclasses

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0 import analysis_ply_pb2_grpc, production_ply_pb2, production_ply_pb2_grpc

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

    normal: PlotDataWrapper
    orientation: PlotDataWrapper
    reference_direction: PlotDataWrapper
    fiber_direction: PlotDataWrapper
    draped_fiber_direction: PlotDataWrapper
    transverse_direction: PlotDataWrapper
    draped_transverse_direction: PlotDataWrapper
    thickness: PlotDataWrapper
    relative_thickness_correction: PlotDataWrapper
    design_angle: PlotDataWrapper
    shear_angle: PlotDataWrapper
    draped_fiber_angle: PlotDataWrapper
    draped_transverse_angle: PlotDataWrapper
    area: PlotDataWrapper
    price: PlotDataWrapper
    volume: PlotDataWrapper
    mass: PlotDataWrapper
    offset: PlotDataWrapper
    cog: PlotDataWrapper


@dataclasses.dataclass
class ProductionPlyNodalData(NodalData):
    """Represents nodal data for a Production Ply."""

    ply_offset: PlotDataWrapper


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
    angle = grpc_data_property_read_only("properties.angle")
    elemental_data = elemental_data_property(ProductionPlyElementalData)
    nodal_data = nodal_data_property(ProductionPlyNodalData)

    analysis_plies = property(
        get_read_only_collection_property(AnalysisPly, analysis_ply_pb2_grpc.ObjectServiceStub)
    )
