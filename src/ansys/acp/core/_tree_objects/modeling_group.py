from __future__ import annotations

from functools import lru_cache
from typing import Any

from ansys.acp.core._grpc_helpers.property_helper import grpc_data_property_read_only
from ansys.api.acp.v0.modeling_group_pb2 import CreateModelingGroupRequest, ModelingGroupInfo
from ansys.api.acp.v0.modeling_group_pb2_grpc import ModelingGroupStub

from .base import CreatableTreeObject

__all__ = ["ModelingGroup"]


class ModelingGroup(CreatableTreeObject):
    COLLECTION_LABEL = "modeling_groups"
    OBJECT_INFO_TYPE = ModelingGroupInfo
    CREATE_REQUEST_TYPE = CreateModelingGroupRequest

    def __init__(self, name: str = "Modeling Group", **kwargs: Any):
        super().__init__(name=name)

        for key, value in kwargs.items():
            setattr(self, key, value)

    # Mypy doesn't like this being a property, see https://github.com/python/mypy/issues/1362
    @lru_cache(maxsize=1)
    def _get_stub(self) -> ModelingGroupStub:
        return ModelingGroupStub(self._channel)

    id = grpc_data_property_read_only("info.id")
