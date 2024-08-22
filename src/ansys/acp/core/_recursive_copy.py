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

from collections.abc import Iterable
from dataclasses import dataclass

import networkx as nx

from ._tree_objects._traversal import (
    all_linked_objects,
    child_objects,
    directly_linked_objects,
    edge_property_lists,
    edge_property_targets,
    linked_object_lists,
)
from ._tree_objects.base import CreatableTreeObject, TreeObject

__all__ = ["recursive_copy"]


@dataclass
class _WalkTreeOptions:
    include_children: bool
    include_linked_objects: bool


def _build_dependency_graph(
    *, source_objects: Iterable[CreatableTreeObject], options: _WalkTreeOptions
) -> tuple[nx.DiGraph, dict[str, CreatableTreeObject]]:
    graph = nx.DiGraph()
    visited_objects: dict[str, CreatableTreeObject] = dict()
    for tree_object in source_objects:
        _build_dependency_graph_impl(
            tree_object=tree_object, graph=graph, visited_objects=visited_objects, options=options
        )
    return graph, visited_objects


def _build_dependency_graph_impl(
    *,
    tree_object: CreatableTreeObject,
    graph: nx.DiGraph,
    visited_objects: dict[str, CreatableTreeObject],
    options: _WalkTreeOptions,
) -> None:
    key = tree_object._resource_path.value
    if key in visited_objects:
        return
    visited_objects[key] = tree_object
    graph.add_node(key)

    if options.include_children:
        for child_object in child_objects(tree_object):
            if not isinstance(child_object, CreatableTreeObject):
                continue
            graph.add_edge(child_object._resource_path.value, key)
            _build_dependency_graph_impl(
                tree_object=child_object,
                graph=graph,
                visited_objects=visited_objects,
                options=options,
            )
    if options.include_linked_objects:
        for linked_object in all_linked_objects(tree_object):
            assert isinstance(linked_object, CreatableTreeObject)
            graph.add_edge(tree_object._resource_path.value, linked_object._resource_path.value)
            _build_dependency_graph_impl(
                tree_object=linked_object,
                graph=graph,
                visited_objects=visited_objects,
                options=options,
            )


def recursive_copy(
    *,
    source_objects: Iterable[CreatableTreeObject],
    parent_mapping: Iterable[tuple[TreeObject, TreeObject]],
    include_children: bool = True,
    include_linked_objects: bool = True,
) -> list[CreatableTreeObject]:
    """Recursively copy a tree of ACP objects.

    This function copies a tree of ACP objects, starting from the given source objects.
    You can specify whether to include children (for example the Modeling Plies in a
    Modeling Group) and linked objects (for example the Rosettes linked to an Oriented
    Selection Set) in the copy.

    To specify where the new objects should be stored, you must provide a list of tuples
    in the ``parent_mapping`` argument. Each tuple contains the original parent object
    as the first element and the new parent object as the second element.
    Note that this mapping may need to contain parent objects that are not direct parents
    of the source objects, if another branch of the tree is included via linked objects.

    The function returns a list of newly created objects.

    .. note::

        Only attributes supported by PyACP are copied to the new objects.

    Parameters
    ----------
    source_objects :
        The starting point of the tree to copy.
    parent_mapping :
        A list of tuples defining where the new objects are stored. Each tuple contains
        the original parent object as the first element and the new parent object as the
        second element.
    include_children :
        Whether to include child objects when creating the tree to copy.
    include_linked_objects :
        Whether to include linked objects when creating the tree to copy.

    Returns
    -------
    :
        A list of newly created objects.

    Examples
    --------
    To copy all Modeling Groups and associated definitions from one model to another,
    you can use the following code:

    .. code-block:: python

        import ansys.acp.core as pyacp

        model1 = ...  # loaded in some way
        model2 = ...  # loaded in some way

        pyacp.recursive_copy(
            source_objects=model1.modeling_groups.values(),
            parent_mapping=[(model1, model2)],
        )

    """
    options = _WalkTreeOptions(
        include_children=include_children, include_linked_objects=include_linked_objects
    )
    graph, visited_objects = _build_dependency_graph(source_objects=source_objects, options=options)

    replacement_mapping = {
        parent._resource_path.value: new_parent for parent, new_parent in parent_mapping
    }
    new_objects: list[CreatableTreeObject] = []

    for node in reversed(list(nx.topological_sort(graph))):
        if node in replacement_mapping:
            # Skip nodes which are already copied (e.g. coming from the parent_mapping)
            continue
        tree_object = visited_objects[node]

        new_tree_object = tree_object.clone()
        for attr_name, linked_object in directly_linked_objects(tree_object):
            new_linked_object = replacement_mapping[linked_object._resource_path.value]
            setattr(new_tree_object, attr_name, new_linked_object)
        for attr_name, linked_object_list in linked_object_lists(tree_object):
            new_linked_objects = [
                replacement_mapping[linked_object._resource_path.value]
                for linked_object in linked_object_list
            ]
            setattr(new_tree_object, attr_name, new_linked_objects)

        # clear edge property lists, then re-create them once the new object is stored
        for attr_name, _ in edge_property_lists(tree_object):
            setattr(new_tree_object, attr_name, [])

        parent_rp = tree_object._resource_path.value.rsplit("/", 2)[0]
        new_parent = replacement_mapping[parent_rp]
        new_tree_object.store(parent=new_parent)

        for attr_name, edge_property_list in edge_property_lists(tree_object):
            new_edge_property_list = [edge.clone() for edge in edge_property_list]
            for edge, edge_prop_name, edge_target in edge_property_targets(new_edge_property_list):
                new_edge_target = replacement_mapping[edge_target._resource_path.value]
                setattr(edge, edge_prop_name, new_edge_target)
            setattr(new_tree_object, attr_name, new_edge_property_list)

        replacement_mapping[node] = new_tree_object
        new_objects.append(new_tree_object)

    return new_objects
