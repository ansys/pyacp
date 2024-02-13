from __future__ import annotations

from typing import Any, TypedDict

from google.protobuf.message import Message

from ..._grpc_helpers.property_helper import grpc_data_property_read_only, mark_grpc_properties
from ...base import PolymorphicMixin as _BasePolymorphicMixin
from ...base import TreeObjectAttribute, TreeObjectAttributeReadOnly
from .variable_property_set_attributes import FieldVariable, InterpolationOptions

__all__ = (
    "_ConstantPropertySet",
    "_PolymorphicMixin",
    "_VariablePropertySet",
    "_ISOTROPIC_PROPERTY_UNAVAILABLE_MSG",
    "_ORTHOTROPIC_PROPERTY_UNAVAILABLE_MSG",
    "_PolymorphicPropertyKwargs",
)


_ISOTROPIC_PROPERTY_UNAVAILABLE_MSG = (
    "This property is only available for isotropic material property sets. "
    "The property set is currently orthotropic"
)
_ORTHOTROPIC_PROPERTY_UNAVAILABLE_MSG = (
    "This property is only available for orthotropic material property sets. "
    "The property set is currently isotropic"
)


class _PolymorphicPropertyKwargs(TypedDict):
    """Type for the extra keyword arguments for properties on polymorphic material property sets."""

    available_on_pb_type: type[Message]
    unavailable_msg: str


class _ConstantPropertySet(TreeObjectAttribute):
    """Base class for constant property sets."""

    _DEFAULT_PB_PROPERTYSET_TYPE: Any

    @classmethod
    def _create_default_pb_object(cls) -> Any:
        return cls._create_pb_object_from_propertyset_type(cls._DEFAULT_PB_PROPERTYSET_TYPE)

    @staticmethod
    def _create_pb_object_from_propertyset_type(pb_type: Any) -> Any:
        return pb_type(values=[pb_type.Data()])


@mark_grpc_properties
class _VariablePropertySet(TreeObjectAttributeReadOnly):
    """Base class for variable property sets."""

    field_variables = grpc_data_property_read_only(
        "field_variables",
        from_protobuf=lambda field_vars: tuple(
            FieldVariable(
                name=val.name,
                values=tuple(float(v) for v in val.values),
                default=val.default,
                lower_limit=val.lower_limit,
                upper_limit=val.upper_limit,
            )
            for val in field_vars
        ),
    )

    interpolation_options = grpc_data_property_read_only(
        "interpolation_options",
        from_protobuf=lambda val: InterpolationOptions(
            algorithm=val.algorithm, cached=val.cached, normalized=val.normalized
        ),
    )


class _PolymorphicMixin(_BasePolymorphicMixin):
    """Mixin class for property sets which can have multiple protobuf types.

    The class attributes defined here are consumed in the wrapper that exposes
    the property set on the parent Material.
    """

    _FIELD_NAME_DEFAULT: str
    _FIELD_NAME_SUFFIX_BY_PB_DATATYPE: dict[type[Message], str]
