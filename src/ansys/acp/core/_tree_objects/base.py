"""
Defines helpers for synchronizing object properties with the backend
via gRPC Put / Get calls.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Type, TypeVar

from grpc import Channel

from ansys.api.acp.v0.base_pb2 import ResourcePath

from .._grpc_helpers.property_helper import grpc_data_property
from .._grpc_helpers.protocols import ObjectInfo, ResourceStub

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
    def from_resource_path(cls: Type[_T], resource_path: str, channel: Channel) -> _T:
        instance = cls()
        instance._pb_object.info.resource_path.value = resource_path
        instance._channel_store = channel
        return instance

    def store(self, parent: TreeObject) -> None:
        raise NotImplementedError()

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
