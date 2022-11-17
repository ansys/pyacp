from __future__ import annotations

from typing import Iterable

from ansys.api.acp.v0 import material_pb2, material_pb2_grpc

from .._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import ply_type_from_pb, ply_type_to_pb, status_type_from_pb, PlyType
from .object_registry import register

__all__ = ["Material"]


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

    def _create_stub(self) -> material_pb2_grpc.ObjectServiceStub:
        return material_pb2_grpc.ObjectServiceStub(self._channel)

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    ply_type = grpc_data_property(
        "properties.ply_type",
        from_protobuf=ply_type_from_pb,
        to_protobuf=ply_type_to_pb,
    )
