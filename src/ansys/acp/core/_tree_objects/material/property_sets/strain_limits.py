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
    "ConstantStrainLimits",
    "VariableStrainLimits",
]


class _StrainLimitsMixin(_PolymorphicMixin):
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.OrthotropicStrainLimitsPropertySet
    _FIELD_NAME_SUFFIX_DEFAULT = "_orthotropic"
    _FIELD_NAME_SUFFIX_BY_PB_DATATYPE = {
        material_pb2.IsotropicStrainLimitsPropertySet: "_isotropic",
        material_pb2.OrthotropicStrainLimitsPropertySet: "_orthotropic",
    }


_ISOTROPIC_KWARGS: _PolymorphicPropertyKwargs = {
    "available_on_pb_type": material_pb2.IsotropicStrainLimitsPropertySet,
    "unavailable_msg": _ISOTROPIC_PROPERTY_UNAVAILABLE_MSG,
}
_ORTHOTROPIC_KWARGS: _PolymorphicPropertyKwargs = {
    "available_on_pb_type": material_pb2.OrthotropicStrainLimitsPropertySet,
    "unavailable_msg": _ORTHOTROPIC_PROPERTY_UNAVAILABLE_MSG,
}


@mark_grpc_properties
class ConstantStrainLimits(_StrainLimitsMixin, _ConstantPropertySet):
    """Constant strain limits material property set."""

    _GRPC_PROPERTIES = tuple()

    def __init__(
        self,
        *,
        eXc: float = 0.0,
        eYc: float = 0.0,
        eZc: float = 0.0,
        eXt: float = 0.0,
        eYt: float = 0.0,
        eZt: float = 0.0,
        eSxy: float = 0.0,
        eSyz: float = 0.0,
        eSxz: float = 0.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.eXc = eXc
        self.eYc = eYc
        self.eZc = eZc
        self.eXt = eXt
        self.eYt = eYt
        self.eZt = eZt
        self.eSxy = eSxy
        self.eSyz = eSyz
        self.eSxz = eSxz

    effective_strain = constant_material_grpc_data_property("effective_strain", **_ISOTROPIC_KWARGS)
    eXc = constant_material_grpc_data_property("eXc", **_ORTHOTROPIC_KWARGS)
    eYc = constant_material_grpc_data_property("eYc", **_ORTHOTROPIC_KWARGS)
    eZc = constant_material_grpc_data_property("eZc", **_ORTHOTROPIC_KWARGS)
    eXt = constant_material_grpc_data_property("eXt", **_ORTHOTROPIC_KWARGS)
    eYt = constant_material_grpc_data_property("eYt", **_ORTHOTROPIC_KWARGS)
    eZt = constant_material_grpc_data_property("eZt", **_ORTHOTROPIC_KWARGS)
    eSxy = constant_material_grpc_data_property("eSxy", **_ORTHOTROPIC_KWARGS)
    eSyz = constant_material_grpc_data_property("eSyz", **_ORTHOTROPIC_KWARGS)
    eSxz = constant_material_grpc_data_property("eSxz", **_ORTHOTROPIC_KWARGS)


@mark_grpc_properties
class VariableStrainLimits(_StrainLimitsMixin, _VariablePropertySet):
    """Variable strain limits material property set."""

    _GRPC_PROPERTIES = tuple()

    effective_strain = variable_material_grpc_data_property("effective_strain", **_ISOTROPIC_KWARGS)
    eXc = variable_material_grpc_data_property("eXc", **_ORTHOTROPIC_KWARGS)
    eYc = variable_material_grpc_data_property("eYc", **_ORTHOTROPIC_KWARGS)
    eZc = variable_material_grpc_data_property("eZc", **_ORTHOTROPIC_KWARGS)
    eXt = variable_material_grpc_data_property("eXt", **_ORTHOTROPIC_KWARGS)
    eYt = variable_material_grpc_data_property("eYt", **_ORTHOTROPIC_KWARGS)
    eZt = variable_material_grpc_data_property("eZt", **_ORTHOTROPIC_KWARGS)
    eSxy = variable_material_grpc_data_property("eSxy", **_ORTHOTROPIC_KWARGS)
    eSyz = variable_material_grpc_data_property("eSyz", **_ORTHOTROPIC_KWARGS)
    eSxz = variable_material_grpc_data_property("eSxz", **_ORTHOTROPIC_KWARGS)
