from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _PolymorphicMixin, _VariablePropertySet
from .property_helper import (
    _constant_material_grpc_data_property,
    _variable_material_grpc_data_property,
)

__all__ = [
    "ConstantStrainLimits",
    "VariableStrainLimits",
]


class _StrainLimitsMixin(_PolymorphicMixin):
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.OrthotropicStrainLimitsPropertySet
    # _PROPERTYSET_NAME = "strain_limits"
    _FIELD_NAME_SUFFIX_DEFAULT = "_orthotropic"
    _FIELD_NAME_SUFFIX_BY_PB_DATATYPE = {
        material_pb2.IsotropicStrainLimitsPropertySet: "_isotropic",
        material_pb2.OrthotropicStrainLimitsPropertySet: "_orthotropic",
    }


@mark_grpc_properties
class ConstantStrainLimits(_StrainLimitsMixin, _ConstantPropertySet):
    GRPC_PROPERTIES = tuple()

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

    effective_strain = _constant_material_grpc_data_property("effective_strain")
    eXc = _constant_material_grpc_data_property("eXc")
    eYc = _constant_material_grpc_data_property("eYc")
    eZc = _constant_material_grpc_data_property("eZc")
    eXt = _constant_material_grpc_data_property("eXt")
    eYt = _constant_material_grpc_data_property("eYt")
    eZt = _constant_material_grpc_data_property("eZt")
    eSxy = _constant_material_grpc_data_property("eSxy")
    eSyz = _constant_material_grpc_data_property("eSyz")
    eSxz = _constant_material_grpc_data_property("eSxz")


@mark_grpc_properties
class VariableStrainLimits(_StrainLimitsMixin, _VariablePropertySet):
    GRPC_PROPERTIES = tuple()

    effective_strain = _variable_material_grpc_data_property("effective_strain")
    eXc = _variable_material_grpc_data_property("eXc")
    eYc = _variable_material_grpc_data_property("eYc")
    eZc = _variable_material_grpc_data_property("eZc")
    eXt = _variable_material_grpc_data_property("eXt")
    eYt = _variable_material_grpc_data_property("eYt")
    eZt = _variable_material_grpc_data_property("eZt")
    eSxy = _variable_material_grpc_data_property("eSxy")
    eSyz = _variable_material_grpc_data_property("eSyz")
    eSxz = _variable_material_grpc_data_property("eSxz")
