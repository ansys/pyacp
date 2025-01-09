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

from ansys.api.acp.v0 import fabric_pb2, fabric_pb2_grpc

from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from ._grpc_helpers.property_helper import (
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
    cut_off_material_type_from_pb,
    cut_off_material_type_to_pb,
    draping_material_type_from_pb,
    draping_material_type_to_pb,
    drop_off_material_type_from_pb,
    drop_off_material_type_to_pb,
    status_type_from_pb,
)
from .material import Material
from .object_registry import register

__all__ = ["Fabric"]


@mark_grpc_properties
@register
class Fabric(CreatableTreeObject, IdTreeObject):
    """Instantiate a Fabric.

    Parameters
    ----------
    name :
        Name of the fabric.
    material :
        Material of the fabric.
    thickness :
        Thickness of the fabric.
    area_price :
        Price per area of the fabric.
    ignore_for_postprocessing :
        Enable this option that the failure computation skips all plies made of this fabric.
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
    area_weight :
        Weight per area of the fabric. Read only.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "fabrics"
    _OBJECT_INFO_TYPE = fabric_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = fabric_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "Fabric",
        material: Material | None = None,
        thickness: float = 0.0,
        area_price: float = 0.0,
        ignore_for_postprocessing: bool = False,
        drop_off_material_handling: DropOffMaterialHandling = "global",
        drop_off_material: Material | None = None,
        cut_off_material_handling: CutOffMaterialHandling = "computed",
        cut_off_material: Material | None = None,
        draping_material_model: DrapingMaterialModel = "woven",
        draping_ud_coefficient: float = 0.0,
    ):
        super().__init__(name=name)

        self.material = material
        self.thickness = thickness
        self.area_price = area_price
        self.ignore_for_postprocessing = ignore_for_postprocessing
        self.drop_off_material_handling = DropOffMaterialHandling(drop_off_material_handling)
        self.drop_off_material = drop_off_material
        self.cut_off_material_handling = CutOffMaterialHandling(cut_off_material_handling)
        self.cut_off_material = cut_off_material
        self.draping_material_model = DrapingMaterialModel(draping_material_model)
        self.draping_ud_coefficient = draping_ud_coefficient

    def _create_stub(self) -> fabric_pb2_grpc.ObjectServiceStub:
        return fabric_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    area_weight: ReadOnlyProperty[float] = grpc_data_property_read_only("properties.area_weight")

    material = grpc_link_property("properties.material", allowed_types=Material)
    thickness: ReadWriteProperty[float, float] = grpc_data_property("properties.thickness")
    area_price: ReadWriteProperty[float, float] = grpc_data_property("properties.area_price")
    ignore_for_postprocessing: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.ignore_for_postprocessing"
    )

    drop_off_material_handling = grpc_data_property(
        "properties.drop_off_material_handling",
        from_protobuf=drop_off_material_type_from_pb,
        to_protobuf=drop_off_material_type_to_pb,
    )
    drop_off_material = grpc_link_property(
        "properties.drop_off_material",
        allowed_types=Material,
        readable_since="25.1",
        writable_since="25.1",
    )
    cut_off_material_handling = grpc_data_property(
        "properties.cut_off_material_handling",
        from_protobuf=cut_off_material_type_from_pb,
        to_protobuf=cut_off_material_type_to_pb,
    )
    cut_off_material = grpc_link_property(
        "properties.cut_off_material",
        allowed_types=Material,
        readable_since="25.1",
        writable_since="25.1",
    )

    draping_material_model = grpc_data_property(
        "properties.draping_material_model",
        from_protobuf=draping_material_type_from_pb,
        to_protobuf=draping_material_type_to_pb,
    )
    draping_ud_coefficient: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.draping_ud_coefficient"
    )
