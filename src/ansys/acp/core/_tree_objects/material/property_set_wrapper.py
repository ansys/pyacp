from __future__ import annotations

from typing import Any, TypeVar

from .._grpc_helpers.property_helper import _exposed_grpc_property
from .._grpc_helpers.protocols import GrpcObject
from .property_set_base import (
    _ConstantPropertySet,
    _MonomorphicMixin,
    _PolymorphicMixin,
    _VariablePropertySet,
)

TC = TypeVar("TC", bound=_ConstantPropertySet)
TV = TypeVar("TV", bound=_VariablePropertySet)


def _property_set_getter(name: str, type_constant: type[TC], type_variable: type[TV]) -> Any:
    assert type_constant._PROPERTYSET_NAME == type_variable._PROPERTYSET_NAME
    assert issubclass(type_constant, _MonomorphicMixin) == issubclass(
        type_variable, _MonomorphicMixin
    )
    is_monomorphic = issubclass(type_constant, _MonomorphicMixin)
    propertyset_name = type_constant._PROPERTYSET_NAME

    def inner(self: GrpcObject) -> TC | TV | None:
        self._get_if_stored()
        if is_monomorphic:
            if not self._pb_object.properties.property_sets.HasField(propertyset_name):
                return None
            propset = getattr(self._pb_object.properties.property_sets, propertyset_name)
        else:
            field_name = self._pb_object.properties.property_sets.WhichOneof(propertyset_name)
            if field_name is None:
                return None
            propset = getattr(
                self._pb_object.properties.property_sets,
                field_name,
            )
        if (len(propset.values) > 1) or (len(propset.field_variables) > 0):
            return type_variable(_parent_object=self)
        if len(propset.values) == 0:
            return None
        return type_constant(_parent_object=self)

    return inner


def _property_set_setter(name: str, type_constant: type[TC], type_variable: type[TV]) -> Any:
    assert type_constant._PROPERTYSET_NAME == type_variable._PROPERTYSET_NAME
    assert issubclass(type_constant, _MonomorphicMixin) == issubclass(
        type_variable, _MonomorphicMixin
    )
    is_monomorphic = issubclass(type_constant, _MonomorphicMixin)
    propertyset_name = type_constant._PROPERTYSET_NAME

    def inner(self: GrpcObject, value: type[TC] | None) -> None:
        self._get_if_stored()
        if isinstance(getattr(self, name), _VariablePropertySet):
            raise AttributeError("Cannot replace variable property sets.")
        if is_monomorphic:
            self._pb_object.properties.property_sets.ClearField(propertyset_name)
        else:
            assert issubclass(type_constant, _PolymorphicMixin)
            for field_name in type_constant._FIELD_NAMES_BY_PB_DATATYPE.values():
                self._pb_object.properties.property_sets.ClearField(field_name)
        if value is not None:
            if is_monomorphic:
                pb_propset = getattr(self._pb_object.properties.property_sets, propertyset_name)
            else:
                assert issubclass(type_constant, _PolymorphicMixin)
                field_name = type_constant._FIELD_NAMES_BY_PB_DATATYPE[type(value._pb_object)]
                pb_propset = getattr(self._pb_object.properties.property_sets, field_name)
            pb_propset.CopyFrom(type(pb_propset)(values=[value._pb_object]))
        self._put_if_stored()

    return inner


def _property_set_deleter(name: str) -> Any:
    def inner(self: GrpcObject) -> None:
        setattr(self, name, None)

    return inner


def wrap_property_set(name: str, type_constant: type[TC], type_variable: type[TV]) -> Any:
    return (
        _exposed_grpc_property(
            _property_set_getter(
                name=name, type_constant=type_constant, type_variable=type_variable
            )
        )
        .setter(
            _property_set_setter(
                name=name, type_constant=type_constant, type_variable=type_variable
            )
        )
        .deleter(_property_set_deleter(name))
    )
