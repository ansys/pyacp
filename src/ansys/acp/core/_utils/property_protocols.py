from typing import Generic, Optional, Protocol, TypeVar

ValueT = TypeVar("ValueT", covariant=True)
ParentT = TypeVar("ParentT")


class ReadOnlyProperty(Generic[ValueT], Protocol):
    def __get__(self, obj: ParentT, objtype: Optional[type[ParentT]] = None) -> ValueT:
        ...
