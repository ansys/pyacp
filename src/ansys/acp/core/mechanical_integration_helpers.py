# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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

from ._utils.typing_helper import PATH

__all__ = [
    "export_mesh_for_acp",
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
    mechanical.run_python_script(
        textwrap.dedent(
            f"""\
            geometry_type = Ansys.Mechanical.DataModel.Enums.GeometryType.Sheet
            unit = Ansys.Mechanical.DataModel.Enums.WBUnitSystemType.ConsistentMKS
            dsid = 0

            Model.InternalObject.WriteHDF5TransferFile(geometry_type, {output_path_str!r}, unit, dsid)
            """
        )
    )


def import_acp_mesh_from_cdb(*, mechanical: "pymechanical.Mechanical", cdb_path: PATH) -> None:
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
    """
    cdb_path = pathlib.Path(cdb_path)

    if cdb_path.suffix != ".cdb":
        raise ValueError(f"The CDB file extension must be '.cdb', not '{cdb_path.suffix}'.")
    cdb_path_str = str(cdb_path)

    mechanical.run_python_script(
        textwrap.dedent(
            f"""\
            initial_geometry_ids = {{obj.ObjectId for obj in Model.Geometry.Children}}

            model_import = Model.AddGeometryImportGroup().AddModelImport()
            model_import.ModelImportSourceFilePath = {cdb_path_str!r}
            model_import.ProcessValidBlockedCDBFile = False
            model_import.ProcessModelData = False
            model_import.Import()

            final_geometry_ids = {{obj.ObjectId for obj in Model.Geometry.Children}}
            new_geometry_ids = final_geometry_ids - initial_geometry_ids
            if len(new_geometry_ids) != 1:
                raise ValueError("Expected 1 new geometry object, but found {{}}.".format(len(new_geometry_ids)))
            new_geometry_id = new_geometry_ids.pop()

            new_geometry = DataModel.GetObjectById(new_geometry_id)
            if len(new_geometry.Children) != 1:
                raise ValueError("Expected 1 body, but got {{}}.".format(len(new_geometry.Children)))

            body = new_geometry.GetChildren(
                Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body, True
            )[0]
            body.AddCommandSnippet().Input = "keyo,matid,3,1\\nkeyo,matid,8,1"
            """
        )
    )


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
    setup_folder_name = "Setup"

    if path.suffix != ".h5":
        raise ValueError(
            f"The composite definitions file extension must be '.h5', not '{path.suffix}'."
        )

    setup_folder = pathlib.Path(mechanical.project_directory) / setup_folder_name
    setup_folder.mkdir(exist_ok=True)
    target_path = setup_folder / path.name
    try:
        shutil.copyfile(path, target_path)
    except shutil.SameFileError:
        pass

    target_path_str = f"{setup_folder_name}::{target_path.resolve()}".replace("\\", "\\\\")

    mechanical.run_python_script(
        textwrap.dedent(
            f"""\
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
            """
        )
    )
