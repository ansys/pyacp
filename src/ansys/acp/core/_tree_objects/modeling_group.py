from __future__ import annotations

from typing import Any, Iterable

from ansys.api.acp.v0 import modeling_group_pb2, modeling_group_pb2_grpc, modeling_ply_pb2_grpc

from ._grpc_helpers.mapping import define_mapping
from ._grpc_helpers.property_helper import mark_grpc_properties
from .base import CreatableTreeObject, IdTreeObject
from .modeling_ply import ModelingPly
from .object_registry import register

__all__ = ["ModelingGroup"]


@mark_grpc_properties
@register
class ModelingGroup(CreatableTreeObject, IdTreeObject):
    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "modeling_groups"
    OBJECT_INFO_TYPE = modeling_group_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = modeling_group_pb2.CreateRequest

    def __init__(self, name: str = "ModelingGroup", **kwargs: Any):
        super().__init__(name=name)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def _create_stub(self) -> modeling_group_pb2_grpc.ObjectServiceStub:
        return modeling_group_pb2_grpc.ObjectServiceStub(self._channel)

    create_modeling_ply, modeling_plies = define_mapping(
        ModelingPly, modeling_ply_pb2_grpc.ObjectServiceStub
    )
