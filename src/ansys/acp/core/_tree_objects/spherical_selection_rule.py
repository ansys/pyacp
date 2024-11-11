# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
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

from ansys.api.acp.v0 import spherical_selection_rule_pb2, spherical_selection_rule_pb2_grpc

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
from .enums import status_type_from_pb
from .object_registry import register
from .rosette import Rosette

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip
from ._elemental_or_nodal_data import ScalarData  # noqa: F401 isort:skip

__all__ = [
    "SphericalSelectionRule",
    "SphericalSelectionRuleElementalData",
    "SphericalSelectionRuleNodalData",
]


@dataclasses.dataclass
class SphericalSelectionRuleElementalData(ElementalData):
    """Represents elemental data for a Spherical Selection Rule."""

    normal: VectorData | None = None


@dataclasses.dataclass
class SphericalSelectionRuleNodalData(NodalData):
    """Represents nodal data for a Spherical Selection Rule."""


@mark_grpc_properties
@register
class SphericalSelectionRule(CreatableTreeObject, IdTreeObject):
    """Instantiate a Spherical Selection Rule.

    Parameters
    ----------
    name :
        Name of the Spherical Selection Rule.
    use_global_coordinate_system :
        Use global coordinate system for origin and direction.
    rosette :
        Rosette used for origin and direction. Only applies if
        ``use_global_coordinate_system`` is False.
    origin :
        Origin of the sphere.
    radius :
        Radius of the sphere.
    relative_rule :
        If True, parameters are evaluated relative to size of the object.
    include_rule :
        Include or exclude area in rule. Setting this to ``False``
        inverts the selection.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "spherical_selection_rules"
    _OBJECT_INFO_TYPE = spherical_selection_rule_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = spherical_selection_rule_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "SphericalSelectionrule",
        use_global_coordinate_system: bool = True,
        rosette: Rosette | None = None,
        origin: tuple[float, ...] = (0.0, 0.0, 0.0),
        radius: float = 0.0,
        relative_rule: bool = False,
        include_rule: bool = True,
    ):
        super().__init__(name=name)
        self.use_global_coordinate_system = use_global_coordinate_system
        self.rosette = rosette
        self.origin = origin
        self.radius = radius
        self.relative_rule = relative_rule
        self.include_rule = include_rule

    def _create_stub(self) -> spherical_selection_rule_pb2_grpc.ObjectServiceStub:
        return spherical_selection_rule_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    use_global_coordinate_system: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_global_coordinate_system"
    )
    rosette = grpc_link_property("properties.rosette", allowed_types=Rosette)
    origin = grpc_data_property(
        "properties.origin", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    direction = grpc_data_property(
        "properties.direction", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    radius: ReadWriteProperty[float, float] = grpc_data_property("properties.radius")
    relative_rule: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.relative_rule_type"
    )
    include_rule: ReadWriteProperty[bool, bool] = grpc_data_property("properties.include_rule_type")

    mesh = full_mesh_property
    shell_mesh = shell_mesh_property
    # selection rules don't have solid mesh data
    elemental_data = elemental_data_property(SphericalSelectionRuleElementalData)
    nodal_data = nodal_data_property(SphericalSelectionRuleNodalData)
