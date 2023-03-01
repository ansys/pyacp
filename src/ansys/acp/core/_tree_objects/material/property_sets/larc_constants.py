from __future__ import annotations

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    _constant_material_grpc_data_property,
    _variable_material_grpc_data_property,
)

__all__ = ["ConstantLaRCConstants", "VariableLaRCConstants"]


class _LaRCConstantsMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.LaRCConstantsPropertySet
    # _PROPERTYSET_NAME = "larc_constants"


@mark_grpc_properties
class ConstantLaRCConstants(_LaRCConstantsMixin, _ConstantPropertySet):
    GRPC_PROPERTIES = tuple()

    def __init__(
        self,
        *,
        fracture_angle_under_compression: float = 0.0,
        fracture_toughness_ratio: float = 0.0,
        fracture_toughness_mode_1: float = 0.0,
        fracture_toughness_mode_2: float = 0.0,
        thin_ply_thickness_limit: float = 0.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.fracture_angle_under_compression = fracture_angle_under_compression
        self.fracture_toughness_ratio = fracture_toughness_ratio
        self.fracture_toughness_mode_1 = fracture_toughness_mode_1
        self.fracture_toughness_mode_2 = fracture_toughness_mode_2
        self.thin_ply_thickness_limit = thin_ply_thickness_limit

    fracture_angle_under_compression = _constant_material_grpc_data_property(
        "fracture_angle_under_compression"
    )
    fracture_toughness_ratio = _constant_material_grpc_data_property("fracture_toughness_ratio")
    fracture_toughness_mode_1 = _constant_material_grpc_data_property("fracture_toughness_mode_1")
    fracture_toughness_mode_2 = _constant_material_grpc_data_property("fracture_toughness_mode_2")
    thin_ply_thickness_limit = _constant_material_grpc_data_property("thin_ply_thickness_limit")


@mark_grpc_properties
class VariableLaRCConstants(_LaRCConstantsMixin, _VariablePropertySet):
    GRPC_PROPERTIES = tuple()

    fracture_angle_under_compression = _variable_material_grpc_data_property(
        "fracture_angle_under_compression"
    )
    fracture_toughness_ratio = _variable_material_grpc_data_property("fracture_toughness_ratio")
    fracture_toughness_mode_1 = _variable_material_grpc_data_property("fracture_toughness_mode_1")
    fracture_toughness_mode_2 = _variable_material_grpc_data_property("fracture_toughness_mode_2")
    thin_ply_thickness_limit = _variable_material_grpc_data_property("thin_ply_thickness_limit")
