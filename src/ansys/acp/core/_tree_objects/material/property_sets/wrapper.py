"""
Implements a helper function ``wrap_property_set`` to expose property sets on the
Material, as a property.
"""

from __future__ import annotations

from typing import Any, TypeVar

from ..._grpc_helpers.property_helper import _exposed_grpc_property
from ..._grpc_helpers.protocols import Editable
from .base import _ConstantPropertySet, _PolymorphicMixin, _VariablePropertySet

TC = TypeVar("TC", bound=_ConstantPropertySet)
TV = TypeVar("TV", bound=_VariablePropertySet)


__all__ = ["wrap_property_set"]


def _property_set_getter(name: str, type_constant: type[TC], type_variable: type[TV]) -> Any:
    assert issubclass(type_constant, _PolymorphicMixin) == issubclass(
        type_variable, _PolymorphicMixin
    )
    is_monomorphic = not issubclass(type_constant, _PolymorphicMixin)

    def inner(self: Editable) -> TC | TV | None:
        self._get_if_stored()
        if is_monomorphic:
            if not self._pb_object.properties.property_sets.HasField(name):
                return None
            propset = getattr(self._pb_object.properties.property_sets, name)
        else:
            field_name = self._pb_object.properties.property_sets.WhichOneof(name)
            if field_name is None:
                return None
            propset = getattr(
                self._pb_object.properties.property_sets,
                field_name,
            )
        if (len(propset.values) > 1) or (len(propset.field_variables) > 0):
            return type_variable(
                _parent_object=self, _attribute_path=f"properties.property_sets.{name}"
            )
        if len(propset.values) == 0:
            return None
        return type_constant(
            _parent_object=self, _attribute_path=f"properties.property_sets.{name}"
        )

    return inner


def _property_set_setter(name: str, type_constant: type[TC], type_variable: type[TV]) -> Any:
    assert issubclass(type_constant, _PolymorphicMixin) == issubclass(
        type_variable, _PolymorphicMixin
    )
    is_monomorphic = not issubclass(type_constant, _PolymorphicMixin)

    def inner(self: Editable, value: type[TC] | None) -> None:
        self._get_if_stored()
        if isinstance(getattr(self, name), _VariablePropertySet):
            raise AttributeError("Cannot replace variable property sets.")
        if is_monomorphic:
            self._pb_object.properties.property_sets.ClearField(name)
        else:
            assert issubclass(type_constant, _PolymorphicMixin)
            for name_suffix in type_constant._FIELD_NAME_SUFFIX_BY_PB_DATATYPE.values():
                self._pb_object.properties.property_sets.ClearField(name + name_suffix)
        if value is not None:
            if is_monomorphic:
                pb_propset = getattr(self._pb_object.properties.property_sets, name)
            else:
                assert issubclass(type_constant, _PolymorphicMixin)
                name_suffix = type_constant._FIELD_NAME_SUFFIX_BY_PB_DATATYPE[
                    type(value._pb_object)
                ]
                pb_propset = getattr(self._pb_object.properties.property_sets, name + name_suffix)
            pb_propset.CopyFrom(value._pb_object)
        self._put_if_stored()

    return inner


def _property_set_deleter(name: str) -> Any:
    def inner(self: Any) -> None:
        setattr(self, name, None)

    return inner


def wrap_property_set(name: str, type_constant: type[TC], type_variable: type[TV]) -> Any:
    """Helper function to define a material property set on the material.

    Expose a property set on the ``Material``, as a property. The property
    automatically chooses the appropriate type (``type_constant`` or ``type_variable``),
    depending on whether the property set is constant (has exactly one value, and
    no field variables), or variable.

    For polymorphic property sets (which are defined as a protobuf 'oneof'), the
    wrapper takes care of storing / constructing the object with the currently
    active field.

    Parameters
    ----------
    name :
        Field name on which the property set is defined. If the property set is
        polymorphic (defined as a protobuf 'oneof'), this is the name of the
        'oneof' itself, not of the contained fields.
    type_constant :
        Type of the property set when the property set is constant (independent
        of field variables).
    type_variable :
        Type of the property set when the property set depends on field variables.
    """
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
