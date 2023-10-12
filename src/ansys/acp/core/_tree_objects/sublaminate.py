from __future__ import annotations

from collections.abc import Iterable, Sequence
import typing
from typing import Any, Callable, Union, get_args

from ansys.api.acp.v0 import sublaminate_pb2, sublaminate_pb2_grpc

from ._grpc_helpers.edge_property_list import GenericEdgePropertyType, define_edge_property_list
from ._grpc_helpers.polymorphic_from_pb import tree_object_from_resource_path
from ._grpc_helpers.property_helper import (
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

_LINKABLE_MATERIAL_TYPES = Union[Fabric, Stackup]


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

    def __init__(self, material: _LINKABLE_MATERIAL_TYPES, angle: float = 0.0):
        self._material = material
        self._angle = angle
        self._callback_apply_changes: Callable[[], None] | None = None

    @property
    def material(self) -> _LINKABLE_MATERIAL_TYPES:
        return self._material

    @material.setter
    def material(self, value: _LINKABLE_MATERIAL_TYPES) -> None:
        self._material = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    @property
    def angle(self) -> float:
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
            resource_path=message.material, channel=parent_object._channel
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
    OBJECT_INFO_TYPE = sublaminate_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = sublaminate_pb2.CreateRequest

    def __init__(
        self,
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

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    thickness = grpc_data_property_read_only("properties.thickness")
    area_weight = grpc_data_property_read_only("properties.area_weight")
    area_price = grpc_data_property_read_only("properties.area_price")

    symmetry = grpc_data_property(
        "properties.symmetry",
        from_protobuf=symmetry_type_from_pb,
        to_protobuf=symmetry_type_to_pb,
    )
    topdown = grpc_data_property("properties.topdown")

    materials = define_edge_property_list("properties.materials", Lamina)
