"""
Defines helpers for synchronizing object properties with the backend
via gRPC Put / Get calls.
"""
from __future__ import annotations

from abc import abstractmethod
from typing import Any, Callable, Generic, Iterable, TypeVar, cast

from grpc import Channel
from typing_extensions import Self

from ansys.api.acp.v0.base_pb2 import CollectionPath, DeleteRequest, GetRequest, ResourcePath

from .._utils.resource_paths import common_path
from .._utils.resource_paths import join as _rp_join
from .._utils.resource_paths import to_parts
from ._grpc_helpers.linked_object_helpers import linked_path_fields, unlink_objects
from ._grpc_helpers.property_helper import (
    _get_data_attribute,
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._grpc_helpers.protocols import (
    CreatableResourceStub,
    CreateRequest,
    Editable,
    Gettable,
    GrpcObjectBase,
    ObjectInfo,
    ReadOnlyResourceStub,
    ResourceStub,
)

_T = TypeVar("_T", bound="TreeObjectBase")


class TreeObjectBase(GrpcObjectBase):
    """
    Base class for ACP tree objects.
    """

    __slots__ = ("_channel_store", "_pb_object")

    _COLLECTION_LABEL: str
    OBJECT_INFO_TYPE: type[ObjectInfo]

    _pb_object: ObjectInfo

    def __init__(self: TreeObjectBase, name: str = "") -> None:
        self._channel_store: Channel | None = None
        self._pb_object: ObjectInfo = self.OBJECT_INFO_TYPE()
        self.name = name

    def clone(self: _T, *, unlink: bool = False) -> _T:
        """Create a new unstored object with the same properties.

        Parameters
        ----------
        unlink:
            If `True`, remove all links to other objects. This can be
            used to store the object to another model, where the links
            would be invalid.
        """
        new_object_info = self.OBJECT_INFO_TYPE()
        new_object_info.properties.CopyFrom(self._pb_object.properties)
        if unlink:
            unlink_objects(new_object_info.properties)
        new_object_info.info.name = self._pb_object.info.name
        return type(self)._from_object_info(object_info=new_object_info)

    def __eq__(self: _T, other: Any) -> bool:
        if not isinstance(other, TreeObject):
            return False
        if not self._is_stored:
            # For unstored objects, fall back to identity comparison
            return self is other
        return self._resource_path.value == other._resource_path.value

    @classmethod
    def _from_object_info(
        cls: type[_T], object_info: ObjectInfo, channel: Channel | None = None
    ) -> _T:
        instance = cls()
        instance._pb_object = object_info
        instance._channel_store = channel
        return instance

    @classmethod
    def _from_resource_path(cls, resource_path: ResourcePath, channel: Channel) -> Self:
        instance = cls()
        instance._pb_object.info.resource_path.CopyFrom(resource_path)
        instance._channel_store = channel
        return instance

    @property
    def _resource_path(self) -> ResourcePath:
        return self._pb_object.info.resource_path

    @property
    def _channel(self) -> Channel:
        if not self._is_stored:
            raise RuntimeError("The server connection is uninitialized.")
        return self._channel_store

    @property
    def _is_stored(self) -> bool:
        return self._channel_store is not None


StubT = TypeVar("StubT")


class StubStore(Generic[StubT]):
    def __init__(self, create_stub_fun: Callable[[], StubT]) -> None:
        self._stub_store: StubT | None = None
        self._create_stub_fun = create_stub_fun

    def get(self, is_stored: bool) -> StubT:
        if not is_stored:
            raise RuntimeError("The server connection is uninitialized.")
        if self._stub_store is None:
            self._stub_store = self._create_stub_fun()
        return self._stub_store


@mark_grpc_properties
class NameTreeObject(GrpcObjectBase):
    """Implements the 'name' attribute for tree objects."""

    name = grpc_data_property("info.name")
    """The name of the object."""

    def __repr__(self) -> str:
        return f"<{type(self).__name__} with name '{self.name}'>"


class TreeObject(TreeObjectBase, NameTreeObject):
    @abstractmethod
    def _create_stub(self) -> ResourceStub:
        ...

    def __init__(self: TreeObject, name: str = "") -> None:
        super().__init__(name=name)
        self._stub_store = StubStore(self._create_stub)

    def delete(self) -> None:
        self._get_stub().Delete(
            DeleteRequest(
                resource_path=self._pb_object.info.resource_path,
                version=self._pb_object.info.version,
            )
        )

    def _get(self) -> None:
        self._pb_object = self._get_stub().Get(
            GetRequest(resource_path=self._pb_object.info.resource_path)
        )

    def _get_if_stored(self) -> None:
        if self._is_stored:
            self._get()

    def _put(self) -> None:
        self._pb_object = self._get_stub().Put(self._pb_object)

    def _put_if_stored(self) -> None:
        if self._is_stored:
            self._put()

    def _get_stub(self) -> ResourceStub:
        return self._stub_store.get(self._is_stored)


class ReadOnlyTreeObject(TreeObjectBase, NameTreeObject):
    def __init__(self: ReadOnlyTreeObject, name: str = "") -> None:
        super().__init__(name=name)
        self._stub_store = StubStore(self._create_stub)

    @abstractmethod
    def _create_stub(self) -> ReadOnlyResourceStub:
        ...

    def _get_stub(self) -> ReadOnlyResourceStub:
        return self._stub_store.get(self._is_stored)

    # Tbd: we could further reduce code duplication by
    # delegating the stub operations to a subobject.
    def _get(self) -> None:
        self._pb_object = self._get_stub().Get(
            GetRequest(resource_path=self._pb_object.info.resource_path)
        )

    def _get_if_stored(self) -> None:
        if self._is_stored:
            self._get()


@mark_grpc_properties
class CreatableTreeObject(TreeObject):
    __slots__: Iterable[str] = tuple()
    CREATE_REQUEST_TYPE: type[CreateRequest]

    def _get_stub(self) -> CreatableResourceStub:
        return cast(CreatableResourceStub, super()._get_stub())

    def store(self: CreatableTreeObject, parent: TreeObject) -> None:
        self._channel_store = parent._channel

        collection_path = CollectionPath(
            value=_rp_join(parent._resource_path.value, self._COLLECTION_LABEL)
        )

        # check that all linked objects are located in the same model
        path_values = [collection_path.value] + [
            path.value for _, _, path in linked_path_fields(self._pb_object.properties)
        ]
        # Since the path starts with 'model/<model_uuid>', the objects belong to
        # the same model iff they share at least the first two parts.
        if len(to_parts(common_path(*path_values))) < 2:
            parent_model_uid = to_parts(parent._resource_path.value)[1]
            wrong_model_paths = []
            for linked_path in path_values:
                if to_parts(linked_path)[1] != parent_model_uid:
                    wrong_model_paths.append(linked_path)
            raise ValueError(
                "The object to store contains links to the following objects, which "
                + "are located on another Model: [\n    "
                + ",\n    ".join(repr(path) for path in wrong_model_paths)
                + "\n]"
            )

        request = self.CREATE_REQUEST_TYPE(
            collection_path=collection_path,
            name=self._pb_object.info.name,
            properties=self._pb_object.properties,
        )
        self._pb_object = self._get_stub().Create(request)


class IdTreeObject(TreeObjectBase):
    """Implements the 'id' attribute for tree objects."""

    id = grpc_data_property_read_only("info.id")

    def __repr__(self) -> str:
        return f"<{type(self).__name__} with id '{self.id}'>"


class TreeObjectAttributeReadOnly:
    """
    Defines an attribute which is defined as a sub-component of a parent
    object's protobuf object (read-only).
    """

    __slots__ = ("_parent_object", "_attribute_path")

    def __init__(
        self,
        *,
        _parent_object: Gettable | None = None,
        _attribute_path: str | None = None,
    ):
        if _parent_object is None != _attribute_path is None:
            raise TypeError(
                "Either both '_parent_object' and '_attribute_path' need to be 'None', or neither."
            )
        self._parent_object: Gettable | None = _parent_object
        self._attribute_path = _attribute_path

    def _get(self) -> None:
        if self._parent_object is None:
            raise RuntimeError("The parent object is not set.")
        self._parent_object._get()

    def _get_if_stored(self) -> None:
        if self._is_stored:
            self._get()

    @property
    def _pb_object_impl(self) -> Any:
        assert self._parent_object is not None
        assert self._attribute_path is not None
        return _get_data_attribute(self._parent_object._pb_object, self._attribute_path)

    @property
    def _pb_object(self) -> Any:
        return self._pb_object_impl

    @property
    def _is_stored(self) -> bool:
        if self._parent_object is None:
            return False
        return self._parent_object._is_stored


class PolymorphicMixin(TreeObjectAttributeReadOnly):
    """
    Mixin class for attributes which can have multiple types, through a
    'oneof' definition.
    """

    @property
    def _pb_object_impl(self) -> Any:
        assert self._parent_object is not None
        assert self._attribute_path is not None
        *sub_path, prop_name = self._attribute_path.split(".")
        parent_attr = _get_data_attribute(self._parent_object._pb_object, ".".join(sub_path))
        return getattr(parent_attr, parent_attr.WhichOneof(prop_name))


class TreeObjectAttribute(TreeObjectAttributeReadOnly):
    """
    Defines an attribute which is defined as a sub-component of a parent
    object's protobuf object (read-write).
    """

    __slots__ = ("_parent_object", "_attribute_path", "_pb_object_store")

    @classmethod
    @abstractmethod
    def _create_default_pb_object(cls) -> Any:
        ...

    def __init__(
        self, *, _parent_object: Editable | None = None, _attribute_path: str | None = None
    ):
        if _parent_object is None:
            self._pb_object_store: Any = self._create_default_pb_object()
        else:
            self._pb_object_store = None
        self._parent_object: Editable | None
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)

    @property
    def _pb_object(self) -> Any:
        if self._parent_object is None:
            return self._pb_object_store
        else:
            return self._pb_object_impl

    def _put(self) -> None:
        if self._parent_object is None:
            raise RuntimeError("The parent object is not set.")
        self._parent_object._put()

    def _put_if_stored(self) -> None:
        if self._is_stored:
            self._put()

# Ensure that the ReadOnlyTreeObject satisfies the Gettable interface
# Tbd: Is there a better way?
def _gettable_protocol_is_satisfied(obj: ReadOnlyTreeObject) -> None:
    dummy: Gettable = obj

# Ensure that the TreeObject satisfies the Editable interface
# Tbd: Is there a better way?
def _editable_protocol_is_satisfied(obj: TreeObject) -> None:
    dummy: Editable = obj
