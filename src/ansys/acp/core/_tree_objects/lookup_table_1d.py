from __future__ import annotations

from collections.abc import Iterable

from ansys.api.acp.v0 import (
    lookup_table_1d_column_pb2_grpc,
    lookup_table_1d_pb2,
    lookup_table_1d_pb2_grpc,
)

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from ._grpc_helpers.mapping import define_create_method, define_mutable_mapping
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .lookup_table_1d_column import LookUpTable1DColumn
from .object_registry import register

__all__ = ["LookUpTable1D"]


@mark_grpc_properties
@register
class LookUpTable1D(CreatableTreeObject, IdTreeObject):
    """Instantiate a 1D Look-Up Table.

    The one-dimensional look-up table is defined along an axis. The locations
    of the data points along the axis are defined by the ``Location`` column,
    which:

    * contains scalar data. When the column contains ``N`` data points (rows),
      it has shape ``(N, )``.
    * is automatically created when the look-up table is instantiated
    * cannot be deleted or renamed

    When the length of the ``Location`` column is changed, the data of the
    other columns is automatically either truncated, or extended with ``NaN``
    values to fit.

    Parameters
    ----------
    origin :
        Origin of the axis w.r.t. which the look-up table locations are
        defined.
    direction :
        Direction of the axis w.r.t. which the look-up table locations are
        defined.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "lookup_tables_1d"
    OBJECT_INFO_TYPE = lookup_table_1d_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = lookup_table_1d_pb2.CreateRequest

    def __init__(
        self,
        name: str = "LookUpTable1D",
        origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
        direction: tuple[float, float, float] = (0.0, 0.0, 0.0),
    ):
        super().__init__(name=name)

        self.origin = origin
        self.direction = direction

    def _create_stub(self) -> lookup_table_1d_pb2_grpc.ObjectServiceStub:
        return lookup_table_1d_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    origin = grpc_data_property(
        "properties.origin", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    direction = grpc_data_property(
        "properties.direction", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )

    create_column = define_create_method(
        LookUpTable1DColumn,
        func_name="create_column",
        parent_class_name="LookUpTable1D",
        module_name=__module__,
    )
    columns = define_mutable_mapping(
        LookUpTable1DColumn, lookup_table_1d_column_pb2_grpc.ObjectServiceStub
    )
