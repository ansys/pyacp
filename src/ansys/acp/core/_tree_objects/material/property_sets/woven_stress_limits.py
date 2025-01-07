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

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from ...base import TreeObject
from .base import _ConstantPropertySet, _VariablePropertySet
from .property_helper import (
    constant_material_grpc_data_property,
    variable_material_grpc_data_property,
)

__all__ = ["ConstantWovenStressLimits", "VariableWovenStressLimits"]


class _WovenStressLimitsMixin:
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.OrthotropicStressLimitsPropertySet


@mark_grpc_properties
class ConstantWovenStressLimits(_WovenStressLimitsMixin, _ConstantPropertySet):
    """Constant stress limits property set for woven materials."""

    _GRPC_PROPERTIES = tuple()
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        Xc: float = 0.0,
        Yc: float = 0.0,
        Zc: float = 0.0,
        Xt: float = 0.0,
        Yt: float = 0.0,
        Zt: float = 0.0,
        Sxy: float = 0.0,
        Syz: float = 0.0,
        Sxz: float = 0.0,
        _parent_object: TreeObject | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(_parent_object=_parent_object, _attribute_path=_attribute_path)
        if _parent_object is not None:
            return
        self.Xc = Xc
        self.Yc = Yc
        self.Zc = Zc
        self.Xt = Xt
        self.Yt = Yt
        self.Zt = Zt
        self.Sxy = Sxy
        self.Syz = Syz
        self.Sxz = Sxz

    Xc = constant_material_grpc_data_property("Xc")
    Yc = constant_material_grpc_data_property("Yc")
    Zc = constant_material_grpc_data_property("Zc")
    Xt = constant_material_grpc_data_property("Xt")
    Yt = constant_material_grpc_data_property("Yt")
    Zt = constant_material_grpc_data_property("Zt")
    Sxy = constant_material_grpc_data_property("Sxy")
    Syz = constant_material_grpc_data_property("Syz")
    Sxz = constant_material_grpc_data_property("Sxz")


@mark_grpc_properties
class VariableWovenStressLimits(_WovenStressLimitsMixin, _VariablePropertySet):
    """Variable stress limits property set for woven materials."""

    _GRPC_PROPERTIES = tuple()
    _SUPPORTED_SINCE = "24.2"

    Xc = variable_material_grpc_data_property("Xc")
    Yc = variable_material_grpc_data_property("Yc")
    Zc = variable_material_grpc_data_property("Zc")
    Xt = variable_material_grpc_data_property("Xt")
    Yt = variable_material_grpc_data_property("Yt")
    Zt = variable_material_grpc_data_property("Zt")
    Sxy = variable_material_grpc_data_property("Sxy")
    Syz = variable_material_grpc_data_property("Syz")
    Sxz = variable_material_grpc_data_property("Sxz")
