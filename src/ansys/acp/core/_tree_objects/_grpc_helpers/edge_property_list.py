from __future__ import annotations

from collections.abc import Iterable, Iterator, MutableSequence
import sys
from typing import Any, Callable, Protocol, TypeVar, cast, overload

from google.protobuf.message import Message
from typing_extensions import Self

from .._object_cache import ObjectCacheMixin, constructor_with_cache
from ..base import CreatableTreeObject
from .property_helper import _exposed_grpc_property, _wrap_doc, grpc_data_getter, grpc_data_setter

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


class EdgePropertyList(ObjectCacheMixin, MutableSequence[ValueT]):
    """Wrap graph edges of a specific type.

    Wraps links between objects of a specific type, for instance FabricWithAngle
    of a stackup. This object handles the conversion of the protobuf messages to the
    corresponding Python object and vice-versa.
    self._object_list holds the Python object. The python objects are stored
    to support editing in-place editing. This is achieved by passing a callback
    function to the python object.

    The edges (and parent object) is updated
    as soon as an item or one of its properties are changed.

    Note: sort is not implemented because the model definition often depends
    on the order.

    The LinkedObjectList should be used for graph edges without a specific type.
    For instance, element sets of an oriented element set.
    """

    @classmethod
    @constructor_with_cache(
        # TODO: check the logic w.r.t. reuse of id in the Python interpreter
        key_getter=lambda *args, parent_object, attribute_name, **kwargs: (
            id(parent_object),
            attribute_name,
        ),
        raise_on_invalid_key=True,
    )
    def _initialize_with_cache(
        cls: type[Self],
        *,
        parent_object: CreatableTreeObject,
        object_type: type[GenericEdgePropertyType],
        attribute_name: str,
        from_pb_constructor: Callable[[CreatableTreeObject, Message, Callable[[], None]], ValueT],
    ) -> Self:
        return cls(
            _parent_object=parent_object,
            _object_type=object_type,
            _attribute_name=attribute_name,
            _from_pb_constructor=from_pb_constructor,
        )

    @staticmethod
    def _cache_key_valid(key: Any) -> bool:
        try:
            (parent_object_id, attribute_name) = key
            if not attribute_name:
                return False
            if not isinstance(parent_object_id, int):
                return False
            return True
        except Exception:
            return False

    def __init__(
        self,
        *,
        _parent_object: CreatableTreeObject,
        _object_type: type[GenericEdgePropertyType],
        _attribute_name: str,
        _from_pb_constructor: Callable[[CreatableTreeObject, Message, Callable[[], None]], ValueT],
    ) -> None:
        getter = grpc_data_getter(_attribute_name, from_protobuf=list)
        setter = grpc_data_setter(_attribute_name, to_protobuf=lambda x: x)

        self._parent_object = _parent_object
        self._object_type = _object_type
        self._name = _attribute_name.split(".")[-1]

        self._object_constructor: Callable[
            [Message], ValueT
        ] = lambda pb_object: _from_pb_constructor(
            self._parent_object, pb_object, self._apply_changes
        )

        # get initial object list
        def get_object_list_from_parent_object() -> list[ValueT]:
            obj_list = []
            for item in getter(_parent_object):
                obj_list.append(self._object_constructor(item))
            return obj_list

        self._object_list = get_object_list_from_parent_object()

        def set_object_list(items: list[ValueT]) -> None:
            """Set the object list on the parent AND updates the internal object list."""
            pb_obj_list = []
            for item in items:
                if not item._check():
                    raise RuntimeError("Cannot initialize incomplete object.")
                pb_obj_list.append(item._to_pb_object())
                # update callback in case item was copied from another tree object
                # or if it is a new object
                item._set_callback_apply_changes(self._apply_changes)
            setter(_parent_object, pb_obj_list)
            # keep object list in sync with the backend. This is needed for the in-place editing
            self._object_list = items

        self._set_object_list = set_object_list

    def __len__(self) -> int:
        return len(self._object_list)

    @overload
    def __getitem__(self, index: int) -> ValueT:
        ...

    @overload
    def __getitem__(self, index: slice) -> list[ValueT]:
        ...

    def __getitem__(self, index: int | slice) -> ValueT | list[ValueT]:
        obj_list = self._object_list[index]
        if not isinstance(obj_list, list):
            assert isinstance(obj_list, self._object_type)
            return cast(ValueT, obj_list)
        return [item for item in obj_list]

    @overload
    def __setitem__(self, key: int, value: ValueT) -> None:
        ...

    @overload
    def __setitem__(self, key: slice, value: Iterable[ValueT]) -> None:
        ...

    def __setitem__(self, key: int | slice, value: ValueT | Iterable[ValueT]) -> None:
        obj_list = self._object_list
        if isinstance(value, Iterable):
            if not isinstance(key, slice):
                raise TypeError("Cannot assign to a single index with an iterable.")
            obj_list[key] = [item for item in value]
        else:
            if not isinstance(key, int):
                raise TypeError("Cannot assign to a slice with a single object.")
            obj_list[key] = value
        self._set_object_list(obj_list)

    def __delitem__(self, key: int | slice) -> None:
        obj_list = self._object_list
        del obj_list[key]
        self._set_object_list(obj_list)

    def __iter__(self) -> Iterator[ValueT]:
        obj_list = self._object_list
        yield from (item for item in obj_list)

    def __reversed__(self) -> Iterator[ValueT]:
        obj_list = self._object_list
        yield from (item for item in reversed(obj_list))

    def __contains__(self, item: object) -> bool:
        return item in self._object_list

    def append(self, value: ValueT) -> None:
        """Append an object to the list.

        Parameters
        ----------
        value :
            The object to append.
        """
        obj_list = self._object_list
        obj_list.append(value)
        self._set_object_list(obj_list)

    def count(self, value: ValueT) -> int:
        """Count the number of occurrences of an object in the list.

        Parameters
        ----------
        value : ValueT
            The object to count.
        """
        return self._object_list.count(value)

    def index(self, value: ValueT, start: int = 0, stop: int = sys.maxsize) -> int:
        """Return the index of the first occurrence of an object in the list.

        Parameters
        ----------
        value :
            The object to search for.
        start :
            The index to start searching from.
        stop :
            The index to stop searching at.
        """
        return self._object_list.index(value, start, stop)

    def extend(self, iterable: Iterable[ValueT]) -> None:
        """Extend the list by appending all the items from the iterable.

        Parameters
        ----------
        iterable :
            The iterable to append.
        """
        obj_list = self._object_list
        obj_list.extend([it for it in iterable])
        self._set_object_list(obj_list)

    def insert(self, index: int, value: ValueT) -> None:
        """Insert an object at a given position.

        Parameters
        ----------
        index :
            The index to insert at.
        value :
            The object to insert.
        """
        obj_list = self._object_list
        obj_list.insert(index, value)
        self._set_object_list(obj_list)

    def pop(self, index: int = -1) -> ValueT:
        """Remove and return the object at the given index.

        Parameters
        ----------
        index :
            The index of the object to remove.
        """
        obj_list = self._object_list
        obj = obj_list.pop(index)
        self._set_object_list(obj_list)
        return obj

    def remove(self, value: ValueT) -> None:
        """Remove the first occurrence of an object from the list.

        Parameters
        ----------
        value :
            The object to remove.
        """
        obj_list = self._object_list
        obj_list.remove(value)
        self._set_object_list(obj_list)

    def reverse(self) -> None:
        """Reverse the list in-place."""
        self._set_object_list(list(reversed(self._object_list)))

    def _apply_changes(self) -> None:
        """Apply changes to the list.

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
        return (
            f"<{self.__class__.__name__}[{self._object_type.__name__}] "
            + f"with parent {self._parent_object!r}, entries {self._object_list!r}>"
        )


def define_edge_property_list(
    attribute_name: str, value_type: type[GenericEdgePropertyType], doc: str | None = None
) -> Any:
    """Define a list of linked tree objects with link properties."""

    def getter(self: CreatableTreeObject) -> EdgePropertyList[GenericEdgePropertyType]:
        return EdgePropertyList._initialize_with_cache(
            parent_object=self,
            object_type=value_type,
            attribute_name=attribute_name,
            from_pb_constructor=value_type._from_pb_object,
        )

    def setter(self: CreatableTreeObject, value: list[GenericEdgePropertyType]) -> None:
        getter(self)[:] = value

    return _wrap_doc(_exposed_grpc_property(getter).setter(setter), doc=doc)
