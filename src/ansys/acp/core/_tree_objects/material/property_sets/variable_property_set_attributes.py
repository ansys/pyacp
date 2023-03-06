from __future__ import annotations

from dataclasses import dataclass

__all__ = (
    "InterpolationOptions",
    "FieldVariable",
)


@dataclass(frozen=True)
class InterpolationOptions:
    """Defines the interpolation options for variable materials."""

    algorithm: str
    cached: bool
    normalized: bool


@dataclass(frozen=True)
class FieldVariable:
    """Defines field variables for variable material properties."""

    name: str
    values: tuple[float, ...]
    default: float
    lower_limit: float
    upper_limit: float
