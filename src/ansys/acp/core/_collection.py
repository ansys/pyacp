from typing import Callable, Generic, Iterator, Optional, Sequence, Tuple, TypeVar

from ansys.api.acp.v0.base_pb2 import BasicInfo

ValueT = TypeVar("ValueT")


class Collection(Generic[ValueT]):
    def __init__(
        self,
        list_method: Callable[[], Sequence[BasicInfo]],
        constructor: Callable[[str], ValueT],
        delete_method: Callable[[BasicInfo], None],
    ):
        # TODO: should the list method return instantiated objects, or
        # do we want to work with the bare protobuf responses here?
        self._list_method = list_method
        self._constructor = constructor
        self._delete_method = delete_method

    def __iter__(self) -> Iterator[str]:
        yield from (obj.id for obj in self._list_method())

    def __getitem__(self, key: str) -> ValueT:
        info = self._get_info_by_id(key)
        return self._constructor(info.resource_path.value)

    def _get_info_by_id(self, key: str) -> BasicInfo:
        for obj in self._list_method():
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
        self._delete_method(info)

    def clear(self) -> None:
        for info in self._list_method():
            self._delete_method(info)

    # def pop(self, key):
    #     raise NotImplementedError()

    # def popitem(self, key):
    #     raise NotImplementedError()

    def values(self) -> Iterator[ValueT]:
        return (self._constructor(obj.resource_path.value) for obj in self._list_method())

    def items(self) -> Iterator[Tuple[str, ValueT]]:
        return ((obj.id, self._constructor(obj.resource_path.value)) for obj in self._list_method())

    def keys(self) -> Iterator[str]:
        return iter(self)

    def __contains__(self, key: str) -> bool:
        return key in list(self)

    def __len__(self) -> int:
        return len(self._list_method())

    def get(self, key: str, default: Optional[ValueT] = None) -> Optional[ValueT]:
        try:
            return self[key]
        except KeyError:
            return default
