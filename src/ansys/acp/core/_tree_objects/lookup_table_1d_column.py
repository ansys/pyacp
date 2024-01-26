from __future__ import annotations

from collections.abc import Iterable

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0 import lookup_table_1d_column_pb2, lookup_table_1d_column_pb2_grpc

from ._grpc_helpers.property_helper import mark_grpc_properties
from .enums import DimensionType, LookUpTableColumnValueType
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
    dimension_type :
        Dimensionality (such as time, length, force, ...) of the column data.
    data :
        The column data. The shape of the data must match the ``value_type``
        and the length of the ``Location`` column of the parent look-up
        table.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "lookup_table_1d_columns"
    OBJECT_INFO_TYPE = lookup_table_1d_column_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = lookup_table_1d_column_pb2.CreateRequest

    def __init__(
        self,
        *,
        name: str = "LookUpTable1DColumn",
        value_type: LookUpTableColumnValueType = LookUpTableColumnValueType.SCALAR,
        dimension_type: DimensionType = DimensionType.DIMENSIONLESS,
        data: npt.NDArray[np.float64] | None = None,
    ):
        super().__init__(name=name, value_type=value_type, dimension_type=dimension_type, data=data)

    def _create_stub(self) -> lookup_table_1d_column_pb2_grpc.ObjectServiceStub:
        return lookup_table_1d_column_pb2_grpc.ObjectServiceStub(self._channel)
