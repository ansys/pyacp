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

"""Base classes for tree objects backed via gRPC API."""
from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Iterable, Iterator
import contextlib
from dataclasses import dataclass
import typing
from typing import Any, Generic, TypeVar, cast

from grpc import Channel
from packaging.version import Version
from packaging.version import parse as parse_version
from typing_extensions import Self

from ansys.api.acp.v0.base_pb2 import CollectionPath, DeleteRequest, GetRequest, ResourcePath

from .._server.acp_instance import ACPInstance, FileTransferHandler
from .._utils.path_to_str import path_to_str_checked
from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from .._utils.resource_paths import common_path
from .._utils.resource_paths import join as _rp_join
from .._utils.resource_paths import to_parts
from .._utils.typing_helper import PATH
from ._grpc_helpers.exceptions import wrap_grpc_errors
from ._grpc_helpers.linked_object_helpers import get_linked_paths, unlink_objects
from ._grpc_helpers.polymorphic_from_pb import (
    CreatableFromResourcePath,
    tree_object_from_resource_path,
)
from ._grpc_helpers.property_helper import (
    _exposed_grpc_property,
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
from ._object_cache import ObjectCacheMixin, constructor_with_cache


@mark_grpc_properties
class TreeObjectBase(ObjectCacheMixin, GrpcObjectBase):
    """Base class for ACP tree objects."""

    __slots__: Iterable[str] = ("_server_wrapper_store", "_pb_object")

    _COLLECTION_LABEL: str
    _OBJECT_INFO_TYPE: type[ObjectInfo]
    _SUPPORTED_SINCE: str

    _pb_object: ObjectInfo
    name: ReadOnlyProperty[str]

    def __init__(self: TreeObjectBase, name: str = "") -> None:
        self._server_wrapper_store: ServerWrapper | None = None
        self._pb_object: ObjectInfo = self._OBJECT_INFO_TYPE()
        # We don't want to invoke gRPC requests for setting the name
        # during object construction, so we set the name directly on
        # the protobuf object.
        self._pb_object.info.name = name

    @staticmethod
    def _cache_key_valid(key: Any) -> bool:
        if not isinstance(key, str):
            return False
        return bool(key)

    def __eq__(self: Self, other: Any) -> bool:
        if not isinstance(other, TreeObject):
            return False
        if not self._is_stored:
            # For unstored objects, fall back to identity comparison
            return self is other
        return self._resource_path.value == other._resource_path.value

    def __hash__(self) -> int:
        return id(self)

    @classmethod
    @constructor_with_cache(
        key_getter=lambda object_info, *args, **kwargs: object_info.info.resource_path.value,
        raise_on_invalid_key=False,
    )
    def _from_object_info(
        cls: type[Self], /, object_info: ObjectInfo, server_wrapper: ServerWrapper | None = None
    ) -> Self:
        instance = cls()
        instance._pb_object = object_info
        instance._server_wrapper_store = server_wrapper
        return instance

    @classmethod
    @constructor_with_cache(
        key_getter=lambda resource_path, *args, **kwargs: resource_path.value,
        raise_on_invalid_key=True,
    )
    def _from_resource_path(
        cls, /, resource_path: ResourcePath, server_wrapper: ServerWrapper
    ) -> Self:
        instance = cls()
        instance._pb_object.info.resource_path.CopyFrom(resource_path)
        instance._server_wrapper_store = server_wrapper
        return instance

    @property
    def _resource_path(self) -> ResourcePath:
        return self._pb_object.info.resource_path

    @property
    def _channel(self) -> Channel:
        return self._server_wrapper.channel

    @property
    def _server_wrapper(self) -> ServerWrapper:
        if not self._is_stored:
            raise RuntimeError("The server connection is uninitialized.")
        assert self._server_wrapper_store is not None
        return self._server_wrapper_store

    @property
    def _server_version(self) -> Version | None:
        if not self._is_stored:
            return None
        return self._server_wrapper.version

    @property
    def _is_stored(self) -> bool:
        return self._server_wrapper_store is not None

    @property
    def parent(self) -> CreatableFromResourcePath:
        """The parent of the object."""
        if not self._is_stored:
            raise RuntimeError("Cannot get the parent of an unstored object.")
        rp_parts = to_parts(self._resource_path.value)
        if len(rp_parts) < 3:
            raise RuntimeError("The object does not have a parent.")

        parent_path = _rp_join(*rp_parts[:-2])
        parent = tree_object_from_resource_path(
            ResourcePath(value=parent_path), server_wrapper=self._server_wrapper
        )
        if parent is None:
            raise RuntimeError("The parent object could not be found.")
        return parent

    def __repr__(self) -> str:
        return f"<{type(self).__name__} with name '{self.name}'>"

    name = grpc_data_property_read_only("info.name", doc="The name of the object.")


StubT = TypeVar("StubT")


@dataclass(frozen=True)
class ServerWrapper:
    """Wrapper for the connection to an ACP instance.

    This class contains the representation of the ACP instance needed by tree objects.
    Its purpose is to minimize the dependency of tree objects on the ACP class.
    """

    channel: Channel
    version: Version
    filetransfer_handler: FileTransferHandler

    @classmethod
    def from_acp_instance(cls, acp_instance: ACPInstance[Any]) -> ServerWrapper:
        """Convert an ACP instance into the wrapper needed by tree objects."""
        return cls(
            channel=acp_instance._channel,
            version=parse_version(acp_instance.server_version),
            filetransfer_handler=acp_instance._filetransfer_handler,
        )

    def auto_upload(self, local_path: PATH | None, allow_none: bool = False) -> str:
        """Handle auto-transfer of a file to the server."""
        if local_path is None:
            if allow_none:
                return ""
            raise TypeError("Expected a Path or str, not 'None'.")
        return path_to_str_checked(
            self.filetransfer_handler.upload_file_if_autotransfer(local_path)
        )

    @contextlib.contextmanager
    def auto_download(self, local_path: PATH) -> Iterator[str]:
        """Handle auto-transfer of a file from the server."""
        export_path = self.filetransfer_handler.to_export_path(local_path)
        yield path_to_str_checked(export_path)
        self.filetransfer_handler.download_file_if_autotransfer(export_path, local_path)


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
    def _create_stub(self) -> EditableAndReadableResourceStub: ...

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
    def _create_stub(self) -> ReadableResourceStub: ...

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
    _CREATE_REQUEST_TYPE: type[CreateRequest]

    def _get_stub(self) -> CreatableEditableAndReadableResourceStub:
        return cast(CreatableEditableAndReadableResourceStub, super()._get_stub())

    def clone(self: Self, *, unlink: bool = False) -> Self:
        """Create a new unstored object with the same properties.

        Parameters
        ----------
        unlink:
            If ``True``, remove all links to other objects. This can be
            used to store the object to another model, where the links
            would be invalid.
        """
        new_object_info = self._OBJECT_INFO_TYPE()
        new_object_info.properties.CopyFrom(self._pb_object.properties)
        if unlink:
            unlink_objects(new_object_info.properties)
            # Since there may be links in the unknown fields, we need to
            # discard them to avoid errors when storing the object.
            new_object_info.properties.DiscardUnknownFields()  # type: ignore
        new_object_info.info.name = self._pb_object.info.name
        return type(self)._from_object_info(object_info=new_object_info)

    def store(self: Self, parent: TreeObject) -> None:
        """Store the object on the server.

        Parameters
        ----------
        parent :
            Parent object to store the object under.
        """
        self._server_wrapper_store = parent._server_wrapper
        assert self._server_version is not None
        if self._server_version < parse_version(self._SUPPORTED_SINCE):
            raise RuntimeError(
                f"The '{type(self).__name__}' object is only supported since version "
                f"{self._SUPPORTED_SINCE} of the ACP gRPC server. The current server version is "
                f"{self._server_version}."
            )

        collection_path = CollectionPath(
            value=_rp_join(parent._resource_path.value, self._COLLECTION_LABEL)
        )

        # check that all linked objects are located in the same model
        path_values = [collection_path.value] + [
            path.value for path in get_linked_paths(self._pb_object.properties)
        ]
        # filter out empty paths
        path_values = [path for path in path_values if path]

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

        request = self._CREATE_REQUEST_TYPE(
            collection_path=collection_path,
            name=self._pb_object.info.name,
            properties=self._pb_object.properties,
        )
        with wrap_grpc_errors():
            self._pb_object = self._get_stub().Create(request)
        resource_path_value = self._resource_path.value
        if not resource_path_value:
            raise ValueError("The resource path must not be empty.")
        self._OBJECT_CACHE[resource_path_value] = self


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

    @property
    def _server_wrapper(self) -> ServerWrapper:
        if self._parent_object is None:
            raise RuntimeError("The parent object is not set.")
        return self._parent_object._server_wrapper


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
    def _create_default_pb_object(cls) -> Any: ...

    def __init__(
        self,
        *,
        _parent_object: Editable | None = None,
        _attribute_path: str | None = None,
        _pb_object: Any | None = None,
    ):
        if (_pb_object is not None) and (_parent_object is not None):
            raise TypeError("The '_pb_object' parameter is not allowed if '_parent_object' is set.")
        if _parent_object is None:
            if _pb_object is None:
                self._pb_object_store: Any = self._create_default_pb_object()
            else:
                self._pb_object_store = _pb_object
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


class TreeObjectAttributeWithCache(ObjectCacheMixin, TreeObjectAttribute):
    """Tree object attribute with instance caching."""

    @classmethod
    @constructor_with_cache(
        key_getter=lambda parent_object, attribute_path: (
            parent_object,
            attribute_path,
        ),
        raise_on_invalid_key=True,
    )
    def _from_parent(cls: type[Self], /, parent_object: TreeObject, attribute_path: str) -> Self:
        return cls(_parent_object=parent_object, _attribute_path=attribute_path)

    @staticmethod
    def _cache_key_valid(key: tuple[Editable, str]) -> bool:
        parent_object, attribute_path = key
        return parent_object is not None and bool(attribute_path)


AttribT = TypeVar("AttribT", bound=TreeObjectAttributeWithCache)


def nested_grpc_object_property(
    pb_path: str,
    object_type: type[AttribT],
) -> ReadWriteProperty[AttribT, AttribT]:
    """Create a property for a nested object attribute.

    Creates a property for a nested object which is backed by the parent
    object's protobuf object. The property is read-write, and instances
    are cached.
    """

    def _getter(self: TreeObject) -> AttribT:
        return object_type._from_parent(parent_object=self, attribute_path=pb_path)

    def _setter(self: TreeObject, value: AttribT) -> None:
        if not isinstance(value, object_type):
            raise TypeError(
                f"Expected an object of type '{object_type.__name__}', got '{type(value).__name__}'."
            )
        _getter(self)._pb_object.CopyFrom(value._pb_object)
        self._put_if_stored()

    return _exposed_grpc_property(_getter).setter(_setter)


if typing.TYPE_CHECKING:  # pragma: no cover
    # Ensure that the ReadOnlyTreeObject satisfies the Gettable interface
    _x: Readable = typing.cast(ReadOnlyTreeObject, None)
    # Ensure that the TreeObject satisfies the Editable and Readable interfaces
    _y: Editable = typing.cast(TreeObject, None)
    _z: Readable = typing.cast(TreeObject, None)

    # Ensure the TreeObjectBase satisfies the CreatableFromResourcePath interface
    _a: CreatableFromResourcePath = typing.cast(TreeObjectBase, None)
