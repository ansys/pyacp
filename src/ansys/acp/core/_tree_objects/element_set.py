from __future__ import annotations

from functools import lru_cache
from typing import Any, Optional

from ansys.api.acp.v0.element_set_pb2 import ElementSetReply
from ansys.api.acp.v0.element_set_pb2_grpc import ElementSetStub

from .._grpc_helpers.property_helper import grpc_data_property
from .._server import ServerProtocol
from .base import TreeObject

__all__ = ["ElementSet"]


class ElementSet(TreeObject):
    COLLECTION_LABEL = "element_sets"

    def __init__(self, **kwargs: Any):
        self._server: Optional[ServerProtocol] = None
        self._pb_object = ElementSetReply()

        for key, value in kwargs.items():
            setattr(self, key, value)

    # Mypy doesn't like this being a property, see https://github.com/python/mypy/issues/1362
    @lru_cache(maxsize=1)
    def _get_stub(self) -> ElementSetStub:
        return ElementSetStub(self._channel)

    id = grpc_data_property("info.id")
