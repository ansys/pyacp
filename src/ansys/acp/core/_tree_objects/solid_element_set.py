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
import dataclasses

from ansys.api.acp.v0 import solid_element_set_pb2, solid_element_set_pb2_grpc

from .._utils.array_conversions import to_tuple_from_1D_array
from .._utils.property_protocols import ReadOnlyProperty
from ._elemental_or_nodal_data import ElementalData, NodalData
from ._grpc_helpers.property_helper import grpc_data_property_read_only, mark_grpc_properties
from ._mesh_data import solid_mesh_property
from .base import IdTreeObject, ReadOnlyTreeObject
from .enums import status_type_from_pb
from .object_registry import register

__all__ = ["SolidElementSet", "SolidElementSetElementalData", "SolidElementSetNodalData"]


@dataclasses.dataclass
class SolidElementSetElementalData(ElementalData):
    """Represents elemental data for a Solid Element Set."""


@dataclasses.dataclass
class SolidElementSetNodalData(NodalData):
    """Represents nodal data for a Solid Element Set."""


@mark_grpc_properties
@register
class SolidElementSet(ReadOnlyTreeObject, IdTreeObject):
    """Instantiate a Solid Element Set.

    Parameters
    ----------
    name: str
        The name of the production ply.
    element_labels :
        Label of elements.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "solid_element_sets"
    _OBJECT_INFO_TYPE = solid_element_set_pb2.ObjectInfo
    _SUPPORTED_SINCE = "25.1"

    def _create_stub(self) -> solid_element_set_pb2_grpc.ObjectServiceStub:
        return solid_element_set_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    element_labels: ReadOnlyProperty[tuple[int, ...]] = grpc_data_property_read_only(
        "properties.element_labels", from_protobuf=to_tuple_from_1D_array
    )

    solid_mesh = solid_mesh_property
