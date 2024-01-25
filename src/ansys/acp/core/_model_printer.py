from typing import Optional

from ._tree_objects.model import Model


class Node:
    def __init__(self, value: str, children: Optional[list["Node"]] = None):
        self.value = value
        self.children: list["Node"] = children if children else []

    def __str__(self, level: Optional[int] = 0) -> str:
        assert level is not None
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


def _add_tree_part(
    tree: Node,
    container_name: str,
    model: Model,
) -> None:
    container = Node(container_name)
    tree.children.append(container)
    for entity_name, entity in getattr(model, container_name).items():
        group_node = Node(entity_name)
        container.children.append(group_node)


def print_model(model: Model) -> None:
    tree = Node("Model")

    _add_tree_part(tree, "element_sets", model)
    _add_tree_part(tree, "materials", model)
    _add_tree_part(tree, "fabrics", model)
    _add_tree_part(tree, "oriented_selection_sets", model)

    modeling_groups = Node("Modeling Groups")
    tree.children.append(modeling_groups)
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

    print(tree)
