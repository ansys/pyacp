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

from ansys.api.acp.v0 import cutoff_selection_rule_pb2, cutoff_selection_rule_pb2_grpc

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
from .enums import (
    CutOffRuleType,
    PlyCutOffType,
    cut_off_rule_type_from_pb,
    cut_off_rule_type_to_pb,
    ply_cut_off_type_from_pb,
    ply_cut_off_type_to_pb,
    status_type_from_pb,
)
from .object_registry import register
from .virtual_geometry import VirtualGeometry

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip
from ._elemental_or_nodal_data import ScalarData  # noqa: F401 isort:skip


__all__ = [
    "CutOffSelectionRule",
    "CutOffSelectionRuleElementalData",
    "CutOffSelectionRuleNodalData",
]


@dataclasses.dataclass
class CutOffSelectionRuleElementalData(ElementalData):
    """Represents elemental data for a Cut-Off Selection Rule."""

    normal: VectorData | None = None


@dataclasses.dataclass
class CutOffSelectionRuleNodalData(NodalData):
    """Represents nodal data for a Cut-Off Selection Rule."""


@mark_grpc_properties
@register
class CutOffSelectionRule(CreatableTreeObject, IdTreeObject):
    """Instantiate a Cut-Off Selection Rule.

    Parameters
    ----------
    name :
        Name of the Cut-Off Selection Rule.
    cut_off_rule_type :
        Determines if the cut-off is defined by a geometry or by a tapering edge.
    cut_off_geometry :
        Geometry used to define the cut-off. Only applies if
        ``cut_off_rule_type`` is GEOMETRY.
    taper_edge_set :
        Edge used to define the cut-off. Only applies if
        ``cut_off_rule_type`` is :attr:`.CutOffRuleType.TAPER`.
    offset :
        Moves the cutting plane along the out-of-plane direction. Always measured
        from the reference surface.
    angle :
        Defines the angle between the cutting plane and the reference surface.
    ply_cut_off_type :
        Either the complete production ply is cut-off
        (:attr:`PlyCutOffType.PRODUCTION_PLY_CUTOFF`) or individual analysis plies
        (:attr:`PlyCutOffType.ANALYSIS_PLY_CUTOFF`).
    ply_tapering :
        Whether the tapering of analysis plies is enabled.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "cutoff_selection_rules"
    _OBJECT_INFO_TYPE = cutoff_selection_rule_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = cutoff_selection_rule_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "CutOffSelectionrule",
        cut_off_rule_type: CutOffRuleType = CutOffRuleType.GEOMETRY,
        cut_off_geometry: VirtualGeometry | None = None,
        taper_edge_set: EdgeSet | None = None,
        offset: float = 0.0,
        angle: float = 0.0,
        ply_cut_off_type: PlyCutOffType = PlyCutOffType.PRODUCTION_PLY_CUTOFF,
        ply_tapering: bool = False,
    ):
        super().__init__(name=name)
        self.cut_off_rule_type = cut_off_rule_type
        self.cut_off_geometry = cut_off_geometry
        self.taper_edge_set = taper_edge_set
        self.offset = offset
        self.angle = angle
        self.ply_cut_off_type = ply_cut_off_type
        self.ply_tapering = ply_tapering

    def _create_stub(self) -> cutoff_selection_rule_pb2_grpc.ObjectServiceStub:
        return cutoff_selection_rule_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    cut_off_rule_type = grpc_data_property(
        "properties.cutoff_rule_type",
        from_protobuf=cut_off_rule_type_from_pb,
        to_protobuf=cut_off_rule_type_to_pb,
    )
    cut_off_geometry = grpc_link_property(
        "properties.cutoff_geometry", allowed_types=VirtualGeometry
    )
    taper_edge_set = grpc_link_property("properties.taper_edge_set", allowed_types=EdgeSet)
    offset: ReadWriteProperty[float, float] = grpc_data_property("properties.offset")
    angle: ReadWriteProperty[float, float] = grpc_data_property("properties.angle")
    ply_cut_off_type = grpc_data_property(
        "properties.ply_cutoff_type",
        from_protobuf=ply_cut_off_type_from_pb,
        to_protobuf=ply_cut_off_type_to_pb,
    )
    ply_tapering: ReadWriteProperty[bool, bool] = grpc_data_property("properties.ply_tapering")

    mesh = full_mesh_property
    shell_mesh = shell_mesh_property
    # selection rules don't have solid mesh data
    elemental_data = elemental_data_property(CutOffSelectionRuleElementalData)
    nodal_data = nodal_data_property(CutOffSelectionRuleNodalData)
