from __future__ import annotations

from typing import Any, overload

from ..._grpc_helpers.property_helper import (
    _PROTOBUF_T,
    _exposed_grpc_property,
    grpc_data_property_read_only,
)

__all__ = ["variable_material_grpc_data_property", "constant_material_grpc_data_property"]

from ..._grpc_helpers.protocols import Editable, Readable


@overload
def variable_material_grpc_data_property(
    name: str, available_on_pb_type: None = None, unavailable_msg: None = None
) -> Any:
    ...


@overload
def variable_material_grpc_data_property(
    name: str,
    available_on_pb_type: type[_PROTOBUF_T],
    unavailable_msg: str,
) -> Any:
    ...


def variable_material_grpc_data_property(
    name: str,
    available_on_pb_type: type[_PROTOBUF_T] | None = None,
    unavailable_msg: str | None = None,
) -> Any:
    """Define a gRPC-backed property for a variable material property set."""

    def _from_protobuf(values: Any) -> tuple[Any]:
        if available_on_pb_type is not None:
            if not all(isinstance(val, available_on_pb_type.Data) for val in values):
                raise AttributeError(f"{name}: {unavailable_msg}")
        return tuple(getattr(val, name) for val in values)

    return grpc_data_property_read_only("values", from_protobuf=_from_protobuf)


def _constant_material_grpc_data_getter(
    name: str, available_on_pb_type: type[_PROTOBUF_T] | None, unavailable_msg: str | None
) -> Any:
    """Create a getter method which obtains the server object via the gRPC Get endpoint."""

    def inner(self: Readable) -> Any:
        self._get_if_stored()
        if available_on_pb_type is not None and not isinstance(
            self._pb_object, available_on_pb_type
        ):
            raise AttributeError(unavailable_msg)
        data_vals = self._pb_object.values
        if len(data_vals) != 1:
            raise RuntimeError(
                "The number of values is inconsistent with a constant material property."
            )
        return getattr(data_vals[0], name)

    return inner


def _constant_material_grpc_data_setter(
    name: str, available_on_pb_type: type[_PROTOBUF_T] | None, unavailable_msg: str | None
) -> Any:
    """Create a setter method which updates the server object via the gRPC Put endpoint."""

    def inner(self: Editable, value: Any) -> None:
        self._get_if_stored()
        if available_on_pb_type is not None and not isinstance(
            self._pb_object, available_on_pb_type
        ):
            raise AttributeError(f"{self.__class__.__name__}.{name}: {unavailable_msg}")
        data_vals = self._pb_object.values
        if len(data_vals) != 1:
            raise RuntimeError(
                "The number of values is inconsistent with a constant material property."
            )
        current_value = getattr(data_vals[0], name)
        try:
            needs_updating = current_value != value
        except TypeError:
            needs_updating = True
        if needs_updating:
            setattr(data_vals[0], name, value)
            self._put_if_stored()

    return inner


@overload
def constant_material_grpc_data_property(
    name: str, available_on_pb_type: None = None, unavailable_msg: None = None
) -> Any:
    ...


@overload
def constant_material_grpc_data_property(
    name: str,
    available_on_pb_type: type[_PROTOBUF_T],
    unavailable_msg: str,
) -> Any:
    ...


def constant_material_grpc_data_property(
    name: str,
    available_on_pb_type: type[_PROTOBUF_T] | None = None,
    unavailable_msg: str | None = None,
) -> Any:
    """Define a gRPC-backed property for a constant material property set."""
    return _exposed_grpc_property(
        _constant_material_grpc_data_getter(
            name=name, available_on_pb_type=available_on_pb_type, unavailable_msg=unavailable_msg
        )
    ).setter(
        _constant_material_grpc_data_setter(
            name=name, available_on_pb_type=available_on_pb_type, unavailable_msg=unavailable_msg
        )
    )
