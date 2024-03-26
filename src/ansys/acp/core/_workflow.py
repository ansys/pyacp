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

import pathlib
import shutil
import tempfile
import typing
from typing import Any, Callable, Optional, Protocol

from . import CADGeometry, UnitSystemType
from ._server.acp_instance import ACP
from ._server.common import ServerProtocol
from ._tree_objects import Model
from ._typing_helper import PATH

# Avoid dependencies on pydpf-composites and dpf-core if it is not used
if typing.TYPE_CHECKING:
    from ansys.dpf.composites.data_sources import ContinuousFiberCompositesFiles
    from ansys.dpf.core import UnitSystem

__all__ = ["ACPWorkflow", "get_composite_post_processing_files", "get_dpf_unit_system"]


class _LocalWorkingDir:
    def __init__(self, path: Optional[PATH] = None):
        self._user_defined_working_dir = None
        self._temp_working_dir = None
        if path is None:
            self._temp_working_dir = tempfile.TemporaryDirectory()
        else:
            self._user_defined_working_dir = pathlib.Path(path)

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
    ) -> pathlib.Path: ...

    def copy_input_file_to_local_workdir(self, path: pathlib.Path) -> pathlib.Path: ...

    def upload_input_file_to_server(self, path: pathlib.Path) -> pathlib.PurePath: ...


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

    def __init__(self, local_working_directory: _LocalWorkingDir, acp: ACP[ServerProtocol]):
        self._local_working_directory = local_working_directory
        self._acp_instance = acp

    def get_file(
        self, get_file_callable: Callable[[pathlib.Path], None], filename: str
    ) -> pathlib.Path:
        get_file_callable(pathlib.Path(filename))
        local_path = self._local_working_directory.path / filename
        self._acp_instance.download_file(remote_filename=filename, local_path=str(local_path))
        return local_path

    def copy_input_file_to_local_workdir(self, path: pathlib.Path) -> pathlib.Path:
        return _copy_file_workdir(path=path, working_directory=self._local_working_directory.path)

    def upload_input_file_to_server(self, path: pathlib.Path) -> pathlib.PurePath:
        return self._acp_instance.upload_file(local_path=path)


def _get_file_transfer_strategy(
    acp: ACP[ServerProtocol], local_working_dir: _LocalWorkingDir
) -> _FileStrategy:
    if acp.is_remote:
        return _RemoteFileTransferStrategy(
            local_working_directory=local_working_dir,
            acp=acp,
        )
    else:
        return _LocalFileTransferStrategy(
            local_working_directory=local_working_dir,
        )


# Todo: Add automated tests for local and remote workflow
class ACPWorkflow:
    r"""Instantiate an ACP Workflow.

    Use the class methods :meth:`.from_cdb_or_dat_file` and
    :meth:`.from_acph5_file` to instantiate the workflow.

    Parameters
    ----------
    acp
        The ACP Client.
    local_file_path :
        Path of the file to load.
    file_format :
        Format of the file to load. Options are ``"acp:h5"``, ``"ansys:cdb"``,
        ``"ansys:dat"``, and ``"ansys:h5"``.
    kwargs :
        Additional keyword arguments to pass to the :meth:`.ACP.import_model` method.

    """

    def __init__(
        self,
        *,
        acp: ACP[ServerProtocol],
        local_working_directory: Optional[PATH] = None,
        local_file_path: PATH,
        file_format: str,
        **kwargs: Any,
    ):
        self._acp_instance = acp
        self._local_working_dir = _LocalWorkingDir(local_working_directory)
        self._file_transfer_strategy = _get_file_transfer_strategy(
            acp=self._acp_instance,
            local_working_dir=self._local_working_dir,
        )

        uploaded_file = self._add_input_file(path=pathlib.Path(local_file_path))
        self._model = self._acp_instance.import_model(
            path=uploaded_file, format=file_format, **kwargs
        )

    @classmethod
    def from_acph5_file(
        cls,
        acp: ACP[ServerProtocol],
        acph5_file_path: PATH,
        local_working_directory: Optional[PATH] = None,
    ) -> "ACPWorkflow":
        """Instantiate an ACP Workflow from an acph5 file.

        Parameters
        ----------
        acp
            The ACP Client.
        acph5_file_path:
            The path to the acph5 file.
        local_working_directory:
            The local working directory. If None, a temporary directory will be created.
        """

        return cls(
            acp=acp,
            local_file_path=acph5_file_path,
            local_working_directory=local_working_directory,
            file_format="acp:h5",
        )

    @classmethod
    def from_cdb_or_dat_file(
        cls,
        *,
        acp: ACP[ServerProtocol],
        cdb_or_dat_file_path: PATH,
        unit_system: UnitSystemType = UnitSystemType.UNDEFINED,
        local_working_directory: Optional[PATH] = None,
    ) -> "ACPWorkflow":
        """Instantiate an ACP Workflow from a cdb file.

        Parameters
        ----------
        acp
            The ACP Client.
        cdb_or_dat_file_path:
            The path to the cdb or dat file.
        unit_system:
            Has to be ``UnitSystemType.UNDEFINED`` if the unit system
            is specified in the cdb or dat file. Needs to be set to a defined unit system
            if the unit system is not set in the cdb or dat file.
        local_working_directory:
            The local working directory. If None, a temporary directory will be created.
        """

        instance = cls(
            acp=acp,
            local_file_path=cdb_or_dat_file_path,
            local_working_directory=local_working_directory,
            file_format="ansys:cdb",
            unit_system=unit_system,
        )

        if instance.model.unit_system == UnitSystemType.UNDEFINED:
            raise ValueError(
                "The input file does not provide a unit system. Please specify the unit system."
            )
        return instance

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
        copy it to the local working directory and return its path.
        """
        return self._file_transfer_strategy.get_file(
            self._model.export_analysis_model, self._model.name + ".cdb"
        )

    def get_local_materials_file(self) -> pathlib.Path:
        """Get the materials.xml file on the local machine.

        Write the materials.xml file, copy it to the local working directory and return its path.
        """
        return self._file_transfer_strategy.get_file(self._model.export_materials, "materials.xml")

    def get_local_composite_definitions_file(self) -> pathlib.Path:
        """Get the composite definitions file on the local machine.

        Write the composite definitions file, copy it to the local working
        directory and return its path.
        """
        return self._file_transfer_strategy.get_file(
            self._model.export_shell_composite_definitions, "ACPCompositeDefinitions.h5"
        )

    def get_local_acph5_file(self) -> pathlib.Path:
        """Get the ACP Project file (in acph5 format) on the local machine.

        Save the acp model to an acph5 file, copy it to the local working
        directory and return its path.
        """
        return self._file_transfer_strategy.get_file(self._model.save, self._model.name + ".acph5")

    def add_cad_geometry_from_local_file(self, path: pathlib.Path) -> CADGeometry:
        """Add a local CAD geometry to the ACP model.

        Parameters
        ----------
        path:
            The path to the CAD geometry file.
        """
        uploaded_file = self._add_input_file(path=path)
        return self._model.create_cad_geometry(external_path=str(uploaded_file))

    def refresh_cad_geometry_from_local_file(
        self, path: pathlib.Path, cad_geometry: CADGeometry
    ) -> None:
        """Refresh the CAD geometry from a local file.

        Parameters
        ----------
        path:
            The path to the CAD geometry file.
        cad_geometry:
            The CADGeometry object to refresh.
        """
        uploaded_file_path = self._add_input_file(path=path)
        cad_geometry.external_path = uploaded_file_path
        cad_geometry.refresh()

    def _add_input_file(self, path: pathlib.Path) -> pathlib.PurePath:
        self._file_transfer_strategy.copy_input_file_to_local_workdir(path=path)
        return self._file_transfer_strategy.upload_input_file_to_server(path=path)


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
    try:
        from ansys.dpf.composites.data_sources import (
            CompositeDefinitionFiles,
            ContinuousFiberCompositesFiles,
        )
    except ImportError as e:
        raise ImportError(
            "The composite post processing files can only be retrieved if the "
            "ansys-dpf-composites package is installed."
        ) from e

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
    try:
        from ansys.dpf.core import unit_systems
    except ImportError as e:
        raise ImportError(
            "The pyACP unit system can only be converted to a DPF unit system if the "
            "ansys-dpf-core package is installed."
        ) from e

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
