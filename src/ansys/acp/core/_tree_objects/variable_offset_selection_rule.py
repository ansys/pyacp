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

from ansys.api.acp.v0 import (
    variable_offset_selection_rule_pb2,
    variable_offset_selection_rule_pb2_grpc,
)

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadWriteProperty
from ._elemental_or_nodal_data import (
    ElementalData,
    NodalData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from ._mesh_data import full_mesh_property, shell_mesh_property
from .base import CreatableTreeObject, IdTreeObject
from .edge_set import EdgeSet
from .element_set import ElementSet
from .enums import status_type_from_pb
from .lookup_table_1d_column import LookUpTable1DColumn
from .object_registry import register

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip
from ._elemental_or_nodal_data import ScalarData  # noqa: F401 isort:skip

__all__ = [
    "VariableOffsetSelectionRule",
    "VariableOffsetSelectionRuleElementalData",
    "VariableOffsetSelectionRuleNodalData",
]


@dataclasses.dataclass
class VariableOffsetSelectionRuleElementalData(ElementalData):
    """Represents elemental data for a VariableOffset Selection Rule."""

    normal: VectorData | None = None


@dataclasses.dataclass
class VariableOffsetSelectionRuleNodalData(NodalData):
    """Represents nodal data for a VariableOffset Selection Rule."""


@mark_grpc_properties
@register
class VariableOffsetSelectionRule(CreatableTreeObject, IdTreeObject):
    """Instantiate a Variable Offset Selection Rule.

    Parameters
    ----------
    name :
        Name of the Variable Offset Selection Rule.
    edge_set :
        Defines the edge along which the rule will be applied to.
    offsets :
        Defines the in-plane offset. Cuts elements which are closer to the edge than this value.
    angles :
        Defines the angle between the reference surface and the cutting plane.
    include_rule :
        Include or exclude area in rule. Setting this to ``False``
        inverts the selection.
    use_offset_correction :
        If enabled, then the offset is measured along the surface of the selected Element Set.
    element_set :
        Defines the surface on which the offset correction is calculated on.
    inherit_from_lookup_table :
        Specifies whether to inherit the Look-Up Table object properties.
    radius_origin :
        Origin of the look-up table axis. Only applies if ``inherit_from_lookup_table``
        is ``False``.
    radius_direction :
        Direction of the look-up table axis. Only applies if ``inherit_from_lookup_table``
        is ``False``.
    distance_along_edge :
        If ``True``, the look-up locations are evaluated along the edge, instead of along
        the axis direction.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "variable_offset_selection_rules"
    _OBJECT_INFO_TYPE = variable_offset_selection_rule_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = variable_offset_selection_rule_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "VariableOffsetSelectionrule",
        edge_set: EdgeSet | None = None,
        offsets: LookUpTable1DColumn | None = None,
        angles: LookUpTable1DColumn | None = None,
        include_rule: bool = True,
        use_offset_correction: bool = False,
        element_set: ElementSet | None = None,
        inherit_from_lookup_table: bool = True,
        radius_origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
        radius_direction: tuple[float, float, float] = (1.0, 0.0, 0.0),
        distance_along_edge: bool = False,
    ):
        super().__init__(name=name)
        self.edge_set = edge_set
        self.offsets = offsets
        self.angles = angles
        self.include_rule = include_rule
        self.use_offset_correction = use_offset_correction
        self.element_set = element_set
        self.inherit_from_lookup_table = inherit_from_lookup_table
        self.radius_origin = radius_origin
        self.radius_direction = radius_direction
        self.distance_along_edge = distance_along_edge

    def _create_stub(self) -> variable_offset_selection_rule_pb2_grpc.ObjectServiceStub:
        return variable_offset_selection_rule_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    edge_set = grpc_link_property("properties.edge_set", allowed_types=EdgeSet)
    offsets = grpc_link_property("properties.offsets", allowed_types=LookUpTable1DColumn)
    angles = grpc_link_property("properties.angles", allowed_types=LookUpTable1DColumn)
    include_rule: ReadWriteProperty[bool, bool] = grpc_data_property("properties.include_rule_type")
    use_offset_correction: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_offset_correction"
    )
    element_set = grpc_link_property("properties.element_set", allowed_types=ElementSet)
    inherit_from_lookup_table: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.inherit_from_lookup_table"
    )
    radius_origin = grpc_data_property(
        "properties.radius_origin",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    radius_direction = grpc_data_property(
        "properties.radius_direction",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    distance_along_edge: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.distance_along_edge"
    )

    mesh = full_mesh_property
    shell_mesh = shell_mesh_property
    # selection rules don't have solid mesh data
    elemental_data = elemental_data_property(VariableOffsetSelectionRuleElementalData)
    nodal_data = nodal_data_property(VariableOffsetSelectionRuleNodalData)
