from __future__ import annotations

from abc import abstractproperty
from typing import Any

from google.protobuf.message import Message

from .._grpc_helpers.property_helper import grpc_data_property_read_only, mark_grpc_properties
from ..base import TreeObjectAttribute, TreeObjectAttributeReadOnly
from .variable_property_set_attributes import FieldVariable, InterpolationOptions

__all__ = ("_ConstantPropertySet", "_MonomorphicMixin", "_PolymorphicMixin", "_VariablePropertySet")


class _ConstantPropertySet(TreeObjectAttribute):
    @abstractproperty
    def _pb_propset_impl(
        self,
    ) -> Any:
        ...

    @property
    def _pb_object_impl(self) -> Any:
        try:
            return self._pb_propset_impl.values[0]
        except IndexError:
            raise RuntimeError("The property set has either been deleted or changed type.")


@mark_grpc_properties
class _VariablePropertySet(TreeObjectAttributeReadOnly):
    _PROPERTYSET_NAME: str

    @abstractproperty
    def _pb_propset_impl(
        self,
    ) -> Message:
        ...

    @property
    def _pb_object_impl(self) -> Message:
        return self._pb_propset_impl

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


class _MonomorphicMixin(TreeObjectAttributeReadOnly):
    _PROPERTYSET_NAME: str

    @property
    def _pb_propset_impl(self) -> Any:
        assert self._parent_object is not None
        return getattr(
            self._parent_object._pb_object.properties.property_sets, self._PROPERTYSET_NAME
        )


class _PolymorphicMixin(TreeObjectAttributeReadOnly):
    _PROPERTYSET_NAME: str
    _FIELD_NAME_DEFAULT: str

    @property
    def _pb_propset_impl(
        self,
    ) -> Message:
        assert self._parent_object is not None
        field_name = (
            self._parent_object._pb_object.properties.property_sets.WhichOneof(
                self._PROPERTYSET_NAME
            )
            or self._FIELD_NAME_DEFAULT
        )
        return getattr(self._parent_object._pb_object.properties.property_sets, field_name)  # type: ignore
