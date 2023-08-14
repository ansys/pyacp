from typing import Dict, Type

from .base import TreeObjectBase

object_registry: Dict[str, Type[TreeObjectBase]] = {}


def register(cls: Type[TreeObjectBase]) -> Type[TreeObjectBase]:
    object_registry[cls._COLLECTION_LABEL] = cls
    return cls
