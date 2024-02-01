from __future__ import annotations

from typing import Generic, Protocol, TypeVar

GetValueT_co = TypeVar("GetValueT_co", covariant=True)
SetValueT_contra = TypeVar("SetValueT_contra", contravariant=True)


class ReadOnlyProperty(Generic[GetValueT_co], Protocol):
    """Interface definition for read-only properties.

    The main purpose of this protocol is to improve the type hints for
    properties which are created from helper functions.
    """
    def __get__(self, obj: object, objtype: type | None = None) -> GetValueT_co:
        ...


class ReadWriteProperty(Generic[GetValueT_co, SetValueT_contra], Protocol):
    """Interface definition for read-write properties.

    The main purpose of this protocol is to improve the type hints for
    properties which are created from helper functions.
    """
    def __get__(self, obj: object, objtype: type | None = None) -> GetValueT_co:
        ...

    def __set__(self, obj: object, value: SetValueT_contra) -> None:
        ...
