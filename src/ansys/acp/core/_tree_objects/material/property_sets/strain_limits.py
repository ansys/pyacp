from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _PolymorphicMixin, _VariablePropertySet
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

    effective_strain = constant_material_grpc_data_property("effective_strain")
    eXc = constant_material_grpc_data_property("eXc")
    eYc = constant_material_grpc_data_property("eYc")
    eZc = constant_material_grpc_data_property("eZc")
    eXt = constant_material_grpc_data_property("eXt")
    eYt = constant_material_grpc_data_property("eYt")
    eZt = constant_material_grpc_data_property("eZt")
    eSxy = constant_material_grpc_data_property("eSxy")
    eSyz = constant_material_grpc_data_property("eSyz")
    eSxz = constant_material_grpc_data_property("eSxz")


@mark_grpc_properties
class VariableStrainLimits(_StrainLimitsMixin, _VariablePropertySet):
    """Variable strain limits material property set."""

    _GRPC_PROPERTIES = tuple()

    effective_strain = variable_material_grpc_data_property("effective_strain")
    eXc = variable_material_grpc_data_property("eXc")
    eYc = variable_material_grpc_data_property("eYc")
    eZc = variable_material_grpc_data_property("eZc")
    eXt = variable_material_grpc_data_property("eXt")
    eYt = variable_material_grpc_data_property("eYt")
    eZt = variable_material_grpc_data_property("eZt")
    eSxy = variable_material_grpc_data_property("eSxy")
    eSyz = variable_material_grpc_data_property("eSyz")
    eSxz = variable_material_grpc_data_property("eSxz")
