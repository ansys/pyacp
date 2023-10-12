from __future__ import annotations

from collections.abc import Iterable
import dataclasses

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0 import boolean_selection_rule_pb2, boolean_selection_rule_pb2_grpc

from ._grpc_helpers.edge_property_list import define_edge_property_list
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import ElementalData, NodalData, elemental_data_property, nodal_data_property
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .linked_selection_rule import LinkedSelectionRule
from .object_registry import register

__all__ = [
    "BooleanSelectionRule",
    "BooleanSelectionRuleElementalData",
    "BooleanSelectionRuleNodalData",
]


@dataclasses.dataclass
class BooleanSelectionRuleElementalData(ElementalData):
    """Represents elemental data for a Boolean Selection Rule."""

    normal: npt.NDArray[np.float64]


@dataclasses.dataclass
class BooleanSelectionRuleNodalData(NodalData):
    """Represents nodal data for a Boolean Selection Rule."""


@mark_grpc_properties
@register
class BooleanSelectionRule(CreatableTreeObject, IdTreeObject):
    """Instantiate a Boolean Selection Rule.

    Parameters
    ----------
    name :
        Name of the Boolean Selection Rule.
    selection_rules :

    include_rule_type :
        Include or exclude area in rule. Setting this to ``False``
        inverts the selection.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "boolean_selection_rules"
    OBJECT_INFO_TYPE = boolean_selection_rule_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = boolean_selection_rule_pb2.CreateRequest

    def __init__(
        self,
        name: str = "BooleanSelectionrule",
        selection_rules: Iterable[LinkedSelectionRule] = (),
        include_rule_type: bool = True,
    ):
        super().__init__(name=name)
        self.selection_rules = selection_rules
        self.include_rule_type = include_rule_type

    def _create_stub(self) -> boolean_selection_rule_pb2_grpc.ObjectServiceStub:
        return boolean_selection_rule_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    selection_rules = define_edge_property_list("properties.selection_rules", LinkedSelectionRule)
    include_rule_type = grpc_data_property("properties.include_rule_type")

    elemental_data = elemental_data_property(BooleanSelectionRuleElementalData)
    nodal_data = nodal_data_property(BooleanSelectionRuleNodalData)
