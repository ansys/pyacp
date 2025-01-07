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
import dataclasses

from ansys.api.acp.v0 import boolean_selection_rule_pb2, boolean_selection_rule_pb2_grpc

from .._utils.property_protocols import ReadWriteProperty
from ._elemental_or_nodal_data import (
    ElementalData,
    NodalData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from ._grpc_helpers.edge_property_list import define_add_method, define_edge_property_list
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import full_mesh_property, shell_mesh_property
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .linked_selection_rule import LinkedSelectionRule
from .object_registry import register

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip
from ._elemental_or_nodal_data import ScalarData  # noqa: F401 isort:skip

__all__ = [
    "BooleanSelectionRule",
    "BooleanSelectionRuleElementalData",
    "BooleanSelectionRuleNodalData",
]


@dataclasses.dataclass
class BooleanSelectionRuleElementalData(ElementalData):
    """Represents elemental data for a Boolean Selection Rule."""

    normal: VectorData | None = None


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

    include_rule :
        Include or exclude area in rule. Setting this to ``False``
        inverts the selection.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "boolean_selection_rules"
    _OBJECT_INFO_TYPE = boolean_selection_rule_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = boolean_selection_rule_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "BooleanSelectionrule",
        selection_rules: Iterable[LinkedSelectionRule] = (),
        include_rule: bool = True,
    ):
        super().__init__(name=name)
        self.selection_rules = selection_rules
        self.include_rule = include_rule

    def _create_stub(self) -> boolean_selection_rule_pb2_grpc.ObjectServiceStub:
        return boolean_selection_rule_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    selection_rules = define_edge_property_list("properties.selection_rules", LinkedSelectionRule)
    add_selection_rule = define_add_method(
        LinkedSelectionRule,
        attribute_name="selection_rules",
        func_name="add_selection_rule",
        parent_class_name="BooleanSelectionRule",
        module_name=__module__,
    )

    include_rule: ReadWriteProperty[bool, bool] = grpc_data_property("properties.include_rule_type")

    mesh = full_mesh_property
    shell_mesh = shell_mesh_property
    # selection rules don't have solid mesh data

    elemental_data = elemental_data_property(BooleanSelectionRuleElementalData)
    nodal_data = nodal_data_property(BooleanSelectionRuleNodalData)
