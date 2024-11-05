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

from collections.abc import Collection, Iterable
import dataclasses

from ansys.api.acp.v0 import solid_element_set_pb2, solid_element_set_pb2_grpc

from .._utils.array_conversions import to_1D_int_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import (
    ElementalData,
    NodalData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .object_registry import register

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip
from ._mesh_data import ScalarData  # noqa: F401 isort:skip

__all__ = [
    "SolidElementSet",
    "SolidElementSetElementalData",
    "SolidElementSetNodalData",
]


@dataclasses.dataclass
class SolidElementSetElementalData(ElementalData):
    """Represents elemental data for a Solid Element Set."""

    normal: VectorData | None = None


@dataclasses.dataclass
class SolidElementSetNodalData(NodalData):
    """Represents nodal data for a Solid Element Set."""


@mark_grpc_properties
@register
class SolidElementSet(CreatableTreeObject, IdTreeObject):
    """Instantiate a Solid Element Set.

    Parameters
    ----------
    name :
        The name of the Solid Element Set.
    element_labels :
        Label of solid elements to be assigned to the Solid Element Set
    """

    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "solid_element_sets"
    _OBJECT_INFO_TYPE = solid_element_set_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = solid_element_set_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "SolidElementSet",
        element_labels: Collection[int] = tuple(),
    ):
        super().__init__(name=name)
        self.element_labels = element_labels

    def _create_stub(self) -> solid_element_set_pb2_grpc.ObjectServiceStub:
        return solid_element_set_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    element_labels: ReadWriteProperty[tuple[int, ...], Collection[int]] = grpc_data_property(
        "properties.element_labels",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_int_array,
    )

    elemental_data = elemental_data_property(SolidElementSetElementalData)
    nodal_data = nodal_data_property(SolidElementSetNodalData)
