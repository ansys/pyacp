# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

import typing
from typing import Protocol

from typing_extensions import Self

from ansys.api.acp.v0.base_pb2 import ResourcePath

if typing.TYPE_CHECKING:  # pragma: no cover
    from ..base import ServerWrapper

__all__ = ["CreatableFromResourcePath", "tree_object_from_resource_path"]


class CreatableFromResourcePath(Protocol):
    """Interface for objects that can be created from a resource path."""

    @classmethod
    def _from_resource_path(
        cls, resource_path: ResourcePath, server_wrapper: ServerWrapper
    ) -> Self: ...


def tree_object_from_resource_path(
    resource_path: ResourcePath,
    server_wrapper: ServerWrapper,
    allowed_types: tuple[type[CreatableFromResourcePath], ...] | None = None,
) -> CreatableFromResourcePath | None:
    """Instantiate a tree object from its resource path.

    Parameters
    ----------
    resource_path :
        Resource path of the object.
    server_wrapper :
        Representation of the ACP server.
    allowed_types :
        Allowed types of the object. If None, all registered types are allowed.
    """
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
    return resource_class._from_resource_path(resource_path, server_wrapper=server_wrapper)
