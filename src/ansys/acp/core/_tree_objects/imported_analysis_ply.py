# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

from collections.abc import Iterable
import dataclasses

import numpy as np

from ansys.api.acp.v0 import imported_analysis_ply_pb2, imported_analysis_ply_pb2_grpc

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

__all__ = ["ImportedAnalysisPly", "ImportedAnalysisPlyElementalData", "ImportedAnalysisPlyNodalData"]


@dataclasses.dataclass
class ImportedAnalysisPlyElementalData(ElementalData):
    """Represents elemental data for an Imported Analysis Ply."""

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
    # area: ScalarData[np.float64] | None = None
    # price: ScalarData[np.float64] | None = None
    # volume: ScalarData[np.float64] | None = None
    # mass: ScalarData[np.float64] | None = None
    # offset: ScalarData[np.float64] | None = None
    # material_1_direction: VectorData | None = None
    # cog: VectorData | None = None


@dataclasses.dataclass
class ImportedAnalysisPlyNodalData(NodalData):
    """Represents nodal data for an Analysis Ply."""

    # ply_offset: VectorData | None = None


@mark_grpc_properties
@register
class ImportedAnalysisPly(ReadOnlyTreeObject, IdTreeObject):
    """Instantiate an Imported Analysis Ply.

    Parameters
    ----------
    name: str
        The name of the Imported Analysis Ply.
    material: Material
        Material of the Imported Analysis ply.
    angle: float
        Angle of the Analysis ply in degrees.
    angle: thickness
        Thickness of the Analysis ply in degrees.
    active_in_post_mode: bool
        If False, deactivates the failure analysis for this ply during post-processing.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "imported_analysis_plies"
    _OBJECT_INFO_TYPE = imported_analysis_ply_pb2.ObjectInfo
    _SUPPORTED_SINCE = "25.1"

    def _create_stub(self) -> imported_analysis_ply_pb2_grpc.ObjectServiceStub:
        return imported_analysis_ply_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    material = grpc_link_property_read_only("properties.material")
    angle: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.angle")
    thickness: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.thickness")
    active_in_post_mode: ReadOnlyProperty[bool] = grpc_data_property_read_only(
        "properties.active_in_post_mode"
    )
    elemental_data = elemental_data_property(ImportedAnalysisPlyElementalData)
    nodal_data = nodal_data_property(ImportedAnalysisPlyNodalData)
