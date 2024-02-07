from typing import Any

from ..._grpc_helpers.property_helper import _exposed_grpc_property, grpc_data_property_read_only

__all__ = ["variable_material_grpc_data_property", "constant_material_grpc_data_property"]

from ..._grpc_helpers.protocols import Editable, Readable


def variable_material_grpc_data_property(name: str) -> Any:
    """Define a gRPC-backed property for a variable material property set."""
    return grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(getattr(val, name) for val in values)
    )


def _constant_material_grpc_data_getter(name: str) -> Any:
    """Create a getter method which obtains the server object via the gRPC Get endpoint."""

    def inner(self: Readable) -> Any:
        self._get_if_stored()
        data_vals = self._pb_object.values
        if len(data_vals) != 1:
            raise RuntimeError(
                "The number of values is inconsistent with a constant material property."
            )
        return getattr(data_vals[0], name)

    return inner


def _constant_material_grpc_data_setter(name: str) -> Any:
    """Create a setter method which updates the server object via the gRPC Put endpoint."""

    def inner(self: Editable, value: Any) -> None:
        self._get_if_stored()
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


def constant_material_grpc_data_property(name: str) -> Any:
    """Define a gRPC-backed property for a constant material property set."""
    return _exposed_grpc_property(_constant_material_grpc_data_getter(name=name)).setter(
        _constant_material_grpc_data_setter(name=name)
    )
