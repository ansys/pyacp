from __future__ import annotations

from enum import Enum

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    _constant_material_grpc_data_property,
    _variable_material_grpc_data_property,
)

__all__ = ["ConstantPuckConstants", "VariablePuckConstants"]


class PuckMaterialType(str, Enum):
    IGNORED = "ignored"
    CARBON = "carbon"
    GLASS = "glass"
    MATERIAL_SPECIFIC = "material-specific"


class _PuckConstantsMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.PuckConstantsPropertySet


@mark_grpc_properties
class ConstantPuckConstants(_PuckConstantsMixin, _ConstantPropertySet):
    _GRPC_PROPERTIES = tuple()

    # TODO: should we implement defaults depending on the 'mat_type'?
    def __init__(
        self,
        *,
        p_21_pos: float = 0.325,
        p_21_neg: float = 0.275,
        p_22_pos: float = 0.225,
        p_22_neg: float = 0.225,
        s: float = 0.5,
        M: float = 0.5,
        interface_weakening_factor: float = 0.8,
        mat_type: str = PuckMaterialType.IGNORED,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.p_21_pos = p_21_pos
        self.p_21_neg = p_21_neg
        self.p_22_pos = p_22_pos
        self.p_22_neg = p_22_neg
        self.s = s
        self.M = M
        self.interface_weakening_factor = interface_weakening_factor
        self.mat_type = mat_type

    p_21_pos = _constant_material_grpc_data_property("p_21_pos")
    p_21_neg = _constant_material_grpc_data_property("p_21_neg")
    p_22_pos = _constant_material_grpc_data_property("p_22_pos")
    p_22_neg = _constant_material_grpc_data_property("p_22_neg")
    s = _constant_material_grpc_data_property("s")
    M = _constant_material_grpc_data_property("M")
    interface_weakening_factor = _constant_material_grpc_data_property("interface_weakening_factor")
    mat_type = grpc_data_property("mat_type")


@mark_grpc_properties
class VariablePuckConstants(_PuckConstantsMixin, _VariablePropertySet):
    _GRPC_PROPERTIES = tuple()

    p_21_pos = _variable_material_grpc_data_property("p_21_pos")
    p_21_neg = _variable_material_grpc_data_property("p_21_neg")
    p_22_pos = _variable_material_grpc_data_property("p_22_pos")
    p_22_neg = _variable_material_grpc_data_property("p_22_neg")
    s = _variable_material_grpc_data_property("s")
    M = _variable_material_grpc_data_property("M")
    interface_weakening_factor = _variable_material_grpc_data_property("interface_weakening_factor")
    mat_type = grpc_data_property_read_only("mat_type")
