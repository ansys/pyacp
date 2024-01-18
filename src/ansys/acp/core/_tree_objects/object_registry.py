from typing import TypeVar

from .base import TreeObjectBase

object_registry: dict[str, type[TreeObjectBase]] = {}

T = TypeVar("T", bound=type[TreeObjectBase])


def register(cls: T) -> T:
    object_registry[cls._COLLECTION_LABEL] = cls
    return cls
