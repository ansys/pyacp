from __future__ import annotations

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore

from google.protobuf.message import Message
import grpc

from ansys.api.acp.v0.base_pb2 import BasicInfo, CollectionPath, Empty


class DeleteRequest(Protocol):
    def __init__(self, info: BasicInfo):
        ...

    @property
    def info(self) -> BasicInfo:
        ...


class ListRequest(Protocol):
    def __init__(self, collection_path: CollectionPath):
        ...

    @property
    def collection_path(self) -> CollectionPath:
        ...


class CreateRequest(Protocol):
    def __init__(self, collection_path: CollectionPath, name: str):
        ...

    @property
    def collection_path(self) -> CollectionPath:
        ...


class ObjectInfo(Protocol):
    @property
    def info(self) -> BasicInfo:
        ...


class ResourceStub(Protocol):
    """Interface definition for ACP Resource service stubs."""

    def __init__(self, channel: grpc.Channel):
        ...

    def Get(self, request: BasicInfo) -> ObjectInfo:
        ...

    def Put(self, request: ObjectInfo) -> Empty:
        ...

    def List(self, request: ListRequest) -> Message:
        ...

    def Delete(self, request: DeleteRequest) -> Empty:
        ...


class CreatableResourceStub(ResourceStub, Protocol):
    def Create(self, request: CreateRequest) -> ObjectInfo:
        ...
