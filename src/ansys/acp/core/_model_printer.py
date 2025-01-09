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

import os

from ._tree_objects._grpc_helpers.mapping import Mapping
from ._tree_objects.base import TreeObjectBase
from ._tree_objects.model import Model
from ._utils.string_manipulation import replace_underscores_and_capitalize

__all__ = ["Node", "print_model", "get_model_tree"]


class Node:
    """A node in a tree representation of the model.

    Parameters
    ----------
    label:
        Label of the node.
    children:
        Children of the node.
    """

    def __init__(self, label: str, children: list["Node"] | None = None):
        self.label = label
        self.children: list["Node"] = children if children else []

    def __str__(self, level: int | None = 0) -> str:
        assert level is not None
        four_spaces = "    "
        ret = four_spaces * level + self.label + os.linesep
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


def print_model(model: Model, *, hide_empty: bool = True) -> None:
    """Print a tree representation of the model.

    Parameters
    ----------
    model:
        pyACP model
    hide_empty :
        Whether to hide empty collections.

    """
    return print(get_model_tree(model, hide_empty=hide_empty))


def get_model_tree(model: Model, *, hide_empty: bool = True) -> Node:
    """Get a tree representation of the model.

    Returns the root node.

    Parameters
    ----------
    model :
        ACP model.
    hide_empty :
        Whether to hide empty collections.
    """
    return _get_model_tree_impl(obj=model, hide_empty=hide_empty)


def _get_model_tree_impl(obj: TreeObjectBase, *, hide_empty: bool) -> Node:
    obj_node = Node(repr(_name_or_id(obj)))
    for attr_name in obj._GRPC_PROPERTIES:
        try:
            attr = getattr(obj, attr_name)
        except (AttributeError, RuntimeError):
            continue
        if isinstance(attr, Mapping):
            collection_node = Node(replace_underscores_and_capitalize(attr_name))
            obj_node.children.append(collection_node)
            for child_obj in attr.values():
                collection_node.children.append(
                    _get_model_tree_impl(child_obj, hide_empty=hide_empty)
                )
            if hide_empty and not collection_node.children:
                obj_node.children.pop()
    return obj_node


def _name_or_id(obj: TreeObjectBase) -> str:
    try:
        return obj.name
    except AttributeError:
        return obj.id  # type: ignore
