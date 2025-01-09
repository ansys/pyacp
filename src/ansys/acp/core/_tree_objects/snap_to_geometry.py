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

from ansys.api.acp.v0 import snap_to_geometry_pb2, snap_to_geometry_pb2_grpc

from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import (
    SnapToGeometryOrientationType,
    snap_to_geometry_orientation_type_from_pb,
    snap_to_geometry_orientation_type_to_pb,
    status_type_from_pb,
)
from .object_registry import register
from .oriented_selection_set import OrientedSelectionSet
from .virtual_geometry import VirtualGeometry

__all__ = ["SnapToGeometry"]


@mark_grpc_properties
@register
class SnapToGeometry(CreatableTreeObject, IdTreeObject):
    """Instantiate a snap-to geometry.

    Parameters
    ----------
    name :
        Name of the snap-to geometry.
    active :
        Inactive snap-to geometries are not used in the solid model extrusion.
    orientation_type :
        Determines whether the snap-to geometry is applied to the top or bottom
        surface of the layup.
    cad_geometry :
        The geometry to snap to.
    oriented_selection_set :
        Defines the extent over which the snap-to geometry is applied. The normal
        of the oriented selection set is used to determine the top and bottom
        surfaces of the layup.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "snap_to_geometries"
    _OBJECT_INFO_TYPE = snap_to_geometry_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = snap_to_geometry_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "SnapToGeometry",
        active: bool = True,
        orientation_type: SnapToGeometryOrientationType = SnapToGeometryOrientationType.TOP,
        cad_geometry: VirtualGeometry | None = None,
        oriented_selection_set: OrientedSelectionSet | None = None,
    ):
        super().__init__(name=name)
        self.active = active
        self.orientation_type = orientation_type
        self.cad_geometry = cad_geometry
        self.oriented_selection_set = oriented_selection_set

    def _create_stub(self) -> snap_to_geometry_pb2_grpc.ObjectServiceStub:
        return snap_to_geometry_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")
    orientation_type = grpc_data_property(
        "properties.orientation_type",
        from_protobuf=snap_to_geometry_orientation_type_from_pb,
        to_protobuf=snap_to_geometry_orientation_type_to_pb,
    )
    cad_geometry = grpc_link_property("properties.cad_geometry", allowed_types=(VirtualGeometry,))
    oriented_selection_set = grpc_link_property(
        "properties.oriented_selection_set", allowed_types=(OrientedSelectionSet,)
    )
