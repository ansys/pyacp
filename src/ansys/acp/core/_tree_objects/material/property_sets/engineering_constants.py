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
    "ConstantEngineeringConstants",
    "VariableEngineeringConstants",
]


class _EngineeringConstantsMixin(_PolymorphicMixin):
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.OrthotropicEngineeringConstantsPropertySet
    _FIELD_NAME_DEFAULT = "_orthotropic"
    _FIELD_NAME_SUFFIX_BY_PB_DATATYPE = {
        material_pb2.IsotropicEngineeringConstantsPropertySet: "_isotropic",
        material_pb2.OrthotropicEngineeringConstantsPropertySet: "_orthotropic",
    }


_ISOTROPIC_KWARGS: _PolymorphicPropertyKwargs = {
    "available_on_pb_type": material_pb2.IsotropicEngineeringConstantsPropertySet,
    "unavailable_msg": _ISOTROPIC_PROPERTY_UNAVAILABLE_MSG,
}
_ORTHOTROPIC_KWARGS: _PolymorphicPropertyKwargs = {
    "available_on_pb_type": material_pb2.OrthotropicEngineeringConstantsPropertySet,
    "unavailable_msg": _ORTHOTROPIC_PROPERTY_UNAVAILABLE_MSG,
}


@mark_grpc_properties
class ConstantEngineeringConstants(_EngineeringConstantsMixin, _ConstantPropertySet):
    """Constant engineering constants material property set."""

    _GRPC_PROPERTIES = tuple()

    def __init__(
        self,
        *,
        E1: float = 0.0,
        E2: float = 0.0,
        E3: float = 0.0,
        nu12: float = 0.0,
        nu23: float = 0.0,
        nu13: float = 0.0,
        G12: float = 0.0,
        G23: float = 0.0,
        G31: float = 0.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.E1 = E1
        self.E2 = E2
        self.E3 = E3
        self.nu12 = nu12
        self.nu23 = nu23
        self.nu13 = nu13
        self.G12 = G12
        self.G23 = G23
        self.G31 = G31

    E = constant_material_grpc_data_property("E", **_ISOTROPIC_KWARGS)
    nu = constant_material_grpc_data_property("nu", **_ISOTROPIC_KWARGS)
    E1 = constant_material_grpc_data_property("E1", **_ORTHOTROPIC_KWARGS)
    E2 = constant_material_grpc_data_property("E2", **_ORTHOTROPIC_KWARGS)
    E3 = constant_material_grpc_data_property("E3", **_ORTHOTROPIC_KWARGS)
    G12 = constant_material_grpc_data_property("G12", **_ORTHOTROPIC_KWARGS)
    G23 = constant_material_grpc_data_property("G23", **_ORTHOTROPIC_KWARGS)
    G31 = constant_material_grpc_data_property("G31", **_ORTHOTROPIC_KWARGS)
    nu12 = constant_material_grpc_data_property("nu12", **_ORTHOTROPIC_KWARGS)
    nu23 = constant_material_grpc_data_property("nu23", **_ORTHOTROPIC_KWARGS)
    nu13 = constant_material_grpc_data_property("nu13", **_ORTHOTROPIC_KWARGS)


@mark_grpc_properties
class VariableEngineeringConstants(_EngineeringConstantsMixin, _VariablePropertySet):
    """Variable engineering constants material property set."""

    _GRPC_PROPERTIES = tuple()

    E = variable_material_grpc_data_property("E", **_ISOTROPIC_KWARGS)
    nu = variable_material_grpc_data_property("nu", **_ISOTROPIC_KWARGS)
    E1 = variable_material_grpc_data_property("E1", **_ORTHOTROPIC_KWARGS)
    E2 = variable_material_grpc_data_property("E2", **_ORTHOTROPIC_KWARGS)
    E3 = variable_material_grpc_data_property("E3", **_ORTHOTROPIC_KWARGS)
    G12 = variable_material_grpc_data_property("G12", **_ORTHOTROPIC_KWARGS)
    G23 = variable_material_grpc_data_property("G23", **_ORTHOTROPIC_KWARGS)
    G31 = variable_material_grpc_data_property("G31", **_ORTHOTROPIC_KWARGS)
    nu12 = variable_material_grpc_data_property("nu12", **_ORTHOTROPIC_KWARGS)
    nu23 = variable_material_grpc_data_property("nu23", **_ORTHOTROPIC_KWARGS)
    nu13 = variable_material_grpc_data_property("nu13", **_ORTHOTROPIC_KWARGS)
