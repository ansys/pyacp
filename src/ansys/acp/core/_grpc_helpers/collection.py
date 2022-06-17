from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Generic,
    Iterator,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
)

if TYPE_CHECKING:
    from mypy_extensions import KwArg, Arg

from grpc import Channel

from ansys.api.acp.v0.base_pb2 import CollectionPath, DeleteRequest, ListRequest

from .._tree_objects.base import CreatableTreeObject, TreeObject
from .._utils.resource_paths import join as _rp_join
from .protocols import ObjectInfo, ResourceStub

ValueT = TypeVar("ValueT", bound=CreatableTreeObject)

__all__ = ["Collection", "define_collection"]


class Collection(Generic[ValueT]):
    def __init__(
        self,
        *,
        channel: Channel,
        collection_path: CollectionPath,
        stub: ResourceStub,
        object_constructor: Callable[[ObjectInfo, Channel], ValueT],
    ) -> None:
        self._collection_path = collection_path
        self._stub = stub

        self._channel = channel
        self._object_constructor = object_constructor

    def __iter__(self) -> Iterator[str]:
        yield from (obj.info.id for obj in self._get_objectinfo_list())

    def __getitem__(self, key: str) -> ValueT:
        obj_info = self._get_objectinfo_by_id(key)
        return self._object_constructor(obj_info, self._channel)

    def _get_objectinfo_list(self) -> List[ObjectInfo]:
        res = self._stub.List(ListRequest(collection_path=self._collection_path)).objects
        if len(set(obj.info.id for obj in res)) != len(res):
            raise ValueError("Duplicate ID in Collection.")
        return res

    def _get_objectinfo_by_id(self, key: str) -> ObjectInfo:
        for obj in self._get_objectinfo_list():
            if obj.info.id == key:
                return obj
        raise KeyError(f"No object with ID '{key}' found.")

    # def __setitem__(self, key: str, value: ValueT) -> None:
    #     raise NotImplementedError()

    # def update(self, other=(), /, **kwds):
    #     raise NotImplementedError()

    # def setdefault(self, key, default=None):
    #     raise NotImplementedError()

    def __delitem__(self, key: str) -> None:
        obj_info = self._get_objectinfo_by_id(key)
        self._stub.Delete(
            DeleteRequest(resource_path=obj_info.info.resource_path, version=obj_info.info.version)
        )

    def clear(self) -> None:
        for obj_info in self._get_objectinfo_list():
            self._stub.Delete(
                DeleteRequest(
                    resource_path=obj_info.info.resource_path, version=obj_info.info.version
                )
            )

    # def pop(self, key):
    #     raise NotImplementedError()

    # def popitem(self, key):
    #     raise NotImplementedError()

    def values(self) -> Iterator[ValueT]:
        return (
            self._object_constructor(obj_info, self._channel)
            for obj_info in self._get_objectinfo_list()
        )

    def items(self) -> Iterator[Tuple[str, ValueT]]:
        return (
            (
                obj_info.info.id,
                self._object_constructor(obj_info, self._channel),
            )
            for obj_info in self._get_objectinfo_list()
        )

    def keys(self) -> Iterator[str]:
        return iter(self)

    def __contains__(self, key: str) -> bool:
        return key in list(self)

    def __len__(self) -> int:
        return len(self._get_objectinfo_list())

    def get(self, key: str, default: Optional[ValueT] = None) -> Optional[ValueT]:
        try:
            return self[key]
        except KeyError:
            return default


ParentT = TypeVar("ParentT", bound=TreeObject)


def define_collection(
    object_class: Type[ValueT], stub_class: Type[ResourceStub]
) -> Tuple[
    Callable[[Arg(ParentT, "self"), KwArg(Any)], ValueT],
    Callable[[Arg(ParentT, "self")], Collection[ValueT]],
]:
    def create_method(self: ParentT, **kwargs: Any) -> ValueT:
        obj = object_class(**kwargs)
        obj.store(parent=self)
        return obj

    create_method.__doc__ = object_class.__init__.__doc__ or object_class.__doc__
    create_method.__annotations__ = object_class.__init__.__annotations__

    @property  # type: ignore
    def collection_property(self: ParentT) -> Collection[ValueT]:
        return Collection(
            channel=self._channel,
            collection_path=CollectionPath(
                value=_rp_join(self._resource_path.value, object_class.COLLECTION_LABEL)
            ),
            object_constructor=object_class._from_object_info,
            stub=stub_class(channel=self._channel),
        )

    return create_method, collection_property
