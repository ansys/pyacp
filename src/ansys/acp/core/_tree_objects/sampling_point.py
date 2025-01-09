# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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

from ansys.api.acp.v0 import sampling_point_pb2, sampling_point_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .object_registry import register
from .rosette import Rosette

__all__ = ["SamplingPoint"]


@mark_grpc_properties
@register
class SamplingPoint(CreatableTreeObject, IdTreeObject):
    """Instantiate a Sampling Point.

    Parameters
    ----------
    name :
        Name of the sampling point.
    point :
        Coordinates of the sampling point.
    direction :
        Direction of the sampling point.
    use_default_reference_direction :
        Whether to use the element coordinate system when computing the laminate
        properties (CLT).
    rosette :
        Rosette defining the coordinate system used when computing the laminate
        properties (CLT). Only used when ``use_default_reference_direction`` is False.
    offset_is_middle :
        Activate this option to offset the reference surface to the mid-plane of the
        laminate for the computation of the ABD matrices and laminate properties (CLT).
    consider_coupling_effect :
        Whether the computation of the laminate engineering constants should consider
        the coupling effect if the B-Matrix of the ABD-Matrix is not zero. Computation
        of the ABD matrices is not affected by this parameter.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "sampling_points"
    _OBJECT_INFO_TYPE = sampling_point_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = sampling_point_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "SamplingPoint",
        point: tuple[float, float, float] = (0.0, 0.0, 0.0),
        direction: tuple[float, float, float] = (0.0, 0.0, 0.0),
        use_default_reference_direction: bool = True,
        rosette: Rosette | None = None,
        offset_is_middle: bool = True,
        consider_coupling_effect: bool = True,
    ):
        super().__init__(name=name)

        self.point = point
        self.direction = direction
        self.use_default_reference_direction = use_default_reference_direction
        self.rosette = rosette
        self.offset_is_middle = offset_is_middle
        self.consider_coupling_effect = consider_coupling_effect

    def _create_stub(self) -> sampling_point_pb2_grpc.ObjectServiceStub:
        return sampling_point_pb2_grpc.ObjectServiceStub(self._channel)

    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    point = grpc_data_property(
        "properties.point", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    direction = grpc_data_property(
        "properties.direction", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    use_default_reference_direction: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_default_reference_direction"
    )
    rosette = grpc_link_property("properties.rosette", allowed_types=Rosette)
    reference_direction = grpc_data_property_read_only(
        "properties.reference_direction",
        from_protobuf=to_tuple_from_1D_array,
        doc="Local x-direction used in the computation of laminate properties (CLT).",
    )
    offset_is_middle: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.offset_is_middle"
    )
    consider_coupling_effect: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.consider_coupling_effect"
    )
