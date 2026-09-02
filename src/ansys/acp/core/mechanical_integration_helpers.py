# Copyright (C) 2022 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""Helper functions for exchanging data between PyACP and PyMechanical."""

import pathlib
import shutil
import textwrap
import typing

if typing.TYPE_CHECKING:
    import ansys.mechanical.core as pymechanical

from ._tree_objects.enums import UnitSystemType
from ._utils.typing_helper import PATH

__all__ = [
    "export_mesh_for_acp",
    "get_mechanical_unit_system_name",
    "import_acp_composite_definitions",
    "import_acp_mesh_from_cdb",
]


def export_mesh_for_acp(*, mechanical: "pymechanical.Mechanical", path: PATH) -> None:
    """Export the mesh from PyMechanical for use in PyACP.

    Parameters
    ----------
    mechanical :
        The PyMechanical instance. This must be a remote instance.
    path :
        The path to save the mesh to. The extension must be '.h5'.
    """
    path = pathlib.Path(path)

    if path.suffix != ".h5":
        raise ValueError(f"The output path extension must be '.h5', not '{path.suffix}'.")
    output_path_str = str(path)
    mechanical.run_python_script(textwrap.dedent(f"""\
            geometry_type = Ansys.Mechanical.DataModel.Enums.GeometryType.Sheet
            unit = Ansys.Mechanical.DataModel.Enums.WBUnitSystemType.ConsistentMKS
            dsid = 0

            Model.InternalObject.WriteHDF5TransferFile(geometry_type, {output_path_str!r}, unit, dsid)
            """))


def get_mechanical_unit_system_name(unit_system: UnitSystemType) -> str:
    """Get the name of the Mechanical unit system corresponding to a PyACP unit system.

    The returned names are values of the ``ModelImportUnitSystemType`` enum in Mechanical.
    They can be used as the ``mechanical_unit_system_name`` argument of :func:`import_acp_mesh_from_cdb`.

    .. note::

        The Mechanical unit system names are not unique for all PyACP unit systems. For example,
        ``MPA`` is consistent with both ``UnitSystemMetricNMMton`` and ``UnitSystemConsistentNMM``
        since ACP uses a more limited set of unit types than Mechanical.
        For general use, carefully review the Mechanical unit system name to select the appropriate
        one.

    """
    unit_systems_map = {
        # no equivalent for the 'UNDEFINED' unit system
        UnitSystemType.SI: "UnitSystemSI",
        UnitSystemType.MKS: "UnitSystemMetricMKS",
        UnitSystemType.uMKS: "UnitSystemMetricUMKS",
        UnitSystemType.CGS: "UnitSystemMetricCGS",
        UnitSystemType.MPA: "UnitSystemMetricNMMton",
        UnitSystemType.BFT: "UnitSystemConsistentBFT",
        UnitSystemType.BIN: "UnitSystemConsistentBIN",
    }

    if unit_system not in unit_systems_map:
        raise ValueError(f"Unit system {unit_system} not supported.")
    return unit_systems_map[unit_system]


def import_acp_mesh_from_cdb(
    *,
    mechanical: "pymechanical.Mechanical",
    cdb_path: PATH,
    mechanical_unit_system_name: str,
    check_valid_blocked_cdb_file: bool = True,
) -> None:
    """Import an ACP CDB mesh into Mechanical.

    Import a mesh exported from ACP in CDB format into Mechanical. This function
    does not import the ACP layup definition, use :func:`import_acp_composite_definitions`
    for this purpose.

    .. warning::

        The named selections exported from ACP are only partially imported.

    Parameters
    ----------
    mechanical :
        The PyMechanical instance. This must be a remote instance.
    cdb_path :
        The path of the CDB file to import. The extension must be '.cdb'.
    mechanical_unit_system_name :
        The name of the Mechanical unit system corresponding to the CDB file units.
        The value must be one of the values of the ``ModelImportUnitSystemType`` enum
        in Mechanical.
    check_valid_blocked_cdb_file :
        If True, check that the CDB file is a valid blocked CDB file.
    """
    cdb_path = pathlib.Path(cdb_path)

    if cdb_path.suffix != ".cdb":
        raise ValueError(f"The CDB file extension must be '.cdb', not '{cdb_path.suffix}'.")
    cdb_path_str = str(cdb_path)

    mechanical_script = textwrap.dedent(f"""\
        model_import = Model.AddGeometryImportGroup().AddModelImport()
        model_import.UnitSystemTypeForImport = ModelImportUnitSystemType.{mechanical_unit_system_name}
        model_import.ModelImportSourceFilePath = {cdb_path_str!r}
        model_import.ProcessValidBlockedCDBFile = {check_valid_blocked_cdb_file}
        model_import.ProcessModelData = False
        model_import.Import()
        """)
    mechanical.run_python_script(mechanical_script)


def import_acp_composite_definitions(*, mechanical: "pymechanical.Mechanical", path: PATH) -> None:
    """Import ACP composite definitions HDF5 into Mechanical.

    Imports the composite layup defined in ACP into Mechanical, as Imported Plies.

    This function does not import the solid mesh, use :func:`import_acp_mesh_from_cdb`
    for this purpose.

    Parameters
    ----------
    mechanical :
        The PyMechanical instance. This must be a remote instance.
    path :
        The path of the file to import. The extension must be '.h5'.
    """
    path = pathlib.Path(path)

    if path.suffix != ".h5":
        raise ValueError(
            f"The composite definitions file extension must be '.h5', not '{path.suffix}'."
        )

    user_files_dir = pathlib.Path(mechanical.project_directory) / "UserFiles"
    user_files_dir.mkdir(exist_ok=True)
    target_path = user_files_dir / path.name
    try:
        shutil.copyfile(path, target_path)
    except shutil.SameFileError:
        pass

    target_path_str = f"Setup::{str(target_path.resolve())}"

    mechanical.run_python_script(textwrap.dedent(f"""\
            import clr
            clr.AddReference("Ansys.Common.Interop.{mechanical.version}")
            composite_definition_paths_coll = Ansys.Common.Interop.AnsCoreObjects.AnsBSTRColl()
            composite_definition_paths_coll.Add({target_path_str!r})
            mapping_paths_coll = Ansys.Common.Interop.AnsCoreObjects.AnsVARIANTColl()
            mapping_paths_coll.Add(None)
            external_model = Model.InternalObject.AddExternalEnhancedModel(
                Ansys.Common.Interop.DSObjectTypes.DSExternalEnhancedModelType.kEXTERNAL_ENHANCEDMODEL_LAYEREDSECTION
            )
            external_model.Import(composite_definition_paths_coll, mapping_paths_coll)
            external_model.Update()
            """))
