from collections.abc import Callable

from mypy_extensions import DefaultNamedArg
from typing_extensions import assert_type

from ansys.acp.core import CADGeometry, Model

model = Model()

# Test that one of the generated 'create_*' methods has the correct type
# signature. This ensures that the type checker understands the
# 'define_create_method' function.

assert_type(
    model.create_cad_geometry,
    Callable[
        [
            DefaultNamedArg(str, "name"),
            DefaultNamedArg(str, "external_path"),
            DefaultNamedArg(float, "scale_factor"),
            DefaultNamedArg(bool, "use_default_precision"),
            DefaultNamedArg(float, "precision"),
            DefaultNamedArg(bool, "use_default_offset"),
            DefaultNamedArg(float, "offset"),
        ],
        CADGeometry,
    ],
)
