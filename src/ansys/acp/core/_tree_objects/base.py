"""Base classes for tree objects backed via gRPC API."""
from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterable
import typing
from typing import Any, Callable, Generic, TypeVar, cast

from grpc import Channel
from typing_extensions import Self

from ansys.api.acp.v0.base_pb2 import CollectionPath, DeleteRequest, GetRequest, ResourcePath

from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from .._utils.resource_paths import common_path
from .._utils.resource_paths import join as _rp_join
from .._utils.resource_paths import to_parts
from ._grpc_helpers.exceptions import wrap_grpc_errors
from ._grpc_helpers.linked_object_helpers import linked_path_fields, unlink_objects
from ._grpc_helpers.property_helper import (
    _get_data_attribute,
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._grpc_helpers.protocols import (
    CreatableEditableAndReadableResourceStub,
    CreateRequest,
    Editable,
    EditableAndReadableResourceStub,
    GrpcObjectBase,
    ObjectInfo,
    Readable,
    ReadableResourceStub,
)

_T = TypeVar("_T", bound="TreeObjectBase")


@mark_grpc_properties
class TreeObjectBase(GrpcObjectBase):
    """Base class for ACP tree objects."""

    __slots__: Iterable[str] = ("_channel_store", "_pb_object")

    _COLLECTION_LABEL: str
    OBJECT_INFO_TYPE: type[ObjectInfo]

    _pb_object: ObjectInfo
    name: ReadOnlyProperty[str]

    def __init__(self: TreeObjectBase, name: str = "") -> None:
        self._channel_store: Channel | None = None
        self._pb_object: ObjectInfo = self.OBJECT_INFO_TYPE()
        # We don't want to invoke gRPC requests for setting the name
        # during object construction, so we set the name directly on
        # the protobuf object.
        self._pb_object.info.name = name

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

    def __repr__(self) -> str:
        return f"<{type(self).__name__} with name '{self.name}'>"

    name = grpc_data_property_read_only("info.name", doc="The name of the object.")


StubT = TypeVar("StubT")


class StubStore(Generic[StubT]):
    """Stores a gRPC stub, and creates it on demand."""

    def __init__(self, create_stub_fun: Callable[[], StubT]) -> None:
        self._stub_store: StubT | None = None
        self._create_stub_fun = create_stub_fun

    def get(self, is_stored: bool) -> StubT:
        """Get the stored stub, or create it if it does not exist."""
        if not is_stored:
            raise RuntimeError("The server connection is uninitialized.")
        if self._stub_store is None:
            self._stub_store = self._create_stub_fun()
        return self._stub_store


class TreeObject(TreeObjectBase):
    """Base class for ACP objects which can be modified or deleted."""

    __slots__: Iterable[str] = ("_stub_store",)
    name: ReadWriteProperty[str, str] = grpc_data_property(
        "info.name", doc="The name of the object."
    )

    @abstractmethod
    def _create_stub(self) -> EditableAndReadableResourceStub:
        ...

    def __init__(self: TreeObject, name: str = "") -> None:
        super().__init__(name=name)
        self._stub_store = StubStore(self._create_stub)

    def delete(self) -> None:
        """Delete the object."""
        with wrap_grpc_errors():
            self._get_stub().Delete(
                DeleteRequest(
                    resource_path=self._pb_object.info.resource_path,
                    version=self._pb_object.info.version,
                )
            )

    def _get(self) -> None:
        with wrap_grpc_errors():
            self._pb_object = self._get_stub().Get(
                GetRequest(resource_path=self._pb_object.info.resource_path)
            )

    def _get_if_stored(self) -> None:
        if self._is_stored:
            self._get()

    def _put(self) -> None:
        with wrap_grpc_errors():
            self._pb_object = self._get_stub().Put(self._pb_object)

    def _put_if_stored(self) -> None:
        if self._is_stored:
            self._put()

    def _get_stub(self) -> EditableAndReadableResourceStub:
        return self._stub_store.get(self._is_stored)


@mark_grpc_properties
class ReadOnlyTreeObject(TreeObjectBase):
    """Base class for read-only ACP objects."""

    def __init__(self: ReadOnlyTreeObject) -> None:
        super().__init__()
        self._stub_store = StubStore(self._create_stub)

    @abstractmethod
    def _create_stub(self) -> ReadableResourceStub:
        ...

    def _get_stub(self) -> ReadableResourceStub:
        return self._stub_store.get(self._is_stored)

    def _get(self) -> None:
        with wrap_grpc_errors():
            self._pb_object = self._get_stub().Get(
                GetRequest(resource_path=self._pb_object.info.resource_path)
            )

    def _get_if_stored(self) -> None:
        if self._is_stored:
            self._get()


@mark_grpc_properties
class CreatableTreeObject(TreeObject):
    """Base class for ACP objects which can be created."""

    __slots__: Iterable[str] = tuple()
    CREATE_REQUEST_TYPE: type[CreateRequest]

    def _get_stub(self) -> CreatableEditableAndReadableResourceStub:
        return cast(CreatableEditableAndReadableResourceStub, super()._get_stub())

    def store(self: CreatableTreeObject, parent: TreeObject) -> None:
        """Store the object on the server.

        Parameters
        ----------
        parent :
            Parent object to store the object under.
        """
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
        with wrap_grpc_errors():
            self._pb_object = self._get_stub().Create(request)


@mark_grpc_properties
class IdTreeObject(TreeObjectBase):
    """Implements the 'id' attribute for tree objects."""

    __slots__: Iterable[str] = tuple()

    id: ReadOnlyProperty[str] = grpc_data_property_read_only(
        "info.id", doc="Identifier of the object, used for example as key in maps."
    )

    def __repr__(self) -> str:
        return f"<{type(self).__name__} with id '{self.id}'>"


class TreeObjectAttributeReadOnly(GrpcObjectBase):
    """Read-only object backed by a sub-component of a parent object's protobuf object."""

    __slots__: Iterable[str] = ("_parent_object", "_attribute_path")

    def __init__(
        self,
        *,
        _parent_object: Readable | None = None,
        _attribute_path: str | None = None,
    ):
        if _parent_object is None != _attribute_path is None:
            raise TypeError(
                "Either both '_parent_object' and '_attribute_path' need to be 'None', or neither."
            )
        self._parent_object: Readable | None = _parent_object
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
    """Mixin class for attributes which can have multiple types, through a 'oneof' definition."""

    @property
    def _pb_object_impl(self) -> Any:
        assert self._parent_object is not None
        assert self._attribute_path is not None
        *sub_path, prop_name = self._attribute_path.split(".")
        parent_attr = _get_data_attribute(self._parent_object._pb_object, ".".join(sub_path))
        return getattr(parent_attr, parent_attr.WhichOneof(prop_name))


class TreeObjectAttribute(TreeObjectAttributeReadOnly):
    """Editable object backed by a sub-component of a parent object's protobuf object."""

    __slots__: Iterable[str] = ("_parent_object", "_attribute_path", "_pb_object_store")

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


if typing.TYPE_CHECKING:
    # Ensure that the ReadOnlyTreeObject satisfies the Gettable interface
    _x: Readable = typing.cast(ReadOnlyTreeObject, None)
    # Ensure that the TreeObject satisfies the Editable interface
    _y: Editable = typing.cast(TreeObject, None)
