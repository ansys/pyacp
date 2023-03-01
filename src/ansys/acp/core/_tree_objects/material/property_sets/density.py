from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    _constant_material_grpc_data_property,
    _variable_material_grpc_data_property,
)

__all__ = ["ConstantDensity", "VariableDensity"]


class _DensityMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.DensityPropertySet


@mark_grpc_properties
class ConstantDensity(_DensityMixin, _ConstantPropertySet):
    GRPC_PROPERTIES = tuple()

    def __init__(
        self,
        *,
        rho: float = 0.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.rho = rho

    rho = _constant_material_grpc_data_property("rho")


@mark_grpc_properties
class VariableDensity(_DensityMixin, _VariablePropertySet):
    GRPC_PROPERTIES = tuple()

    rho = _variable_material_grpc_data_property("rho")
