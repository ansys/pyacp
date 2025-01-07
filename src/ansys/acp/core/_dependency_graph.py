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

from collections.abc import Iterable, Iterator
from dataclasses import dataclass

import networkx as nx

from ._tree_objects._grpc_helpers.linked_object_helpers import get_linked_paths
from ._tree_objects._grpc_helpers.mapping import Mapping
from ._tree_objects._grpc_helpers.polymorphic_from_pb import tree_object_from_resource_path
from ._tree_objects.base import CreatableTreeObject, TreeObject


@dataclass
class _WalkTreeOptions:
    include_children: bool
    include_linked_objects: bool


def _build_dependency_graph(
    *, source_objects: Iterable[CreatableTreeObject], options: _WalkTreeOptions
) -> nx.DiGraph:
    """Build a dependency graph of the given objects."""
    graph = nx.DiGraph()

    # We need to manually keep track of which objects have been visited,
    # since the node may also be created when being linked to.
    visited_objects: set[CreatableTreeObject] = set()
    for tree_object in source_objects:
        _build_dependency_graph_impl(
            tree_object=tree_object, graph=graph, visited_objects=visited_objects, options=options
        )
    return graph


def _build_dependency_graph_impl(
    *,
    tree_object: CreatableTreeObject,
    graph: nx.DiGraph,
    visited_objects: set[CreatableTreeObject],
    options: _WalkTreeOptions,
) -> None:

    if tree_object in visited_objects:
        return

    visited_objects.add(tree_object)
    graph.add_node(tree_object)

    if options.include_children:
        for child_object in _yield_child_objects(tree_object):
            if not isinstance(child_object, CreatableTreeObject):
                continue
            graph.add_edge(child_object, tree_object)
            _build_dependency_graph_impl(
                tree_object=child_object,
                graph=graph,
                visited_objects=visited_objects,
                options=options,
            )
    if options.include_linked_objects:
        for linked_object in _yield_linked_objects(tree_object):
            graph.add_edge(tree_object, linked_object)
            _build_dependency_graph_impl(
                tree_object=linked_object,
                graph=graph,
                visited_objects=visited_objects,
                options=options,
            )


def _yield_child_objects(tree_object: TreeObject) -> Iterator[TreeObject]:
    for attr_name in tree_object._GRPC_PROPERTIES:
        try:
            attr = getattr(tree_object, attr_name)
        except (AttributeError, RuntimeError):
            continue
        if isinstance(attr, Mapping):
            yield from attr.values()


def _yield_linked_objects(tree_object: TreeObject) -> Iterator[CreatableTreeObject]:
    for linked_path in get_linked_paths(tree_object._pb_object.properties):
        linked_object = tree_object_from_resource_path(
            linked_path, server_wrapper=tree_object._server_wrapper
        )
        assert isinstance(linked_object, CreatableTreeObject)
        yield linked_object
