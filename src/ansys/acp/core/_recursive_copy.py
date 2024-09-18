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

from ._tree_objects import LookUpTable1D, LookUpTable1DColumn, LookUpTable3D, LookUpTable3DColumn
from ._tree_objects._grpc_helpers.linked_object_helpers import get_linked_paths
from ._tree_objects._traversal import all_linked_objects, child_objects
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
            graph.add_edge(key, linked_object._resource_path.value)
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

    The ``parent_mapping`` argument can also include objects which are part of the
    ``source_objects`` list. In this case, the function will not create a new object for
    the parent, but will use the existing object instead.

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

    To copy all definitions from one model to another, you can use the following code:

    .. code-block:: python

        import ansys.acp.core as pyacp

        model1 = ...  # loaded in some way
        model2 = ...  # loaded in some way

        pyacp.recursive_copy(
            source_objects=[model1],
            parent_mapping=[(model1, model2)],
        )
    """
    options = _WalkTreeOptions(
        include_children=include_children, include_linked_objects=include_linked_objects
    )
    # Build up a graph of the objects to clone. Graph edges represent a dependency:
    # - from child to parent node
    # - from source to target of a link
    graph, visited_objects = _build_dependency_graph(source_objects=source_objects, options=options)

    replacement_mapping = {
        parent._resource_path.value: new_parent for parent, new_parent in parent_mapping
    }
    new_objects: list[CreatableTreeObject] = []

    # The 'topological_sort' of the graph ensures that each node is only handled
    # once its parent and linked objects are stored.
    for node in reversed(list(nx.topological_sort(graph))):
        if node in replacement_mapping:
            # Skip nodes which are already copied (e.g. coming from the parent_mapping)
            continue
        tree_object = visited_objects[node]

        if isinstance(tree_object, (LookUpTable1DColumn, LookUpTable3DColumn)):
            # handled explicitly while copying the LookUpTable object
            if tree_object.name == "Location":
                continue

        new_tree_object = tree_object.clone()

        # If the linked objects are also copied, replace them with the new objects.
        # Otherwise, we can directly store the new object.
        if include_linked_objects:
            for linked_resource_path in get_linked_paths(new_tree_object._pb_object.properties):
                # TODO: handle case when linked objects are not (yet) supported by PyACP or
                # the server, but are included in the API.
                linked_resource_path.value = replacement_mapping[
                    linked_resource_path.value
                ]._resource_path.value

        parent_rp = tree_object._resource_path.value.rsplit("/", 2)[0]
        try:
            new_parent = replacement_mapping[parent_rp]
        except KeyError as exc:
            raise KeyError(
                f"Parent object not found in 'parent_mapping' for object '{tree_object!r}'."
            ) from exc

        new_tree_object.store(parent=new_parent)

        # NOTE: if there are more type-specific fixes needed, we may want
        # to implement a more generic way to handle these.
        # Explicit fix for LookUpTable, since the Location column needs to
        # be set correctly s.t. other columns may be stored.
        if isinstance(new_tree_object, (LookUpTable1D, LookUpTable3D)):
            assert isinstance(tree_object, (LookUpTable1D, LookUpTable3D))
            new_tree_object.columns["Location"].data = tree_object.columns["Location"].data

        replacement_mapping[node] = new_tree_object
        new_objects.append(new_tree_object)

    return new_objects
