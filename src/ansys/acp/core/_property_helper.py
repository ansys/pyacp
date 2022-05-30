from __future__ import annotations

from typing import Any
from typing import Callable

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore

from google.protobuf.message import Message


class ResourceStub(Protocol):
    def Get(self, request: Message) -> Message:
        ...

    def Put(self, request: Message) -> Message:
        ...


class ResourceProtocol(Protocol):
    def _set_data_attribute(self, key: str, value: Any) -> None:
        ...

    def _get_data_attribute(self, key: str) -> Any:
        ...

    def _get(self) -> None:
        ...

    def _put(self) -> None:
        ...


def grpc_data_getter(name: str) -> Callable[[ResourceProtocol], Any]:
    def inner(self: ResourceProtocol) -> Any:
        self._get()
        return self._get_data_attribute(name)

    return inner


def grpc_data_setter(name: str) -> Callable[[ResourceProtocol, Any], None]:
    def inner(self: ResourceProtocol, value: Any) -> None:
        self._get()
        current_value = self._get_data_attribute(name)
        if current_value != value:
            self._set_data_attribute(name, value)
            self._put()

    return inner


def grpc_data_property(name: str) -> Any:
    return property(grpc_data_getter(name)).setter(grpc_data_setter(name))
