# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

from enum import Enum

from ansys.api.acp.v0 import material_pb2

from ...._utils.property_protocols import ReadWriteProperty
from ..._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    constant_material_grpc_data_property,
    variable_material_grpc_data_property,
)

__all__ = ["ConstantPuckConstants", "VariablePuckConstants", "PuckMaterialType"]


class PuckMaterialType(str, Enum):
    """Possible Puck material types."""

    IGNORED = "ignored"
    CARBON = "carbon"
    GLASS = "glass"
    MATERIAL_SPECIFIC = "material-specific"


class _PuckConstantsMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.PuckConstantsPropertySet


@mark_grpc_properties
class ConstantPuckConstants(_PuckConstantsMixin, _ConstantPropertySet):
    """Constant Puck constants material property set."""

    _GRPC_PROPERTIES = tuple()
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        p_21_pos: float | None = None,
        p_21_neg: float | None = None,
        p_22_pos: float | None = None,
        p_22_neg: float | None = None,
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

        def val_or_default(val: float | None, default: float) -> float:
            if val is not None:
                return val
            return default

        self.mat_type = PuckMaterialType(mat_type)

        if mat_type in (PuckMaterialType.IGNORED, PuckMaterialType.MATERIAL_SPECIFIC):
            self.p_21_pos = val_or_default(p_21_pos, 0.325)
            self.p_21_neg = val_or_default(p_21_neg, 0.275)
            self.p_22_pos = val_or_default(p_22_pos, 0.225)
            self.p_22_neg = val_or_default(p_22_neg, 0.225)
        elif mat_type == PuckMaterialType.CARBON:
            self.p_21_pos = val_or_default(p_21_pos, 0.35)
            self.p_21_neg = val_or_default(p_21_neg, 0.3)
            self.p_22_pos = val_or_default(p_22_pos, 0.25)
            self.p_22_neg = val_or_default(p_22_neg, 0.25)
        elif mat_type == PuckMaterialType.GLASS:
            self.p_21_pos = val_or_default(p_21_pos, 0.3)
            self.p_21_neg = val_or_default(p_21_neg, 0.25)
            self.p_22_pos = val_or_default(p_22_pos, 0.2)
            self.p_22_neg = val_or_default(p_22_neg, 0.2)
        else:
            raise ValueError(f"Unknown 'mat_type': '{mat_type}'")

        self.s = s
        self.M = M
        self.interface_weakening_factor = interface_weakening_factor

    p_21_pos = constant_material_grpc_data_property("p_21_pos")
    p_21_neg = constant_material_grpc_data_property("p_21_neg")
    p_22_pos = constant_material_grpc_data_property("p_22_pos")
    p_22_neg = constant_material_grpc_data_property("p_22_neg")
    s = constant_material_grpc_data_property("s")
    M = constant_material_grpc_data_property("M")
    interface_weakening_factor = constant_material_grpc_data_property("interface_weakening_factor")
    mat_type: ReadWriteProperty[PuckMaterialType, PuckMaterialType] = grpc_data_property(
        "mat_type", from_protobuf=PuckMaterialType
    )


@mark_grpc_properties
class VariablePuckConstants(_PuckConstantsMixin, _VariablePropertySet):
    """Variable Puck constants material property set."""

    _GRPC_PROPERTIES = tuple()
    _SUPPORTED_SINCE = "24.2"

    p_21_pos = variable_material_grpc_data_property("p_21_pos")
    p_21_neg = variable_material_grpc_data_property("p_21_neg")
    p_22_pos = variable_material_grpc_data_property("p_22_pos")
    p_22_neg = variable_material_grpc_data_property("p_22_neg")
    s = variable_material_grpc_data_property("s")
    M = variable_material_grpc_data_property("M")
    interface_weakening_factor = variable_material_grpc_data_property("interface_weakening_factor")
    mat_type = grpc_data_property_read_only("mat_type", from_protobuf=PuckMaterialType)
