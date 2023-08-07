import sys
from typing import Any, Callable, Generic, Iterable, Iterator, List, Type, TypeVar, Union, cast

from grpc import Channel
import numpy as np

from ansys.api.acp.v0.base_pb2 import ResourcePath

from ..base import CreatableTreeObject, TreeObject
from .property_helper import _exposed_grpc_property, grpc_data_getter, grpc_data_setter

ValueT = TypeVar("ValueT", bound=CreatableTreeObject)


__all__ = ["LinkedObjectList", "define_linked_object_list"]


class LinkedObjectList(Generic[ValueT]):
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
            Callable[[], List[ResourcePath]], lambda: getter(parent_object)
        )

        def set_resourcepath_list(value: List[ResourcePath]) -> None:
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

    def __getitem__(self, index: Union[int, slice]) -> Union[ValueT, List[ValueT]]:
        resource_path = self._get_resourcepath_list()[index]
        if not isinstance(resource_path, list):
            assert isinstance(resource_path, ResourcePath)
            return self._object_constructor(resource_path)
        return [self._object_constructor(item) for item in resource_path]

    def __setitem__(self, key: Union[int, slice], value: Union[ValueT, List[ValueT]]) -> None:
        resource_path_list = self._get_resourcepath_list()
        if isinstance(value, TreeObject):
            key = cast(int, key)
            resource_path_list[key] = value._resource_path
        else:
            key = cast(slice, key)
            resource_path_list[key] = [item._resource_path for item in value]
        self._set_resourcepath_list(resource_path_list)

    def __delitem__(self, key: Union[int, slice]) -> None:
        resource_path_list = self._get_resourcepath_list()
        del resource_path_list[key]
        self._set_resourcepath_list(resource_path_list)

    def __iter__(self) -> Iterator[ValueT]:
        resource_path_list = self._get_resourcepath_list()
        yield from (self._object_constructor(item) for item in resource_path_list)

    def __reversed__(self) -> Iterator[ValueT]:
        resource_path_list = self._get_resourcepath_list()
        yield from (self._object_constructor(item) for item in reversed(resource_path_list))

    def __contains__(self, item: ValueT) -> bool:
        return item._resource_path in self._get_resourcepath_list()

    def append(self, object: ValueT) -> None:
        resource_path_list = self._get_resourcepath_list()
        resource_path_list.append(object._resource_path)
        self._set_resourcepath_list(resource_path_list)

    def count(self, value: ValueT) -> int:
        return self._get_resourcepath_list().count(value._resource_path)

    def index(self, value: ValueT, start: int = 0, stop: int = sys.maxsize) -> int:
        return self._get_resourcepath_list().index(value._resource_path, start, stop)

    def extend(self, iterable: Iterable[ValueT]) -> None:
        resource_path_list = self._get_resourcepath_list()
        resource_path_list.extend([it._resource_path for it in iterable])
        self._set_resourcepath_list(resource_path_list)

    def insert(self, index: int, object: ValueT) -> None:
        resource_path_list = self._get_resourcepath_list()
        resource_path_list.insert(index, object._resource_path)
        self._set_resourcepath_list(resource_path_list)

    def pop(self, index: int = -1) -> ValueT:
        resource_path_list = self._get_resourcepath_list()
        rp = resource_path_list.pop(index)
        self._set_resourcepath_list(resource_path_list)
        return self._object_constructor(rp)

    def remove(self, value: ValueT) -> None:
        resource_path_list = self._get_resourcepath_list()
        resource_path_list.remove(value._resource_path)
        self._set_resourcepath_list(resource_path_list)

    def reverse(self) -> None:
        self._set_resourcepath_list(list(reversed(self._get_resourcepath_list())))

    def sort(
        self, *, key: Callable[[ValueT], Any] = lambda obj: obj.name, reverse: bool = False
    ) -> None:
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


def define_linked_object_list(attribute_name: str, object_class: Type[ChildT]) -> Any:
    def getter(self: ValueT) -> LinkedObjectList[ChildT]:
        return LinkedObjectList(
            parent_object=self,
            attribute_name=attribute_name,
            object_constructor=object_class._from_resource_path,
        )

    def setter(self: ValueT, value: List[ChildT]) -> None:
        getter(self)[:] = value

    return _exposed_grpc_property(getter).setter(setter)
