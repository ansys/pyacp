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

from collections.abc import Collection, Iterable

from ansys.api.acp.v0 import edge_set_pb2, edge_set_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_1D_int_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .element_set import ElementSet
from .enums import EdgeSetType, edge_set_type_from_pb, edge_set_type_to_pb, status_type_from_pb
from .object_registry import register


@mark_grpc_properties
@register
class EdgeSet(CreatableTreeObject, IdTreeObject):
    """Instantiate an edge set.

    Parameters
    ----------
    name :
        Name of the edge set.
    edge_set_type :
        Determines how the edge set is defined. Can be one of:

        * :attr:`.EdgeSetType.BY_REFERENCE`: define the edge set using an :class:`.ElementSet`.
        * :attr:`.EdgeSetType.BY_NODES`: define the edge set using a list of node labels.

    defining_node_labels :
        Labels of the nodes in the edge set.
        This parameter only applies when ``edge_set_type`` is :attr:`.EdgeSetType.BY_NODES`.
    element_set :
        The boundary of this element set defines the initial
        edge set.
        This parameter only applies when ``edge_set_type`` is :attr:`.EdgeSetType.BY_REFERENCE`.
    limit_angle :
        The edge set is cropped if the angle between two element edges exceeds this limits (in degrees).
        Use ``-1.`` to disable cropping.
        This parameter only applies when ``edge_set_type`` is :attr:`.EdgeSetType.BY_REFERENCE`.
    origin :
        Defines the starting point of the edge set.
        This parameter only applies when ``edge_set_type`` is :attr:`.EdgeSetType.BY_REFERENCE`.
    """

    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "edge_sets"
    _OBJECT_INFO_TYPE = edge_set_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = edge_set_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "EdgeSet",
        edge_set_type: EdgeSetType = EdgeSetType.BY_REFERENCE,
        defining_node_labels: Collection[int] = tuple(),
        element_set: ElementSet | None = None,
        limit_angle: float = -1.0,
        origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
    ):
        super().__init__(
            name=name,
        )
        self.edge_set_type = edge_set_type
        self.defining_node_labels = defining_node_labels
        self.element_set = element_set
        self.limit_angle = limit_angle
        self.origin = origin

    def _create_stub(self) -> edge_set_pb2_grpc.ObjectServiceStub:
        return edge_set_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")

    edge_set_type = grpc_data_property(
        "properties.edge_set_type",
        from_protobuf=edge_set_type_from_pb,
        to_protobuf=edge_set_type_to_pb,
    )
    defining_node_labels = grpc_data_property(
        "properties.defining_node_labels",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_int_array,
    )
    element_set = grpc_link_property("properties.element_set", allowed_types=ElementSet)
    limit_angle: ReadWriteProperty[float, float] = grpc_data_property("properties.limit_angle")
    origin = grpc_data_property(
        "properties.origin", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
