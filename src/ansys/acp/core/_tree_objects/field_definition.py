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

from collections.abc import Iterable, Sequence
import typing

from ansys.api.acp.v0 import field_definition_pb2, field_definition_pb2_grpc

from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.linked_object_list import define_polymorphic_linked_object_list
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .element_set import ElementSet
from .enums import status_type_from_pb
from .lookup_table_1d_column import LookUpTable1DColumn
from .lookup_table_3d_column import LookUpTable3DColumn
from .modeling_ply import ModelingPly
from .object_registry import register
from .oriented_selection_set import OrientedSelectionSet

__all__ = ["FieldDefinition"]


_SCOPE_ENTITIES_LINKABLE_TO_FIELD_DEFINITION: typing.TypeAlias = typing.Union[
    ElementSet,
    OrientedSelectionSet,
    ModelingPly,
]


@mark_grpc_properties
@register
class FieldDefinition(CreatableTreeObject, IdTreeObject):
    """Instantiate a Field Definition.

    A field definition is used to configure the state of variable materials.
    For instance, a Lookup Table can be used to define the distribution of a
    state of material field (e.g. degradation). The field definition allows
    to define the material field per element or per ply and element.

    Note: Field definitions are currently only supported through (Py)Mechanical.
    The direct interface of PyACP to (Py)MADL ignores field definitions.

    Parameters
    ----------
    name :
        Name of the field definition.
    active :
        Inactive field definitions are ignored.
    field_variable_name :
        Links the material field to a field variable name.
        The field variable name must be defined in the material properties.
        Note that the ``Temperature`` and ``Shear Angle`` field variables are not available
        for Field Definitions. Temperature is defined through the solution and `Shear Angle`
        is defined via draping calculations.
    scope_entities :
        Define the scope of the field definition. You can use a combination
        of Element Sets and Oriented Selection Sets for elemental scope.
        For ply-wise field definitions, a combination of Modeling Plies can be selected.
        Note that the field definition is only applied to the Analysis Plies attached to
        the Modeling Plies. A combination of elemental and ply-wise definition is not supported.
    scalar_field :
        Select the scalar Look-Up Table column from which the state of the field
        variable is interpolated from.
    full_mapping :
        Specify to include the shell offset of each analysis ply for the interpolation process.
        The default is to interpolate the state of the field variables at the shell element centroid.
        For solid elements, the position of each analysis ply is automatically considered.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "field_definitions"
    _OBJECT_INFO_TYPE = field_definition_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = field_definition_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "FieldDefinition",
        active: bool = True,
        field_variable_name: str = "",
        scope_entities: Sequence[_SCOPE_ENTITIES_LINKABLE_TO_FIELD_DEFINITION] = tuple(),
        scalar_field: LookUpTable1DColumn | LookUpTable3DColumn | None = None,
        full_mapping: bool = False,
    ):
        super().__init__(name=name)

        self.active = active
        self.field_variable_name = field_variable_name
        self.scope_entities = scope_entities
        self.scalar_field = scalar_field
        self.full_mapping = full_mapping

    def _create_stub(self) -> field_definition_pb2_grpc.ObjectServiceStub:
        return field_definition_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")
    field_variable_name: ReadWriteProperty[str, str] = grpc_data_property(
        "properties.field_variable_name"
    )

    scope_entities = define_polymorphic_linked_object_list(
        "properties.scope_entities",
        allowed_types=(
            ElementSet,
            OrientedSelectionSet,
            ModelingPly,
        ),
    )

    scalar_field = grpc_link_property(
        "properties.scalar_field", allowed_types=(LookUpTable1DColumn, LookUpTable3DColumn)
    )

    full_mapping: ReadWriteProperty[bool, bool] = grpc_data_property("properties.full_mapping")
