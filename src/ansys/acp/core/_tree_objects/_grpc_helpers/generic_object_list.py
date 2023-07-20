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
from typing_extensions import Self

from ..base import CreatableTreeObject
from .property_helper import grpc_data_getter, grpc_data_setter

__all__ = ["GenericObjectList", "define_generic_object_list", "GenericObjectType"]

class GenericObjectList:
    pass


class GenericObjectType(Protocol):
    """Interface definition for ACP Resource service stubs."""

    def __init__(self, *kwargs: Any) -> None:
        ...

    @classmethod
    def object_constructor(cls, parent_object: CreatableTreeObject, message: Any, generic_list_obj: GenericObjectList) -> Self:
        ...

    def message_type(self) -> Type[Message]:
        ...

    def to_pb_object(self) -> Message:
        ...

    def check(self) -> bool:
        ...


ValueT = TypeVar("ValueT", bound=GenericObjectType)


class GenericObjectList(Generic[ValueT]):
    def __init__(
            self,
            *,
            parent_object: CreatableTreeObject,
            object_class: Type[GenericObjectType],
            attribute_name: str,
            object_constructor: Callable[[CreatableTreeObject, Message], ValueT],
    ) -> None:
        getter = grpc_data_getter(attribute_name, from_protobuf=list)
        setter = grpc_data_setter(attribute_name, to_protobuf=lambda x: x)

        self._parent_object = parent_object
        self._object_class = object_class
        self._attribute_name = attribute_name
        self._message_type = object_class().message_type()

        self._object_constructor: Callable[
            [Message], ValueT
        ] = lambda pb_object: object_constructor(self._parent_object, pb_object, self)

        # get initial object list
        def get_object_list_from_parent_object() -> List[GenericObjectType]:
            obj_list = []
            for item in getter(parent_object):
                obj_list.append(self._object_constructor(item))
            return obj_list

        self._object_list = get_object_list_from_parent_object()

        def set_object_list(value: List[GenericObjectType]) -> None:
            pb_obj_list = []
            for item in value:
                if not item.check():
                    raise RuntimeError("Cannot initialize incomplete object.")
                pb_obj_list.append(item.to_pb_object())
            setter(parent_object, pb_obj_list)
            # keep object list in sync with the backend
            self._object_list = get_object_list_from_parent_object()

        self._set_object_list = set_object_list

    def __len__(self) -> int:
        return len(self._object_list)

    def __getitem__(self, index: Union[int, slice]) -> Union[ValueT, List[ValueT]]:
        obj_list = self._object_list[index]
        if not isinstance(obj_list, list):
            assert isinstance(obj_list, self._object_class)
            return obj_list
        return [item for item in obj_list]

    def __setitem__(self, key: Union[int, slice], value: Union[ValueT, List[ValueT]]) -> None:
        obj_list = self._object_list
        if isinstance(value, Iterable):
            key = cast(slice, key)
            obj_list[key] = [item for item in value]
        else:
            key = cast(int, key)
            obj_list[key] = value
        self._set_object_list(obj_list)

    def __delitem__(self, key: Union[int, slice]) -> None:
        obj_list = self._object_list
        del obj_list[key]
        self._set_object_list(obj_list)

    def __iter__(self) -> Iterator[ValueT]:
        obj_list = self._object_list
        yield from (item for item in obj_list)

    def __reversed__(self) -> Iterator[ValueT]:
        obj_list = self._object_list
        yield from (item for item in reversed(obj_list))

    def __contains__(self, item: ValueT) -> bool:
        return item in self._object_list

    def append(self, value: ValueT) -> None:
        obj_list = self._object_list
        obj_list.append(value)
        self._set_object_list(obj_list)

    def count(self, value: ValueT) -> int:
        return self._object_list.count(value)

    def index(self, value: ValueT, start: int = 0, stop: int = sys.maxsize) -> int:
        return self._object_list.index(value, start, stop)

    def extend(self, iterable: Iterable[ValueT]) -> None:
        obj_list = self._object_list
        obj_list.extend([it for it in iterable])
        self._set_object_list(obj_list)

    def insert(self, index: int, value: ValueT) -> None:
        obj_list = self._object_list
        obj_list.insert(index, value)
        self._set_object_list(obj_list)

    def pop(self, index: int = -1) -> ValueT:
        obj_list = self._object_list
        obj = obj_list.pop(index)
        self._set_object_list(obj_list)
        return obj

    def remove(self, value: ValueT) -> None:
        obj_list = self._object_list
        obj_list.remove(value)
        self._set_object_list(obj_list)

    def reverse(self) -> None:
        self._set_object_list(list(reversed(self._object_list)))

    """
    It does not make to sense to sort them because the model depends on the order
    def sort(
        self, *, key: Callable[[ValueT], Any] = lambda obj: obj.__lt__, reverse: bool = False
    ) -> None:
        pb_object_list = self._get_pb_object_list()
        evaluated_key_list = [key(self._object_constructor(obj)) for obj in pb_object_list]
        idx_list = np.argsort(evaluated_key_list)
        if reverse:
            idx_list = idx_list[::-1]
        pb_object_list = list(np.array(pb_object_list)[idx_list])
        self._set_pb_object_list(pb_object_list)

    """

    def __eq__(self, other: Any) -> Any:
        return list(self) == other


def define_generic_object_list(attribute_name: str, value_type: Type[GenericObjectType]) -> Any:
    def getter(self: CreatableTreeObject) -> GenericObjectList[GenericObjectType]:
        return GenericObjectList(
            parent_object=self,
            object_class=value_type,
            attribute_name=attribute_name,
            object_constructor=value_type.object_constructor,
        )

    def setter(self: CreatableTreeObject, value: List[GenericObjectType]) -> None:
        getter(self)[:] = value

    return property(getter).setter(setter)
