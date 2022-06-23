from typing import Type

from .base import TreeObject

object_registry = {}


def register(cls: Type[TreeObject]) -> Type[TreeObject]:
    object_registry[cls.COLLECTION_LABEL] = cls
    return cls
