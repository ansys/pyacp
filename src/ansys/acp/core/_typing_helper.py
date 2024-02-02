"""Helpers for defining type annotations."""
import os
from typing import Union

__all__ = ["PATH", "StrEnum"]

PATH = Union[str, os.PathLike[str]]

try:
    from enum import StrEnum  # type: ignore
except ImportError:
    # For Python 3.10 and below, emulate the behavior of StrEnum by
    # inheriting from str and enum.Enum.
    # Note that this does *not* work on Python 3.11+, since the default
    # Enum format method has changed and will not return the value of
    # the enum member.
    import enum

    class StrEnum(str, enum.Enum):  # type: ignore
        pass
