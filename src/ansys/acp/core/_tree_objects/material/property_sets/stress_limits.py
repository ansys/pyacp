from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import (
    _ISOTROPIC_PROPERTY_UNAVAILABLE_MSG,
    _ORTHOTROPIC_PROPERTY_UNAVAILABLE_MSG,
    _ConstantPropertySet,
    _PolymorphicMixin,
    _PolymorphicPropertyKwargs,
    _VariablePropertySet,
)
from .property_helper import (
    constant_material_grpc_data_property,
    variable_material_grpc_data_property,
)

__all__ = [
    "ConstantStressLimits",
    "VariableStressLimits",
]


class _StressLimitsMixin(_PolymorphicMixin):
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.OrthotropicStressLimitsPropertySet
    _FIELD_NAME_SUFFIX_DEFAULT = "_orthotropic"
    _FIELD_NAME_SUFFIX_BY_PB_DATATYPE = {
        material_pb2.IsotropicStressLimitsPropertySet: "_isotropic",
        material_pb2.OrthotropicStressLimitsPropertySet: "_orthotropic",
    }


_ISOTROPIC_KWARGS: _PolymorphicPropertyKwargs = {
    "available_on_pb_type": material_pb2.IsotropicStressLimitsPropertySet,
    "unavailable_msg": _ISOTROPIC_PROPERTY_UNAVAILABLE_MSG,
}
_ORTHOTROPIC_KWARGS: _PolymorphicPropertyKwargs = {
    "available_on_pb_type": material_pb2.OrthotropicStressLimitsPropertySet,
    "unavailable_msg": _ORTHOTROPIC_PROPERTY_UNAVAILABLE_MSG,
}


@mark_grpc_properties
class ConstantStressLimits(_StressLimitsMixin, _ConstantPropertySet):
    """Constant stress limits material property set."""

    _GRPC_PROPERTIES = tuple()

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

    effective_stress = constant_material_grpc_data_property("effective_stress", **_ISOTROPIC_KWARGS)
    Xc = constant_material_grpc_data_property("Xc", **_ORTHOTROPIC_KWARGS)
    Yc = constant_material_grpc_data_property("Yc", **_ORTHOTROPIC_KWARGS)
    Zc = constant_material_grpc_data_property("Zc", **_ORTHOTROPIC_KWARGS)
    Xt = constant_material_grpc_data_property("Xt", **_ORTHOTROPIC_KWARGS)
    Yt = constant_material_grpc_data_property("Yt", **_ORTHOTROPIC_KWARGS)
    Zt = constant_material_grpc_data_property("Zt", **_ORTHOTROPIC_KWARGS)
    Sxy = constant_material_grpc_data_property("Sxy", **_ORTHOTROPIC_KWARGS)
    Syz = constant_material_grpc_data_property("Syz", **_ORTHOTROPIC_KWARGS)
    Sxz = constant_material_grpc_data_property("Sxz", **_ORTHOTROPIC_KWARGS)


@mark_grpc_properties
class VariableStressLimits(_StressLimitsMixin, _VariablePropertySet):
    """Variable stress limits material property set."""

    _GRPC_PROPERTIES = tuple()

    effective_stress = variable_material_grpc_data_property("effective_stress", **_ISOTROPIC_KWARGS)
    Xc = variable_material_grpc_data_property("Xc", **_ORTHOTROPIC_KWARGS)
    Yc = variable_material_grpc_data_property("Yc", **_ORTHOTROPIC_KWARGS)
    Zc = variable_material_grpc_data_property("Zc", **_ORTHOTROPIC_KWARGS)
    Xt = variable_material_grpc_data_property("Xt", **_ORTHOTROPIC_KWARGS)
    Yt = variable_material_grpc_data_property("Yt", **_ORTHOTROPIC_KWARGS)
    Zt = variable_material_grpc_data_property("Zt", **_ORTHOTROPIC_KWARGS)
    Sxy = variable_material_grpc_data_property("Sxy", **_ORTHOTROPIC_KWARGS)
    Syz = variable_material_grpc_data_property("Syz", **_ORTHOTROPIC_KWARGS)
    Sxz = variable_material_grpc_data_property("Sxz", **_ORTHOTROPIC_KWARGS)
