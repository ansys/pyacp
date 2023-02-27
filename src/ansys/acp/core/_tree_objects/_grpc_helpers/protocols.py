from __future__ import annotations

import textwrap
from typing import Any, Protocol

from google.protobuf.message import Message
import grpc
from typing_extensions import Self

from ansys.api.acp.v0.base_pb2 import (
    BasicInfo,
    CollectionPath,
    DeleteRequest,
    Empty,
    GetRequest,
    ListRequest,
    ResourcePath,
)


class CreateRequest(Protocol):
    def __init__(self, collection_path: CollectionPath, name: str, properties: Message):
        ...


class ObjectInfo(Protocol):
    @property
    def info(self) -> BasicInfo:
        ...

    @property
    def properties(self) -> Message:
        ...


class ListReply(Protocol):
    @property
    def objects(self) -> list[ObjectInfo]:
        ...


class ResourceStub(Protocol):
    """Interface definition for ACP Resource service stubs."""

    def __init__(self, channel: grpc.Channel):
        ...

    def Get(self, request: GetRequest) -> ObjectInfo:
        ...

    def Put(self, request: ObjectInfo) -> ObjectInfo:
        ...

    def List(self, request: ListRequest) -> ListReply:
        ...

    def Delete(self, request: DeleteRequest) -> Empty:
        ...


class CreatableResourceStub(ResourceStub, Protocol):
    def Create(self, request: CreateRequest) -> ObjectInfo:
        ...


class GrpcObjectReadOnly(Protocol):
    GRPC_PROPERTIES: tuple[str, ...]

    @property
    def _pb_object(self) -> Any:
        ...

    def _get(self) -> None:
        ...

    def _get_if_stored(self) -> None:
        if self._is_stored:
            self._get()

    @property
    def _is_stored(self) -> bool:
        ...

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


class GrpcObject(GrpcObjectReadOnly, Protocol):
    @property
    def _pb_object(self) -> Any:
        ...

    @_pb_object.setter
    def _pb_object(self, value: Any) -> None:
        ...

    def _put(self) -> None:
        ...

    def _put_if_stored(self) -> None:
        if self._is_stored:
            self._put()


class RootGrpcObject(GrpcObject, Protocol):
    _pb_object: ObjectInfo

    @property
    def _channel(self) -> grpc.Channel:
        ...

    @classmethod
    def _from_resource_path(cls, resource_path: ResourcePath, channel: grpc.Channel) -> Self:
        ...
