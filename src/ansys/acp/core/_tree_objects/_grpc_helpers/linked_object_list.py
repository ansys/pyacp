from __future__ import annotations

from collections.abc import Iterable, Iterator, MutableSequence
from functools import partial
import sys
from typing import Any, Callable, TypeVar, cast, overload

from grpc import Channel
import numpy as np

from ansys.api.acp.v0.base_pb2 import ResourcePath

from ..base import CreatableTreeObject, TreeObject
from .polymorphic_from_pb import tree_object_from_resource_path
from .property_helper import _exposed_grpc_property, _wrap_doc, grpc_data_getter, grpc_data_setter

ValueT = TypeVar("ValueT", bound=CreatableTreeObject)


__all__ = ["LinkedObjectList", "define_linked_object_list"]


class LinkedObjectList(MutableSequence[ValueT]):
    """List of linked tree objects."""
    def __init__(
        self,
        *,
        parent_object: TreeObject,
        attribute_name: str,
        object_constructor: Callable[[ResourcePath, Channel], ValueT],
    ) -> None:
        getter = grpc_data_getter(attribute_name, from_protobuf=list)
        setter = grpc_data_setter(attribute_name, to_protobuf=lambda x: x)

        self._get_resourcepath_list = cast(
            Callable[[], list[ResourcePath]], lambda: getter(parent_object)
        )

        def set_resourcepath_list(value: list[ResourcePath]) -> None:
            if not all([rp.value for rp in value]):
                # Check for empty resource paths
                raise RuntimeError("Cannot link to unstored objects.")
            setter(parent_object, value)

        self._set_resourcepath_list = set_resourcepath_list
        self._object_constructor: Callable[
            [ResourcePath], ValueT
        ] = lambda resource_path: object_constructor(resource_path, parent_object._channel)

    def __len__(self) -> int:
        return len(self._get_resourcepath_list())

    @overload
    def __getitem__(self, index: int) -> ValueT:
        ...

    @overload
    def __getitem__(self, index: slice) -> list[ValueT]:
        ...

    def __getitem__(self, index: int | slice) -> ValueT | list[ValueT]:
        resource_path = self._get_resourcepath_list()[index]
        if not isinstance(resource_path, list):
            assert isinstance(resource_path, ResourcePath)
            return self._object_constructor(resource_path)
        return [self._object_constructor(item) for item in resource_path]

    @overload
    def __setitem__(self, key: int, value: ValueT) -> None:
        ...

    @overload
    def __setitem__(self, key: slice, value: Iterable[ValueT]) -> None:
        ...

    def __setitem__(self, key: int | slice, value: ValueT | Iterable[ValueT]) -> None:
        resource_path_list = self._get_resourcepath_list()
        if isinstance(value, TreeObject):
            if not isinstance(key, int):
                raise TypeError("Cannot assign to a slice with a single object.")
            resource_path_list[key] = value._resource_path
        else:
            if not isinstance(key, slice):
                raise TypeError("Cannot assign to a single index with an iterable.")
            resource_path_list[key] = [item._resource_path for item in value]
        self._set_resourcepath_list(resource_path_list)

    def __delitem__(self, key: int | slice) -> None:
        resource_path_list = self._get_resourcepath_list()
        del resource_path_list[key]
        self._set_resourcepath_list(resource_path_list)

    def __iter__(self) -> Iterator[ValueT]:
        resource_path_list = self._get_resourcepath_list()
        yield from (self._object_constructor(item) for item in resource_path_list)

    def __reversed__(self) -> Iterator[ValueT]:
        resource_path_list = self._get_resourcepath_list()
        yield from (self._object_constructor(item) for item in reversed(resource_path_list))

    def __contains__(self, item: object) -> bool:
        return (
            hasattr(item, "_resource_path") and item._resource_path in self._get_resourcepath_list()
        )

    def append(self, object: ValueT) -> None:
        """Append an object to the list.

        Parameters
        ----------
        object:
            Object to append.
        """
        resource_path_list = self._get_resourcepath_list()
        resource_path_list.append(object._resource_path)
        self._set_resourcepath_list(resource_path_list)

    def count(self, value: ValueT) -> int:
        """Count the number of occurrences of an object in the list.

        Parameters
        ----------
        value:
            Object to count.
        """
        return self._get_resourcepath_list().count(value._resource_path)

    def index(self, value: ValueT, start: int = 0, stop: int = sys.maxsize) -> int:
        """Return the index of the first occurrence of an object in the list.

        Parameters
        ----------
        value:
            Object to find.
        """
        return self._get_resourcepath_list().index(value._resource_path, start, stop)

    def extend(self, iterable: Iterable[ValueT]) -> None:
        """Extend the list with an iterable of objects.

        Parameters
        ----------
        iterable:
            Iterable of objects to append.
        """
        resource_path_list = self._get_resourcepath_list()
        resource_path_list.extend([it._resource_path for it in iterable])
        self._set_resourcepath_list(resource_path_list)

    def insert(self, index: int, object: ValueT) -> None:
        """Insert an object at a given index.

        Parameters
        ----------
        index:
            Index to insert at.
        object:
            Object to insert.
        """
        resource_path_list = self._get_resourcepath_list()
        resource_path_list.insert(index, object._resource_path)
        self._set_resourcepath_list(resource_path_list)

    def pop(self, index: int = -1) -> ValueT:
        """Remove and return an object from the list.

        Parameters
        ----------
        index:
            Index of the object to be removed.
        """
        resource_path_list = self._get_resourcepath_list()
        rp = resource_path_list.pop(index)
        self._set_resourcepath_list(resource_path_list)
        return self._object_constructor(rp)

    def remove(self, value: ValueT) -> None:
        """Remove the first occurrence of an object from the list.

        Parameters
        ----------
        value:
            Object to remove.
        """
        resource_path_list = self._get_resourcepath_list()
        resource_path_list.remove(value._resource_path)
        self._set_resourcepath_list(resource_path_list)

    def reverse(self) -> None:
        """Reverse the list in-place."""
        self._set_resourcepath_list(list(reversed(self._get_resourcepath_list())))

    def sort(
        self, *, key: Callable[[ValueT], Any] = lambda obj: obj.name, reverse: bool = False
    ) -> None:
        """Sort the list in-place.

        Parameters
        ----------
        key:
            Key function to sort by.
        reverse:
            Whether to sort in reverse order.
        """
        resource_path_list = self._get_resourcepath_list()
        evaluated_key_list = [key(self._object_constructor(rp)) for rp in resource_path_list]
        idx_list = np.argsort(evaluated_key_list)
        if reverse:
            idx_list = idx_list[::-1]
        resource_path_list = list(np.array(resource_path_list)[idx_list])
        self._set_resourcepath_list(resource_path_list)

    def __eq__(self, other: Any) -> Any:
        return list(self) == other


ChildT = TypeVar("ChildT", bound=CreatableTreeObject)


def define_linked_object_list(
    attribute_name: str, object_class: type[ChildT], doc: str | None = None
) -> Any:
    """Define a list of linked tree objects."""
    def getter(self: ValueT) -> LinkedObjectList[ChildT]:
        return LinkedObjectList(
            parent_object=self,
            attribute_name=attribute_name,
            object_constructor=object_class._from_resource_path,
        )

    def setter(self: ValueT, value: list[ChildT]) -> None:
        getter(self)[:] = value

    return _wrap_doc(_exposed_grpc_property(getter).setter(setter), doc=doc)


def define_polymorphic_linked_object_list(
    attribute_name: str, allowed_types: tuple[Any, ...]
) -> Any:
    """Define a list of linked tree objects with polymorphic types."""
    def getter(self: ValueT) -> LinkedObjectList[Any]:
        return LinkedObjectList(
            parent_object=self,
            attribute_name=attribute_name,
            object_constructor=partial(tree_object_from_resource_path, allowed_types=allowed_types),
        )

    def setter(self: ValueT, value: list[Any]) -> None:
        getter(self)[:] = value

    return _exposed_grpc_property(getter).setter(setter)
