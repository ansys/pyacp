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
    lookup_table_3d_column_pb2_grpc,
    lookup_table_3d_pb2,
    lookup_table_3d_pb2_grpc,
)

from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.mapping import define_create_method, define_mutable_mapping
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import (
    LookUpTable3DInterpolationAlgorithm,
    lookup_table_3d_interpolation_algorithm_from_pb,
    lookup_table_3d_interpolation_algorithm_to_pb,
    status_type_from_pb,
)
from .lookup_table_3d_column import LookUpTable3DColumn
from .object_registry import register

__all__ = ["LookUpTable3D"]


@mark_grpc_properties
@register
class LookUpTable3D(CreatableTreeObject, IdTreeObject):
    """Instantiate a 3D Look-Up Table.

    The three-dimensional look-up table is defined by 3D data points. The
    locations of these data points are defined by the ``Location`` column,
    which:

    * has shape ``(N, 3)``, where ``N`` is the number of data points (rows)
    * is automatically created when the look-up table is instantiated
    * cannot be deleted or renamed

    When the length of the ``Location`` column is changed, the data of the
    other columns is automatically either truncated, or extended with ``NaN``
    values to fit.

    Parameters
    ----------
    interpolation_algorithm :
        Algorithm used to interpolate the values of the look-up table.
    use_default_search_radius :
        If ``True``, estimate the search radius used in the weightest nearest
        neighbor algorithm automatically.
    search_radius :
        Search radius used for the interpolation with the weighted nearest
        neighbor algorithm.
    num_min_neighbors :
        Minimum number of neighbors used for the interpolation when using the
        weighted nearest neighbor algorithm.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "lookup_tables_3d"
    _OBJECT_INFO_TYPE = lookup_table_3d_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = lookup_table_3d_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "LookUpTable3D",
        interpolation_algorithm: LookUpTable3DInterpolationAlgorithm = LookUpTable3DInterpolationAlgorithm.WEIGHTED_NEAREST_NEIGHBOR,  # noqa: E501
        use_default_search_radius: bool = True,
        search_radius: float = 0.0,
        num_min_neighbors: int = 1,
    ):
        super().__init__(name=name)

        self.interpolation_algorithm = interpolation_algorithm
        self.use_default_search_radius = use_default_search_radius
        self.search_radius = search_radius
        self.num_min_neighbors = num_min_neighbors

    def _create_stub(self) -> lookup_table_3d_pb2_grpc.ObjectServiceStub:
        return lookup_table_3d_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    interpolation_algorithm = grpc_data_property(
        "properties.interpolation_algorithm",
        from_protobuf=lookup_table_3d_interpolation_algorithm_from_pb,
        to_protobuf=lookup_table_3d_interpolation_algorithm_to_pb,
    )
    use_default_search_radius: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_default_search_radius"
    )
    search_radius: ReadWriteProperty[float, float] = grpc_data_property("properties.search_radius")
    num_min_neighbors: ReadWriteProperty[int, int] = grpc_data_property(
        "properties.num_min_neighbors"
    )

    create_column = define_create_method(
        LookUpTable3DColumn,
        func_name="create_column",
        parent_class_name="LookUpTable3D",
        module_name=__module__,
    )
    columns = define_mutable_mapping(
        LookUpTable3DColumn, lookup_table_3d_column_pb2_grpc.ObjectServiceStub
    )
