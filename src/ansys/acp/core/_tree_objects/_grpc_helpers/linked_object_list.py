# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator, MutableSequence
from functools import partial
import sys
from typing import Any, TypeVar, cast, overload

from grpc import Channel
import numpy as np
from typing_extensions import Self

from ansys.api.acp.v0.base_pb2 import ResourcePath

from .._object_cache import ObjectCacheMixin, constructor_with_cache
from ..base import TreeObject, TreeObjectBase
from .polymorphic_from_pb import tree_object_from_resource_path
from .property_helper import _exposed_grpc_property, _wrap_doc, grpc_data_getter, grpc_data_setter

ValueT = TypeVar("ValueT", bound=TreeObjectBase)


__all__ = ["LinkedObjectList", "define_linked_object_list", "define_polymorphic_linked_object_list"]


class LinkedObjectList(ObjectCacheMixin, MutableSequence[ValueT]):
    """List of linked tree objects."""

    @classmethod
    @constructor_with_cache(
        # NOTE greschd Feb'23:
        # We use the parent object's id() as part of the cache key since
        # the LinkedObjectList keeps its parent alive. This means the
        # id() does not change (and cannot be reused) as long as the
        # cache entry is alive.
        # This is somewhat incidental, but checked (indirectly) by the
        # object permanence tests. If we want to get rid of this, we
        # would instead need to find a way to handle the case where the
        # parent object is being stored.
        key_getter=lambda *args, parent_object, attribute_name, **kwargs: (
            id(parent_object),
            attribute_name,
        ),
        raise_on_invalid_key=True,
    )
    def _initialize_with_cache(
        cls: type[Self],
        *,
        parent_object: TreeObject,
        attribute_name: str,
        object_constructor: Callable[[ResourcePath, Channel], ValueT],
        allowed_types: tuple[type[ValueT], ...],
    ) -> Self:
        return cls(
            _parent_object=parent_object,
            _attribute_name=attribute_name,
            _object_constructor=object_constructor,
            _allowed_types=allowed_types,
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
        _parent_object: TreeObject,
        _attribute_name: str,
        _object_constructor: Callable[[ResourcePath, Channel], ValueT],
        _allowed_types: tuple[Any, ...],
    ) -> None:
        getter = grpc_data_getter(_attribute_name, from_protobuf=list)
        setter = grpc_data_setter(_attribute_name, to_protobuf=lambda x: x)

        self._get_resourcepath_list = cast(
            Callable[[], list[ResourcePath]], lambda: getter(_parent_object)
        )

        def set_resourcepath_list(value: list[ResourcePath]) -> None:
            if not all([rp.value for rp in value]):
                # Check for empty resource paths
                raise RuntimeError("Cannot link to unstored objects.")
            setter(_parent_object, value)

        self._set_resourcepath_list = set_resourcepath_list
        self._object_constructor: Callable[[ResourcePath], ValueT] = (
            lambda resource_path: _object_constructor(resource_path, _parent_object._server_wrapper)
        )
        self._allowed_types = _allowed_types
        self._allowed_types_str = ", ".join([cls.__name__ for cls in _allowed_types])

    def __len__(self) -> int:
        return len(self._get_resourcepath_list())

    @overload
    def __getitem__(self, index: int) -> ValueT: ...

    @overload
    def __getitem__(self, index: slice) -> list[ValueT]: ...

    def __getitem__(self, index: int | slice) -> ValueT | list[ValueT]:
        resource_path = self._get_resourcepath_list()[index]
        if not isinstance(resource_path, list):
            assert isinstance(resource_path, ResourcePath)
            return self._object_constructor(resource_path)
        return [self._object_constructor(item) for item in resource_path]

    @overload
    def __setitem__(self, key: int, value: ValueT) -> None: ...

    @overload
    def __setitem__(self, key: slice, value: Iterable[ValueT]) -> None: ...

    def __setitem__(self, key: int | slice, value: ValueT | Iterable[ValueT]) -> None:
        resource_path_list = self._get_resourcepath_list()
        if isinstance(value, TreeObjectBase):
            self._check_type(value)
            if not isinstance(key, int):
                raise TypeError("Cannot assign to a slice with a single object.")
            resource_path_list[key] = value._resource_path
        else:
            if not isinstance(key, slice):
                raise TypeError("Cannot assign to a single index with an iterable.")
            for item in value:
                self._check_type(item)
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
        self._check_type(object)
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
        for it in iterable:
            self._check_type(it)
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
        self._check_type(object)
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

    def __repr__(self) -> str:
        return f"<LinkedObjectList([{', '.join(repr(val) for val in self)}])>"

    def _check_type(self, object: Any) -> None:
        if not isinstance(object, self._allowed_types):
            raise TypeError(
                f"List items must be of type {self._allowed_types_str}, not {type(object).__name__}."
            )


ParentT = TypeVar("ParentT", bound=TreeObject)
ChildT = TypeVar("ChildT", bound=TreeObjectBase)


def define_linked_object_list(
    attribute_name: str, object_class: type[ChildT], doc: str | None = None
) -> Any:
    """Define a list of linked tree objects."""

    def getter(self: ParentT) -> LinkedObjectList[ChildT]:
        return LinkedObjectList._initialize_with_cache(
            parent_object=self,
            attribute_name=attribute_name,
            object_constructor=object_class._from_resource_path,
            allowed_types=(object_class,),
        )

    def setter(self: ParentT, value: list[ChildT]) -> None:
        getter(self)[:] = value

    return _wrap_doc(_exposed_grpc_property(getter).setter(setter), doc=doc)


def define_polymorphic_linked_object_list(
    attribute_name: str,
    allowed_types: tuple[Any, ...] | None = None,
    allowed_types_getter: Callable[[], tuple[Any, ...]] | None = None,
) -> Any:
    """Define a list of linked tree objects with polymorphic types."""
    if allowed_types is None != allowed_types_getter is None:
        raise ValueError("Exactly one of allowed_types and allowed_types_getter must be provided.")

    def getter(self: ParentT) -> LinkedObjectList[Any]:
        nonlocal allowed_types
        if allowed_types_getter is not None:
            allowed_types = allowed_types_getter()

        assert allowed_types is not None
        return LinkedObjectList(
            _parent_object=self,
            _attribute_name=attribute_name,
            _object_constructor=partial(
                tree_object_from_resource_path, allowed_types=allowed_types
            ),
            _allowed_types=allowed_types,
        )

    def setter(self: ParentT, value: list[Any]) -> None:
        getter(self)[:] = value

    return _exposed_grpc_property(getter).setter(setter)
