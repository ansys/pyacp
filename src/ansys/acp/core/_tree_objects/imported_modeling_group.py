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

from collections.abc import Iterable

from ansys.api.acp.v0 import (
    imported_modeling_group_pb2,
    imported_modeling_group_pb2_grpc,
    imported_modeling_ply_pb2_grpc,
)

from ._grpc_helpers.mapping import define_create_method, define_mutable_mapping
from ._grpc_helpers.property_helper import mark_grpc_properties
from .base import CreatableTreeObject, IdTreeObject
from .imported_modeling_ply import ImportedModelingPly
from .object_registry import register

__all__ = ["ImportedModelingGroup"]


@mark_grpc_properties
@register
class ImportedModelingGroup(CreatableTreeObject, IdTreeObject):
    """Instantiate an imported modeling group.

    Parameters
    ----------
    name : str
        Name of the imported modeling group.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "imported_modeling_groups"
    _OBJECT_INFO_TYPE = imported_modeling_group_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = imported_modeling_group_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(self, *, name: str = "ImportedModelingGroup"):
        super().__init__(name=name)

    def _create_stub(self) -> imported_modeling_group_pb2_grpc.ObjectServiceStub:
        return imported_modeling_group_pb2_grpc.ObjectServiceStub(self._channel)

    create_imported_modeling_ply = define_create_method(
        ImportedModelingPly,
        func_name="create_imported_modeling_ply",
        parent_class_name="ImportedModelingGroup",
        module_name=__module__,
    )
    imported_modeling_plies = define_mutable_mapping(
        ImportedModelingPly, imported_modeling_ply_pb2_grpc.ObjectServiceStub
    )
