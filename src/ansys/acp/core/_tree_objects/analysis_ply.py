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

    normal: VectorData
    orientation: VectorData
    reference_direction: VectorData
    fiber_direction: VectorData
    draped_fiber_direction: VectorData
    transverse_direction: VectorData
    draped_transverse_direction: VectorData
    thickness: ScalarData[np.float64]
    relative_thickness_correction: ScalarData[np.float64]
    design_angle: ScalarData[np.float64]
    shear_angle: ScalarData[np.float64]
    draped_fiber_angle: ScalarData[np.float64]
    draped_transverse_angle: ScalarData[np.float64]
    area: ScalarData[np.float64]
    price: ScalarData[np.float64]
    volume: ScalarData[np.float64]
    mass: ScalarData[np.float64]
    offset: ScalarData[np.float64]
    material_1_direction: VectorData
    cog: VectorData


@dataclasses.dataclass
class AnalysisPlyNodalData(NodalData):
    """Represents nodal data for a Analysis Ply."""

    ply_offset: VectorData


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
    angle: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.angle")
    active_in_post_mode: ReadOnlyProperty[bool] = grpc_data_property_read_only(
        "properties.active_in_post_mode"
    )
    elemental_data = elemental_data_property(AnalysisPlyElementalData)
    nodal_data = nodal_data_property(AnalysisPlyNodalData)
