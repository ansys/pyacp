from __future__ import annotations

from typing import Any

from ansys.api.acp.v0 import material_pb2

from .._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ..base import TreeObject
from .property_set_base import (
    _ConstantPropertySet,
    _MonomorphicMixin,
    _PolymorphicMixin,
    _VariablePropertySet,
)

__all__ = [
    "ConstantDensity",
    "VariableDensity",
    "ConstantEngineeringConstants",
    "VariableEngineeringConstants",
]


def _variable_material_grpc_data_property(name: str) -> Any:
    return grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(getattr(val, name) for val in values)
    )


@mark_grpc_properties
class ConstantDensity(_MonomorphicMixin, _ConstantPropertySet):
    GRPC_PROPERTIES = tuple()
    _DEFAULT_PB_OBJECT_CONSTRUCTOR = material_pb2.DensityPropertySet.Data
    _pb_object: material_pb2.DensityPropertySet.Data
    _PROPERTYSET_NAME = "density"

    def __init__(self, *, rho: float = 0.0, _parent_object: TreeObject | None = None):
        super().__init__(_parent_object=_parent_object)
        if _parent_object is not None:
            return
        self.rho = rho

    rho = grpc_data_property("rho")


@mark_grpc_properties
class VariableDensity(_MonomorphicMixin, _VariablePropertySet):
    GRPC_PROPERTIES = tuple()
    _PROPERTYSET_NAME = "density"

    rho = _variable_material_grpc_data_property("rho")


class _EngineeringConstantsMixin(_PolymorphicMixin):
    _PROPERTYSET_NAME = "engineering_constants"
    _FIELD_NAME_DEFAULT = "engineering_constants_orthotropic"
    _FIELD_NAMES_BY_PB_DATATYPE = {
        material_pb2.IsotropicEngineeringConstantsPropertySet.Data: "engineering_constants_isotropic",
        material_pb2.OrthotropicEngineeringConstantsPropertySet.Data: "engineering_constants_orthotropic",
    }


@mark_grpc_properties
class ConstantEngineeringConstants(_EngineeringConstantsMixin, _ConstantPropertySet):
    GRPC_PROPERTIES = tuple()
    _DEFAULT_PB_OBJECT_CONSTRUCTOR = material_pb2.OrthotropicEngineeringConstantsPropertySet.Data
    # _pb_object: (
    #     material_pb2.IsotropicEngineeringConstantsPropertySet.Data
    #     | material_pb2.OrthotropicEngineeringConstantsPropertySet.Data
    # )

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
    ):
        super().__init__(_parent_object=_parent_object)
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

    E = grpc_data_property("E")
    nu = grpc_data_property("nu")
    E1 = grpc_data_property("E1")
    E2 = grpc_data_property("E2")
    E3 = grpc_data_property("E3")
    G12 = grpc_data_property("G12")
    G23 = grpc_data_property("G23")
    G31 = grpc_data_property("G31")
    nu12 = grpc_data_property("nu12")
    nu23 = grpc_data_property("nu23")
    nu13 = grpc_data_property("nu13")


@mark_grpc_properties
class VariableEngineeringConstants(_EngineeringConstantsMixin, _VariablePropertySet):
    GRPC_PROPERTIES = tuple()

    E = _variable_material_grpc_data_property("E")
    nu = _variable_material_grpc_data_property("nu")
    E1 = _variable_material_grpc_data_property("E1")
    E2 = _variable_material_grpc_data_property("E2")
    E3 = _variable_material_grpc_data_property("E3")
    G12 = _variable_material_grpc_data_property("G12")
    G23 = _variable_material_grpc_data_property("G23")
    G31 = _variable_material_grpc_data_property("G31")
    nu12 = _variable_material_grpc_data_property("nu12")
    nu23 = _variable_material_grpc_data_property("nu23")
    nu13 = _variable_material_grpc_data_property("nu13")
