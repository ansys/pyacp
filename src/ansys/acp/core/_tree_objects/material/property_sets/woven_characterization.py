from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    _constant_material_grpc_data_property,
    _variable_material_grpc_data_property,
)

__all__ = ["ConstantWovenCharacterization", "VariableWovenCharacterization"]


class _WovenCharacterizationMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.WovenCharacterizationPropertySet


@mark_grpc_properties
class ConstantWovenCharacterization(_WovenCharacterizationMixin, _ConstantPropertySet):
    _GRPC_PROPERTIES = tuple()

    def __init__(
        self,
        *,
        orientation_1: float = 0.0,
        E1_1: float = 0.0,
        E2_1: float = 0.0,
        G12_1: float = 0.0,
        G23_1: float = 0.0,
        nu12_1: float = 0.0,
        orientation_2: float = 0.0,
        E1_2: float = 0.0,
        E2_2: float = 0.0,
        G12_2: float = 0.0,
        G23_2: float = 0.0,
        nu12_2: float = 0.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.orientation_1 = orientation_1
        self.E1_1 = E1_1
        self.E2_1 = E2_1
        self.G12_1 = G12_1
        self.G23_1 = G23_1
        self.nu12_1 = nu12_1
        self.orientation_2 = orientation_2
        self.E1_2 = E1_2
        self.E2_2 = E2_2
        self.G12_2 = G12_2
        self.G23_2 = G23_2
        self.nu12_2 = nu12_2

    orientation_1 = _constant_material_grpc_data_property("orientation_1")
    E1_1 = _constant_material_grpc_data_property("E1_1")
    E2_1 = _constant_material_grpc_data_property("E2_1")
    G12_1 = _constant_material_grpc_data_property("G12_1")
    G23_1 = _constant_material_grpc_data_property("G23_1")
    nu12_1 = _constant_material_grpc_data_property("nu12_1")
    orientation_2 = _constant_material_grpc_data_property("orientation_2")
    E1_2 = _constant_material_grpc_data_property("E1_2")
    E2_2 = _constant_material_grpc_data_property("E2_2")
    G12_2 = _constant_material_grpc_data_property("G12_2")
    G23_2 = _constant_material_grpc_data_property("G23_2")
    nu12_2 = _constant_material_grpc_data_property("nu12_2")


@mark_grpc_properties
class VariableWovenCharacterization(_WovenCharacterizationMixin, _VariablePropertySet):
    _GRPC_PROPERTIES = tuple()

    E1_1 = _variable_material_grpc_data_property("E1_1")
    E2_1 = _variable_material_grpc_data_property("E2_1")
    G12_1 = _variable_material_grpc_data_property("G12_1")
    G23_1 = _variable_material_grpc_data_property("G23_1")
    nu12_1 = _variable_material_grpc_data_property("nu12_1")
    orientation_2 = _variable_material_grpc_data_property("orientation_2")
    E1_2 = _variable_material_grpc_data_property("E1_2")
    E2_2 = _variable_material_grpc_data_property("E2_2")
    G12_2 = _variable_material_grpc_data_property("G12_2")
    G23_2 = _variable_material_grpc_data_property("G23_2")
    nu12_2 = _variable_material_grpc_data_property("nu12_2")
