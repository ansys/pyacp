from contextlib import contextmanager
import os
from typing import Any, Optional, TypeVar
import warnings

IS_PYACP = True

__all__ = ["check_property", "relpath_if_possible"]

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


def relpath_if_possible(path, start=os.path.curdir):
    """Tries to get a relative path, if this fails, returns an absolute path

    calls os.path.relpath which raises a ValueError if path and start are not on the same drive on windows
    in this case we return an absolute path and write a warning to the log
    """
    try:
        return os.path.relpath(path, start)
    except ValueError as e:
        warnings.warn(
            f"Cannot create relative path (path={path}, start={start}): {e}. Using absolute path instead."
        )
        return os.path.abspath(path)


@contextmanager
def suppress_for_pyacp():
    try:
        yield
    except Exception:
        if not IS_PYACP:
            raise
