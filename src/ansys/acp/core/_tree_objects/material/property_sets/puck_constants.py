from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    _constant_material_grpc_data_property,
    _variable_material_grpc_data_property,
)

__all__ = ["ConstantPuckConstants", "VariablePuckConstants"]

# TODO: handle material classification


class _PuckConstantsMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.PuckConstantsPropertySet
    # _PROPERTYSET_NAME = "puck_constants"


@mark_grpc_properties
class ConstantPuckConstants(_PuckConstantsMixin, _ConstantPropertySet):
    GRPC_PROPERTIES = tuple()

    def __init__(
        self,
        *,
        # TODO: check defaults
        p21_pos: float = 0.0,
        p21_neg: float = 0.0,
        p22_pos: float = 0.0,
        p22_neg: float = 0.0,
        s: float = 0.0,
        M: float = 0.0,
        interface_weakening_factor: float = 0.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.p21_pos = p21_pos
        self.p21_neg = p21_neg
        self.p22_pos = p22_pos
        self.p22_neg = p22_neg
        self.s = s
        self.M = M
        self.interface_weakening_factor = interface_weakening_factor

    p21_pos = _constant_material_grpc_data_property("p21_pos")
    p21_neg = _constant_material_grpc_data_property("p21_neg")
    p22_pos = _constant_material_grpc_data_property("p22_pos")
    p22_neg = _constant_material_grpc_data_property("p22_neg")
    s = _constant_material_grpc_data_property("s")
    M = _constant_material_grpc_data_property("M")
    interface_weakening_factor = _constant_material_grpc_data_property("interface_weakening_factor")


@mark_grpc_properties
class VariablePuckConstants(_PuckConstantsMixin, _VariablePropertySet):
    GRPC_PROPERTIES = tuple()

    p21_pos = _variable_material_grpc_data_property("p21_pos")
    p21_neg = _variable_material_grpc_data_property("p21_neg")
    p22_pos = _variable_material_grpc_data_property("p22_pos")
    p22_neg = _variable_material_grpc_data_property("p22_neg")
    s = _variable_material_grpc_data_property("s")
    M = _variable_material_grpc_data_property("M")
    interface_weakening_factor = _variable_material_grpc_data_property("interface_weakening_factor")
