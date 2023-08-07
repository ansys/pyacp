from __future__ import annotations

import typing
from typing import Callable, Union

from typing_extensions import Self

from ansys.api.acp.v0 import linked_selection_rule_pb2

from ._grpc_helpers.edge_property_list import GenericEdgePropertyType
from ._grpc_helpers.polymorphic_from_pb import tree_object_from_resource_path
from .base import CreatableTreeObject
from .cylindrical_selection_rule import CylindricalSelectionRule
from .enums import (
    BooleanOperationType,
    boolean_operation_type_from_pb,
    boolean_operation_type_to_pb,
)
from .parallel_selection_rule import ParallelSelectionRule
from .spherical_selection_rule import SphericalSelectionRule
from .tube_selection_rule import TubeSelectionRule

_LINKABLE_SELECTION_RULE_TYPES = Union[
    ParallelSelectionRule,
    CylindricalSelectionRule,
    SphericalSelectionRule,
    TubeSelectionRule,
]


class LinkedSelectionRule(GenericEdgePropertyType):
    """Defines selection rules linked to a Boolean Selection Rule or Modeling Ply.

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
    """

    def __init__(
        self,
        selection_rule: _LINKABLE_SELECTION_RULE_TYPES,
        operation_type: BooleanOperationType = BooleanOperationType.INTERSECT,
        template_rule: bool = False,
        parameter_1: float = 0.0,
        parameter_2: float = 0.0,
    ):
        self._selection_rule = selection_rule
        self._operation_type = operation_type
        self._template_rule = template_rule
        self._parameter_1 = parameter_1
        self._parameter_2 = parameter_2
        self._callback_apply_changes: Callable[[], None] | None = None

    @property
    def selection_rule(self) -> _LINKABLE_SELECTION_RULE_TYPES:
        return self._selection_rule

    @selection_rule.setter
    def selection_rule(self, value: _LINKABLE_SELECTION_RULE_TYPES) -> None:
        self._selection_rule = value
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @property
    def operation_type(self) -> BooleanOperationType:
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value: BooleanOperationType) -> None:
        self._operation_type = value
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @property
    def template_rule(self) -> bool:
        return self._template_rule

    @template_rule.setter
    def template_rule(self, value: bool) -> None:
        self._template_rule = value
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @property
    def parameter_1(self) -> float:
        return self._parameter_1

    @parameter_1.setter
    def parameter_1(self, value: float) -> None:
        self._parameter_1 = value
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @property
    def parameter_2(self) -> float:
        return self._parameter_2

    @parameter_2.setter
    def parameter_2(self, value: float) -> None:
        self._parameter_2 = value
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @classmethod
    def _from_pb_object(
        cls,
        parent_object: CreatableTreeObject,
        message: linked_selection_rule_pb2.LinkedSelectionRule,
        apply_changes: Callable[[], None],
    ) -> Self:
        selection_rule = tree_object_from_resource_path(
            resource_path=message.resource_path, channel=parent_object._channel
        )
        allowed_types = typing.get_args(_LINKABLE_SELECTION_RULE_TYPES)
        if not isinstance(selection_rule, allowed_types):
            raise TypeError(
                f"Expected selection_rule to be of type {allowed_types}, "
                f"got {type(selection_rule)}."
            )
        selection_rule = typing.cast(_LINKABLE_SELECTION_RULE_TYPES, selection_rule)
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
            operation_type=boolean_operation_type_to_pb(self.operation_type),
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
