import sys
from typing import (
    Any,
    Callable,
    Generic,
    Iterable,
    Iterator,
    List,
    Protocol,
    Type,
    TypeVar,
    Union,
    cast,
)

from google.protobuf.message import Message
import numpy as np
from typing_extensions import Self

from ..base import CreatableTreeObject, TreeObject
from .property_helper import grpc_data_getter, grpc_data_setter

__all__ = ["GenericObjectList", "define_generic_object_list", "GenericObjectType"]


class GenericObjectType(Protocol):
    """Interface definition for ACP Resource service stubs."""

    def __init__(self, *kwargs):
        ...

    def object_constructor(self, parent_object: CreatableTreeObject, message: Message) -> Self:
        ...

    def message_type(self) -> Type[Message]:
        ...

    def to_pb_object(self) -> Message:
        ...

    def check(self) -> bool:
        ...

    def __equal__(self, other: Self) -> bool:
        ...


ValueT = TypeVar("ValueT", bound=GenericObjectType)


class GenericObjectList(Generic[ValueT]):
    def __init__(
        self,
        *,
        parent_object: TreeObject,
        object_class: Type[Any],
        attribute_name: str,
        object_constructor: Callable[[TreeObject, Message], ValueT],
    ) -> None:
        getter = grpc_data_getter(attribute_name, from_protobuf=list)
        setter = grpc_data_setter(attribute_name, to_protobuf=lambda x: x)

        self._parent_object = parent_object
        self._object_class = object_class
        self._attribute_name = attribute_name
        self._message_type = object_class().message_type()

        self._get_pb_object_list = cast(
            Callable[[], List[self._message_type]], lambda: getter(parent_object)
        )

        def set_pb_object_list(value: List[object_class().message_type()]) -> None:
            for item in value:
                if not self._object_class(self._parent_object, item).check():
                    raise RuntimeError("Cannot initialize incomplete object.")
            setter(parent_object, value)

        self._set_pb_object_list = set_pb_object_list
        self._object_constructor: Callable[
            [Message], ValueT
        ] = lambda pb_object: object_constructor(
            parent_object=self._parent_object, message=pb_object
        )

    def __len__(self) -> int:
        return len(self._get_pb_object_list())

    def __getitem__(self, index: Union[int, slice]) -> Union[ValueT, List[ValueT]]:
        pb_object = self._get_pb_object_list()[index]
        if not isinstance(pb_object, list):
            assert isinstance(pb_object, self._message_type)
            return self._object_constructor(pb_object)
        return [self._object_constructor(item) for item in pb_object]

    def __setitem__(self, key: Union[int, slice], value: Union[ValueT, List[ValueT]]) -> None:
        pb_object_list = self._get_pb_object_list()
        if isinstance(value, self._object_class):
            key = cast(int, key)
            pb_object_list[key] = value.to_pb_object()
        else:
            key = cast(slice, key)
            pb_object_list[key] = [item.to_pb_object() for item in value]
        self._set_pb_object_list(pb_object_list)

    def __delitem__(self, key: Union[int, slice]) -> None:
        pb_object_list = self._get_pb_object_list()
        del pb_object_list[key]
        self._set_pb_object_list(pb_object_list)

    def __iter__(self) -> Iterator[ValueT]:
        pb_object_list = self._get_pb_object_list()
        yield from (self._object_constructor(item) for item in pb_object_list)

    def __reversed__(self) -> Iterator[ValueT]:
        pb_object_list = self._get_pb_object_list()
        yield from (self._object_constructor(item) for item in reversed(pb_object_list))

    def __contains__(self, item: ValueT) -> bool:
        return item.to_pb_object() in self._get_pb_object_list()

    def append(self, value: ValueT) -> None:
        pb_object_list = self._get_pb_object_list()
        pb_object_list.append(value.to_pb_object())
        self._set_pb_object_list(pb_object_list)

    def count(self, value: ValueT) -> int:
        return self._get_pb_object_list().count(value.to_pb_object())

    def index(self, value: ValueT, start: int = 0, stop: int = sys.maxsize) -> int:
        return self._get_pb_object_list().index(value.to_pb_object(), start, stop)

    def extend(self, iterable: Iterable[ValueT]) -> None:
        pb_object_list = self._get_pb_object_list()
        pb_object_list.extend([it.to_pb_object() for it in iterable])
        self._set_pb_object_list(pb_object_list)

    def insert(self, index: int, value: ValueT) -> None:
        pb_object_list = self._get_pb_object_list()
        pb_object_list.insert(index, value.to_pb_object())
        self._set_pb_object_list(pb_object_list)

    def pop(self, index: int = -1) -> ValueT:
        pb_object_list = self._get_pb_object_list()
        rp = pb_object_list.pop(index)
        self._set_resourcepath_list(pb_object_list)
        return self._object_constructor(rp)

    def remove(self, value: ValueT) -> None:
        pb_object_list = self._get_pb_object_list()
        pb_object_list.remove(value.to_pb_object())
        self._set_pb_object_list(pb_object_list)

    def reverse(self) -> None:
        self._set_pb_object_list(list(reversed(self._get_pb_object_list())))

    def sort(
        self, *, key: Callable[[ValueT], Any] = lambda obj: obj.name, reverse: bool = False
    ) -> None:
        pb_object_list = self._get_pb_object_list()
        evaluated_key_list = [key(self._object_constructor(rp)) for rp in pb_object_list]
        idx_list = np.argsort(evaluated_key_list)
        if reverse:
            idx_list = idx_list[::-1]
        pb_object_list = list(np.array(pb_object_list)[idx_list])
        self._set_pb_object_list(pb_object_list)

    def __eq__(self, other: Any) -> Any:
        return list(self) == other


ChildT = TypeVar("ChildT", bound=GenericObjectType)


def define_generic_object_list(attribute_name: str, value_type: ChildT) -> Any:
    def getter(self: ValueT) -> GenericObjectList[ChildT]:
        return GenericObjectList(
            parent_object=self,
            object_class=value_type,
            attribute_name=attribute_name,
            object_constructor=value_type.object_constructor,
        )

    def setter(self: ValueT, value: List[ChildT]) -> None:
        getter(self)[:] = value

    return property(getter).setter(setter)
