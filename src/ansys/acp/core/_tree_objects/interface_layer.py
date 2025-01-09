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
import dataclasses

from ansys.api.acp.v0 import interface_layer_pb2, interface_layer_pb2_grpc

from .._utils.property_protocols import ReadWriteProperty
from ._elemental_or_nodal_data import (
    ElementalData,
    NodalData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from ._grpc_helpers.linked_object_list import (
    define_linked_object_list,
    define_polymorphic_linked_object_list,
)
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import full_mesh_property, shell_mesh_property
from .base import CreatableTreeObject, IdTreeObject
from .element_set import ElementSet
from .enums import status_type_from_pb
from .object_registry import register
from .oriented_selection_set import OrientedSelectionSet


@dataclasses.dataclass
class InterfaceLayerElementalData(ElementalData):
    """Represents elemental data for a Modeling Ply."""

    normal: VectorData | None = None


@dataclasses.dataclass
class InterfaceLayerNodalData(NodalData):
    """Represents nodal data for a Modeling Ply."""

    ply_offset: VectorData | None = None


@mark_grpc_properties
@register
class InterfaceLayer(CreatableTreeObject, IdTreeObject):
    """Instantiate an interface layer.

    The interface layer is a separation layer in the stacking sequence. It can be
    used to analyze the crack growth of existing cracks. They can also be used to
    define contacts zones between two layers.
    The topology is defined with an interface layer in ACP, while all other fracture
    settings need to be specified in the downstream analysis (MAPDL or Mechanical).

    Parameters
    ----------
    name :
        Name of the interface layer.
    global_ply_nr :
        Global ply number for the stacking sequence.
    active :
        Inactive interface layers are ignored in ACP and the downstream analysis.
    oriented_selection_sets :
        Oriented Selection Set for the expansion of the interface layer.
    open_area_sets :
        Defines the initial crack of a Virtual Crack Closure Technique (VCCT) layer.
        Can contain ``OrientedSelectionSet`` and ``ElementSet`` objects.
    """

    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "interface_layers"
    _OBJECT_INFO_TYPE = interface_layer_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = interface_layer_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "InterfaceLayer",
        global_ply_nr: int = 0,
        active: bool = True,
        oriented_selection_sets: Iterable[OrientedSelectionSet] = (),
        open_area_sets: Iterable[ElementSet | OrientedSelectionSet] = (),
    ):
        super().__init__(name=name)
        self.global_ply_nr = global_ply_nr
        self.active = active
        self.oriented_selection_sets = oriented_selection_sets
        self.open_area_sets = open_area_sets

    def _create_stub(self) -> interface_layer_pb2_grpc.ObjectServiceStub:
        return interface_layer_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    global_ply_nr: ReadWriteProperty[int, int] = grpc_data_property("properties.global_ply_nr")
    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")
    oriented_selection_sets = define_linked_object_list(
        "properties.oriented_selection_sets", OrientedSelectionSet
    )
    open_area_sets = define_polymorphic_linked_object_list(
        "properties.open_area_sets", allowed_types=(ElementSet, OrientedSelectionSet)
    )

    mesh = full_mesh_property
    shell_mesh = shell_mesh_property

    elemental_data = elemental_data_property(InterfaceLayerElementalData)
    nodal_data = nodal_data_property(InterfaceLayerNodalData)
