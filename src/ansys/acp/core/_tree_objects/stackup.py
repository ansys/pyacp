from __future__ import annotations

from typing import Iterable, Sequence

from ansys.api.acp.v0 import stackup_pb2, stackup_pb2_grpc

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
    SymmetryType,
    cut_off_material_type_from_pb,
    cut_off_material_type_to_pb,
    draping_material_type_from_pb,
    draping_material_type_to_pb,
    drop_off_material_type_from_pb,
    drop_off_material_type_to_pb,
    symmetry_type_to_pb,
    symmetry_type_from_pb,
    status_type_from_pb,
)
from .material import Material
from .fabric import Fabric
from .object_registry import register

__all__ = ["Stackup"]


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
        Price per area of the fabric.
    drop_off_material_handling :
        Defines the material of drop-off elements in the solid model extrusion.
    drop_off_material :
        Specify the material of drop-off elements in the solid model.
    cut_off_material_handling :
        Defines the material of cut-off elements in solid models if cut-off geometries are active.
    cut_off_material :
        Define the cut-off material if this ply is shaped by a cut-off geometry.
    draping_material_model :
        Specifies the draping model of the fabric.
    draping_ud_coefficient :
        Set the draping coefficient of the uni-directional draping model. Must be in the range of 0 to 1.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "stackups"
    OBJECT_INFO_TYPE = stackup_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = stackup_pb2.CreateRequest

    def __init__(
        self,
        name: str = "Stackup",
        symmetry: SymmetryType = "no_symmetry",
        topdown: bool = True,
        fabrics: Sequence[FabricWithAngle] | None = None,
        area_price: float = 0.0,
        drop_off_material_handling: DropoffMaterialType = "global",
        drop_off_material: Material | None = None,
        cut_off_material: Material | None = None,
        cut_off_material_handling: CutoffMaterialType = "computed",
        draping_material_model: DrapingMaterialType = "woven",
        draping_ud_coefficient: float = 0.0,
    ):
        super().__init__(name=name)

        self.symmetry = SymmetryType(symmetry)
        self.topdown = topdown
        self.area_price = area_price
        self.fabrics = fabrics
        self.drop_off_material_handling = DropoffMaterialType(drop_off_material_handling)
        self.drop_off_materia = drop_off_material
        self.cut_off_material_handling = CutoffMaterialType(cut_off_material_handling)
        self.cut_off_material = cut_off_material
        self.draping_material_model = DrapingMaterialType(draping_material_model)
        self.draping_ud_coefficient = draping_ud_coefficient

    def _create_stub(self) -> stackup_pb2_grpc.ObjectServiceStub:
        return stackup_pb2_grpc.ObjectServiceStub(self._channel)

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    symmetry = grpc_data_property(
        "properties.symmetry",
        from_protobuf=symmetry_type_from_pb,
        to_protobuf=symmetry_type_to_pb,
    )
    topdown = grpc_data_property("properties.topdown")
    area_price = grpc_data_property("properties.area_price")
    ignore_for_postprocessing = grpc_data_property("properties.ignore_for_postprocessing")

    drop_off_material_handling = grpc_data_property(
        "properties.drop_off_material_handling",
        from_protobuf=drop_off_material_type_from_pb,
        to_protobuf=drop_off_material_type_to_pb,
    )
    drop_off_material = grpc_link_property("properties.drop_off_material")
    cut_off_material_handling = grpc_data_property(
        "properties.cut_off_material_handling",
        from_protobuf=cut_off_material_type_from_pb,
        to_protobuf=cut_off_material_type_to_pb,
    )
    cut_off_material = grpc_link_property("properties.cut_off_material")
    draping_material_model = grpc_data_property(
        "properties.draping_material_model",
        from_protobuf=draping_material_type_from_pb,
        to_protobuf=draping_material_type_to_pb,
    )
    draping_ud_coefficient = grpc_data_property("properties.draping_ud_coefficient")
