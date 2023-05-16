from typing import Any, Optional, TypeVar

__all__ = ["check_property"]

T = TypeVar("T")


def check_property(obj: Any, *, name: str, value: T, set_value: Optional[T] = None):
    assert hasattr(obj, name), f"Object '{obj}' has no property named '{name}'"
    assert (
        getattr(obj, name) == value
    ), f"Test of property '{name}' failed! value '{getattr( obj, name )}' instead of '{value}'."
    if set_value is not None:
        setattr(obj, name, set_value)
        assert (
            getattr(obj, name) == set_value
        ), f"Setter of property '{name}' failed! value '{getattr(obj, name)}' instead of '{value}'."
