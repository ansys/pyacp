from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    _constant_material_grpc_data_property,
    _variable_material_grpc_data_property,
)

__all__ = ["ConstantTsaiWuConstants", "VariableTsaiWuConstants"]


class _TsaiWuConstantsMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.TsaiWuConstantsPropertySet
    # _PROPERTYSET_NAME = "tsai_wu_constants"


@mark_grpc_properties
class ConstantTsaiWuConstants(_TsaiWuConstantsMixin, _ConstantPropertySet):
    GRPC_PROPERTIES = tuple()

    def __init__(
        self,
        *,
        XY: float = 0.0,
        XZ: float = 0.0,
        YZ: float = 0.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.XY = XY
        self.XZ = XZ
        self.YZ = YZ

    XY = _constant_material_grpc_data_property("XY")
    XZ = _constant_material_grpc_data_property("XZ")
    YZ = _constant_material_grpc_data_property("YZ")


@mark_grpc_properties
class VariableTsaiWuConstants(_TsaiWuConstantsMixin, _VariablePropertySet):
    GRPC_PROPERTIES = tuple()

    XY = _variable_material_grpc_data_property("XY")
    XZ = _variable_material_grpc_data_property("XZ")
    YZ = _variable_material_grpc_data_property("YZ")
