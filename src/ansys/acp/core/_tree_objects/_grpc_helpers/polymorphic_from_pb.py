from __future__ import annotations

from typing import Protocol

import grpc
from typing_extensions import Self

from ansys.api.acp.v0.base_pb2 import ResourcePath

__all__ = ["CreatableFromResourcePath", "tree_object_from_resource_path"]


class CreatableFromResourcePath(Protocol):
    @classmethod
    def _from_resource_path(cls, resource_path: ResourcePath, channel: grpc.Channel) -> Self:
        ...


def tree_object_from_resource_path(
    resource_path: ResourcePath,
    channel: grpc.Channel,
    allowed_types: tuple[type[CreatableFromResourcePath], ...] | None = None,
) -> CreatableFromResourcePath | None:
    #  Import here to avoid circular references. Cannot use the registry before
    #  all the object have been imported.
    from ..object_registry import object_registry

    # Resource path represents an object that is not set as an empty string
    # For instance fabric.material = None
    if resource_path.value == "":
        return None

    collection_name = resource_path.value.split("/")[::2][-1]
    resource_class: type[CreatableFromResourcePath] = object_registry[collection_name]
    if allowed_types is not None:
        if not issubclass(resource_class, allowed_types):
            raise TypeError(
                f"Resource path {resource_path.value} does not point to a valid "
                f"object type. Allowed types: {allowed_types}"
            )
    return resource_class._from_resource_path(resource_path, channel)