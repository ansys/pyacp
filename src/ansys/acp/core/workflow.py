import pathlib
from typing import Callable, Optional, Protocol

from ansys.dpf.composites.data_sources import (
    CompositeDefinitionFiles,
    ContinuousFiberCompositesFiles,
)

from . import Model
from ._client import Client
from ._typing_helper import PATH


class FileStrategy(Protocol):
    def get_file(
        self, get_file_callable: Callable[[pathlib.Path], None], filename: str
    ) -> pathlib.Path:
        ...


class LocalFileStrategy:
    def __init__(self, local_working_directory: pathlib.Path):
        self._local_working_directory = local_working_directory

    def get_file(
        self, get_file_callable: Callable[[pathlib.Path], None], filename: str
    ) -> pathlib.Path:
        local_path = self._local_working_directory / filename
        get_file_callable(self._local_working_directory / filename)
        return local_path


class RemoteFileStrategy:
    def __init__(self, local_working_directory: pathlib.Path, acp_client: Client):
        self._local_working_directory = local_working_directory
        self._acp_client = acp_client

    def get_file(
        self, get_file_callable: Callable[[pathlib.Path], None], filename: str
    ) -> pathlib.Path:
        get_file_callable(pathlib.Path(filename))
        local_path = self._acp_client.local_working_dir.path / filename
        self._acp_client.download_file(remote_filename=filename, local_path=str(local_path))
        return local_path


def _get_file_strategy(acp_client: Client) -> FileStrategy:
    if acp_client.is_remote:
        return RemoteFileStrategy(
            local_working_directory=acp_client.local_working_dir.path,
            acp_client=acp_client,
        )
    else:
        return LocalFileStrategy(
            local_working_directory=acp_client.local_working_dir.path,
        )


class ACPWorkflow:
    def __init__(
        self,
        acp_client: Client,
        cdb_file_path: Optional[PATH] = None,
        h5_file_path: Optional[PATH] = None,
    ):
        self._acp_client = acp_client

        if cdb_file_path is not None:
            uploaded_file = self._acp_client.upload_file(local_path=cdb_file_path)
            if h5_file_path is None:
                self._model = self._acp_client.import_model(path=uploaded_file, format="ansys:cdb")

        if h5_file_path is not None:
            uploaded_file = self._acp_client.upload_file(local_path=h5_file_path)
            self._model = self._acp_client.import_model(path=uploaded_file)

        self._file_strategy = _get_file_strategy(acp_client=self._acp_client)

    @property
    def model(self) -> Model:
        return self._model

    def get_local_cdb_file(self) -> pathlib.Path:
        return self._file_strategy.get_file(
            self._model.save_analysis_model, self._model.name + ".cdb"
        )

    def get_local_materials_file(self) -> pathlib.Path:
        return self._file_strategy.get_file(self._model.export_materials, "materials.xml")

    def get_local_composite_definitions_file(self) -> pathlib.Path:
        return self._file_strategy.get_file(
            self._model.export_shell_composite_definitions, "ACPCompositeDefinitions.h5"
        )

    def get_local_acp_h5(self) -> pathlib.Path:
        return self._file_strategy.get_file(self._model.save, "model.acph5")


def get_composite_post_processing_files(
    acp_files: ACPWorkflow, local_rst_file_path: PATH
) -> ContinuousFiberCompositesFiles:
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
