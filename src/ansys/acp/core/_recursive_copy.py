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
from typing import cast

import networkx as nx

from ._tree_objects import LookUpTable1D, LookUpTable1DColumn, LookUpTable3D, LookUpTable3DColumn
from ._tree_objects._grpc_helpers.linked_object_helpers import get_linked_paths
from ._tree_objects._traversal import all_linked_objects, child_objects
from ._tree_objects.base import CreatableTreeObject, TreeObject
from ._typing_helper import StrEnum

__all__ = ["recursive_copy", "LinkedObjectHandling"]


@dataclass
class _WalkTreeOptions:
    include_children: bool
    include_linked_objects: bool


def _build_dependency_graph(
    *, source_objects: Iterable[CreatableTreeObject], options: _WalkTreeOptions
) -> nx.DiGraph:
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
        for child_object in child_objects(tree_object):
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
        for linked_object in all_linked_objects(tree_object):
            assert isinstance(linked_object, CreatableTreeObject)
            graph.add_edge(tree_object, linked_object)
            _build_dependency_graph_impl(
                tree_object=linked_object,
                graph=graph,
                visited_objects=visited_objects,
                options=options,
            )


class LinkedObjectHandling(StrEnum):
    """Defines options for handling linked objects when copying a tree of ACP objects."""

    COPY = "copy"
    KEEP = "keep"
    DISCARD = "discard"


def recursive_copy(
    *,
    source_objects: Iterable[CreatableTreeObject],
    parent_mapping: dict[TreeObject, TreeObject],
    linked_object_handling: LinkedObjectHandling | str = "copy",
) -> dict[CreatableTreeObject, CreatableTreeObject]:
    """Recursively copy a tree of ACP objects.

    This function copies a tree of ACP objects, starting from the given source objects.
    The copied tree includes all child objects. Linked objects can optionally be included,
    controlled by the ``linked_object_handling`` argument.

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
    linked_object_handling :
        Defines how linked objects are handled. The following options are available:

        - ``"copy"``: Copy the linked objects, and replace the links.
        - ``"keep"``: Keep linking to the original objects, and do not
          copy them (unless they are otherwise included in the tree).
        - ``"discard"``: Discard object links.

        Note that when copying objects between two models, only the ``"copy"`` and
        ``"discard"`` options are valid. If you wish to use links to existing objects,
        the ``"copy"`` option can be used, specifying how links should be replaced in
        the ``parent_mapping`` argument.

    Returns
    -------
    :
        A mapping of the newly created objects. The keys are the original objects,
        and the values are the new objects.

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
    linked_object_handling = LinkedObjectHandling(linked_object_handling)

    options = _WalkTreeOptions(
        include_children=True,
        include_linked_objects=linked_object_handling == LinkedObjectHandling.COPY,
    )
    # Build up a graph of the objects to clone. Graph edges represent a dependency:
    # - from child to parent node
    # - from source to target of a link
    graph = _build_dependency_graph(source_objects=source_objects, options=options)

    replacement_mapping = dict(parent_mapping)
    # keep track of the new resource paths for easy replacement of linked objects
    resource_path_replacement_mapping = {
        obj._resource_path.value: new_obj._resource_path.value
        for obj, new_obj in parent_mapping.items()
    }

    # The 'topological_sort' of the graph ensures that each node is only handled
    # once its parent and linked objects are stored.
    for tree_object in reversed(list(nx.topological_sort(graph))):
        if tree_object in replacement_mapping:
            # Skip nodes which are already copied (e.g. coming from the parent_mapping)
            continue

        if isinstance(tree_object, (LookUpTable1DColumn, LookUpTable3DColumn)):
            # handled explicitly while copying the LookUpTable object
            if tree_object.name == "Location":
                continue

        new_tree_object = tree_object.clone(
            unlink=linked_object_handling == LinkedObjectHandling.DISCARD
        )

        # If the linked objects are also copied, replace them with the new objects.
        # Otherwise, we can directly store the new object.
        if linked_object_handling == LinkedObjectHandling.COPY:
            for linked_resource_path in get_linked_paths(new_tree_object._pb_object.properties):
                # TODO: handle case when linked objects are not (yet) supported by PyACP or
                # the server, but are included in the API.
                linked_resource_path.value = resource_path_replacement_mapping[
                    linked_resource_path.value
                ]

        try:
            new_parent = replacement_mapping[tree_object.parent]
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

        replacement_mapping[tree_object] = new_tree_object
        resource_path_replacement_mapping[tree_object._resource_path.value] = (
            new_tree_object._resource_path.value
        )

    # Return a mapping of only the newly created objects
    # (key: old object, value: new object).
    # The type cast is necessary because the 'parent_mapping' could also
    # include non-creatable objects, but the filter ensures that only
    # creatable objects are returned.
    return {
        cast(CreatableTreeObject, old_obj): cast(CreatableTreeObject, new_obj)
        for old_obj, new_obj in replacement_mapping.items()
        if old_obj is not new_obj
    }
