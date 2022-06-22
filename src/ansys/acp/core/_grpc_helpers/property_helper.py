"""
Defines helpers for synchronizing object properties with the backend
via gRPC Put / Get calls.
"""
from __future__ import annotations

from functools import reduce
from typing import TYPE_CHECKING, Any, Callable

from ansys.api.acp.v0.base_pb2 import GetRequest

if TYPE_CHECKING:
    # Causes a circular import if imported at runtime
    from .._tree_objects.base import TreeObject

from .protocols import ObjectInfo

_TO_PROTOBUF_T = Callable[[Any], Any]
_FROM_PROTOBUF_T = Callable[[Any], Any]


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
