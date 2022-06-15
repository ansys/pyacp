from dataclasses import dataclass
from typing import List, Type, cast

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore

from grpc import Channel

from ansys.api.acp.v0.base_pb2 import BasicInfo, CollectionPath

from ..protocols import CreatableResourceStub, CreateRequest, DeleteRequest, ListRequest, ObjectInfo

__all__ = [
    "StubWrapper",
    "SimpleStubInfo",
    "SimpleStubWrapper",
]


class StubWrapper(Protocol):
    def __init__(self, channel: Channel):
        ...

    def get(self, basic_info: BasicInfo) -> ObjectInfo:
        ...

    def put(self, object_info: ObjectInfo) -> None:
        ...

    def list(self, collection_path: CollectionPath) -> List[ObjectInfo]:
        ...

    def delete(self, basic_info: BasicInfo) -> None:
        ...

    def create(self, collection_path: CollectionPath, name: str) -> ObjectInfo:
        ...


@dataclass
class SimpleStubInfo:
    stub_class: Type[CreatableResourceStub]
    list_attribute: str
    list_request_class: Type[ListRequest]
    create_request_class: Type[CreateRequest]
    delete_request_class: Type[DeleteRequest]


class SimpleStubWrapper:
    _STUB_INFO: SimpleStubInfo

    def __init__(self, channel: Channel):
        self._channel = channel
        self._stub = self._STUB_INFO.stub_class(self._channel)

    def get(self, basic_info: BasicInfo) -> ObjectInfo:
        return self._stub.Get(basic_info)

    def put(self, object_info: ObjectInfo) -> None:
        self._stub.Put(object_info)

    def list(self, collection_path: CollectionPath) -> List[ObjectInfo]:
        return cast(
            List[ObjectInfo],
            getattr(
                self._stub.List(
                    self._STUB_INFO.list_request_class(collection_path=collection_path)
                ),
                self._STUB_INFO.list_attribute,
            ),
        )

    def delete(self, basic_info: BasicInfo) -> None:
        self._stub.Delete(self._STUB_INFO.delete_request_class(info=basic_info))

    def create(self, collection_path: CollectionPath, name: str) -> ObjectInfo:
        return self._stub.Create(
            self._STUB_INFO.create_request_class(collection_path=collection_path, name=name)
        )
