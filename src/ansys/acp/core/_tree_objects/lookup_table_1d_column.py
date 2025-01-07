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

from ansys.api.acp.v0 import lookup_table_1d_column_pb2, lookup_table_1d_column_pb2_grpc

from ._grpc_helpers.property_helper import mark_grpc_properties
from .enums import LookUpTableColumnValueType, PhysicalDimension
from .lookup_table_column_base import LookUpTableColumnBase
from .object_registry import register

__all__ = ["LookUpTable1DColumn"]


@mark_grpc_properties
@register
class LookUpTable1DColumn(LookUpTableColumnBase):
    """Instantiate a Column of a 1D Look-Up Table.

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

    _COLLECTION_LABEL = "lookup_table_1d_columns"
    _OBJECT_INFO_TYPE = lookup_table_1d_column_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = lookup_table_1d_column_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "LookUpTable1DColumn",
        value_type: LookUpTableColumnValueType = LookUpTableColumnValueType.SCALAR,
        physical_dimension: PhysicalDimension = PhysicalDimension.DIMENSIONLESS,
        data: npt.NDArray[np.float64] | None = None,
    ):
        super().__init__(
            name=name, value_type=value_type, physical_dimension=physical_dimension, data=data
        )

    def _create_stub(self) -> lookup_table_1d_column_pb2_grpc.ObjectServiceStub:
        return lookup_table_1d_column_pb2_grpc.ObjectServiceStub(self._channel)
