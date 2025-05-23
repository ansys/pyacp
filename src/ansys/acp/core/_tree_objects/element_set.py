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
import dataclasses

from ansys.api.acp.v0 import element_set_pb2, element_set_pb2_grpc

from .._utils.array_conversions import to_1D_int_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from ._elemental_or_nodal_data import (
    ElementalData,
    NodalData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import full_mesh_property, shell_mesh_property
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .object_registry import register

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip
from ._elemental_or_nodal_data import ScalarData  # noqa: F401 isort:skip

__all__ = [
    "ElementSet",
    "ElementSetElementalData",
    "ElementSetNodalData",
]


@dataclasses.dataclass
class ElementSetElementalData(ElementalData):
    """Represents elemental data for an Element Set."""

    normal: VectorData | None = None


@dataclasses.dataclass
class ElementSetNodalData(NodalData):
    """Represents nodal data for an Element Set."""


@mark_grpc_properties
@register
class ElementSet(CreatableTreeObject, IdTreeObject):
    """Instantiate an Element Set.

    Parameters
    ----------
    name :
        The name of the Element Set.
    middle_offset :
        If True, enforce that the laminate mid-plane is moved onto the reference surface.
    element_labels :
        Label of elements to be assigned to Element Set
    """

    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "element_sets"
    _OBJECT_INFO_TYPE = element_set_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = element_set_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "ElementSet",
        middle_offset: bool = False,
        element_labels: Collection[int] = tuple(),
    ):
        super().__init__(name=name)
        self.middle_offset = middle_offset
        self.element_labels = element_labels

    def _create_stub(self) -> element_set_pb2_grpc.ObjectServiceStub:
        return element_set_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    middle_offset: ReadWriteProperty[bool, bool] = grpc_data_property("properties.middle_offset")
    element_labels: ReadWriteProperty[tuple[int, ...], Collection[int]] = grpc_data_property(
        "properties.element_labels",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_int_array,
    )

    mesh = full_mesh_property
    shell_mesh = shell_mesh_property
    elemental_data = elemental_data_property(ElementSetElementalData)
    nodal_data = nodal_data_property(ElementSetNodalData)
