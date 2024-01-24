from __future__ import annotations

from collections.abc import Iterable
import dataclasses

from ansys.api.acp.v0 import parallel_selection_rule_pb2, parallel_selection_rule_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
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
from .rosette import Rosette

__all__ = [
    "ParallelSelectionRule",
    "ParallelSelectionRuleElementalData",
    "ParallelSelectionRuleNodalData",
]


@dataclasses.dataclass
class ParallelSelectionRuleElementalData(ElementalData):
    """Represents elemental data for a Parallel Selection Rule."""

    normal: VectorData


@dataclasses.dataclass
class ParallelSelectionRuleNodalData(NodalData):
    """Represents nodal data for a Parallel Selection Rule."""


@mark_grpc_properties
@register
class ParallelSelectionRule(CreatableTreeObject, IdTreeObject):
    """Instantiate a Parallel Selection Rule.

    Parameters
    ----------
    name :
        Name of the Parallel Selection Rule.
    use_global_coordinate_system :
        Use global coordinate system for origin and direction.
    rosette :
        Rosette used for origin and direction. Only applies if
        ``use_global_coordinate_system`` is False.
    origin :
        Origin of the Parallel Selection Rule.
    direction :
        Direction of the Parallel Selection Rule.
    lower_limit :
        Negative distance of the Parallel Selection Rule.
    upper_limit :
        Positive distance of the Parallel Selection Rule.
    relative_rule_type :
        If True, parameters are evaluated relative to size of the object.
    include_rule_type :
        Include or exclude area in rule. Setting this to ``False``
        inverts the selection.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "parallel_selection_rules"
    OBJECT_INFO_TYPE = parallel_selection_rule_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = parallel_selection_rule_pb2.CreateRequest

    def __init__(
        self,
        name: str = "ParallelSelectionrule",
        use_global_coordinate_system: bool = True,
        rosette: Rosette | None = None,
        origin: tuple[float, ...] = (0.0, 0.0, 0.0),
        direction: tuple[float, ...] = (1.0, 0.0, 0.0),
        lower_limit: float = 0.0,
        upper_limit: float = 0.0,
        relative_rule_type: bool = False,
        include_rule_type: bool = True,
    ):
        super().__init__(name=name)
        self.use_global_coordinate_system = use_global_coordinate_system
        self.rosette = rosette
        self.origin = origin
        self.direction = direction
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.relative_rule_type = relative_rule_type
        self.include_rule_type = include_rule_type

    def _create_stub(self) -> parallel_selection_rule_pb2_grpc.ObjectServiceStub:
        return parallel_selection_rule_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    use_global_coordinate_system = grpc_data_property("properties.use_global_coordinate_system")
    rosette = grpc_link_property("properties.rosette")
    origin = grpc_data_property(
        "properties.origin", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    direction = grpc_data_property(
        "properties.direction", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    lower_limit = grpc_data_property("properties.lower_limit")
    upper_limit = grpc_data_property("properties.upper_limit")
    relative_rule_type = grpc_data_property("properties.relative_rule_type")
    include_rule_type = grpc_data_property("properties.include_rule_type")

    elemental_data = elemental_data_property(ParallelSelectionRuleElementalData)
    nodal_data = nodal_data_property(ParallelSelectionRuleNodalData)
