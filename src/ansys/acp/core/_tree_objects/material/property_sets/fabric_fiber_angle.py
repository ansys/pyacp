from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    _constant_material_grpc_data_property,
    _variable_material_grpc_data_property,
)

__all__ = ["ConstantFabricFiberAngle", "VariableFabricFiberAngle"]


class _FabricFiberAngleMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.FabricFiberAnglePropertySet


@mark_grpc_properties
class ConstantFabricFiberAngle(_FabricFiberAngleMixin, _ConstantPropertySet):
    GRPC_PROPERTIES = tuple()

    def __init__(
        self,
        *,
        fabric_fiber_angle: float = 0.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.fabric_fiber_angle = fabric_fiber_angle

    fabric_fiber_angle = _constant_material_grpc_data_property("fabric_fiber_angle")


@mark_grpc_properties
class VariableFabricFiberAngle(_FabricFiberAngleMixin, _VariablePropertySet):
    GRPC_PROPERTIES = tuple()

    fabric_fiber_angle = _variable_material_grpc_data_property("fabric_fiber_angle")
