import pathlib
import shutil
import tempfile
import typing
from typing import Callable, Optional, Protocol

from . import UnitSystemType
from ._client import Client
from ._tree_objects import Model
from ._typing_helper import PATH

# Avoid dependencies on pydpf-composites and dpf-core if it is not used
if typing.TYPE_CHECKING:
    from ansys.dpf.composites.data_sources import ContinuousFiberCompositesFiles
    from ansys.dpf.core import UnitSystem

__all__ = ["ACPWorkflow", "get_composite_post_processing_files", "get_dpf_unit_system"]


class _LocalWorkingDir:
    def __init__(self, path: Optional[pathlib.Path] = None):
        self._user_defined_working_dir = None
        self._temp_working_dir = None
        if path is None:
            self._temp_working_dir = tempfile.TemporaryDirectory()
        else:
            self._user_defined_working_dir = path

    @property
    def path(self) -> pathlib.Path:
        if self._user_defined_working_dir is not None:
            return self._user_defined_working_dir
        else:
            # Make typechecker happy
            assert self._temp_working_dir is not None
            return pathlib.Path(self._temp_working_dir.name)


class _FileStrategy(Protocol):
    def get_file(
        self, get_file_callable: Callable[[pathlib.Path], None], filename: str
    ) -> pathlib.Path:
        ...

    def copy_input_file_to_local_workdir(self, path: pathlib.Path) -> pathlib.Path:
        ...

    def upload_input_file_to_server(self, path: pathlib.Path) -> pathlib.PurePath:
        ...


def _copy_file_workdir(path: pathlib.Path, working_directory: pathlib.Path) -> pathlib.Path:
    try:
        shutil.copy(path, working_directory)
    except shutil.SameFileError:
        pass
    return working_directory / path.name


class _LocalFileTransferStrategy:
    """File transfer strategy for local workflows.

    Save output files to the local working directory and do nothing for input files.
    """

    def __init__(self, local_working_directory: _LocalWorkingDir):
        self._local_working_directory = local_working_directory

    def get_file(
        self, get_file_callable: Callable[[pathlib.Path], None], filename: str
    ) -> pathlib.Path:
        local_path = self._local_working_directory.path / filename
        get_file_callable(self._local_working_directory.path / filename)
        return local_path

    def copy_input_file_to_local_workdir(self, path: pathlib.Path) -> pathlib.Path:
        return _copy_file_workdir(path=path, working_directory=self._local_working_directory.path)

    def upload_input_file_to_server(self, path: pathlib.Path) -> pathlib.PurePath:
        return path


class _RemoteFileTransferStrategy:
    """File transfer strategy for remote workflows.

    Download output files from the server to the local working directory and upload
    input files to the server.
    """

    def __init__(self, local_working_directory: _LocalWorkingDir, acp_client: Client):
        self._local_working_directory = local_working_directory
        self._acp_client = acp_client

    def get_file(
        self, get_file_callable: Callable[[pathlib.Path], None], filename: str
    ) -> pathlib.Path:
        get_file_callable(pathlib.Path(filename))
        local_path = self._local_working_directory.path / filename
        self._acp_client.download_file(remote_filename=filename, local_path=str(local_path))
        return local_path

    def copy_input_file_to_local_workdir(self, path: pathlib.Path) -> pathlib.Path:
        return _copy_file_workdir(path=path, working_directory=self._local_working_directory.path)

    def upload_input_file_to_server(self, path: pathlib.Path) -> pathlib.PurePath:
        return self._acp_client.upload_file(local_path=path)


def _get_file_transfer_strategy(
    acp_client: Client, local_working_dir: _LocalWorkingDir
) -> _FileStrategy:
    if acp_client.is_remote:
        return _RemoteFileTransferStrategy(
            local_working_directory=local_working_dir,
            acp_client=acp_client,
        )
    else:
        return _LocalFileTransferStrategy(
            local_working_directory=local_working_dir,
        )


# Todo: Add automated tests for local and remote workflow
# Todo: update logic when cdb is part of the acph5
class ACPWorkflow:
    r"""Instantiate an ACP Workflow.

    Supports starting from a \*.cbd or \*.acph5 file

    Parameters
    ----------
    acp_client
        The ACP Client
    local_working_directory:
        The local working directory. If None, a temporary directory will be created.
    cdb_file_path:
        The path to the cdb file.
    h5_file_path:
        The path to the h5 file.
    """

    def __init__(
        self,
        *,
        acp_client: Client,
        local_working_directory: Optional[pathlib.Path] = None,
        cdb_file_path: Optional[PATH] = None,
        acph5_file_path: Optional[PATH] = None,
    ):
        self._acp_client = acp_client
        self._local_working_dir = _LocalWorkingDir(local_working_directory)
        self._file_transfer_strategy = _get_file_transfer_strategy(
            acp_client=self._acp_client,
            local_working_dir=self._local_working_dir,
        )

        if cdb_file_path is not None:
            uploaded_file = self._add_input_file(path=pathlib.Path(cdb_file_path))
            if h5_file_path is None:
                self._model = self._acp_client.import_model(path=uploaded_file, format="ansys:cdb")

        if h5_file_path is not None:
            uploaded_file = self._add_input_file(path=pathlib.Path(h5_file_path))
            self._model = self._acp_client.import_model(path=uploaded_file)

    @property
    def model(self) -> Model:
        """Get the ACP Model."""
        return self._model

    @property
    def working_directory(self) -> _LocalWorkingDir:
        """Get the working directory."""
        return self._local_working_dir

    def get_local_cdb_file(self) -> pathlib.Path:
        """Get the cdb file on the local machine.

        Write the analysis model including the layup definition in cdb format,
        copy it to the local working directory and return its path."""
        return self._file_strategy.get_file(
            self._model.save_analysis_model, self._model.name + ".cdb"
        )

    def get_local_materials_file(self) -> pathlib.Path:
        """Get the materials.xml file on the local machine.

        Write the materials.xml file, copy it to the local working directory and return its path."""
        return self._file_strategy.get_file(self._model.export_materials, "materials.xml")

    def get_local_composite_definitions_file(self) -> pathlib.Path:
        """Get the composite definitions file on the local machine.

        Write the composite definitions file, copy it
         to the local working directory and return its path."""
        return self._file_strategy.get_file(
            self._model.export_shell_composite_definitions, "ACPCompositeDefinitions.h5"
        )

    def get_local_acp_h5_file(self) -> pathlib.Path:
        """Get the ACP Project file (in acph5 format) on the local machine.

        Save the acp model to an acph5 file, copy it
         to the local working directory and return its path."""
        return self._file_strategy.get_file(self._model.save, self._model.name + ".acph5")

    def _add_input_file(self, path: pathlib.Path) -> pathlib.PurePath:
        self._file_strategy.copy_input_file_to_local_workdir(path=path)
        return self._file_strategy.upload_input_file_to_server(path=path)


def get_composite_post_processing_files(
    acp_workflow: ACPWorkflow, local_rst_file_path: PATH
) -> "ContinuousFiberCompositesFiles":
    """Get the files object needed for pydpf-composites from the workflow and the rst path.

    Only supports the shell workflow.

    Parameters
    ----------
    acp_workflow:
        The ACPWorkflow object.
    local_rst_file_path:
        Local path to the rst file.
    """

    # Only import here to avoid dependency on ansys.dpf.composites if it is not used
    from ansys.dpf.composites.data_sources import (
        CompositeDefinitionFiles,
        ContinuousFiberCompositesFiles,
    )

    composite_files = ContinuousFiberCompositesFiles(
        rst=local_rst_file_path,
        composite={
            "shell": CompositeDefinitionFiles(
                definition=acp_workflow.get_local_composite_definitions_file()
            ),
        },
        engineering_data=acp_workflow.get_local_materials_file(),
    )
    return composite_files


def get_dpf_unit_system(unit_system: UnitSystemType) -> "UnitSystem":
    """Convert pyACP unit system to DPF unit system.

    Parameters
    ----------
    unit_system
        The pyACP unit system.
    """
    from ansys.dpf.core import unit_systems

    unit_systems_map = {
        UnitSystemType.UNDEFINED: unit_systems.undefined,
        # looks like the only difference from MKS to SI is
        # that temperature is defined as Kelvin in SI and °C in MKS.
        # We should still force the user to use MKS in this case.
        UnitSystemType.SI: None,
        UnitSystemType.MKS: unit_systems.solver_mks,
        UnitSystemType.uMKS: unit_systems.solver_umks,
        UnitSystemType.CGS: unit_systems.solver_cgs,
        # MPA is equivalent to nmm
        UnitSystemType.MPA: unit_systems.solver_nmm,
        UnitSystemType.BFT: unit_systems.solver_bft,
        UnitSystemType.BIN: unit_systems.solver_bin,
    }

    if unit_systems_map[unit_system] is None:
        raise ValueError(f"Unit system {unit_system} not supported. Use MKS instead of SI.")
    if unit_system not in unit_systems_map:
        raise ValueError(f"Unit system {unit_system} not supported.")

    return unit_systems_map[unit_system]
