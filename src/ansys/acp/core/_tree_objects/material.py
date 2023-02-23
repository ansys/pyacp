from __future__ import annotations

from typing import Iterable

from ansys.api.acp.v0 import material_pb2, material_pb2_grpc

from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject, TreeObjectAttribute
from .enums import PlyType, ply_type_from_pb, ply_type_to_pb, status_type_from_pb
from .object_registry import register

__all__ = ["Material"]


# TODO: the ACP 'Model.create_material' sets the density and engineering constants
# property sets to all-zero. The same should be done here.


@mark_grpc_properties
class DensityPropertySet(TreeObjectAttribute):
    GRPC_PROPERTIES = tuple()

    rho = grpc_data_property(
        "properties.property_sets.density",
        to_protobuf=lambda x: material_pb2.DensityPropertySet(
            values=[material_pb2.DensityPropertySet.Data(rho=x)],
        ),
        from_protobuf=lambda pb_data: pb_data.values[0].rho if pb_data.values else None,
    )


@mark_grpc_properties
@register
class Material(CreatableTreeObject, IdTreeObject):
    """Instantiate a Material.

    Parameters
    ----------
    name :
        Name of the Material.
    ply_type :
        Define the type of material such as core, uni-directional (regular), woven, or isotropic.
    """

    __slots__: Iterable[str] = tuple()

    COLLECTION_LABEL = "materials"
    OBJECT_INFO_TYPE = material_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = material_pb2.CreateRequest

    def __init__(self, name: str = "Material", ply_type: PlyType = "undefined"):
        super().__init__(name=name)

        self.ply_type = ply_type
        self.density.rho = 0.0
        # TODO: set engineering constants to zero

        # self.density = TreeObjectAttribute(parent_object=self)

    @property
    def density(self) -> DensityPropertySet:
        return DensityPropertySet(parent_object=self)

    # @property
    # def engineering_constants(self):
    #     if isotropic:
    #         return IsotropicEngineeringConstantsPropertySet
    #     else:
    #         return IsotropicEngineeringConstantsPropertySet

    def _create_stub(self) -> material_pb2_grpc.ObjectServiceStub:
        return material_pb2_grpc.ObjectServiceStub(self._channel)

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    ply_type = grpc_data_property(
        "properties.ply_type",
        from_protobuf=ply_type_from_pb,
        to_protobuf=ply_type_to_pb,
    )
