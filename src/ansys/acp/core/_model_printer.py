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

import os
from typing import Optional

from ._tree_objects.model import Model
from ._utils.visualization import _replace_underscores_and_capitalize

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

    def __init__(self, label: str, children: Optional[list["Node"]] = None):
        self.label = label
        self.children: list["Node"] = children if children else []

    def __str__(self, level: Optional[int] = 0) -> str:
        assert level is not None
        four_spaces = "    "
        ret = four_spaces * level + self.label + os.linesep
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


def _add_tree_part(
    tree: Node,
    container_name: str,
    model: Model,
) -> None:
    items = list(getattr(model, container_name).items())
    if len(items) == 0:
        return
    container = Node(_replace_underscores_and_capitalize(container_name))
    tree.children.append(container)
    for entity_name, entity in items:
        group_node = Node(entity_name)
        container.children.append(group_node)


def print_model(model: Model) -> None:
    """Print a tree representation of the model.

    Parameters
    ----------
    model:
        pyACP model

    """
    return print(get_model_tree(model))


def get_model_tree(model: Model) -> Node:
    """Get a tree representation of the model.

    Returns the root node.

    Parameters
    ----------
    model:
        pyACP model.
    """
    model_node = Node("Model")

    material_data = Node("Material Data")
    model_node.children.append(material_data)
    _add_tree_part(material_data, "materials", model)
    _add_tree_part(material_data, "fabrics", model)
    _add_tree_part(material_data, "stackups", model)
    _add_tree_part(material_data, "sublaminates", model)

    _add_tree_part(model_node, "element_sets", model)
    _add_tree_part(model_node, "edge_sets", model)

    geometry = Node("Geometry")
    model_node.children.append(geometry)
    _add_tree_part(geometry, "cad_geometries", model)
    _add_tree_part(geometry, "virtual_geometries", model)

    _add_tree_part(model_node, "rosettes", model)

    lookup_table = Node("Lookup Tables")
    model_node.children.append(lookup_table)
    _add_tree_part(lookup_table, "lookup_tables_1d", model)
    _add_tree_part(lookup_table, "lookup_tables_3d", model)

    selection_rules = Node("Selection Rules")
    model_node.children.append(selection_rules)
    _add_tree_part(selection_rules, "parallel_selection_rules", model)
    _add_tree_part(selection_rules, "cylindrical_selection_rules", model)
    _add_tree_part(selection_rules, "spherical_selection_rules", model)
    _add_tree_part(selection_rules, "tube_selection_rules", model)
    _add_tree_part(selection_rules, "cutoff_selection_rules", model)
    _add_tree_part(selection_rules, "geometrical_selection_rules", model)
    _add_tree_part(selection_rules, "variable_offset_selection_rules", model)
    _add_tree_part(selection_rules, "boolean_selection_rules", model)

    _add_tree_part(model_node, "oriented_selection_sets", model)

    modeling_groups = Node("Modeling Groups")
    model_node.children.append(modeling_groups)
    for modeling_group_name, modeling_group in model.modeling_groups.items():
        group_node = Node(modeling_group_name)
        modeling_groups.children.append(group_node)
        for modeling_ply_name, modeling_ply in modeling_group.modeling_plies.items():
            modeling_ply_node = Node(modeling_ply_name)
            group_node.children.append(modeling_ply_node)
            for production_ply_name, production_ply in modeling_ply.production_plies.items():
                production_ply_node = Node(production_ply_name)
                modeling_ply_node.children.append(production_ply_node)
                for analysis_ply_name, analysis_ply in production_ply.analysis_plies.items():
                    analysis_ply_node = Node(analysis_ply_name)
                    production_ply_node.children.append(analysis_ply_node)

    _add_tree_part(model_node, "sensors", model)

    return model_node
