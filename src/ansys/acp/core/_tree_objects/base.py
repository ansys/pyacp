"""
Defines helpers for synchronizing object properties with the backend
via gRPC Put / Get calls.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
import textwrap
from typing import Any, Iterable, Optional, Tuple, Type, TypeVar, cast

from grpc import Channel

from ansys.api.acp.v0.base_pb2 import CollectionPath, DeleteRequest, ResourcePath

from .._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .._grpc_helpers.protocols import CreatableResourceStub, CreateRequest, ObjectInfo, ResourceStub
from .._utils.resource_paths import join as _rp_join

_T = TypeVar("_T", bound="TreeObject")


@mark_grpc_properties  # type: ignore # see https://github.com/python/mypy/issues/4717
class TreeObject(ABC):
    """
    Base class for ACP tree objects.
    """

    __slots__ = ("_channel_store", "_stub_store", "_pb_object")

    COLLECTION_LABEL: str
    OBJECT_INFO_TYPE: Type[ObjectInfo]
    GRPC_PROPERTIES: Tuple[str, ...]

    def __init__(self: TreeObject, name: str = "") -> None:
        self._channel_store: Optional[Channel] = None
        self._stub_store: Optional[ResourceStub] = None
        self._pb_object: ObjectInfo = self.OBJECT_INFO_TYPE()
        self.name = name

    def clone(self: _T) -> _T:
        """Create a new unstored object with the same properties."""
        new_object_info = self.OBJECT_INFO_TYPE()
        new_object_info.properties.CopyFrom(self._pb_object.properties)
        new_object_info.info.name = self._pb_object.info.name
        return type(self)._from_object_info(object_info=new_object_info)

    def delete(self: _T) -> None:
        self._get_stub().Delete(
            DeleteRequest(
                resource_path=self._pb_object.info.resource_path,
                version=self._pb_object.info.version,
            )
        )

    def __eq__(self: _T, other: Any) -> bool:
        if not isinstance(other, TreeObject):
            return False
        if not self._is_stored:
            # For unstored objects, fall back to identity comparison
            return self is other
        return self._resource_path.value == other._resource_path.value

    @classmethod
    def _from_object_info(
        cls: Type[_T], object_info: ObjectInfo, channel: Optional[Channel] = None
    ) -> _T:
        instance = cls()
        instance._pb_object = object_info
        instance._channel_store = channel
        return instance

    @classmethod
    def _from_resource_path(cls: Type[_T], resource_path: ResourcePath, channel: Channel) -> _T:
        instance = cls()
        instance._pb_object.info.resource_path.CopyFrom(resource_path)
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

    def _get_stub(self) -> ResourceStub:
        if not self._is_stored:
            raise RuntimeError("The server connection is uninitialized.")
        if self._stub_store is None:
            self._stub_store = self._create_stub()
        return self._stub_store

    @abstractmethod
    def _create_stub(self) -> ResourceStub:
        ...

    @property
    def _is_stored(self) -> bool:
        return self._channel_store is not None

    def __repr__(self) -> str:
        return f"<{type(self).__name__} with name '{self.name}'>"

    def __str__(self) -> str:
        string_items = []
        for attr_name in self.GRPC_PROPERTIES:
            try:
                value_repr = repr(getattr(self, attr_name))
            except:
                value_repr = "<unavailable>"
            string_items.append(f"{attr_name}={value_repr}")
        type_name = type(self).__name__
        if not string_items:
            content = ""
        elif len(string_items) == 1:
            content = string_items[0]
        else:
            content = ",\n".join(string_items)
            content = f"\n{textwrap.indent(content, ' ' * 4)}\n"
        return f"{type_name}({content})"

    name = grpc_data_property("info.name")
    """The name of the object."""


@mark_grpc_properties  # type: ignore # see https://github.com/python/mypy/issues/4717
class CreatableTreeObject(TreeObject, ABC):
    __slots__: Iterable[str] = tuple()
    CREATE_REQUEST_TYPE: Type[CreateRequest]

    def _get_stub(self) -> CreatableResourceStub:
        return cast(CreatableResourceStub, super()._get_stub())

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


@mark_grpc_properties  # type: ignore # see https://github.com/python/mypy/issues/4717
class IdTreeObject(TreeObject, ABC):
    """Implements the 'id' attribute for tree objects."""

    __slots__: Iterable[str] = tuple()

    id = grpc_data_property_read_only("info.id")

    def __repr__(self) -> str:
        return f"<{type(self).__name__} with id '{self.id}'>"
