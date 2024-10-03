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

from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING

from ansys.api.acp.v0 import butt_joint_sequence_pb2, butt_joint_sequence_pb2_grpc

from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.edge_property_list import (
    EdgePropertyTypeBase,
    define_add_method,
    define_edge_property_list,
    edge_property_type_attribute,
    edge_property_type_linked_object,
)
from ._grpc_helpers.linked_object_list import define_polymorphic_linked_object_list
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .modeling_ply import ModelingPly
from .object_registry import register

if TYPE_CHECKING:
    # Creates a circular import if imported at the top-level, since the ButtJointSequence
    # is a direct child of the ModelingGroup.
    from .modeling_group import ModelingGroup

__all__ = ["ButtJointSequence", "PrimaryPly"]


def _get_allowed_sequence_types() -> tuple[type, ...]:
    from .modeling_group import ModelingGroup

    return (ModelingGroup, ModelingPly)


@mark_grpc_properties
class PrimaryPly(EdgePropertyTypeBase):
    """Defines a primary ply of a butt joint sequence.

    Parameters
    ----------
    sequence :
        Modeling group or modeling ply defining the primary ply.
    level :
        Level of the primary ply. Plies with a higher level inherit the thickness
        from adjacent plies with a lower level.

    """

    __slots__: tuple[str, ...] = tuple()

    _PB_OBJECT_TYPE = butt_joint_sequence_pb2.PrimaryPly
    _SUPPORTED_SINCE = "25.1"

    def __init__(self, sequence: ModelingGroup | ModelingPly | None = None, level: int = 1):
        super().__init__()
        self.sequence = sequence
        self.level = level

    sequence: ReadWriteProperty[
        ModelingGroup | ModelingPly | None, ModelingGroup | ModelingPly | None
    ] = edge_property_type_linked_object(
        "sequence", allowed_types_getter=_get_allowed_sequence_types
    )
    level: ReadWriteProperty[int, int] = edge_property_type_attribute("level")


@mark_grpc_properties
@register
class ButtJointSequence(CreatableTreeObject, IdTreeObject):
    """Instantiate a ButtJointSequence.

    Parameters
    ----------
    name :
        Name of the butt joint sequence.
    primary_plies :
        Primary plies are the source of a butt joint and they pass the thickness to
        adjacent plies. Plies with a higher level inherit the thickness from those
        with a lower level.
    secondary_plies :
        Secondary plies are butt-joined to adjacent primary plies and they inherit
        the thickness.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "butt_joint_sequences"
    _OBJECT_INFO_TYPE = butt_joint_sequence_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = butt_joint_sequence_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "ButtJointSequence",
        active: bool = True,
        global_ply_nr: int = 0,
        primary_plies: Sequence[PrimaryPly] = (),
        secondary_plies: Sequence[ModelingGroup | ModelingPly] = (),
    ):
        super().__init__(name=name)
        self.active = active
        self.global_ply_nr = global_ply_nr
        self.primary_plies = primary_plies
        self.secondary_plies = secondary_plies

    def _create_stub(self) -> butt_joint_sequence_pb2_grpc.ObjectServiceStub:
        return butt_joint_sequence_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")
    global_ply_nr: ReadWriteProperty[int, int] = grpc_data_property("properties.global_ply_nr")

    primary_plies = define_edge_property_list("properties.primary_plies", PrimaryPly)
    add_primary_ply = define_add_method(
        PrimaryPly,
        attribute_name="primary_plies",
        func_name="add_primary_ply",
        parent_class_name="ButtJointSequence",
        module_name=__module__,
    )

    secondary_plies = define_polymorphic_linked_object_list(
        "properties.secondary_plies", allowed_types_getter=_get_allowed_sequence_types
    )
