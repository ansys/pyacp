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

from collections.abc import Callable
import typing
from typing import TypeAlias, Union

from typing_extensions import Self

from ansys.api.acp.v0 import linked_selection_rule_pb2

from ._grpc_helpers.edge_property_list import GenericEdgePropertyType
from ._grpc_helpers.polymorphic_from_pb import tree_object_from_resource_path
from ._grpc_helpers.property_helper import _exposed_grpc_property, mark_grpc_properties
from .base import CreatableTreeObject
from .cut_off_selection_rule import CutOffSelectionRule
from .cylindrical_selection_rule import CylindricalSelectionRule
from .enums import (
    BooleanOperationType,
    boolean_operation_type_from_pb,
    boolean_operation_type_to_pb,
)
from .geometrical_selection_rule import GeometricalSelectionRule
from .parallel_selection_rule import ParallelSelectionRule
from .spherical_selection_rule import SphericalSelectionRule
from .tube_selection_rule import TubeSelectionRule
from .variable_offset_selection_rule import VariableOffsetSelectionRule

if typing.TYPE_CHECKING:  # pragma: no cover
    # Since the 'LinkedSelectionRule' class is used by the boolean selection rule,
    # this would cause a circular import at run-time.
    from .boolean_selection_rule import BooleanSelectionRule

_LINKABLE_SELECTION_RULE_TYPES: TypeAlias = Union[
    "BooleanSelectionRule",
    CutOffSelectionRule,
    CylindricalSelectionRule,
    GeometricalSelectionRule,
    ParallelSelectionRule,
    SphericalSelectionRule,
    TubeSelectionRule,
    VariableOffsetSelectionRule,
]


@mark_grpc_properties
class LinkedSelectionRule(GenericEdgePropertyType):
    r"""Defines selection rules linked to a Boolean Selection Rule or Modeling Ply.

    Parameters
    ----------
    selection_rule :
        Link to an existing selection rule.
    operation_type :
        Determines how the selection rule is combined with other selection rules.
    template_rule :
        If ``True``, the selection rule is a template rule. This means the parameter
        values are taken from the ``parameter_1`` and ``parameter_2`` attributes,
        not from the linked selection rule.
    parameter_1 :
        First parameter value of the selection rule. Only applies if ``template_rule``
        is ``True``.
    parameter_2 :
        Second parameter value of the selection rule. Only applies if ``template_rule``
        is ``True``.


    The ``parameter_1`` and ``parameter_2`` attributes determine the values of the
    following parameters, depending on the type of selection rule:

    ====================================== ================================== ===================
    Rule Type                              ``parameter_1``                    ``parameter_2``
    ====================================== ================================== ===================
    :class:`.ParallelSelectionRule`        ``lower_limit``                    ``upper_limit``
    :class:`.CylindricalSelectionRule`     ``radius``                         \-
    :class:`.SphericalSelectionRule`       ``radius``                         \-
    :class:`.TubeSelectionRule`            ``outer_radius``                   ``inner_radius``
    :class:`.GeometricalSelectionRule`     ``in_plane_capture_tolerance``     \-
    :class:`.VariableOffsetSelectionRule`  \-                                 \-
    :class:`.BooleanSelectionRule`         \-                                 \-
    ====================================== ================================== ===================

    Note that :class:`.CutOffSelectionRule` and :class:`.BooleanSelectionRule` objects cannot be linked to
    a Boolean Selection Rule, only to a Modeling Ply..
    """

    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        selection_rule: _LINKABLE_SELECTION_RULE_TYPES,
        *,
        operation_type: BooleanOperationType = BooleanOperationType.INTERSECT,
        template_rule: bool = False,
        parameter_1: float = 0.0,
        parameter_2: float = 0.0,
    ):
        # The '_callback_apply_changes' needs to be set first, otherwise the
        # setter methods will not work. We go through the setters instead of
        # directly setting the attributes to ensure the setter validation is
        # performed.
        self._callback_apply_changes: Callable[[], None] | None = None
        self.selection_rule = selection_rule
        self.operation_type = operation_type
        self.template_rule = template_rule
        self.parameter_1 = parameter_1
        self.parameter_2 = parameter_2

    @_exposed_grpc_property
    def selection_rule(self) -> _LINKABLE_SELECTION_RULE_TYPES:
        """Link to an existing selection rule."""
        return self._selection_rule

    @selection_rule.setter
    def selection_rule(self, value: _LINKABLE_SELECTION_RULE_TYPES) -> None:
        self._selection_rule = value
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def operation_type(self) -> BooleanOperationType:
        """Operation to combine the selection rule with other selection rules."""
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value: BooleanOperationType) -> None:
        # The backend converts the operation automatically; this is confusing
        # in the scripting context where the associated warning may not be visible.
        if isinstance(self._selection_rule, CutOffSelectionRule):
            if value != BooleanOperationType.INTERSECT:
                raise ValueError(
                    "Cannot use a boolean operation other than 'INTERSECT' with a "
                    "CutOffSelectionRule."
                )

        self._operation_type = value
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def template_rule(self) -> bool:
        """Whether the selection rule is a template rule."""
        return self._template_rule

    @template_rule.setter
    def template_rule(self, value: bool) -> None:
        self._template_rule = value
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def parameter_1(self) -> float:
        """First template parameter of the selection rule."""
        return self._parameter_1

    @parameter_1.setter
    def parameter_1(self, value: float) -> None:
        self._parameter_1 = value
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def parameter_2(self) -> float:
        """Second template parameter of the selection rule."""
        return self._parameter_2

    @parameter_2.setter
    def parameter_2(self, value: float) -> None:
        self._parameter_2 = value
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    def _set_callback_apply_changes(self, callback_apply_changes: Callable[[], None]) -> None:
        self._callback_apply_changes = callback_apply_changes

    @classmethod
    def _from_pb_object(
        cls,
        parent_object: CreatableTreeObject,
        message: linked_selection_rule_pb2.LinkedSelectionRule,
        apply_changes: Callable[[], None],
    ) -> Self:
        from .boolean_selection_rule import BooleanSelectionRule

        # Cannot link to objects of the same type as the parent.
        allowed_types_list = [
            ParallelSelectionRule,
            CylindricalSelectionRule,
            SphericalSelectionRule,
            TubeSelectionRule,
            GeometricalSelectionRule,
            VariableOffsetSelectionRule,
        ]
        if not isinstance(parent_object, BooleanSelectionRule):
            allowed_types_list += [CutOffSelectionRule, BooleanSelectionRule]
        allowed_types = tuple(allowed_types_list)

        selection_rule = tree_object_from_resource_path(
            resource_path=message.resource_path, server_wrapper=parent_object._server_wrapper
        )
        if not isinstance(selection_rule, allowed_types):
            raise TypeError(
                f"Expected selection_rule to be of type {allowed_types}, "
                f"got {type(selection_rule)}."
            )
        selection_rule = typing.cast("_LINKABLE_SELECTION_RULE_TYPES", selection_rule)
        new_obj = cls(
            selection_rule=selection_rule,
            operation_type=boolean_operation_type_from_pb(message.operation_type),
            template_rule=message.template_rule,
            parameter_1=message.parameter_1,
            parameter_2=message.parameter_2,
        )
        new_obj._set_callback_apply_changes(apply_changes)
        return new_obj

    def _to_pb_object(self) -> linked_selection_rule_pb2.LinkedSelectionRule:
        return linked_selection_rule_pb2.LinkedSelectionRule(
            resource_path=self.selection_rule._resource_path,
            operation_type=typing.cast(
                typing.Any, boolean_operation_type_to_pb(self.operation_type)
            ),
            template_rule=self.template_rule,
            parameter_1=self.parameter_1,
            parameter_2=self.parameter_2,
        )

    def _check(self) -> bool:
        # Check for empty resource paths
        return bool(self.selection_rule._resource_path.value)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, type(self)):
            return (
                self.selection_rule._resource_path == other.selection_rule._resource_path
                and self.operation_type == other.operation_type
                and self.template_rule == other.template_rule
                and self.parameter_1 == other.parameter_1
                and self.parameter_2 == other.parameter_2
            )

        return False

    def __repr__(self) -> str:
        return (
            f"LinkedSelectionRule(selection_rule={self.selection_rule.__repr__()}, "
            f"operation_type={self.operation_type}, "
            f"template_rule={self.template_rule}, "
            f"parameter_1={self.parameter_1}, "
            f"parameter_2={self.parameter_2})"
        )

    def clone(self) -> LinkedSelectionRule:
        """Create a new unstored LinkedSelectionRule with the same properties."""
        return LinkedSelectionRule(
            selection_rule=self.selection_rule,
            operation_type=self.operation_type,
            template_rule=self.template_rule,
            parameter_1=self.parameter_1,
            parameter_2=self.parameter_2,
        )
