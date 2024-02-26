from __future__ import annotations

from collections.abc import Iterable
import dataclasses

import numpy as np

from ansys.api.acp.v0 import analysis_ply_pb2, analysis_ply_pb2_grpc

from .._utils.property_protocols import ReadOnlyProperty
from ._grpc_helpers.property_helper import (
    grpc_data_property_read_only,
    grpc_link_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import (
    ElementalData,
    NodalData,
    ScalarData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from .base import IdTreeObject, ReadOnlyTreeObject
from .enums import status_type_from_pb
from .object_registry import register

__all__ = ["AnalysisPly", "AnalysisPlyElementalData", "AnalysisPlyNodalData"]


@dataclasses.dataclass
class AnalysisPlyElementalData(ElementalData):
    """Represents elemental data for a Analysis Ply."""

    normal: VectorData | None = None
    orientation: VectorData | None = None
    reference_direction: VectorData | None = None
    fiber_direction: VectorData | None = None
    draped_fiber_direction: VectorData | None = None
    transverse_direction: VectorData | None = None
    draped_transverse_direction: VectorData | None = None
    thickness: ScalarData[np.float64] | None = None
    relative_thickness_correction: ScalarData[np.float64] | None = None
    design_angle: ScalarData[np.float64] | None = None
    shear_angle: ScalarData[np.float64] | None = None
    draped_fiber_angle: ScalarData[np.float64] | None = None
    draped_transverse_angle: ScalarData[np.float64] | None = None
    area: ScalarData[np.float64] | None = None
    price: ScalarData[np.float64] | None = None
    volume: ScalarData[np.float64] | None = None
    mass: ScalarData[np.float64] | None = None
    offset: ScalarData[np.float64] | None = None
    material_1_direction: VectorData | None = None
    cog: VectorData | None = None


@dataclasses.dataclass
class AnalysisPlyNodalData(NodalData):
    """Represents nodal data for an Analysis Ply."""

    ply_offset: VectorData | None = None


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
    _OBJECT_INFO_TYPE = analysis_ply_pb2.ObjectInfo

    def _create_stub(self) -> analysis_ply_pb2_grpc.ObjectServiceStub:
        return analysis_ply_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    material = grpc_link_property_read_only("properties.material")
    angle: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.angle")
    active_in_post_mode: ReadOnlyProperty[bool] = grpc_data_property_read_only(
        "properties.active_in_post_mode"
    )
    elemental_data = elemental_data_property(AnalysisPlyElementalData)
    nodal_data = nodal_data_property(AnalysisPlyNodalData)
