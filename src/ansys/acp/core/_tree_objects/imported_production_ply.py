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

from ansys.api.acp.v0 import (
    imported_analysis_ply_pb2_grpc,
    imported_production_ply_pb2,
    imported_production_ply_pb2_grpc,
)

from .._utils.property_protocols import ReadOnlyProperty
from ._grpc_helpers.mapping import get_read_only_collection_property
from ._grpc_helpers.property_helper import (
    grpc_data_property_read_only,
    grpc_link_property_read_only,
    mark_grpc_properties,
)
from .base import IdTreeObject, ReadOnlyTreeObject
from .enums import status_type_from_pb
from .imported_analysis_ply import ImportedAnalysisPly
from .object_registry import register

__all__ = [
    "ImportedProductionPly",
]


@mark_grpc_properties
@register
class ImportedProductionPly(ReadOnlyTreeObject, IdTreeObject):
    """Instantiate an Imported Production Ply.

    Parameters
    ----------
    name: str
        The name of the imported production ply.
    material: Material
        Material of the imported production ply.
    angle: float
        Angle of the imported production ply in degrees.
    thickness: float
        Thickness of the imported production ply in degrees.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "imported_production_plies"
    _OBJECT_INFO_TYPE = imported_production_ply_pb2.ObjectInfo
    _SUPPORTED_SINCE = "25.1"

    def _create_stub(self) -> imported_production_ply_pb2_grpc.ObjectServiceStub:
        return imported_production_ply_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    material = grpc_link_property_read_only("properties.material")
    angle: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.angle")
    thickness: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.thickness")

    imported_analysis_plies = get_read_only_collection_property(
        ImportedAnalysisPly, imported_analysis_ply_pb2_grpc.ObjectServiceStub
    )
