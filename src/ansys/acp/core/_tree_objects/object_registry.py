from typing import Dict, Type

from .base import TreeObject

object_registry: Dict[str, Type[TreeObject]] = {}


def register(cls: Type[TreeObject]) -> Type[TreeObject]:
    object_registry[cls.COLLECTION_LABEL] = cls
    return cls
