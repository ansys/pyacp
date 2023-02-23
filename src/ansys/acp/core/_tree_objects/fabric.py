from __future__ import annotations

from typing import Iterable

from ansys.api.acp.v0 import fabric_pb2, fabric_pb2_grpc

from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import (
    CutoffMaterialType,
    DrapingMaterialType,
    DropoffMaterialType,
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
        Name of the Rosette.
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
    cut_off_material_handling :
        Defines the material of cut-off elements in solid models if cut-off geometries are active.
    draping_material_model :
        Specifies the draping model of the fabric.
    draping_ud_coefficient :
        Set the draping coefficient of the uni-directional draping model. Must be in the range of 0 to 1.

    """

    __slots__: Iterable[str] = tuple()

    COLLECTION_LABEL = "fabrics"
    OBJECT_INFO_TYPE = fabric_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = fabric_pb2.CreateRequest

    def __init__(
        self,
        name: str = "Fabric",
        material: Material | None = None,
        thickness: float = 0.0,
        area_price: float = 0.0,
        ignore_for_postprocessing: bool = False,
        drop_off_material_handling: DropoffMaterialType = "global",
        cut_off_material_handling: CutoffMaterialType = "computed",
        draping_material_model: DrapingMaterialType = "woven",
        draping_ud_coefficient: float = 0.0,
    ):
        super().__init__(name=name)

        self.material = material
        self.thickness = thickness
        self.area_price = area_price
        self.ignore_for_postprocessing = ignore_for_postprocessing
        self.drop_off_material_handling = DropoffMaterialType(drop_off_material_handling)
        self.cut_off_material_handling = CutoffMaterialType(cut_off_material_handling)
        self.draping_material_model = DrapingMaterialType(draping_material_model)
        self.draping_ud_coefficient = draping_ud_coefficient

    def _create_stub(self) -> fabric_pb2_grpc.ObjectServiceStub:
        return fabric_pb2_grpc.ObjectServiceStub(self._channel)

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    material = grpc_link_property("properties.material")
    thickness = grpc_data_property("properties.thickness")
    area_price = grpc_data_property("properties.area_price")
    ignore_for_postprocessing = grpc_data_property("properties.ignore_for_postprocessing")

    drop_off_material_handling = grpc_data_property(
        "properties.drop_off_material_handling",
        from_protobuf=drop_off_material_type_from_pb,
        to_protobuf=drop_off_material_type_to_pb,
    )
    cut_off_material_handling = grpc_data_property(
        "properties.cut_off_material_handling",
        from_protobuf=cut_off_material_type_from_pb,
        to_protobuf=cut_off_material_type_to_pb,
    )
    draping_material_model = grpc_data_property(
        "properties.draping_material_model",
        from_protobuf=draping_material_type_from_pb,
        to_protobuf=draping_material_type_to_pb,
    )

    draping_ud_coefficient = grpc_data_property("properties.draping_ud_coefficient")
