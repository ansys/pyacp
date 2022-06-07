from __future__ import annotations

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore

from google.protobuf.message import Message

from ansys.api.acp.v0.base_pb2 import BasicInfo, CollectionPath, Empty


class DeleteRequest(Protocol):
    def __init__(self, info: BasicInfo):
        ...

    @property
    def info(self) -> BasicInfo:
        ...


class ListRequest(Protocol):
    @property
    def collection_path(self) -> CollectionPath:
        ...


class ResourceStub(Protocol):
    """Interface definition for ACP Resource service stubs."""

    def Get(self, request: Message) -> Message:
        ...

    def Put(self, request: Message) -> Message:
        ...

    def List(self, request: ListRequest) -> Message:
        ...

    def Delete(self, request: DeleteRequest) -> Empty:
        ...
