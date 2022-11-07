from __future__ import annotations

from typing import Any, Iterable

from ansys.acp.core._grpc_helpers.property_helper import (
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ansys.acp.core._tree_objects.modeling_ply import ModelingPly
from ansys.api.acp.v0 import modeling_group_pb2, modeling_group_pb2_grpc, modeling_ply_pb2_grpc

from .._grpc_helpers.mapping import define_mapping
from .base import CreatableTreeObject
from .object_registry import register

__all__ = ["ModelingGroup"]


@mark_grpc_properties
@register
class ModelingGroup(CreatableTreeObject):
    __slots__: Iterable[str] = tuple()

    COLLECTION_LABEL = "modeling_groups"
    OBJECT_INFO_TYPE = modeling_group_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = modeling_group_pb2.CreateRequest

    def __init__(self, name: str = "ModelingGroup", **kwargs: Any):
        super().__init__(name=name)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def _create_stub(self) -> modeling_group_pb2_grpc.ObjectServiceStub:
        return modeling_group_pb2_grpc.ObjectServiceStub(self._channel)

    id = grpc_data_property_read_only("info.id")

    create_modeling_ply, modeling_plies = define_mapping(
        ModelingPly, modeling_ply_pb2_grpc.ObjectServiceStub
    )
