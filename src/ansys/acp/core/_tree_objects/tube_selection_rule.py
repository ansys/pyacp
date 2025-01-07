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

from ansys.api.acp.v0 import tube_selection_rule_pb2, tube_selection_rule_pb2_grpc

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
from .enums import status_type_from_pb
from .object_registry import register

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip
from ._elemental_or_nodal_data import ScalarData  # noqa: F401 isort:skip

__all__ = [
    "TubeSelectionRule",
    "TubeSelectionRuleElementalData",
    "TubeSelectionRuleNodalData",
]


@dataclasses.dataclass
class TubeSelectionRuleElementalData(ElementalData):
    """Represents elemental data for a Tube Selection Rule."""

    normal: VectorData | None = None


@dataclasses.dataclass
class TubeSelectionRuleNodalData(NodalData):
    """Represents nodal data for a Tube Selection Rule."""


@mark_grpc_properties
@register
class TubeSelectionRule(CreatableTreeObject, IdTreeObject):
    """Instantiate a Tube Selection Rule.

    Parameters
    ----------
    name :
        Name of the Tube Selection Rule.
    edge_set :
        Edge Set defining the path of the tube.
    outer_radius :
        Outer radius of the tube.
    inner_radius :
        Inner radius of the tube.
    include_rule :
        Include or exclude area in rule. Setting this to ``False``
        inverts the selection.
    extend_endings :
        Enable this option to extend the endings of the tube.
    symmetrical_extension :
        Whether the extensions have equal length on both sides or not.
    head :
        Defines the head of the tube. Select a point nearby one of the free ends
        of the tube. Only needed if the extensions are asymmetric.
    head_extension :
        Defines the length of the extension at the head of the tube. In case of
        symmetry, this value is used for both sides.
    tail_extension :
        Defines the length of the extension at the tail of the tube. Only needed
        if the extensions are asymmetric.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "tube_selection_rules"
    _OBJECT_INFO_TYPE = tube_selection_rule_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = tube_selection_rule_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "TubeSelectionrule",
        edge_set: EdgeSet | None = None,
        outer_radius: float = 1.0,
        inner_radius: float = 0.0,
        include_rule: bool = True,
        extend_endings: bool = False,
        symmetrical_extension: bool = True,
        head: tuple[float, float, float] = (0.0, 0.0, 0.0),
        head_extension: float = 0.0,
        tail_extension: float = 0.0,
    ):
        super().__init__(name=name)
        self.edge_set = edge_set
        self.outer_radius = outer_radius
        self.inner_radius = inner_radius
        self.include_rule = include_rule
        self.extend_endings = extend_endings
        self.symmetrical_extension = symmetrical_extension
        self.head = head
        self.head_extension = head_extension
        self.tail_extension = tail_extension

    def _create_stub(self) -> tube_selection_rule_pb2_grpc.ObjectServiceStub:
        return tube_selection_rule_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    edge_set = grpc_link_property("properties.edge_set", allowed_types=EdgeSet)
    outer_radius: ReadWriteProperty[float, float] = grpc_data_property("properties.outer_radius")
    inner_radius: ReadWriteProperty[float, float] = grpc_data_property("properties.inner_radius")
    include_rule: ReadWriteProperty[bool, bool] = grpc_data_property("properties.include_rule_type")
    extend_endings: ReadWriteProperty[bool, bool] = grpc_data_property("properties.extend_endings")
    symmetrical_extension: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.symmetrical_extension"
    )
    head = grpc_data_property(
        "properties.head", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    head_extension: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.head_extension"
    )
    tail_extension: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.tail_extension"
    )

    mesh = full_mesh_property
    shell_mesh = shell_mesh_property
    # selection rules don't have solid mesh data
    elemental_data = elemental_data_property(TubeSelectionRuleElementalData)
    nodal_data = nodal_data_property(TubeSelectionRuleNodalData)
