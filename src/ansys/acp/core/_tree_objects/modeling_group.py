from __future__ import annotations

from functools import lru_cache
from typing import Any

from ansys.acp.core._grpc_helpers.property_helper import grpc_data_property_read_only
from ansys.api.acp.v0.modeling_group_pb2 import ModelingGroupReply
from ansys.api.acp.v0.modeling_group_pb2_grpc import ModelingGroupStub

from .base import TreeObjectBase

__all__ = ["ModelingGroup"]


class ModelingGroup(TreeObjectBase):
    COLLECTION_LABEL = "modeling_groups"
    OBJECT_INFO_TYPE = ModelingGroupReply

    def __init__(self, name: str = "Modeling Group", **kwargs: Any):
        super().__init__(name=name)

        for key, value in kwargs.items():
            setattr(self, key, value)

    # Mypy doesn't like this being a property, see https://github.com/python/mypy/issues/1362
    @lru_cache(maxsize=1)
    def _get_stub(self) -> ModelingGroupStub:
        return ModelingGroupStub(self._channel)

    id = grpc_data_property_read_only("info.id")
