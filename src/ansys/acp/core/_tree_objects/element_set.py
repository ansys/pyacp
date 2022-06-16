from __future__ import annotations

from functools import lru_cache

from ansys.api.acp.v0.element_set_pb2 import CreateElementSetRequest, ElementSetInfo
from ansys.api.acp.v0.element_set_pb2_grpc import ElementSetStub

from .._grpc_helpers.property_helper import grpc_data_property
from .base import CreatableTreeObject

__all__ = ["ElementSet"]


class ElementSet(CreatableTreeObject):
    COLLECTION_LABEL = "element_sets"
    OBJECT_INFO_TYPE = ElementSetInfo
    CREATE_REQUEST_TYPE = CreateElementSetRequest

    def __init__(self, name: str = "Element Set"):
        """Instantiate an Element Set.

        Parameters
        ----------
        name :
            The name of the Element Set.
        """
        super().__init__(name=name)

    # Mypy doesn't like this being a property, see https://github.com/python/mypy/issues/1362
    @lru_cache(maxsize=1)
    def _get_stub(self) -> ElementSetStub:
        return ElementSetStub(self._channel)

    id = grpc_data_property("info.id")
