# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
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

from collections.abc import Iterator
from typing import TypeVar

from ._grpc_helpers.edge_property_list import EdgePropertyList, GenericEdgePropertyType
from ._grpc_helpers.linked_object_list import LinkedObjectList
from ._grpc_helpers.mapping import Mapping
from .base import CreatableTreeObject, TreeObjectBase

__all__ = [
    "all_linked_objects",
    "child_objects",
    "directly_linked_objects",
    "linked_object_lists",
    "edge_property_lists",
    "edge_property_targets",
]


def all_linked_objects(tree_object: TreeObjectBase) -> Iterator[TreeObjectBase]:
    """Yield all objects linked to the given tree object."""
    for _, linked_object in directly_linked_objects(tree_object):
        yield linked_object
    for _, linked_object_list in linked_object_lists(tree_object):
        yield from linked_object_list
    for _, edge_property_list in edge_property_lists(tree_object):
        for _, _, linked_object in edge_property_targets(edge_property_list):
            yield linked_object


def child_objects(tree_object: TreeObjectBase) -> Iterator[TreeObjectBase]:
    """Yield all child objects of the given tree object."""
    for _, mapping in _yield_attrs_of_type(tree_object, Mapping):
        yield from mapping.values()


def directly_linked_objects(tree_object: TreeObjectBase) -> Iterator[tuple[str, TreeObjectBase]]:
    """Yield the attribute name and linked object for all directly linked objects."""
    yield from _yield_attrs_of_type(tree_object, TreeObjectBase)


def linked_object_lists(
    tree_object: TreeObjectBase,
) -> Iterator[tuple[str, LinkedObjectList[CreatableTreeObject]]]:
    """Yield the attribute name and linked object list for all linked object lists."""
    yield from _yield_attrs_of_type(tree_object, LinkedObjectList)


def edge_property_lists(
    tree_object: TreeObjectBase,
) -> Iterator[tuple[str, EdgePropertyList[GenericEdgePropertyType]]]:
    """Yield the attribute name and edge property list for all edge property lists."""
    yield from _yield_attrs_of_type(tree_object, EdgePropertyList)


def edge_property_targets(
    edge_property_list: EdgePropertyList[GenericEdgePropertyType],
) -> Iterator[tuple[GenericEdgePropertyType, str, TreeObjectBase]]:
    """Yield the edge property, edge property name, and linked object for all edge properties."""
    for edge in edge_property_list:
        for edge_prop_name in edge._GRPC_PROPERTIES:
            try:
                edge_prop = getattr(edge, edge_prop_name)
            except (AttributeError, RuntimeError):
                continue
            if isinstance(edge_prop, TreeObjectBase):
                yield (edge, edge_prop_name, edge_prop)


T = TypeVar("T")


def _yield_attrs_of_type(tree_object: TreeObjectBase, type_: type[T]) -> Iterator[tuple[str, T]]:
    for attr_name in tree_object._GRPC_PROPERTIES:
        try:
            attr = getattr(tree_object, attr_name)
        except (AttributeError, RuntimeError):
            continue
        if isinstance(attr, type_):
            yield (attr_name, attr)
