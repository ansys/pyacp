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

import numpy as np
import numpy.typing as npt

from .._utils.array_conversions import to_ND_double_array_from_numpy_or_list, to_numpy
from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_data_setter,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import (
    LookUpTableColumnValueType,
    PhysicalDimension,
    lookup_table_column_value_type_from_pb,
    lookup_table_column_value_type_to_pb,
    physical_dimension_from_pb,
    physical_dimension_to_pb,
)

__all__ = ["LookUpTableColumnBase"]


@mark_grpc_properties
class LookUpTableColumnBase(CreatableTreeObject, IdTreeObject):
    """Base class for columns of 1D and 3D look-up tables.

    Parameters
    ----------
    value_type :
        Determines whether the column data is scalar (one entry per row) or
        directional (three entries per row).
        Note that the ``value_type`` can only be set when constructing the
        column, and is read-only afterwards.
    physical_dimension :
        Dimensionality (such as time, length, force, ...) of the column data.
    data :
        The column data. The shape of the data must match the ``value_type``
        and the length of the ``Location`` column of the parent look-up
        table.
    """

    __slots__: Iterable[str] = tuple()

    def __init__(
        self,
        *,
        name: str,
        value_type: LookUpTableColumnValueType = LookUpTableColumnValueType.SCALAR,
        physical_dimension: PhysicalDimension = PhysicalDimension.DIMENSIONLESS,
        data: npt.NDArray[np.float64] | None = None,
    ):
        super().__init__(name=name)

        # Since the value_type is settable only before the 'data' is set [1],
        # we allow it only via the constructor. To nevertheless reuse the
        # property_helper code, we simply instantiate the setter function.
        #
        # [1] In the API, the 'data' and 'value_type' need to match.
        grpc_data_setter("properties.value_type", to_protobuf=lookup_table_column_value_type_to_pb)(
            self, value_type
        )

        self.physical_dimension = physical_dimension
        if data is not None:
            self.data = data

    value_type = grpc_data_property_read_only(
        "properties.value_type", from_protobuf=lookup_table_column_value_type_from_pb
    )

    # We renamed 'dimension_type' to 'physical_dimension' compared to the API, since
    # 'dimension_type' could also be understood as the number of spatial dimensions.
    physical_dimension = grpc_data_property(
        "properties.dimension_type",
        from_protobuf=physical_dimension_from_pb,
        to_protobuf=physical_dimension_to_pb,
    )
    data: ReadWriteProperty[npt.NDArray[np.float64], npt.NDArray[np.float64]] = grpc_data_property(
        "properties.data",
        from_protobuf=to_numpy,
        to_protobuf=to_ND_double_array_from_numpy_or_list,
    )
