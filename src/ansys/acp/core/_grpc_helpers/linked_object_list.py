from typing import Any, Callable, Generic, Iterable, Iterator, List, TypeVar, Union

from .._tree_objects.base import CreatableTreeObject

ValueT = TypeVar("ValueT", bound=CreatableTreeObject)


class LinkedObjectList(Generic[ValueT]):
    #     def __init__(self, ):

    def __len__(self) -> int:
        raise NotImplementedError()

    def __getitem__(self, index: Union[int, slice]) -> ValueT:
        raise NotImplementedError()

    def __setitem__(self, key: Union[int, slice], value: Union[ValueT, List[ValueT]]) -> None:
        raise NotImplementedError()

    def __delitem__(self, key: Union[int, slice], value: ValueT) -> None:
        raise NotImplementedError()

    def __iter__(self) -> Iterator[ValueT]:
        raise NotImplementedError()

    def __reversed__(self) -> Iterator[ValueT]:
        raise NotImplementedError()

    def __contains__(self, item: ValueT) -> bool:
        raise NotImplementedError()

    def append(self, object: ValueT) -> None:
        raise NotImplementedError()

    def count(self, value: ValueT) -> int:
        raise NotImplementedError()

    def index(self, value: ValueT, start: int = 0, stop: int = ...) -> int:
        raise NotImplementedError()

    def extend(self, iterable: Iterable[ValueT]) -> None:
        raise NotImplementedError()

    def insert(self, index: int, object: ValueT) -> None:
        raise NotImplementedError()

    def pop(self, index: int = -1) -> ValueT:
        raise NotImplementedError()

    def remove(self, value: ValueT) -> None:
        raise NotImplementedError()

    def reverse(self) -> None:
        raise NotImplementedError()

    def sort(self, *, key: Callable[[ValueT], Any], reverse: bool = False) -> None:
        raise NotImplementedError()
