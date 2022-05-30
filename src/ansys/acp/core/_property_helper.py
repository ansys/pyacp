"""
Defines helpers for synchronizing object properties with the backend
via gRPC Put / Get calls.
"""
from __future__ import annotations

from typing import Any, Callable

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore

from google.protobuf.message import Message


class ResourceStub(Protocol):
    """Interface definition for ACP Resource service stubs."""

    def Get(self, request: Message) -> Message:
        ...

    def Put(self, request: Message) -> Message:
        ...


class ResourceProtocol(Protocol):
    """
    Interface definition for objects which can make use of the grpc
    property helpers.
    """

    def _set_data_attribute(self, key: str, value: Any) -> None:
        ...

    def _get_data_attribute(self, key: str) -> Any:
        ...

    def _get(self) -> None:
        ...

    def _put(self) -> None:
        ...


def grpc_data_getter(name: str) -> Callable[[ResourceProtocol], Any]:
    """
    Creates a getter method which obtains the server object via the gRPC
    Get endpoint.
    """

    def inner(self: ResourceProtocol) -> Any:
        self._get()
        return self._get_data_attribute(name)

    return inner


def grpc_data_setter(name: str) -> Callable[[ResourceProtocol, Any], None]:
    """
    Creates a setter method which updates the server object via the gRPC
    Put endpoint.
    """

    def inner(self: ResourceProtocol, value: Any) -> None:
        self._get()
        current_value = self._get_data_attribute(name)
        if current_value != value:
            self._set_data_attribute(name, value)
            self._put()

    return inner


def grpc_data_property(name: str) -> Any:
    """
    Helper for defining properties accessed via gRPC. The property getter
    and setter make calls to the gRPC Get and Put endpoints to synchronize
    the local object with the remote backend.
    """
    return property(grpc_data_getter(name)).setter(grpc_data_setter(name))
