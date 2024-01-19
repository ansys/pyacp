from __future__ import annotations

from collections.abc import Iterator
import textwrap
from typing import TYPE_CHECKING, Callable, Generic, TypeVar

if TYPE_CHECKING:
    from mypy_extensions import Arg

from grpc import Channel

from ansys.api.acp.v0.base_pb2 import CollectionPath, DeleteRequest, ListRequest

from ..._utils.resource_paths import join as _rp_join
from ..base import CreatableTreeObject, TreeObject
from .protocols import EditableAndReadableResourceStub, ObjectInfo, ReadableResourceStub

ValueT = TypeVar("ValueT", bound=CreatableTreeObject)

__all__ = ["Mapping", "MutableMapping", "define_mutable_mapping"]


class Mapping(Generic[ValueT]):
    """
    Note: We could derive from collections.abc.Mapping to make sure
    this class conforms to the Mapping interface.
    """

    def __init__(
        self,
        *,
        channel: Channel,
        collection_path: CollectionPath,
        stub: ReadableResourceStub,
        object_constructor: Callable[[ObjectInfo, Channel | None], ValueT],
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

    def _get_objectinfo_list(self) -> list[ObjectInfo]:
        res = self._stub.List(ListRequest(collection_path=self._collection_path)).objects
        if len({obj.info.id for obj in res}) != len(res):
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

    def values(self) -> Iterator[ValueT]:
        return (
            self._object_constructor(obj_info, self._channel)
            for obj_info in self._get_objectinfo_list()
        )

    def items(self) -> Iterator[tuple[str, ValueT]]:
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

    def get(self, key: str, default: ValueT | None = None) -> ValueT | None:
        try:
            return self[key]
        except KeyError:
            return default


class MutableMapping(Mapping[ValueT]):
    def __init__(
        self,
        *,
        channel: Channel,
        collection_path: CollectionPath,
        stub: EditableAndReadableResourceStub,
        object_constructor: Callable[[ObjectInfo, Channel | None], ValueT],
    ) -> None:
        self._collection_path = collection_path
        self._stub: EditableAndReadableResourceStub = stub

        self._channel = channel
        self._object_constructor = object_constructor

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

    def pop(self, key: str) -> ValueT:
        obj_info = self._get_objectinfo_by_id(key)
        return self._pop_from_info(obj_info)

    def popitem(self) -> ValueT:
        obj_info = self._get_objectinfo_list()[0]
        return self._pop_from_info(obj_info)

    def _pop_from_info(self, object_info: ObjectInfo) -> ValueT:
        obj = self._object_constructor(object_info, self._channel)
        new_obj = obj.clone()
        obj.delete()
        return new_obj


ParentT = TypeVar("ParentT", bound=TreeObject)


def get_read_only_collection_property(
    object_class: type[ValueT], stub_class: type[ReadableResourceStub]
) -> Callable[[ParentT], Mapping[ValueT]]:
    def collection_property(self: ParentT) -> Mapping[ValueT]:
        return Mapping(
            channel=self._channel,
            collection_path=CollectionPath(
                value=_rp_join(self._resource_path.value, object_class._COLLECTION_LABEL)
            ),
            object_constructor=object_class._from_object_info,
            stub=stub_class(channel=self._channel),
        )

    return collection_property


def define_mutable_mapping(
    object_class: type[ValueT], stub_class: type[EditableAndReadableResourceStub]
) -> tuple[Callable[[Arg(ParentT, "self"), Arg(ValueT)], None], property]:
    def add_method(self: ParentT, tree_object: ValueT) -> None:
        if not isinstance(tree_object, object_class):
            raise TypeError(f"Expected {object_class.__name__}, got {type(tree_object).__name__}.")
        tree_object._store(parent=self)

    # docstrings need to be regular strings, not f-strings. Hence, we need
    # to define the __doc__ separately here.
    add_method.__doc__ = textwrap.dedent(
        f"""\
        Add a {object_class.__name__} to the collection.

        Parameters
        ----------
        tree_object :
            The {object_class.__name__} to add.
        """
    )
    add_method.__annotations__["tree_object"] = object_class

    def collection_property(self: ParentT) -> MutableMapping[ValueT]:
        return MutableMapping(
            channel=self._channel,
            collection_path=CollectionPath(
                value=_rp_join(self._resource_path.value, object_class._COLLECTION_LABEL)
            ),
            object_constructor=object_class._from_object_info,
            stub=stub_class(channel=self._channel),
        )

    return add_method, property(collection_property)
