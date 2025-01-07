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
from functools import reduce

from google.protobuf.message import Message

from ansys.api.acp.v0 import extrusion_guide_pb2, extrusion_guide_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.property_helper import (
    _PROTOBUF_T,
    _get_data_attribute,
    _set_data_attribute,
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from ._grpc_helpers.protocols import ObjectInfo
from .base import CreatableTreeObject, IdTreeObject
from .edge_set import EdgeSet
from .enums import (
    ExtrusionGuideType,
    extrusion_guide_type_from_pb,
    extrusion_guide_type_to_pb,
    status_type_from_pb,
)
from .object_registry import register
from .virtual_geometry import VirtualGeometry

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip

__all__ = [
    "ExtrusionGuide",
]


@mark_grpc_properties
@register
class ExtrusionGuide(CreatableTreeObject, IdTreeObject):
    """Instantiate an Extrusion Guide of a Solid Model.

    Parameters
    ----------
    name :
        The name of the Oriented Selection Set.
    active :
        Inactive extrusion guides are not used in the solid model extrusion.
    edge_set :
        Edge Set along which the Extrusion Guide acts.
    extrusion_guide_type :
        Type of the extrusion such as by direction or by geometry.
    cad_geometry  :
        CAD geometry along which the extrusion guide runs.
        Needed if the extrusion type is set to :attr:`ExtrusionGuideType.BY_GEOMETRY`.
    direction :
        Direction along which the extrusion guide runs. Need if
        the extrusion type is set to :attr:`ExtrusionGuideType.BY_DIRECTION`.
    radius :
        Controls the sphere of influence for mesh morphing.
    depth :
        Defines the bias of the mesh morphing.
    use_curvature_correction :
        Apply a curvature correction during the solid model extrusion which results in
        a smoother extruded surface. Under certain circumstances, deactivating
        curvature correction can lead to better extrusion results.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "extrusion_guides"
    _OBJECT_INFO_TYPE = extrusion_guide_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = extrusion_guide_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "ExtrusionGuide",
        active: bool = True,
        edge_set: EdgeSet | None = None,
        extrusion_guide_type: ExtrusionGuideType = "by_direction",
        cad_geometry: VirtualGeometry | None = None,
        direction: tuple[float, float, float] = (0.0, 0.0, 1.0),
        radius: float = 0.0,
        depth: float = 0.0,
        use_curvature_correction: bool = False,
    ):
        super().__init__(name=name)
        self.active = active
        self.edge_set = edge_set
        self.extrusion_guide_type = ExtrusionGuideType(extrusion_guide_type)
        self.cad_geometry = cad_geometry
        self.direction = direction
        self.radius = radius
        self.depth = depth
        self.use_curvature_correction = use_curvature_correction

    def _create_stub(self) -> extrusion_guide_pb2_grpc.ObjectServiceStub:
        return extrusion_guide_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")

    edge_set = grpc_link_property("properties.edge_set", allowed_types=(EdgeSet,))

    extrusion_guide_type = grpc_data_property(
        "properties.extrusion_guide_type",
        from_protobuf=extrusion_guide_type_from_pb,
        to_protobuf=extrusion_guide_type_to_pb,
    )

    cad_geometry = grpc_link_property("properties.cad_geometry", allowed_types=(VirtualGeometry,))

    radius: ReadWriteProperty[float, float] = grpc_data_property("properties.radius")

    depth: ReadWriteProperty[float, float] = grpc_data_property("properties.depth")

    use_curvature_correction: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_curvature_correction"
    )

    # The extrusion guide type is not stored by the backend directly. Instead,
    # it is derived from the property direction. Therefore, setting and getting
    # the direction is blocked if the extrusion guide type is not `by_direction`.
    # See Feature 1122546 in ADO. Once resolved, this check becomes obsolete
    # but ensure backward compatibility.
    @staticmethod
    def _set_direction_attribute(pb_obj: ObjectInfo, name: str, value: _PROTOBUF_T) -> None:
        # name is "properties.direction"
        if (
            hasattr(pb_obj.properties, "extrusion_guide_type")
            and getattr(pb_obj.properties, "extrusion_guide_type")
            != extrusion_guide_pb2.BY_DIRECTION
        ):
            array = to_tuple_from_1D_array(value)
            if array and sum(array) != 0:
                raise RuntimeError(
                    "Cannot set direction if extrusion guide type is not 'by_direction'!"
                )
        _set_data_attribute(pb_obj, name, value)

    @staticmethod
    def _get_direction_attribute(pb_obj: Message, name: str, check_optional: bool) -> _PROTOBUF_T:
        # name is "properties.direction"
        name_parts = name.split(".")
        parent_obj = reduce(getattr, name_parts[:-1], pb_obj)
        if (
            hasattr(parent_obj, "extrusion_guide_type")
            and getattr(parent_obj, "extrusion_guide_type") != extrusion_guide_pb2.BY_DIRECTION
        ):
            raise RuntimeError(
                "Cannot access direction if the extrusion guide type is not 'by_direction'!"
            )
        return _get_data_attribute(pb_obj, name, check_optional)

    direction = grpc_data_property(
        "properties.direction",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
        setter_func=_set_direction_attribute,
        getter_func=_get_direction_attribute,
    )
