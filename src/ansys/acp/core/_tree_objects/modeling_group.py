from __future__ import annotations

from typing import Any

from ansys.acp.core._grpc_helpers.property_helper import grpc_data_property_read_only
from ansys.api.acp.v0 import modeling_group_pb2, modeling_group_pb2_grpc

from .base import CreatableTreeObject

__all__ = ["ModelingGroup"]


class ModelingGroup(CreatableTreeObject):
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
