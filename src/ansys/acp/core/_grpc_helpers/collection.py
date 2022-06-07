from typing import Callable, Generic, Iterator, List, Optional, Tuple, Type, TypeVar

from ansys.api.acp.v0.base_pb2 import BasicInfo

from .protocols import DeleteRequest, ListRequest, ResourceStub

ValueT = TypeVar("ValueT")


class Collection(Generic[ValueT]):
    def __init__(
        self,
        stub: ResourceStub,
        list_request: ListRequest,
        list_attribute: str,
        delete_request_class: Type[DeleteRequest],
        object_constructor: Callable[[str], ValueT],
    ):
        self._stub = stub
        self._list_request = list_request
        self._list_attribute = list_attribute
        self._delete_request_class = delete_request_class
        self._object_constructor = object_constructor

    def __iter__(self) -> Iterator[str]:
        yield from (obj.id for obj in self._get_info_list())

    def __getitem__(self, key: str) -> ValueT:
        info = self._get_info_by_id(key)
        return self._object_constructor(info.resource_path.value)

    def _get_info_list(self) -> List[BasicInfo]:
        return [
            obj.info for obj in getattr(self._stub.List(self._list_request), self._list_attribute)
        ]

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
