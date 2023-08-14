from __future__ import annotations

import dataclasses
from typing import Iterable

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
    material_1_direction: npt.NDArray[np.float64]
    cog: npt.NDArray[np.float64]


@dataclasses.dataclass
class AnalysisPlyNodalData(NodalData):
    """Represents nodal data for a Analysis Ply."""

    ply_offset: npt.NDArray[np.float64]


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
