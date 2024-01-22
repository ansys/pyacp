from __future__ import annotations

from collections.abc import Iterable

import numpy as np
import numpy.typing as npt

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
    dimension_type :
        Dimensionality (such as time, length, force, ...) of the column data.
    data :
        The column data. The shape of the data must match the ``value_type``
        and the length of the ``Location`` column of the parent look-up
        table.
    """

    __slots__: Iterable[str] = tuple()

    def __init__(
        self,
        name: str,
        value_type: LookUpTableColumnValueType = LookUpTableColumnValueType.SCALAR,
        dimension_type: DimensionType = DimensionType.DIMENSIONLESS,
        data: PlotDataWrapper | None = None,
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
