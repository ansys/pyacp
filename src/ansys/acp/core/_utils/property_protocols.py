from __future__ import annotations

from typing import Generic, Protocol, TypeVar

GetValueT_co = TypeVar("GetValueT_co", covariant=True)
SetValueT_contra = TypeVar("SetValueT_contra", contravariant=True)


class ReadOnlyProperty(Generic[GetValueT_co], Protocol):
    def __get__(self, obj: object, objtype: type | None = None) -> GetValueT_co:
        ...


class ReadWriteProperty(Generic[GetValueT_co, SetValueT_contra], Protocol):
    def __get__(self, obj: object, objtype: type | None = None) -> GetValueT_co:
        ...

    def __set__(self, obj: object, value: SetValueT_contra) -> None:
        ...
