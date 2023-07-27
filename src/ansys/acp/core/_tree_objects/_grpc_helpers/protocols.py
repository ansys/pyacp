from __future__ import annotations

import textwrap
from typing import Any, Protocol

from google.protobuf.message import Message
import grpc

from ansys.api.acp.v0.base_pb2 import (
    BasicInfo,
    CollectionPath,
    DeleteRequest,
    Empty,
    GetRequest,
    ListRequest,
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


class ReadOnlyResourceStub(Protocol):
    """Interface definition for ACP Resource service stubs."""

    def __init__(self, channel: grpc.Channel):
        ...

    def Get(self, request: GetRequest) -> ObjectInfo:
        ...

    def List(self, request: ListRequest) -> ListReply:
        ...


class CreatableResourceStub(ResourceStub, Protocol):
    def Create(self, request: CreateRequest) -> ObjectInfo:
        ...


class GrpcObjectBase(Protocol):
    _GRPC_PROPERTIES: tuple[str, ...]

    def __str__(self) -> str:
        string_items = []
        for attr_name in self._GRPC_PROPERTIES:
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


class Gettable(Protocol):
    def _get(self) -> None:
        ...

    def _get_if_stored(self) -> None:
        ...

    @property
    def _is_stored(self) -> bool:
        ...

    @property
    def _channel(self) -> grpc.Channel:
        ...

    _pb_object: Any


class Editable(Gettable, Protocol):
    def _put(self) -> None:
        ...

    def _put_if_stored(self) -> None:
        ...
