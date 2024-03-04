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

from ansys.api.acp.v0 import modeling_group_pb2, modeling_group_pb2_grpc, modeling_ply_pb2_grpc

from ._grpc_helpers.mapping import define_create_method, define_mutable_mapping
from ._grpc_helpers.property_helper import mark_grpc_properties
from ._mesh_data import (
    ElementalData,
    NodalData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from .base import CreatableTreeObject, IdTreeObject
from .modeling_ply import ModelingPly
from .object_registry import register

__all__ = ["ModelingGroup"]


@dataclasses.dataclass
class ModelingGroupElementalData(ElementalData):
    """Represents elemental data for an Modeling Group."""

    normal: VectorData | None = None


@dataclasses.dataclass
class ModelingGroupNodalData(NodalData):
    """Represents nodal data for an Modeling Group."""


@mark_grpc_properties
@register
class ModelingGroup(CreatableTreeObject, IdTreeObject):
    """Instantiate a modeling group.

    Parameters
    ----------
    name
        Name of the modeling group.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "modeling_groups"
    _OBJECT_INFO_TYPE = modeling_group_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = modeling_group_pb2.CreateRequest

    def __init__(self, *, name: str = "ModelingGroup"):
        super().__init__(name=name)

    def _create_stub(self) -> modeling_group_pb2_grpc.ObjectServiceStub:
        return modeling_group_pb2_grpc.ObjectServiceStub(self._channel)

    create_modeling_ply = define_create_method(
        ModelingPly,
        func_name="create_modeling_ply",
        parent_class_name="ModelingGroup",
        module_name=__module__,
    )
    modeling_plies = define_mutable_mapping(ModelingPly, modeling_ply_pb2_grpc.ObjectServiceStub)

    elemental_data = elemental_data_property(ModelingGroupElementalData)
    nodal_data = nodal_data_property(ModelingGroupNodalData)
