from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    constant_material_grpc_data_property,
    variable_material_grpc_data_property,
)

__all__ = ["ConstantTsaiWuConstants", "VariableTsaiWuConstants"]


class _TsaiWuConstantsMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.TsaiWuConstantsPropertySet


@mark_grpc_properties
class ConstantTsaiWuConstants(_TsaiWuConstantsMixin, _ConstantPropertySet):
    """Constant Tsai-Wu constants material property set."""
    _GRPC_PROPERTIES = tuple()

    def __init__(
        self,
        *,
        XY: float = -1.0,
        XZ: float = -1.0,
        YZ: float = -1.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.XY = XY
        self.XZ = XZ
        self.YZ = YZ

    XY = constant_material_grpc_data_property("XY")
    XZ = constant_material_grpc_data_property("XZ")
    YZ = constant_material_grpc_data_property("YZ")


@mark_grpc_properties
class VariableTsaiWuConstants(_TsaiWuConstantsMixin, _VariablePropertySet):
    """Variable Tsai-Wu constants material property set."""
    _GRPC_PROPERTIES = tuple()

    XY = variable_material_grpc_data_property("XY")
    XZ = variable_material_grpc_data_property("XZ")
    YZ = variable_material_grpc_data_property("YZ")
