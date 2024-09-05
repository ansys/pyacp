# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
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

from collections.abc import Iterable
import dataclasses

import numpy as np

from ansys.api.acp.v0 import solid_model_pb2, solid_model_pb2_grpc

from ._grpc_helpers.mapping import define_create_method, define_mutable_mapping
from ._grpc_helpers.property_helper import mark_grpc_properties
from ._mesh_data import (
    ElementalData,
    NodalData,
    ScalarData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from .base import CreatableTreeObject, IdTreeObject
from .object_registry import register

__all__ = ["SolidModel"]


@dataclasses.dataclass
class SolidModelElementalData(ElementalData):
    """Represents elemental data for an Solid Model."""

    normal: VectorData | None = None
    orientation: VectorData | None = None
    reference_direction: VectorData | None = None
    fiber_direction: VectorData | None = None
    draped_fiber_direction: VectorData | None = None
    transverse_direction: VectorData | None = None
    draped_transverse_direction: VectorData | None = None
    thickness: ScalarData[np.float64] | None = None
    relative_thickness_correction: ScalarData[np.float64] | None = None
    design_angle: ScalarData[np.float64] | None = None
    shear_angle: ScalarData[np.float64] | None = None
    draped_fiber_angle: ScalarData[np.float64] | None = None
    draped_transverse_angle: ScalarData[np.float64] | None = None
    area: ScalarData[np.float64] | None = None
    price: ScalarData[np.float64] | None = None
    volume: ScalarData[np.float64] | None = None
    mass: ScalarData[np.float64] | None = None
    offset: ScalarData[np.float64] | None = None
    cog: VectorData | None = None


@dataclasses.dataclass
class SolidModelNodalData(NodalData):
    """Represents nodal data for an Solid Model."""

    ply_offset: VectorData | None = None


@mark_grpc_properties
@register
class SolidModel(CreatableTreeObject, IdTreeObject):
    """Instantiate a solid model.

    Parameters
    ----------
    name
        Name of the solid model.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "solid_models"
    _OBJECT_INFO_TYPE = solid_model_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = solid_model_pb2.CreateRequest

    def __init__(self, *, name: str = "SolidModel"):
        super().__init__(name=name)

    def _create_stub(self) -> solid_model_pb2_grpc.ObjectServiceStub:
        return solid_model_pb2_grpc.ObjectServiceStub(self._channel)

    elemental_data = elemental_data_property(SolidModelElementalData)
    nodal_data = nodal_data_property(SolidModelNodalData)
