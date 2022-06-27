from __future__ import annotations

from typing import Iterable

from ansys.api.acp.v0 import material_pb2, material_pb2_grpc

from .._grpc_helpers.property_helper import grpc_data_property_read_only
from .base import CreatableTreeObject
from .enums import status_type_from_pb
from .object_registry import register

__all__ = ["Material"]


@register
class Material(CreatableTreeObject):
    """Instantiate a Material.

    Parameters
    ----------
    name :
        Name of the Material.
    """

    __slots__: Iterable[str] = tuple()

    COLLECTION_LABEL = "materials"
    OBJECT_INFO_TYPE = material_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = material_pb2.CreateRequest

    def __init__(self, name: str = "Material"):
        super().__init__(name=name)

    def _create_stub(self) -> material_pb2_grpc.ObjectServiceStub:
        return material_pb2_grpc.ObjectServiceStub(self._channel)

    id = grpc_data_property_read_only("info.id")

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
