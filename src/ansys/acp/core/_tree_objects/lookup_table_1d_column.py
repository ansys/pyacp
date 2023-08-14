from __future__ import annotations

from typing import Iterable

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0 import lookup_table_1d_column_pb2, lookup_table_1d_column_pb2_grpc

from .._utils.array_conversions import to_ND_double_array_from_numpy, to_numpy
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_data_setter,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import (
    DimensionType,
    LookUpTableColumnValueType,
    dimension_type_from_pb,
    dimension_type_to_pb,
    lookup_table_column_value_type_from_pb,
    lookup_table_column_value_type_to_pb,
    status_type_from_pb,
)
from .object_registry import register

__all__ = ["LookUpTable1DColumn"]


@mark_grpc_properties
@register
class LookUpTable1DColumn(CreatableTreeObject, IdTreeObject):
    """Instantiate a Column of a 1D Look-Up Table.

    Parameters
    ----------
    value_type :
        Determines whether the column data is scalar (one entry per row) or
        directional (three entries per row).
    dimension_type :
        Dimensionality of the column data.
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
        name: str = "LookUpTable1DColumn",
        value_type: LookUpTableColumnValueType = LookUpTableColumnValueType.SCALAR,
        dimension_type: DimensionType = DimensionType.DIMENSIONLESS,
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

        self.dimension_type = dimension_type
        if data is not None:
            self.data = data

    def _create_stub(self) -> lookup_table_1d_column_pb2_grpc.ObjectServiceStub:
        return lookup_table_1d_column_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    value_type = grpc_data_property_read_only(
        "properties.value_type", from_protobuf=lookup_table_column_value_type_from_pb
    )
    dimension_type = grpc_data_property(
        "properties.dimension_type",
        from_protobuf=dimension_type_from_pb,
        to_protobuf=dimension_type_to_pb,
    )
    data = grpc_data_property(
        "properties.data",
        from_protobuf=to_numpy,
        to_protobuf=to_ND_double_array_from_numpy,
    )
