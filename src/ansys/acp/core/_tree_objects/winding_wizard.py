# Copyright (C) 2022 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

from collections.abc import Callable, Iterable, Sequence
from typing import Any, Self

from ansys.api.acp.v0 import winding_wizard_pb2, winding_wizard_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.edge_property_list import (
    GenericEdgePropertyType,
    define_add_method,
    define_edge_property_list,
)
from ._grpc_helpers.property_helper import (
    _exposed_grpc_property,
    grpc_data_property,
    mark_grpc_properties,
)
from ._import_object import ImportObjectMixin
from .base import (
    CreatableTreeObject,
    IdTreeObject,
)
from .fabric import Fabric
from .object_registry import register


@mark_grpc_properties
class Layer(GenericEdgePropertyType):
    """Defines a layer in the winding wizard.

    Parameters
    ----------
    fabric :
        Defines the fabric of this layer.
    nominal_angle :
        Angle with respect to the axis of symmetry in degree. Must be between -90 and 90 degrees.
    has_limits :
        Specifies if the ply has limits in the axial direction.
    lower_limit :
        Lower ply limit in axial direction.
    upper_limit :
        Upper ply limit in axial direction.
    add_mirrored_ply :
        Add an additional ply with the inverse angle.
    """

    _SUPPORTED_SINCE = "27.1"

    def __init__(
        self,
        fabric: Fabric,
        *,
        nominal_angle: float = 0.0,
        has_limits: bool = False,
        lower_limit: float = 0.0,
        upper_limit: float = 0.0,
        add_mirrored_ply: bool = False,
    ):
        self._callback_apply_changes: Callable[[], None] | None = None
        self.fabric = fabric
        self.nominal_angle = nominal_angle
        self.has_limits = has_limits
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.add_mirrored_ply = add_mirrored_ply

    @_exposed_grpc_property
    def fabric(self) -> Fabric:
        """Linked fabric."""
        return self._fabric

    @fabric.setter
    def fabric(self, value: Fabric) -> None:
        if not isinstance(value, Fabric):
            raise TypeError(f"Expected a Fabric, got {type(value)}")
        self._fabric = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def nominal_angle(self) -> float:
        """Angle with respect to the axis of symmetry in degree. Must be between -90 and 90 degrees."""
        return self._nominal_angle

    @nominal_angle.setter
    def nominal_angle(self, value: float) -> None:
        self._nominal_angle = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def has_limits(self) -> bool:
        """Specify if the ply has limits in the axial direction."""
        return self._has_limits

    @has_limits.setter
    def has_limits(self, value: bool) -> None:
        self._has_limits = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def lower_limit(self) -> float:
        """Lower ply limit in axial direction."""
        return self._lower_limit

    @lower_limit.setter
    def lower_limit(self, value: float) -> None:
        self._lower_limit = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def upper_limit(self) -> float:
        """Upper ply limit in axial direction."""
        return self._upper_limit

    @upper_limit.setter
    def upper_limit(self, value: float) -> None:
        self._upper_limit = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def add_mirrored_ply(self) -> bool:
        """Add an additional ply with the inverse angle."""
        return self._add_mirrored_ply

    @add_mirrored_ply.setter
    def add_mirrored_ply(self, value: bool) -> None:
        self._add_mirrored_ply = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    def _set_callback_apply_changes(self, callback: Callable[[], None]) -> None:
        self._callback_apply_changes = callback

    @classmethod
    def _from_pb_object(
        cls,
        parent_object: CreatableTreeObject,
        message: winding_wizard_pb2.Layer,
        apply_changes: Callable[[], None],
    ) -> Layer:
        new_obj = cls(
            fabric=Fabric._from_resource_path(message.fabric, parent_object._server_wrapper),
            nominal_angle=message.nominal_angle,
            has_limits=message.has_limits,
            lower_limit=message.lower_limit,
            upper_limit=message.upper_limit,
            add_mirrored_ply=message.add_mirrored_ply,
        )
        new_obj._set_callback_apply_changes(apply_changes)
        return new_obj

    def _to_pb_object(self) -> winding_wizard_pb2.Layer:
        return winding_wizard_pb2.Layer(
            fabric=self.fabric._resource_path,
            nominal_angle=self.nominal_angle,
            has_limits=self.has_limits,
            lower_limit=self.lower_limit,
            upper_limit=self.upper_limit,
            add_mirrored_ply=self.add_mirrored_ply,
        )

    def _check(self) -> bool:
        # Check for empty resource paths
        return bool(self.fabric._resource_path.value)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return (
                self.fabric._resource_path == other.fabric._resource_path
                and self.nominal_angle == other.nominal_angle
                and self.has_limits == other.has_limits
                and self.lower_limit == other.lower_limit
                and self.upper_limit == other.upper_limit
                and self.add_mirrored_ply == other.add_mirrored_ply
            )
        return False

    def __repr__(self) -> str:
        return (
            f"Layer(fabric={self.fabric!r}, "
            f"nominal_angle={self.nominal_angle}, "
            f"has_limits={self.has_limits}, "
            f"lower_limit={self.lower_limit}, "
            f"upper_limit={self.upper_limit}, "
            f"add_mirrored_ply={self.add_mirrored_ply})"
        )

    def clone(self) -> Self:
        """Create a new unstored layer with the same properties."""
        return type(self)(
            fabric=self.fabric,
            nominal_angle=self.nominal_angle,
            has_limits=self.has_limits,
            lower_limit=self.lower_limit,
            upper_limit=self.upper_limit,
            add_mirrored_ply=self.add_mirrored_ply,
        )


@mark_grpc_properties
@register
class WindingWizard(ImportObjectMixin, CreatableTreeObject, IdTreeObject):
    """Initialize a WindingWizard object.

    Parameters
    ----------
    name :
        Name of the winding wizard object.
    origin :
        Point on the axis of symmetry.
    reference_radius :
        Reference radius where nominal angle and nominal thickness are defined.
    axial_direction :
        Direction vector of the axis of symmetry.
    max_angle_with_thickness_correction :
        No thickness correction is applied for absolute angles above this limit.
    layers :
        Layer configuration for the winding wizard.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "winding_wizards"
    _OBJECT_INFO_TYPE = winding_wizard_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = winding_wizard_pb2.CreateRequest
    _SUPPORTED_SINCE = "27.1"

    def __init__(
        self,
        *,
        name: str = "WindingWizard",
        origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
        axial_direction: tuple[float, float, float] = (0.0, 0.0, 1.0),
        reference_radius: float = 0.0,
        max_angle_with_thickness_correction: float = 90.0,
        layers: Sequence[Layer] = (),
    ) -> None:
        super().__init__(name=name)
        self.origin = origin
        self.axial_direction = axial_direction
        self.reference_radius = reference_radius
        self.max_angle_with_thickness_correction = max_angle_with_thickness_correction
        self.layers = layers

    def _create_stub(self) -> winding_wizard_pb2_grpc.ObjectServiceStub:
        """Create a gRPC stub for the WindingWizard object."""
        return winding_wizard_pb2_grpc.ObjectServiceStub(self._channel)

    origin = grpc_data_property(
        "properties.origin",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    axial_direction = grpc_data_property(
        "properties.axial_direction",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    reference_radius: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.reference_radius"
    )
    max_angle_with_thickness_correction: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.max_angle_with_thickness_correction"
    )
    layers = define_edge_property_list("properties.layers", Layer)
    add_layer = define_add_method(
        Layer,
        attribute_name="layers",
        func_name="add_layer",
        parent_class_name="WindingWizard",
        module_name=__module__,
    )
