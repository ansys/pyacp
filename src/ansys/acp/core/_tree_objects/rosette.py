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

from ansys.api.acp.v0 import rosette_pb2, rosette_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadOnlyProperty
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .object_registry import register

__all__ = ["Rosette"]


@mark_grpc_properties
@register
class Rosette(CreatableTreeObject, IdTreeObject):
    """Instantiate a Rosette.

    Parameters
    ----------
    name :
        Name of the Rosette.
    origin :
        Coordinates of the Rosette origin.
    dir1 :
        Direction 1 (x-direction) vector of the Rosette.
    dir2 :
        Direction 2 (y-direction) vector of the Rosette.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "rosettes"
    _OBJECT_INFO_TYPE = rosette_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = rosette_pb2.CreateRequest

    def __init__(
        self,
        *,
        name: str = "Rosette",
        origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
        dir1: tuple[float, float, float] = (1.0, 0.0, 0.0),
        dir2: tuple[float, float, float] = (0.0, 1.0, 0.0),
    ):
        super().__init__(name=name)

        self.origin = origin
        self.dir1 = dir1
        self.dir2 = dir2

    def _create_stub(self) -> rosette_pb2_grpc.ObjectServiceStub:
        return rosette_pb2_grpc.ObjectServiceStub(self._channel)

    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    origin = grpc_data_property(
        "properties.origin", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    dir1 = grpc_data_property(
        "properties.dir1", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    dir2 = grpc_data_property(
        "properties.dir2", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
