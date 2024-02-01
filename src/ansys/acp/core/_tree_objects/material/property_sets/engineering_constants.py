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

    E = constant_material_grpc_data_property("E")
    nu = constant_material_grpc_data_property("nu")
    E1 = constant_material_grpc_data_property("E1")
    E2 = constant_material_grpc_data_property("E2")
    E3 = constant_material_grpc_data_property("E3")
    G12 = constant_material_grpc_data_property("G12")
    G23 = constant_material_grpc_data_property("G23")
    G31 = constant_material_grpc_data_property("G31")
    nu12 = constant_material_grpc_data_property("nu12")
    nu23 = constant_material_grpc_data_property("nu23")
    nu13 = constant_material_grpc_data_property("nu13")


@mark_grpc_properties
class VariableEngineeringConstants(_EngineeringConstantsMixin, _VariablePropertySet):
    """Variable engineering constants material property set."""
    _GRPC_PROPERTIES = tuple()

    E = variable_material_grpc_data_property("E")
    nu = variable_material_grpc_data_property("nu")
    E1 = variable_material_grpc_data_property("E1")
    E2 = variable_material_grpc_data_property("E2")
    E3 = variable_material_grpc_data_property("E3")
    G12 = variable_material_grpc_data_property("G12")
    G23 = variable_material_grpc_data_property("G23")
    G31 = variable_material_grpc_data_property("G31")
    nu12 = variable_material_grpc_data_property("nu12")
    nu23 = variable_material_grpc_data_property("nu23")
    nu13 = variable_material_grpc_data_property("nu13")
