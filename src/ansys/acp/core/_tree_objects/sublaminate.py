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

from collections.abc import Callable, Iterable, Sequence
import typing
from typing import Any, TypeAlias, Union, get_args

from typing_extensions import Self

from ansys.api.acp.v0 import sublaminate_pb2, sublaminate_pb2_grpc

from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from ._grpc_helpers.edge_property_list import (
    GenericEdgePropertyType,
    define_add_method,
    define_edge_property_list,
)
from ._grpc_helpers.polymorphic_from_pb import tree_object_from_resource_path
from ._grpc_helpers.property_helper import (
    _exposed_grpc_property,
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import SymmetryType, status_type_from_pb, symmetry_type_from_pb, symmetry_type_to_pb
from .fabric import Fabric
from .object_registry import register
from .stackup import Stackup

__all__ = ["SubLaminate", "Lamina"]

_LINKABLE_MATERIAL_TYPES: TypeAlias = Union[Fabric, Stackup]


@mark_grpc_properties
class Lamina(GenericEdgePropertyType):
    """
    Class to link a material with a sub-laminate.

    Parameters
    ----------
    material :
        Link to an existing fabric or stackup.
    angle :
        Orientation angle in degree of the material with respect to the reference direction.

    """

    _SUPPORTED_SINCE = "24.2"

    def __init__(self, material: _LINKABLE_MATERIAL_TYPES, angle: float = 0.0):
        self._callback_apply_changes: Callable[[], None] | None = None
        self.material = material
        self.angle = angle

    @_exposed_grpc_property
    def material(self) -> _LINKABLE_MATERIAL_TYPES:
        """Link to an existing fabric or stackup."""
        return self._material

    @material.setter
    def material(self, value: _LINKABLE_MATERIAL_TYPES) -> None:
        if not isinstance(value, get_args(_LINKABLE_MATERIAL_TYPES)):
            raise TypeError(
                f"Expected material to be of type {get_args(_LINKABLE_MATERIAL_TYPES)}, "
                f"got {type(value)}."
            )
        self._material: _LINKABLE_MATERIAL_TYPES = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def angle(self) -> float:
        """Orientation angle in degree of the material with respect to the reference direction."""
        return self._angle

    @angle.setter
    def angle(self, value: float) -> None:
        self._angle = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    def _set_callback_apply_changes(self, callback_apply_changes: Callable[[], None]) -> None:
        self._callback_apply_changes = callback_apply_changes

    @classmethod
    def _from_pb_object(
        cls,
        parent_object: CreatableTreeObject,
        message: sublaminate_pb2.Lamina,
        apply_changes: Callable[[], None],
    ) -> Lamina:
        material = tree_object_from_resource_path(
            resource_path=message.material, server_wrapper=parent_object._server_wrapper
        )

        if not isinstance(material, get_args(_LINKABLE_MATERIAL_TYPES)):
            raise TypeError(
                f"Expected material to be of type {get_args(_LINKABLE_MATERIAL_TYPES)}, "
                f"got {type(material)}."
            )

        material = typing.cast("_LINKABLE_MATERIAL_TYPES", material)
        new_obj = cls(
            material=material,
            angle=message.angle,
        )
        new_obj._set_callback_apply_changes(apply_changes)
        return new_obj

    def _to_pb_object(self) -> sublaminate_pb2.Lamina:
        return sublaminate_pb2.Lamina(material=self.material._resource_path, angle=self.angle)

    def _check(self) -> bool:
        # Check for empty resource paths
        return bool(self.material._resource_path.value)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return (
                self.material._resource_path == other.material._resource_path
                and self.angle == other.angle
            )

        return False

    def __repr__(self) -> str:
        return f"Lamina(material={self.material.__repr__()}, angle={self.angle})"

    def clone(self) -> Self:
        """Create a new unstored Lamina with the same properties."""
        return type(self)(material=self.material, angle=self.angle)


@mark_grpc_properties
@register
class SubLaminate(CreatableTreeObject, IdTreeObject):
    """Instantiate a SubLaminate.

    Parameters
    ----------
    name :
        Name of the sub-laminate.
    symmetry :
        Whether the sub-laminate is odd or even symmetrical, or none.
    topdown :
        The first material in the list is placed first in the mold if topdown is true.
    materials :
        List of materials (fabrics and stackups) with angles which build the sub-laminate.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "sublaminates"
    _OBJECT_INFO_TYPE = sublaminate_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = sublaminate_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "SubLaminate",
        symmetry: SymmetryType = "no_symmetry",
        topdown: bool = True,
        materials: Sequence[Lamina] = tuple(),
    ):
        super().__init__(name=name)

        self.symmetry = SymmetryType(symmetry)
        self.topdown = topdown
        self.materials = materials

    def _create_stub(self) -> sublaminate_pb2_grpc.ObjectServiceStub:
        return sublaminate_pb2_grpc.ObjectServiceStub(self._channel)

    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    thickness: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.thickness")
    area_weight: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.area_weight")
    area_price: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.area_price")

    symmetry = grpc_data_property(
        "properties.symmetry",
        from_protobuf=symmetry_type_from_pb,
        to_protobuf=symmetry_type_to_pb,
    )
    topdown: ReadWriteProperty[bool, bool] = grpc_data_property("properties.topdown")

    materials = define_edge_property_list("properties.materials", Lamina)
    add_material = define_add_method(
        Lamina,
        attribute_name="materials",
        func_name="add_material",
        parent_class_name="SubLaminate",
        module_name=__module__,
    )
