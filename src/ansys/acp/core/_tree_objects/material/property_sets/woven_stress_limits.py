from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    _constant_material_grpc_data_property,
    _variable_material_grpc_data_property,
)

__all__ = ["ConstantWovenStressLimits", "VariableWovenStressLimits"]


class _WovenStressLimitsMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.OrthotropicStressLimitsPropertySet
    # _PROPERTYSET_NAME = "woven_stress_limits"


@mark_grpc_properties
class ConstantWovenStressLimits(_WovenStressLimitsMixin, _ConstantPropertySet):
    GRPC_PROPERTIES = tuple()

    def __init__(
        self,
        *,
        Xc: float = 0.0,
        Yc: float = 0.0,
        Zc: float = 0.0,
        Xt: float = 0.0,
        Yt: float = 0.0,
        Zt: float = 0.0,
        Sxy: float = 0.0,
        Syz: float = 0.0,
        Sxz: float = 0.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.Xc = Xc
        self.Yc = Yc
        self.Zc = Zc
        self.Xt = Xt
        self.Yt = Yt
        self.Zt = Zt
        self.Sxy = Sxy
        self.Syz = Syz
        self.Sxz = Sxz

    Xc = _constant_material_grpc_data_property("Xc")
    Yc = _constant_material_grpc_data_property("Yc")
    Zc = _constant_material_grpc_data_property("Zc")
    Xt = _constant_material_grpc_data_property("Xt")
    Yt = _constant_material_grpc_data_property("Yt")
    Zt = _constant_material_grpc_data_property("Zt")
    Sxy = _constant_material_grpc_data_property("Sxy")
    Syz = _constant_material_grpc_data_property("Syz")
    Sxz = _constant_material_grpc_data_property("Sxz")


@mark_grpc_properties
class VariableWovenStressLimits(_WovenStressLimitsMixin, _VariablePropertySet):
    GRPC_PROPERTIES = tuple()

    Xc = _variable_material_grpc_data_property("Xc")
    Yc = _variable_material_grpc_data_property("Yc")
    Zc = _variable_material_grpc_data_property("Zc")
    Xt = _variable_material_grpc_data_property("Xt")
    Yt = _variable_material_grpc_data_property("Yt")
    Zt = _variable_material_grpc_data_property("Zt")
    Sxy = _variable_material_grpc_data_property("Sxy")
    Syz = _variable_material_grpc_data_property("Syz")
    Sxz = _variable_material_grpc_data_property("Sxz")
