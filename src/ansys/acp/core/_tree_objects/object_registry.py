from .base import TreeObjectBase

object_registry: dict[str, type[TreeObjectBase]] = {}


def register(cls: type[TreeObjectBase]) -> type[TreeObjectBase]:
    object_registry[cls._COLLECTION_LABEL] = cls
    return cls
