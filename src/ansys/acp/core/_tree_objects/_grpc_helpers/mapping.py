from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Callable, Generic, TypeVar

from grpc import Channel
from typing_extensions import Concatenate, ParamSpec, Self

from ansys.api.acp.v0.base_pb2 import CollectionPath, DeleteRequest, ListRequest

from ..._utils.property_protocols import ReadOnlyProperty
from ..._utils.resource_paths import join as _rp_join
from .._object_cache import ObjectCacheMixin, constructor_with_cache
from ..base import CreatableTreeObject, TreeObject, TreeObjectBase
from .exceptions import wrap_grpc_errors
from .property_helper import _exposed_grpc_property, _wrap_doc
from .protocols import EditableAndReadableResourceStub, ObjectInfo, ReadableResourceStub

ValueT = TypeVar("ValueT", bound=TreeObjectBase)
CreatableValueT = TypeVar("CreatableValueT", bound=CreatableTreeObject)

__all__ = ["Mapping", "MutableMapping", "define_mutable_mapping", "define_create_method"]


class Mapping(ObjectCacheMixin, Generic[ValueT]):
    """Mapping interface for collections of TreeObjects.

    Note: We could derive from collections.abc.Mapping to make sure
    this class conforms to the Mapping interface.
    """

    @classmethod
    @constructor_with_cache(
        key_getter=lambda *args, collection_path, **kwargs: collection_path.value,
        raise_on_invalid_key=True,
    )
    def _initialize_with_cache(
        cls,
        *,
        channel: Channel,
        collection_path: CollectionPath,
        stub: ReadableResourceStub,
        object_constructor: Callable[[ObjectInfo, Channel | None], ValueT],
    ) -> Self:
        return cls(
            _channel=channel,
            _collection_path=collection_path,
            _stub=stub,
            _object_constructor=object_constructor,
        )

    def __init__(
        self,
        *,
        _channel: Channel,
        _collection_path: CollectionPath,
        _stub: ReadableResourceStub,
        _object_constructor: Callable[[ObjectInfo, Channel | None], ValueT],
    ) -> None:
        self._collection_path = _collection_path
        self._stub = _stub

        self._channel = _channel
        self._object_constructor = _object_constructor

    @staticmethod
    def _cache_key_valid(key: Any) -> bool:
        if isinstance(key, str):
            return bool(key)
        return False

    def __iter__(self) -> Iterator[str]:
        yield from (obj.info.id for obj in self._get_objectinfo_list())

    def __getitem__(self, key: str) -> ValueT:
        obj_info = self._get_objectinfo_by_id(key)
        return self._object_constructor(obj_info, self._channel)

    def _get_objectinfo_list(self) -> list[ObjectInfo]:
        with wrap_grpc_errors():
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
        """Return an iterator over the values of the mapping."""
        return (
            self._object_constructor(obj_info, self._channel)
            for obj_info in self._get_objectinfo_list()
        )

    def items(self) -> Iterator[tuple[str, ValueT]]:
        """Return an iterator over the (key, value) pairs of the mapping."""
        return (
            (
                obj_info.info.id,
                self._object_constructor(obj_info, self._channel),
            )
            for obj_info in self._get_objectinfo_list()
        )

    def keys(self) -> Iterator[str]:
        """Return an iterator over the keys of the mapping."""
        return iter(self)

    def __contains__(self, key: str) -> bool:
        """Return True if the mapping contains the given key."""
        return key in list(self)

    def __len__(self) -> int:
        """Return the number of items in the mapping."""
        return len(self._get_objectinfo_list())

    def get(self, key: str, default: ValueT | None = None) -> ValueT | None:
        """Return the value for key if key is in the mapping, else default."""
        try:
            return self[key]
        except KeyError:
            return default

    def __repr__(self) -> str:
        try:
            from ..object_registry import object_registry

            collection_label = self._collection_path.value.rsplit("/", 1)[-1]
            value_type = object_registry[collection_label]
            return f"<{self.__class__.__name__}[{value_type.__name__}] with keys {list(self)}>"
        except:
            return super().__repr__()


class MutableMapping(Mapping[CreatableValueT]):
    """Mutable mapping interface for collections of TreeObjects."""

    @classmethod
    @constructor_with_cache(
        key_getter=lambda *args, collection_path, **kwargs: collection_path.value,
        raise_on_invalid_key=True,
    )
    def _initialize_with_cache(
        cls,
        *,
        channel: Channel,
        collection_path: CollectionPath,
        stub: EditableAndReadableResourceStub,  # type: ignore # violates Liskov substitution
        object_constructor: Callable[[ObjectInfo, Channel | None], CreatableValueT],
    ) -> Self:
        return cls(
            _channel=channel,
            _collection_path=collection_path,
            _stub=stub,
            _object_constructor=object_constructor,
        )

    def __init__(
        self,
        *,
        _channel: Channel,
        _collection_path: CollectionPath,
        _stub: EditableAndReadableResourceStub,
        _object_constructor: Callable[[ObjectInfo, Channel | None], CreatableValueT],
    ) -> None:
        self._collection_path = _collection_path
        self._stub: EditableAndReadableResourceStub = _stub
        self._channel = _channel
        self._object_constructor = _object_constructor

    def __delitem__(self, key: str) -> None:
        obj_info = self._get_objectinfo_by_id(key)
        with wrap_grpc_errors():
            self._stub.Delete(
                DeleteRequest(
                    resource_path=obj_info.info.resource_path, version=obj_info.info.version
                )
            )

    def clear(self) -> None:
        """Remove all items from the mapping."""
        for obj_info in self._get_objectinfo_list():
            with wrap_grpc_errors():
                self._stub.Delete(
                    DeleteRequest(
                        resource_path=obj_info.info.resource_path, version=obj_info.info.version
                    )
                )

    def pop(self, key: str) -> CreatableValueT:
        """Remove and return the value for key."""
        obj_info = self._get_objectinfo_by_id(key)
        return self._pop_from_info(obj_info)

    def popitem(self) -> CreatableValueT:
        """Remove and return an arbitrary (key, value) pair from the mapping."""
        obj_info = self._get_objectinfo_list()[0]
        return self._pop_from_info(obj_info)

    def _pop_from_info(self, object_info: ObjectInfo) -> CreatableValueT:
        obj = self._object_constructor(object_info, self._channel)
        new_obj = obj.clone()
        obj.delete()
        return new_obj


ParentT = TypeVar("ParentT", bound=TreeObject)


def get_read_only_collection_property(
    object_class: type[ValueT],
    stub_class: type[ReadableResourceStub],
    doc: str | None = None,
    requires_uptodate: bool = False,
) -> ReadOnlyProperty[Mapping[ValueT]]:
    """Define a read-only mapping of child tree objects."""

    def collection_property(self: ParentT) -> Mapping[ValueT]:
        if requires_uptodate and not self.status == "UPTODATE":
            raise RuntimeError(
                f"The object {self.id} must be up-to-date to access {object_class.__name__}."
            )
        return Mapping._initialize_with_cache(
            channel=self._channel,
            collection_path=CollectionPath(
                value=_rp_join(self._resource_path.value, object_class._COLLECTION_LABEL)
            ),
            object_constructor=object_class._from_object_info,
            stub=stub_class(channel=self._channel),
        )

    return _wrap_doc(_exposed_grpc_property(collection_property), doc=doc)


P = ParamSpec("P")


def define_create_method(
    object_class: Callable[P, CreatableValueT],
    func_name: str,
    parent_class_name: str,
    module_name: str,
) -> Callable[Concatenate[ParentT, P], CreatableValueT]:
    """Define a create method for child tree objects."""

    def inner(self: ParentT, /, *args: P.args, **kwargs: P.kwargs) -> CreatableValueT:
        obj = object_class(*args, **kwargs)
        obj.store(parent=self)
        return obj

    # NOTE: This relies on our convention to document the tree object classes
    # on the class itself, instead of the __init__ method.
    inner.__doc__ = object_class.__doc__

    inner.__name__ = func_name
    inner.__qualname__ = f"{parent_class_name}.{func_name}"
    inner.__module__ = module_name
    return inner


def define_mutable_mapping(
    object_class: type[CreatableValueT],
    stub_class: type[EditableAndReadableResourceStub],
    doc: str | None = None,
) -> ReadOnlyProperty[MutableMapping[CreatableValueT]]:
    """Define a mutable mapping of child tree objects."""

    def collection_property(self: ParentT) -> MutableMapping[CreatableValueT]:
        return MutableMapping._initialize_with_cache(
            channel=self._channel,
            collection_path=CollectionPath(
                value=_rp_join(self._resource_path.value, object_class._COLLECTION_LABEL)
            ),
            object_constructor=object_class._from_object_info,
            stub=stub_class(channel=self._channel),
        )

    return _wrap_doc(_exposed_grpc_property(collection_property), doc=doc)
