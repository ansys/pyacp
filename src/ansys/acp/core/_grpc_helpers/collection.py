from typing import Callable, Generic, Iterator, List, Optional, Tuple, Type, TypeVar

from ansys.api.acp.v0.base_pb2 import BasicInfo, CollectionPath

from .._property_helper import ResourceProtocol
from .._server import ServerProtocol
from .protocols import DeleteRequest, ListRequest, ResourceStub

ValueT = TypeVar("ValueT", bound=ResourceProtocol)


class Collection(Generic[ValueT]):
    def __init__(
        self,
        *,
        server: ServerProtocol,
        stub_class: Type[ResourceStub],
        collection_path: CollectionPath,
        list_attribute: str,
        list_request_class: Type[ListRequest],
        delete_request_class: Type[DeleteRequest],
        object_class: Type[ValueT],
    ):
        self._stub = stub_class(server.channel)
        self._list_attribute = list_attribute
        self._list_request = list_request_class(collection_path=collection_path)
        self._delete_request_class = delete_request_class
        self._object_constructor: Callable[[str], ValueT] = lambda resource_path: object_class(
            resource_path=resource_path, server=server
        )

    def __iter__(self) -> Iterator[str]:
        yield from (obj.id for obj in self._get_info_list())

    def __getitem__(self, key: str) -> ValueT:
        info = self._get_info_by_id(key)
        return self._object_constructor(info.resource_path.value)

    def _get_info_list(self) -> List[BasicInfo]:
        res = [
            obj.info for obj in getattr(self._stub.List(self._list_request), self._list_attribute)
        ]
        if len(set(obj.id for obj in res)) != len(res):
            raise ValueError("Duplicate ID in Collection.")
        return res

    def _get_info_by_id(self, key: str) -> BasicInfo:
        for obj in self._get_info_list():
            if obj.id == key:
                return obj
        raise KeyError(f"No object with ID '{key}' found.")

    # def __setitem__(self, key: str, value: ValueT) -> None:
    #     raise NotImplementedError()

    # def update(self, other=(), /, **kwds):
    #     raise NotImplementedError()

    # def setdefault(self, key, default=None):
    #     raise NotImplementedError()

    def __delitem__(self, key: str) -> None:
        info = self._get_info_by_id(key)
        self._stub.Delete(self._delete_request_class(info=info))

    def clear(self) -> None:
        for info in self._get_info_list():
            self._stub.Delete(self._delete_request_class(info=info))

    # def pop(self, key):
    #     raise NotImplementedError()

    # def popitem(self, key):
    #     raise NotImplementedError()

    def values(self) -> Iterator[ValueT]:
        return (self._object_constructor(obj.resource_path.value) for obj in self._get_info_list())

    def items(self) -> Iterator[Tuple[str, ValueT]]:
        return (
            (obj.id, self._object_constructor(obj.resource_path.value))
            for obj in self._get_info_list()
        )

    def keys(self) -> Iterator[str]:
        return iter(self)

    def __contains__(self, key: str) -> bool:
        return key in list(self)

    def __len__(self) -> int:
        return len(self._get_info_list())

    def get(self, key: str, default: Optional[ValueT] = None) -> Optional[ValueT]:
        try:
            return self[key]
        except KeyError:
            return default
