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

from collections.abc import Callable, Iterable, Sequence
from typing import TYPE_CHECKING, Any, Union, cast

from typing_extensions import Self

from ansys.api.acp.v0 import butt_joint_sequence_pb2, butt_joint_sequence_pb2_grpc

from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.edge_property_list import (
    GenericEdgePropertyType,
    define_add_method,
    define_edge_property_list,
)
from ._grpc_helpers.linked_object_list import define_polymorphic_linked_object_list
from ._grpc_helpers.polymorphic_from_pb import tree_object_from_resource_path
from ._grpc_helpers.property_helper import (
    _exposed_grpc_property,
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .modeling_ply import ModelingPly
from .object_registry import register

if TYPE_CHECKING:  # pragma: no cover
    # Creates a circular import if imported at the top-level, since the ButtJointSequence
    # is a direct child of the ModelingGroup.
    from .modeling_group import ModelingGroup

__all__ = ["ButtJointSequence", "PrimaryPly"]


@mark_grpc_properties
class PrimaryPly(GenericEdgePropertyType):
    """Defines a primary ply of a butt joint sequence.

    Parameters
    ----------
    sequence :
        Modeling group or modeling ply defining the primary ply.
    level :
        Level of the primary ply. Plies with a higher level inherit the thickness
        from adjacent plies with a lower level.

    """

    _SUPPORTED_SINCE = "25.1"

    def __init__(self, sequence: ModelingGroup | ModelingPly, level: int = 1):
        self._callback_apply_changes: Callable[[], None] | None = None
        self.sequence = sequence
        self.level = level

    @_exposed_grpc_property
    def sequence(self) -> ModelingGroup | ModelingPly:
        """Linked sequence."""
        return self._sequence

    @sequence.setter
    def sequence(self, value: ModelingGroup | ModelingPly) -> None:
        from .modeling_group import ModelingGroup

        if not isinstance(value, (ModelingGroup, ModelingPly)):
            raise TypeError(f"Expected a ModelingGroup or ModelingPly, got {type(value)}")
        self._sequence = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def level(self) -> int:
        """Level of the primary ply.

        Plies with a higher level inherit the thickness from adjacent plies with a lower level.
        """
        return self._level

    @level.setter
    def level(self, value: int) -> None:
        self._level = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    def _set_callback_apply_changes(self, callback_apply_changes: Callable[[], None]) -> None:
        self._callback_apply_changes = callback_apply_changes

    @classmethod
    def _from_pb_object(
        cls,
        parent_object: CreatableTreeObject,
        message: butt_joint_sequence_pb2.PrimaryPly,
        apply_changes: Callable[[], None],
    ) -> Self:
        from .modeling_group import ModelingGroup  # imported here to avoid circular import

        new_obj = cls(
            sequence=cast(
                Union["ModelingGroup", ModelingPly],
                tree_object_from_resource_path(
                    message.sequence,
                    server_wrapper=parent_object._server_wrapper,
                    allowed_types=(ModelingGroup, ModelingPly),
                ),
            ),
            level=message.level,
        )
        new_obj._set_callback_apply_changes(apply_changes)
        return new_obj

    def _to_pb_object(self) -> butt_joint_sequence_pb2.PrimaryPly:
        return butt_joint_sequence_pb2.PrimaryPly(
            sequence=self.sequence._resource_path, level=self.level
        )

    def _check(self) -> bool:
        # Check for empty resource paths
        return bool(self.sequence._resource_path.value)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return (
                self.sequence._resource_path == other.sequence._resource_path
                and self.level == other.level
            )

        return False

    def __repr__(self) -> str:
        return f"PrimaryPly(sequence={self.sequence.__repr__()}, level={self.level})"

    def clone(self) -> Self:
        """Create a new unstored PrimaryPly with the same properties."""
        return type(self)(sequence=self.sequence, level=self.level)


def _get_allowed_secondary_ply_types() -> tuple[type, ...]:
    from .modeling_group import ModelingGroup

    return (ModelingGroup, ModelingPly)


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
        "properties.secondary_plies", allowed_types_getter=_get_allowed_secondary_ply_types
    )
