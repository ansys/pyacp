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
from typing import Any

from typing_extensions import Self

from ansys.api.acp.v0 import stackup_pb2, stackup_pb2_grpc

from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from ._grpc_helpers.edge_property_list import (
    GenericEdgePropertyType,
    define_add_method,
    define_edge_property_list,
)
from ._grpc_helpers.property_helper import (
    _exposed_grpc_property,
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import (
    CutOffMaterialHandling,
    DrapingMaterialModel,
    DropOffMaterialHandling,
    SymmetryType,
    cut_off_material_type_from_pb,
    cut_off_material_type_to_pb,
    draping_material_type_from_pb,
    draping_material_type_to_pb,
    drop_off_material_type_from_pb,
    drop_off_material_type_to_pb,
    status_type_from_pb,
    symmetry_type_from_pb,
    symmetry_type_to_pb,
)
from .fabric import Fabric
from .material import Material
from .object_registry import register

__all__ = ["Stackup", "FabricWithAngle"]


@mark_grpc_properties
class FabricWithAngle(GenericEdgePropertyType):
    """Defines a fabric of a stackup.

    Parameters
    ----------
    fabric :
        Link to an existing fabric.
    angle :
        Orientation angle in degree of the fabric with respect to the reference direction.

    """

    _SUPPORTED_SINCE = "24.2"

    def __init__(self, fabric: Fabric, angle: float = 0.0):
        self._callback_apply_changes: Callable[[], None] | None = None
        self.fabric = fabric
        self.angle = angle

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
    def angle(self) -> float:
        """Orientation angle in degree of the fabric with respect to the reference direction."""
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
        message: stackup_pb2.FabricWithAngle,
        apply_changes: Callable[[], None],
    ) -> FabricWithAngle:
        new_obj = cls(
            fabric=Fabric._from_resource_path(message.fabric, parent_object._channel),
            angle=message.angle,
        )
        new_obj._set_callback_apply_changes(apply_changes)
        return new_obj

    def _to_pb_object(self) -> stackup_pb2.FabricWithAngle:
        return stackup_pb2.FabricWithAngle(fabric=self.fabric._resource_path, angle=self.angle)

    def _check(self) -> bool:
        # Check for empty resource paths
        return bool(self.fabric._resource_path.value)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return (
                self.fabric._resource_path == other.fabric._resource_path
                and self.angle == other.angle
            )

        return False

    def __repr__(self) -> str:
        return f"FabricWithAngle(fabric={self.fabric.__repr__()}, angle={self.angle})"

    def clone(self) -> Self:
        """Create a new unstored FabricWithAngle with the same properties."""
        return type(self)(fabric=self.fabric, angle=self.angle)


@mark_grpc_properties
@register
class Stackup(CreatableTreeObject, IdTreeObject):
    """Instantiate a Stackup.

    Parameters
    ----------
    name :
        Name of the stackup.
    symmetry :
        Whether the stackup is odd or even symmetrical, or none.
    topdown :
        The first fabric in the list is placed first in the mold if topdown is true.
    fabrics :
        List of fabrics with angles which build the stackup.
    area_price :
        Price per area of the stackup.
    drop_off_material_handling :
        Defines the material of drop-off elements in the solid model extrusion.
    drop_off_material :
        Specify the material of drop-off elements in the solid model.
    cut_off_material_handling :
        Defines the material of cut-off elements in solid models if cut-off geometries are active.
    cut_off_material :
        Define the cut-off material if a ply with this material is shaped by a cut-off geometry.
    draping_material_model :
        Specifies the draping model of the fabric.
    draping_ud_coefficient :
        Set the draping coefficient of the uni-directional draping model. Must be in the range of 0 to 1.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "stackups"
    _OBJECT_INFO_TYPE = stackup_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = stackup_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "Stackup",
        symmetry: SymmetryType = "no_symmetry",
        topdown: bool = True,
        fabrics: Sequence[FabricWithAngle] = tuple(),
        area_price: float = 0.0,
        drop_off_material_handling: DropOffMaterialHandling = "global",
        drop_off_material: Material | None = None,
        cut_off_material: Material | None = None,
        cut_off_material_handling: CutOffMaterialHandling = "computed",
        draping_material_model: DrapingMaterialModel = "woven",
        draping_ud_coefficient: float = 0.0,
    ):
        super().__init__(name=name)

        self.symmetry = SymmetryType(symmetry)
        self.topdown = topdown
        self.area_price = area_price
        self.fabrics = fabrics
        self.drop_off_material_handling = DropOffMaterialHandling(drop_off_material_handling)
        self.drop_off_material = drop_off_material
        self.cut_off_material_handling = CutOffMaterialHandling(cut_off_material_handling)
        self.cut_off_material = cut_off_material
        self.draping_material_model = DrapingMaterialModel(draping_material_model)
        self.draping_ud_coefficient = draping_ud_coefficient

    def _create_stub(self) -> stackup_pb2_grpc.ObjectServiceStub:
        return stackup_pb2_grpc.ObjectServiceStub(self._channel)

    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    thickness: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.thickness")
    area_weight: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.area_weight")

    symmetry = grpc_data_property(
        "properties.symmetry",
        from_protobuf=symmetry_type_from_pb,
        to_protobuf=symmetry_type_to_pb,
    )
    topdown: ReadWriteProperty[bool, bool] = grpc_data_property("properties.topdown")
    area_price: ReadWriteProperty[float, float] = grpc_data_property("properties.area_price")
    ignore_for_postprocessing: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.ignore_for_postprocessing"
    )

    drop_off_material_handling = grpc_data_property(
        "properties.drop_off_material_handling",
        from_protobuf=drop_off_material_type_from_pb,
        to_protobuf=drop_off_material_type_to_pb,
    )
    drop_off_material = grpc_link_property("properties.drop_off_material", allowed_types=Material)
    cut_off_material_handling = grpc_data_property(
        "properties.cut_off_material_handling",
        from_protobuf=cut_off_material_type_from_pb,
        to_protobuf=cut_off_material_type_to_pb,
    )
    cut_off_material = grpc_link_property("properties.cut_off_material", allowed_types=Material)
    draping_material_model = grpc_data_property(
        "properties.draping_material_model",
        from_protobuf=draping_material_type_from_pb,
        to_protobuf=draping_material_type_to_pb,
    )
    draping_ud_coefficient: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.draping_ud_coefficient"
    )

    fabrics = define_edge_property_list("properties.fabrics", FabricWithAngle)
    add_fabric = define_add_method(
        FabricWithAngle,
        attribute_name="fabrics",
        func_name="add_fabric",
        parent_class_name="Stackup",
        module_name=__module__,
    )
