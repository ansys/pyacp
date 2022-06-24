"""
Defines helpers for synchronizing object properties with the backend
via gRPC Put / Get calls.
"""
from __future__ import annotations

from functools import reduce
from typing import TYPE_CHECKING, Any, Callable

from ansys.api.acp.v0.base_pb2 import GetRequest, ResourcePath

if TYPE_CHECKING:
    # Causes a circular import if imported at runtime
    from .._tree_objects.base import TreeObject

from .protocols import ObjectInfo

_TO_PROTOBUF_T = Callable[[Any], Any]
_FROM_PROTOBUF_T = Callable[[Any], Any]


def grpc_linked_object_getter(name: str) -> Callable[[TreeObject], Any]:
    """
    Creates a getter method which obtains the linked server object
    """

    def inner(self: TreeObject) -> Any:
        #  Import here to avoid circular references. Cannot use the registry before
        #  all the object have been imported.
        from .._tree_objects.object_registry import object_registry

        if not self._is_stored:
            raise Exception("Cannot get linked object from unstored object")
        self._pb_object = self._get_stub().Get(
            GetRequest(resource_path=self._pb_object.info.resource_path)
        )
        object_resource_path = _get_data_attribute(self._pb_object, name)

        # Resource path represents an object that is not set as an empty string
        # For instance fabric.material = None
        if object_resource_path.value == "":
            return None
        resource_type = object_resource_path.value.split("/")[::2][-1]
        resource_class = object_registry[resource_type]

        return resource_class._from_resource_path(object_resource_path, self._channel)

    return inner


def grpc_data_getter(name: str, from_protobuf: _FROM_PROTOBUF_T) -> Callable[[TreeObject], Any]:
    """
    Creates a getter method which obtains the server object via the gRPC
    Get endpoint.
    """

    def inner(self: TreeObject) -> Any:
        if self._is_stored:
            self._pb_object = self._get_stub().Get(
                GetRequest(resource_path=self._pb_object.info.resource_path)
            )
        return from_protobuf(_get_data_attribute(self._pb_object, name))

    return inner


def grpc_data_setter(name: str, to_protobuf: _TO_PROTOBUF_T) -> Callable[[TreeObject, Any], None]:
    """
    Creates a setter method which updates the server object via the gRPC
    Put endpoint.
    """

    def inner(self: TreeObject, value: Any) -> None:
        if self._is_stored:
            self._pb_object = self._get_stub().Get(
                GetRequest(resource_path=self._pb_object.info.resource_path)
            )
        current_value = _get_data_attribute(self._pb_object, name)
        value_pb = to_protobuf(value)
        try:
            needs_updating = current_value != value_pb
        except TypeError:
            needs_updating = True
        if needs_updating:
            _set_data_attribute(self._pb_object, name, value_pb)
            if self._is_stored:
                self._pb_object = self._get_stub().Put(self._pb_object)

    return inner


def _get_data_attribute(pb_obj: ObjectInfo, name: str) -> Any:
    name_parts = name.split(".")
    return reduce(getattr, name_parts, pb_obj)


def _set_data_attribute(pb_obj: ObjectInfo, name: str, value: Any) -> None:
    name_parts = name.split(".")

    try:
        parent = reduce(getattr, name_parts[:-1], pb_obj)
        setattr(parent, name_parts[-1], value)
    except AttributeError:
        target_object: Any = reduce(getattr, name_parts, pb_obj)
        if hasattr(target_object, "CopyFrom"):
            target_object.CopyFrom(value)
        else:
            try:
                target_object[:] = value
            except TypeError:
                del target_object[:]
                for item in value:
                    target_object.add().CopyFrom(item)


def grpc_data_property(
    name: str,
    to_protobuf: _TO_PROTOBUF_T = lambda x: x,
    from_protobuf: _FROM_PROTOBUF_T = lambda x: x,
) -> Any:
    """
    Helper for defining properties accessed via gRPC. The property getter
    and setter make calls to the gRPC Get and Put endpoints to synchronize
    the local object with the remote backend.
    """
    return property(grpc_data_getter(name, from_protobuf=from_protobuf)).setter(
        grpc_data_setter(name, to_protobuf=to_protobuf)
    )


def grpc_data_property_read_only(name: str, from_protobuf: _FROM_PROTOBUF_T = lambda x: x) -> Any:
    """
    Helper for defining properties accessed via gRPC. The property getter
    makes call to the gRPC Get endpoints to synchronize
    the local object with the remote backend.
    """
    return property(grpc_data_getter(name, from_protobuf=from_protobuf))


def grpc_link_property(name: str) -> Any:
    """
    Helper for defining linked properties accessed via gRPC. The property getter
    makes call to the gRPC Get endpoints to get the linked object
    """
    return property(grpc_linked_object_getter(name)).setter(
        # Resource path represents an object that is not set as an empty string
        grpc_data_setter(
            name=name,
            to_protobuf=lambda obj: ResourcePath(value="") if obj is None else obj._resource_path,
        )
    )


def grpc_link_property_read_only(name: str) -> Any:
    """
    Helper for defining linked properties accessed via gRPC. The property getter
    makes call to the gRPC Get endpoints to get the linked object
    """
    return property(grpc_linked_object_getter(name))
