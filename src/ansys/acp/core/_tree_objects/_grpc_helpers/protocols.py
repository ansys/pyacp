from __future__ import annotations

from collections.abc import Iterable
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
    """Interface definition for CreateRequest messages.

    The CreateRequest message is used to create a new object in a collection.
    """
    def __init__(self, collection_path: CollectionPath, name: str, properties: Message):
        ...


class ObjectInfo(Protocol):
    """Interface definition for ObjectInfo messages.

    The ObjectInfo message contains the full information about an object.
    """
    @property
    def info(self) -> BasicInfo:
        """Provide basic information about the object."""
        ...

    @property
    def properties(self) -> Message:
        """Properties of the object."""
        ...


class ListReply(Protocol):
    """Interface definition for ListReply messages.

    The ListReply message contains a list of objects in a collection.
    """
    @property
    def objects(self) -> list[ObjectInfo]:
        """List of objects in the collection."""
        ...


class EditableResourceStub(Protocol):
    """Interface definition for ACP Resource service stubs.

    This interface defines the edit methods for ACP Resource service stubs.
    """

    def Put(self, request: ObjectInfo) -> ObjectInfo:
        """RPC method for updating an object."""
        ...

    def Delete(self, request: DeleteRequest) -> Empty:
        """RPC method for deleting an object."""
        ...


class ReadableResourceStub(Protocol):
    """Interface definition for ACP Resource service stubs.

    This interface defines the read methods for ACP Resource service stubs.
    """

    def __init__(self, channel: grpc.Channel):
        ...

    def Get(self, request: GetRequest) -> ObjectInfo:
        """RPC method for getting an object's information."""
        ...

    def List(self, request: ListRequest) -> ListReply:
        """RPC method for listing objects in a collection."""
        ...


class EditableAndReadableResourceStub(EditableResourceStub, ReadableResourceStub, Protocol):
    """Interface definition for ACP Resource service stubs.

    This interface defines the edit and read methods for ACP Resource service stubs.
    """
    ...


class CreatableResourceStub(Protocol):
    """Interface definition for ACP Resource service stubs.

    This interface defines the create methods for ACP Resource service stubs.
    """
    def Create(self, request: CreateRequest) -> ObjectInfo:
        """RPC method for creating an object."""
        ...


class CreatableEditableAndReadableResourceStub(
    CreatableResourceStub, EditableResourceStub, ReadableResourceStub, Protocol
):
    """Interface definition for ACP Resource service stubs.

    This interface defines the create, edit, and read methods for ACP Resource service stubs.
    """
    ...


class GrpcObjectBase(Protocol):
    """Interface definition for objects which are backed by a gRPC API."""
    __slots__: Iterable[str] = tuple()
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


class Readable(Protocol):
    """Interface definition for readable objects."""
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


class Editable(Readable, Protocol):
    """Interface definition for editable objects."""
    def _put(self) -> None:
        ...

    def _put_if_stored(self) -> None:
        ...
