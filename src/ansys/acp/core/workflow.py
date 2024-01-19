import pathlib
from typing import Callable, Optional

from ansys.dpf.composites.data_sources import (
    CompositeDefinitionFiles,
    ContinuousFiberCompositesFiles,
)

from ._client import Client
from ._typing_helper import PATH


class LocalFileStrategy:
    def __init__(self, local_working_directory: pathlib.Path):
        self._local_working_directory = local_working_directory

    def get_file(self, get_file_callable: Callable[[None], pathlib.Path], filename: str):
        local_path = self._local_working_directory / filename
        get_file_callable(self._local_working_directory / filename)
        return local_path


class RemoteFileStrategy:
    def __init__(self, local_working_directory: pathlib.Path, acp_client: Client):
        self._local_working_directory = local_working_directory
        self._acp_client = acp_client

    def get_file(self, get_file_callable: Callable[[pathlib.Path], None], filename: str):
        get_file_callable(pathlib.Path(filename))
        local_path = self._acp_client.local_working_dir.path / filename
        self._acp_client.download_file(remote_filename=filename, local_path=str(local_path))
        return local_path


class ACPWorkflow:
    # Todo: We need to always upload referenced files (e.g. geometries) to the server
    # Read linked file paths from acph5 file if they exist:
    #    * cdb
    #    * geometries (upload only needed if a refresh is requested)
    #    * others?
    def __init__(
        self,
        acp_client: Client,
        cdb_file_path: Optional[PATH] = None,
        h5_file_path: Optional[PATH] = None,
    ):
        self._acp_client = acp_client

        # todo copy to temp directory if it is used
        if cdb_file_path is not None:
            uploaded_file = self._acp_client.upload_file(local_path=cdb_file_path)
            if h5_file_path is None:
                self._model = self._acp_client.import_model(path=uploaded_file, format="ansys:cdb")

        # todo copy to temp directory if it is used
        if h5_file_path is not None:
            uploaded_file = self._acp_client.upload_file(local_path=h5_file_path)
            self._model = self._acp_client.import_model(path=uploaded_file)

        if self._acp_client.is_remote:
            self._file_strategy = RemoteFileStrategy(
                local_working_directory=self._acp_client.local_working_dir.path,
                acp_client=self._acp_client,
            )
        else:
            self._file_strategy = LocalFileStrategy(
                local_working_directory=self._acp_client.local_working_dir.path,
            )

    @property
    def model(self):
        return self._model

    def get_local_cdb_file(self):
        return self._file_strategy.get_file(
            self._model.save_analysis_model, self._model.name + ".cdb"
        )

    def get_local_materials_file(self):
        return self._file_strategy.get_file(self._model.export_materials, "materials.xml")

    def get_local_composite_definitions_file(self):
        return self._file_strategy.get_file(
            self._model.export_shell_composite_definitions, "ACPCompositeDefinitions.h5"
        )

    def get_local_acp_h5(self):
        return self._file_strategy.get_file(self._model.save, "model.acph5")


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


def print_model(model):
    tree = Node("Model")

    def add_tree_part(
        tree,
        name,
    ):
        entities = Node(name)
        tree.children.append(entities)
        for entity_name, entity in getattr(model, name).items():
            group_node = Node(entity_name)
            entities.children.append(group_node)

    add_tree_part(tree, "element_sets")
    add_tree_part(tree, "materials")
    add_tree_part(tree, "fabrics")
    add_tree_part(tree, "oriented_selection_sets")

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


def get_composite_post_processing_files(acp_files: ACPWorkflow, local_rst_file_path: PATH):
    composite_files = ContinuousFiberCompositesFiles(
        rst=local_rst_file_path,
        composite={
            "shell": CompositeDefinitionFiles(
                definition=acp_files.get_local_composite_definitions_file()
            ),
        },
        engineering_data=acp_files.get_local_materials_file(),
    )
    return composite_files
