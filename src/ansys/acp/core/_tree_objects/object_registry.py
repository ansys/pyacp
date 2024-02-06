from typing import TypeVar

from .base import TreeObjectBase

object_registry: dict[str, type[TreeObjectBase]] = {}

T = TypeVar("T", bound=type[TreeObjectBase])


def register(cls: T) -> T:
    """Class decorator for ACP tree objects.

    Registers the tree object, enabling it to be instantiated polymorphically
    from a resource path.
    """
    object_registry[cls._COLLECTION_LABEL] = cls
    return cls
