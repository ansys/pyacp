"""
Defines helpers for synchronizing object properties with the backend
via gRPC Put / Get calls.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Type, TypeVar

from grpc import Channel

from ansys.api.acp.v0.base_pb2 import CollectionPath, ResourcePath

from .._grpc_helpers.property_helper import grpc_data_property
from .._grpc_helpers.protocols import CreatableResourceStub, CreateRequest, ObjectInfo, ResourceStub
from .._utils.resource_paths import join as _rp_join

_T = TypeVar("_T", bound="TreeObject")


class TreeObject(ABC):
    """
    Base class for ACP tree objects.
    """

    COLLECTION_LABEL: str
    OBJECT_INFO_TYPE: Type[ObjectInfo]

    def __init__(self: TreeObject, name: str = "") -> None:
        self._channel_store: Optional[Channel] = None
        self._pb_object: ObjectInfo = self.OBJECT_INFO_TYPE()
        self.name = name

    @classmethod
    def _from_object_info(cls: Type[_T], object_info: ObjectInfo, channel: Optional[Channel]) -> _T:
        instance = cls()
        instance._pb_object = object_info
        instance._channel_store = channel
        return instance

    @property
    def _resource_path(self) -> ResourcePath:
        return self._pb_object.info.resource_path

    @property
    def _channel(self) -> Channel:
        if not self._is_stored:
            raise RuntimeError("The server connection is uninitialized.")
        return self._channel_store

    @abstractmethod
    def _get_stub(self) -> ResourceStub:
        ...

    @property
    def _is_stored(self) -> bool:
        return self._channel_store is not None

    name = grpc_data_property("info.name")
    """The name of the object."""


class CreatableTreeObject(TreeObject, ABC):
    CREATE_REQUEST_TYPE: Type[CreateRequest]

    @abstractmethod
    def _get_stub(self) -> CreatableResourceStub:
        ...

    def store(self: CreatableTreeObject, parent: TreeObject) -> None:
        self._channel_store = parent._channel

        collection_path = CollectionPath(
            value=_rp_join(parent._resource_path.value, self.COLLECTION_LABEL)
        )
        request = self.CREATE_REQUEST_TYPE(
            collection_path=collection_path,
            name=self._pb_object.info.name,
            properties=self._pb_object.properties,
        )
        self._pb_object = self._get_stub().Create(request)
