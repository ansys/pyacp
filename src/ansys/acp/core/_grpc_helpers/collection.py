from __future__ import annotations

from typing import Callable, Generic, Iterator, List, Optional, Tuple, Type, TypeVar

from ansys.api.acp.v0.base_pb2 import BasicInfo, CollectionPath, ResourcePath

from .._property_helper import ResourceProtocol
from .._resource_paths import join as _rp_join
from .._server import ServerProtocol
from .protocols import DeleteRequest, ListRequest, ResourceStub

ValueT = TypeVar("ValueT", bound=ResourceProtocol)


class Collection(Generic[ValueT]):
    def __init__(
        self,
        *,
        list_function: Callable[[], List[BasicInfo]],
        delete_function: Callable[[BasicInfo], None],
        constructor: Callable[[str], ValueT],
    ):
        self._list_function = list_function
        self._delete_function = delete_function
        self._constructor = constructor

    @classmethod
    def from_types(
        cls,
        *,
        server: ServerProtocol,
        parent_resource_path: ResourcePath,
        stub_class: Type[ResourceStub],
        list_attribute: str,
        list_request_class: Type[ListRequest],
        delete_request_class: Type[DeleteRequest],
        object_class: Type[ValueT],
    ) -> Collection[ValueT]:
        stub = stub_class(server.channel)

        collection_path = CollectionPath(
            value=_rp_join(parent_resource_path.value, object_class.COLLECTION_LABEL)
        )
        list_request = list_request_class(collection_path=collection_path)

        def list_function() -> List[BasicInfo]:
            return [obj.info for obj in getattr(stub.List(list_request), list_attribute)]

        def delete_function(info: BasicInfo) -> None:
            stub.Delete(delete_request_class(info=info))

        def constructor(resource_path: str) -> ValueT:
            return object_class(resource_path=resource_path, server=server)

        return cls(
            list_function=list_function, delete_function=delete_function, constructor=constructor
        )

    def __iter__(self) -> Iterator[str]:
        yield from (obj.id for obj in self._get_info_list())

    def __getitem__(self, key: str) -> ValueT:
        info = self._get_info_by_id(key)
        return self._constructor(info.resource_path.value)

    def _get_info_list(self) -> List[BasicInfo]:
        res = self._list_function()
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
        self._delete_function(info)

    def clear(self) -> None:
        for info in self._get_info_list():
            self._delete_function(info)

    # def pop(self, key):
    #     raise NotImplementedError()

    # def popitem(self, key):
    #     raise NotImplementedError()

    def values(self) -> Iterator[ValueT]:
        return (self._constructor(obj.resource_path.value) for obj in self._get_info_list())

    def items(self) -> Iterator[Tuple[str, ValueT]]:
        return (
            (obj.id, self._constructor(obj.resource_path.value)) for obj in self._get_info_list()
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
