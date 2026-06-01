# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Helper functions to show the structure of the ACP feature tree."""

from .._model_printer import Node
from .._tree_objects._grpc_helpers.property_helper import _exposed_grpc_mapping_property
from .._tree_objects.base import TreeObjectBase
from .._tree_objects.model import Model

__all__ = [
    "print_feature_tree",
    "get_feature_tree",
]


def print_feature_tree(show_lines: bool = False) -> None:
    """Print a tree representation of the PyACP features.

    Parameters
    ----------
    show_lines :
        Whether to show lines connecting the nodes.

    """
    print(get_feature_tree().to_string(show_lines=show_lines))


def get_feature_tree() -> Node:
    """Get a tree representation of the PyACP features."""
    return _get_feature_tree_impl(Model, False)


def _get_feature_tree_impl(root_cls: type[TreeObjectBase], read_only: bool) -> Node:
    label = root_cls.__name__
    if read_only:
        label += " (read-only)"
    grpc_properties = [getattr(root_cls, attr_name) for attr_name in root_cls._GRPC_PROPERTIES]
    return Node(
        label=label,
        children=[
            _get_feature_tree_impl(prop._value_type, read_only=prop._read_only)  # type: ignore
            for prop in grpc_properties
            if isinstance(prop, _exposed_grpc_mapping_property)
        ],
    )
