from __future__ import annotations

from typing import Any

from google.protobuf.message import Message

from ..._grpc_helpers.property_helper import grpc_data_property_read_only, mark_grpc_properties
from ...base import PolymorphicMixin as _BasePolymorphicMixin
from ...base import TreeObjectAttribute, TreeObjectAttributeReadOnly
from ..variable_property_set_attributes import FieldVariable, InterpolationOptions

__all__ = ("_ConstantPropertySet", "_PolymorphicMixin", "_VariablePropertySet")


class _ConstantPropertySet(TreeObjectAttribute):
    _DEFAULT_PB_PROPERTYSET_TYPE: Any

    @classmethod
    def _create_default_pb_object(cls) -> Any:
        return cls._DEFAULT_PB_PROPERTYSET_TYPE(values=[cls._DEFAULT_PB_PROPERTYSET_TYPE.Data()])


@mark_grpc_properties
class _VariablePropertySet(TreeObjectAttributeReadOnly):
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
    _FIELD_NAME_DEFAULT: str
    _FIELD_NAME_SUFFIX_BY_PB_DATATYPE: dict[type[Message], str]
