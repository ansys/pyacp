from collections.abc import Callable
from typing import Union

from mypy_extensions import Arg, DefaultNamedArg
from typing_extensions import assert_type

from ansys.acp.core import (
    BooleanOperationType,
    BooleanSelectionRule,
    CutOffSelectionRule,
    CylindricalSelectionRule,
    GeometricalSelectionRule,
    LinkedSelectionRule,
    ParallelSelectionRule,
    SphericalSelectionRule,
    TubeSelectionRule,
    VariableOffsetSelectionRule,
)

boolean_rule = BooleanSelectionRule()

# Test that one of the generated 'create_*' methods has the correct type
# signature. This ensures that the type checker understands the
# 'define_create_method' function.

assert_type(
    boolean_rule.add_selection_rule,
    Callable[
        [
            Arg(
                Union[
                    BooleanSelectionRule,
                    CutOffSelectionRule,
                    CylindricalSelectionRule,
                    GeometricalSelectionRule,
                    ParallelSelectionRule,
                    SphericalSelectionRule,
                    TubeSelectionRule,
                    VariableOffsetSelectionRule,
                ],
                "selection_rule",
            ),
            DefaultNamedArg(BooleanOperationType, "operation_type"),
            DefaultNamedArg(bool, "template_rule"),
            DefaultNamedArg(float, "parameter_1"),
            DefaultNamedArg(float, "parameter_2"),
        ],
        LinkedSelectionRule,
    ],
)
