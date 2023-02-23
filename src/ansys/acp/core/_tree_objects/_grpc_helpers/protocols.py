from __future__ import annotations

from typing import Protocol

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


class GrpcObjectContainer(Protocol):
    GRPC_PROPERTIES: tuple[str, ...]
    _pb_object: ObjectInfo

    # @abstractmethod
    def _get_stub(self) -> ResourceStub:
        ...

    @property
    def _is_stored(self) -> bool:
        ...


class OwningGrpcObjectContainer(GrpcObjectContainer, Protocol):
    @property
    def _channel(self) -> grpc.Channel:
        ...

    @classmethod
    def _from_resource_path(cls, resource_path: ResourcePath, channel: grpc.Channel) -> Self:
        ...
