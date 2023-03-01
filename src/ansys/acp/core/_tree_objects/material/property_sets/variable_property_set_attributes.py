from __future__ import annotations

from dataclasses import dataclass

__all__ = (
    "InterpolationOptions",
    "FieldVariable",
)


@dataclass(frozen=True)
class InterpolationOptions:
    algorithm: str
    cached: bool
    normalized: bool


@dataclass(frozen=True)
class FieldVariable:
    name: str
    values: tuple[float, ...]
    default: float
    lower_limit: float
    upper_limit: float
