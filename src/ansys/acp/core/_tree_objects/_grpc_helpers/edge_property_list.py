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

__all__ = ["EdgePropertyList", "define_edge_property_list", "GenericEdgePropertyType"]


class GenericEdgePropertyType(Protocol):
    """Protocol for the definition of ACP edge properties such as FabricWithAngle."""

    def __init__(self, *kwargs: Any) -> None:
        ...

    @classmethod
    def _from_pb_object(
        cls,
        parent_object: CreatableTreeObject,
        message: Any,
        callback_apply_changes: Callable[[], None],
    ) -> Self:
        ...

    def _to_pb_object(self) -> Message:
        ...

    def _check(self) -> bool:
        ...

    def _set_callback_apply_changes(self, callback_apply_changes: Callable[[], None]) -> None:
        ...


ValueT = TypeVar("ValueT", bound=GenericEdgePropertyType)


class EdgePropertyList(Generic[ValueT]):
    def __init__(
        self,
        *,
        parent_object: CreatableTreeObject,
        object_type: Type[GenericEdgePropertyType],
        attribute_name: str,
        from_pb_constructor: Callable[[CreatableTreeObject, Message, Callable[[], None]], ValueT],
    ) -> None:
        getter = grpc_data_getter(attribute_name, from_protobuf=list)
        setter = grpc_data_setter(attribute_name, to_protobuf=lambda x: x)

        self._parent_object = parent_object
        self._object_type = object_type
        self._name = attribute_name.split(".")[-1]

        self._object_constructor: Callable[
            [Message], ValueT
        ] = lambda pb_object: from_pb_constructor(
            self._parent_object, pb_object, self._apply_changes
        )

        # get initial object list
        def get_object_list_from_parent_object() -> List[ValueT]:
            obj_list = []
            for item in getter(parent_object):
                obj_list.append(self._object_constructor(item))
            return obj_list

        self._object_list = get_object_list_from_parent_object()

        def set_object_list(value: List[ValueT]) -> None:
            pb_obj_list = []
            for item in value:
                if not item._check():
                    raise RuntimeError("Cannot initialize incomplete object.")
                pb_obj_list.append(item._to_pb_object())
                # update callback in case item was copied from another tree object
                # or if it is a new object
                item._set_callback_apply_changes(self._apply_changes)
            setter(parent_object, pb_obj_list)
            # keep object list in sync with the backend. This is needed for the in-place editing
            self._object_list = value

        self._set_object_list = set_object_list

    def __len__(self) -> int:
        return len(self._object_list)

    def __getitem__(self, index: Union[int, slice]) -> Union[ValueT, List[ValueT]]:
        obj_list = self._object_list[index]
        if not isinstance(obj_list, list):
            assert isinstance(obj_list, self._object_type)
            return cast(ValueT, obj_list)
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

    def _apply_changes(self) -> None:
        """
        Use to support in-place modification.
        This function applies the changes if someone edits one entry of the list.
        """
        self._set_object_list(self._object_list)

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

    def __repr__(self) -> str:
        entries = ", ".join(f"{item}" for item in self._object_list)
        return f"{self._parent_object.name} - {self._name}({entries})"


def define_edge_property_list(
    attribute_name: str, value_type: Type[GenericEdgePropertyType]
) -> Any:
    def getter(self: CreatableTreeObject) -> EdgePropertyList[GenericEdgePropertyType]:
        return EdgePropertyList(
            parent_object=self,
            object_type=value_type,
            attribute_name=attribute_name,
            from_pb_constructor=value_type._from_pb_object,
        )

    def setter(self: CreatableTreeObject, value: List[GenericEdgePropertyType]) -> None:
        getter(self)[:] = value

    return property(getter).setter(setter)
