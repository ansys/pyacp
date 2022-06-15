from __future__ import annotations

from typing import Any, Callable, Generic, Iterator, List, Optional, Tuple, Type, TypeVar

from grpc import Channel

from ansys.api.acp.v0.base_pb2 import BasicInfo, CollectionPath, ResourcePath

from .._resource_paths import join as _rp_join
from .._tree_objects.base import TreeObject
from .stub_info.base import StubWrapper

ValueT = TypeVar("ValueT", bound=TreeObject)

__all__ = ["Collection", "define_collection"]


class Collection(Generic[ValueT]):
    def __init__(
        self,
        *,
        list_function: Callable[[], List[BasicInfo]],
        delete_function: Callable[[BasicInfo], None],
        constructor: Callable[[str], ValueT],
    ):
        self._list_function = list_function
        self._delete_function = delete_function
        self._constructor = constructor

    @classmethod
    def from_types(
        cls,
        *,
        channel: Channel,
        parent_resource_path: ResourcePath,
        stub_wrapper: StubWrapper,
        object_class: Type[ValueT],
    ) -> Collection[ValueT]:
        collection_path = CollectionPath(
            value=_rp_join(parent_resource_path.value, object_class.COLLECTION_LABEL)
        )

        def list_function() -> List[BasicInfo]:
            return [obj.info for obj in stub_wrapper.list(collection_path)]

        def delete_function(info: BasicInfo) -> None:
            stub_wrapper.delete(info)

        def constructor(resource_path: str) -> ValueT:
            return object_class.from_resource_path(resource_path=resource_path, channel=channel)

        return cls(
            list_function=list_function, delete_function=delete_function, constructor=constructor
        )

    def __iter__(self) -> Iterator[str]:
        yield from (obj.id for obj in self._get_info_list())

    def __getitem__(self, key: str) -> ValueT:
        info = self._get_info_by_id(key)
        return self._constructor(info.resource_path.value)

    def _get_info_list(self) -> List[BasicInfo]:
        res = self._list_function()
        if len(set(obj.id for obj in res)) != len(res):
            raise ValueError("Duplicate ID in Collection.")
        return res

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
        self._delete_function(info)

    def clear(self) -> None:
        for info in self._get_info_list():
            self._delete_function(info)

    # def pop(self, key):
    #     raise NotImplementedError()

    # def popitem(self, key):
    #     raise NotImplementedError()

    def values(self) -> Iterator[ValueT]:
        return (self._constructor(obj.resource_path.value) for obj in self._get_info_list())

    def items(self) -> Iterator[Tuple[str, ValueT]]:
        return (
            (obj.id, self._constructor(obj.resource_path.value)) for obj in self._get_info_list()
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


ParentT = TypeVar("ParentT", bound=TreeObject)


def define_collection(
    object_class: Type[ValueT], stub_wrapper_class: Type[StubWrapper]
) -> Tuple[Callable[[ParentT, str], ValueT], Callable[[ParentT], Collection[ValueT]]]:
    def create_method(self: ParentT, name: str, **kwargs: Any) -> ValueT:
        collection_path = CollectionPath(
            value=_rp_join(self._pb_object.info.resource_path.value, object_class.COLLECTION_LABEL)
        )
        stub = stub_wrapper_class(self._channel)
        # FIXME: harmonize on using the 'initialize + store' approach
        from .._tree_objects.rosette import Rosette

        if object_class is Rosette:
            obj = object_class(name, **kwargs)
            obj.store(parent=self)
            return obj
        reply = stub.create(collection_path=collection_path, name=name)
        return object_class.from_resource_path(
            resource_path=reply.info.resource_path.value, channel=self._channel
        )

    @property  # type: ignore
    def collection_property(self: ParentT) -> Collection[ValueT]:
        return Collection.from_types(
            channel=self._channel,
            parent_resource_path=self._pb_object.info.resource_path,
            object_class=object_class,
            stub_wrapper=stub_wrapper_class(channel=self._channel),
        )

    return create_method, collection_property
