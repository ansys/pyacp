from __future__ import annotations

from collections.abc import Iterable
import dataclasses

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0 import analysis_ply_pb2, analysis_ply_pb2_grpc

from ._grpc_helpers.property_helper import (
    grpc_data_property_read_only,
    grpc_link_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import ElementalData, NodalData, elemental_data_property, nodal_data_property
from .base import IdTreeObject, ReadOnlyTreeObject
from .enums import status_type_from_pb
from .object_registry import register

__all__ = ["AnalysisPly", "AnalysisPlyElementalData", "AnalysisPlyNodalData"]


@dataclasses.dataclass
class AnalysisPlyElementalData(ElementalData):
    """Represents elemental data for a Analysis Ply."""

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
    material_1_direction: PlotDataWrapper
    cog: PlotDataWrapper


@dataclasses.dataclass
class AnalysisPlyNodalData(NodalData):
    """Represents nodal data for a Analysis Ply."""

    ply_offset: PlotDataWrapper


@mark_grpc_properties
@register
class AnalysisPly(ReadOnlyTreeObject, IdTreeObject):
    """Instantiate an Analysis Ply.

    Parameters
    ----------
    name: str
        The name of the Analysis Ply.
    material: Material
        Material of the Analysis ply.
    angle: float
        Angle of the Analysis ply in degrees.
    active_in_post_mode: bool
        If False, deactivates the failure analysis for this ply during post-processing.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "analysis_plies"
    OBJECT_INFO_TYPE = analysis_ply_pb2.ObjectInfo

    def _create_stub(self) -> analysis_ply_pb2_grpc.ObjectServiceStub:
        return analysis_ply_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    material = grpc_link_property_read_only("properties.material")
    angle = grpc_data_property_read_only("properties.angle")
    active_in_post_mode = grpc_data_property_read_only("properties.active_in_post_mode")
    elemental_data = elemental_data_property(AnalysisPlyElementalData)
    nodal_data = nodal_data_property(AnalysisPlyNodalData)
