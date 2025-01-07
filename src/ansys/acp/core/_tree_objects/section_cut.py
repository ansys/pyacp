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

from collections.abc import Sequence

from ansys.api.acp.v0 import section_cut_pb2, section_cut_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from ._grpc_helpers.linked_object_list import define_linked_object_list
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .element_set import ElementSet
from .enums import (
    ExtrusionType,
    IntersectionType,
    SectionCutType,
    extrusion_type_from_pb,
    extrusion_type_to_pb,
    intersection_type_from_pb,
    intersection_type_to_pb,
    section_cut_type_from_pb,
    section_cut_type_to_pb,
    status_type_from_pb,
)
from .object_registry import register

__all__ = ["SectionCut"]


@mark_grpc_properties
@register
class SectionCut(CreatableTreeObject, IdTreeObject):
    r"""Instantiate a Section Cut.

    Parameters
    ----------
    name :
        Name of the section cut.
    active :
        Inactive section cuts are not evaluated.
    origin :
        Defines the origin of the section cut plane.
    normal :
        Defines the normal vector of the section cut plane.
    in_plane_reference_direction1 :
        Defines the in-plane transverse direction of the beam. Used for the surface
        section cut and section cut measures.
    scope_entire_model :
        If True, the section cut is applied to the entire model. Otherwise, the
        section cut is applied only to the element sets specified in
        ``scope_element_sets``.
    scope_element_sets :
        The element sets to which the section cut is applied. Used only if
        ``scope_entire_model`` is False.
    extrusion_type :
        Determines the extrusion method used to create the section cut.
    scale_factor :
        Scale factor applied to the ply thicknesses.
    core_scale_factor :
        Scale factor applied to the core thicknesses.
    section_cut_type :
        Determines whether the section cut is extruded by modeling ply, production
        ply, or analysis ply.
    intersection_type :
        Determines the method used to compute a wire frame section cut. Used only
        if ``extrusion_type`` is ``ExtrusionType.WIRE_FRAME``.
    use_default_tolerance :
        If True, the segment tolerance is computed as 0.1\% of the averaged element size.
        Otherwise, the ``tolerance`` value is used.
        Used only if ``extrusion_type`` is ``ExtrusionType.SURFACE_NORMAL`` or
        ``ExtrusionType.SURFACE_SWEEP_BASED``.
    tolerance :
        Defines the minimum length of the segments. Segments shorter than this value
        are merged.
        Used only if ``extrusion_type`` is ``ExtrusionType.SURFACE_NORMAL`` or
        ``ExtrusionType.SURFACE_SWEEP_BASED``, and ``use_default_tolerance`` is
        False.
    use_default_interpolation_settings :
        If True, default interpolation settings are used by the sweep-based extrusion.
        Used only if ``extrusion_type`` is ``ExtrusionType.SURFACE_SWEEP_BASED``.
    search_radius :
        Search radius of the interpolation algorithm used in the sweep-based extrusion.
        Used only if ``extrusion_type`` is ``ExtrusionType.SURFACE_SWEEP_BASED`` and
        ``use_default_interpolation_settings`` is False.
    number_of_interpolation_points :
        Number of interpolation points of the interpolation algorithm used in the
        sweep-based extrusion.
        Used only if ``extrusion_type`` is ``ExtrusionType.SURFACE_SWEEP_BASED`` and
        ``use_default_interpolation_settings`` is False.

    """

    __slots__ = ()

    _COLLECTION_LABEL = "section_cuts"
    _OBJECT_INFO_TYPE = section_cut_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = section_cut_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "SectionCut",
        active: bool = True,
        origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
        normal: tuple[float, float, float] = (0.0, 0.0, 1.0),
        in_plane_reference_direction1: tuple[float, float, float] = (1.0, 0.0, 0.0),
        scope_entire_model: bool = True,
        scope_element_sets: Sequence[ElementSet] = tuple(),
        extrusion_type: ExtrusionType = ExtrusionType.WIRE_FRAME,
        scale_factor: float = 1.0,
        core_scale_factor: float = 1.0,
        section_cut_type: SectionCutType = SectionCutType.MODELING_PLY_WISE,
        intersection_type: IntersectionType = IntersectionType.NORMAL_TO_SURFACE,
        use_default_tolerance: bool = True,
        tolerance: float = 0.0,
        use_default_interpolation_settings: bool = True,
        search_radius: float = 0.0,
        number_of_interpolation_points: int = 1,
    ) -> None:
        super().__init__(name=name)
        self.active = active
        self.origin = origin
        self.normal = normal
        self.in_plane_reference_direction1 = in_plane_reference_direction1
        self.scope_entire_model = scope_entire_model
        self.scope_element_sets = scope_element_sets
        self.extrusion_type = extrusion_type
        self.scale_factor = scale_factor
        self.core_scale_factor = core_scale_factor
        self.section_cut_type = section_cut_type
        self.intersection_type = intersection_type
        self.use_default_tolerance = use_default_tolerance
        self.tolerance = tolerance
        self.use_default_interpolation_settings = use_default_interpolation_settings
        self.search_radius = search_radius
        self.number_of_interpolation_points = number_of_interpolation_points

    def _create_stub(self) -> section_cut_pb2_grpc.ObjectServiceStub:
        return section_cut_pb2_grpc.ObjectServiceStub(self._channel)

    # general properties
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")

    # position properties
    origin = grpc_data_property(
        "properties.origin", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    normal = grpc_data_property(
        "properties.normal", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    in_plane_reference_direction1 = grpc_data_property(
        "properties.in_plane_reference_direction1",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )

    # scoping properties
    scope_entire_model: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.scope_entire_model"
    )
    scope_element_sets = define_linked_object_list("properties.scope_element_sets", ElementSet)

    # extrusion properties
    extrusion_type = grpc_data_property(
        "properties.extrusion_type",
        from_protobuf=extrusion_type_from_pb,
        to_protobuf=extrusion_type_to_pb,
    )
    scale_factor: ReadWriteProperty[float, float] = grpc_data_property("properties.scale_factor")
    core_scale_factor: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.core_scale_factor"
    )
    section_cut_type = grpc_data_property(
        "properties.section_cut_type",
        from_protobuf=section_cut_type_from_pb,
        to_protobuf=section_cut_type_to_pb,
    )

    # wireframe properties
    intersection_type = grpc_data_property(
        "properties.intersection_type",
        from_protobuf=intersection_type_from_pb,
        to_protobuf=intersection_type_to_pb,
    )

    # surface properties - general
    use_default_tolerance: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_default_tolerance"
    )
    tolerance: ReadWriteProperty[float, float] = grpc_data_property("properties.tolerance")
    # surface properties - sweep-based
    use_default_interpolation_settings: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_default_interpolation_settings"
    )
    search_radius: ReadWriteProperty[float, float] = grpc_data_property("properties.search_radius")
    number_of_interpolation_points: ReadWriteProperty[int, int] = grpc_data_property(
        "properties.number_of_interpolation_points"
    )
