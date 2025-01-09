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

from ansys.api.acp.v0 import cut_off_geometry_pb2, cut_off_geometry_pb2_grpc

from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import (
    CutOffGeometryOrientationType,
    cut_off_geometry_orientation_type_from_pb,
    cut_off_geometry_orientation_type_to_pb,
    status_type_from_pb,
)
from .object_registry import register
from .virtual_geometry import VirtualGeometry

__all__ = ["CutOffGeometry"]


@mark_grpc_properties
@register
class CutOffGeometry(CreatableTreeObject, IdTreeObject):
    """Instantiate a cut-off geometry.

    Parameters
    ----------
    name :
        Name of the cut-off geometry.
    active :
        Inactive cut-off geometries are not used in the solid model extrusion.
    cad_geometry :
        The geometry defining the cut-off.
    orientation_type :
        Determines the cutting orientation of a surface/body geometry. Allows to
        switch between include and exclude.
    relative_merge_tolerance :
        Set the merging tolerance for neighboring nodes relative to the element size.
    """

    __slots__: Iterable[str] = ()

    _COLLECTION_LABEL = "cut_off_geometries"
    _OBJECT_INFO_TYPE = cut_off_geometry_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = cut_off_geometry_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "CutOffGeometry",
        active: bool = True,
        cad_geometry: VirtualGeometry | None = None,
        orientation_type: CutOffGeometryOrientationType = CutOffGeometryOrientationType.UP,
        relative_merge_tolerance: float = 0.1,
    ):
        super().__init__(
            name=name,
        )
        self.active = active
        self.cad_geometry = cad_geometry
        self.orientation_type = orientation_type
        self.relative_merge_tolerance = relative_merge_tolerance

    def _create_stub(self) -> cut_off_geometry_pb2_grpc.ObjectServiceStub:
        return cut_off_geometry_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")
    cad_geometry = grpc_link_property("properties.cad_geometry", allowed_types=(VirtualGeometry,))
    orientation_type = grpc_data_property(
        "properties.orientation",
        from_protobuf=cut_off_geometry_orientation_type_from_pb,
        to_protobuf=cut_off_geometry_orientation_type_to_pb,
    )
    relative_merge_tolerance: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.relative_merge_tolerance"
    )
