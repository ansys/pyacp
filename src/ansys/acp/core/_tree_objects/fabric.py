from __future__ import annotations

from functools import lru_cache

from ansys.api.acp.v0 import fabric_pb2, fabric_pb2_grpc

from ansys.api.acp.v0.drop_off_material_pb2 import MaterialHandlingType as DropoffMaterialType
from ansys.api.acp.v0.drop_off_material_pb2 import MaterialHandlingType as CutoffMaterialType
from ansys.api.acp.v0.ply_material_pb2 import DrapingMaterialType

from .._grpc_helpers.property_helper import grpc_data_property, grpc_data_property_read_only
from .._grpc_helpers.linked_object_list import define_linked_object_list
from .._utils.enum_conversions import status_type_to_string
from .._utils.linked_objec_conversion import from_rp_to_tree_object, from_tree_object_to_rp
from .base import CreatableTreeObject

from .material import Material

__all__ = ["Fabric"]


class Fabric(CreatableTreeObject):
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

    COLLECTION_LABEL = "fabrics"
    OBJECT_INFO_TYPE = fabric_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = fabric_pb2.CreateRequest

    def __init__(
        self,
        name: str = "Fabric",
        material: Material = None,
        thickness: float = 0.,
        area_price: float = 0.,
        ignore_for_postprocessing: bool = False,
        drop_off_material_handling: DropoffMaterialType = DropoffMaterialType.GLOBAL,
        cut_off_material_handling: CutoffMaterialType = CutoffMaterialType.COMPUTED,
        draping_material_model: DrapingMaterialType = DrapingMaterialType.WOVEN,
        draping_ud_coefficient: float = 0.
    ):
        super().__init__(name=name)

        self.material = material
        self.thickness = thickness
        self.area_price = area_price
        self.ignore_for_postprocessing = ignore_for_postprocessing
        self.drop_off_material_handling = drop_off_material_handling
        self.cut_off_material_handling = cut_off_material_handling
        self.draping_material_model = draping_material_model
        self.draping_ud_coefficient = draping_ud_coefficient

    # Mypy doesn't like this being a property, see https://github.com/python/mypy/issues/1362
    @lru_cache(maxsize=1)
    def _get_stub(self) -> fabric_pb2_grpc.ObjectServiceStub:
        return fabric_pb2_grpc.ObjectServiceStub(self._channel)

    id = grpc_data_property_read_only("info.id")

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_to_string)

    material = grpc_data_property( "properties.material")
    thickness = grpc_data_property("properties.thickness")
    area_price = grpc_data_property("properties.area_price")
    ignore_for_postprocessing = grpc_data_property("properties.ignore_for_postprocessing")

    draping_ud_coefficient = grpc_data_property("properties.draping_ud_coefficient")

    material = grpc_data_property("properties.material",
                                  to_protobuf=from_rp_to_tree_object())


