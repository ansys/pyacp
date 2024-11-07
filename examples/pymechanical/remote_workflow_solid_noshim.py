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

# type: ignore
import os
import pathlib
import textwrap

from constants import (
    COMPOSITE_DEFINITIONS_H5,
    MATML_FILE,
    SOLID_MODEL_CDB_FILE,
    SOLID_MODEL_COMPOSITE_DEFINITIONS_H5,
)
from postprocess_results import postprocess_results
from setup_acp_model import setup_and_update_acp_model

import ansys.mechanical.core as pymechanical

"""
 Full composites workflow that uses 'remote' PyMechanical.
 See embedded_workflow.py for more comments.
"""

ANSYS_VERSION = "251"

# The following lines show how to start the PyMechanical container, currently disabled because
# a local instance is used.
# Run the Mechanical Docker container: docker run
# -e ANSYSLMD_LICENSE_FILE=1055@example@example.com -p 50054:10000 ghcr.io/ansys/mechanical:24.1.0
# mechanical = pymechanical.launch_mechanical(batch=False, port=50054, start_instance=False)

# Note: It looks like the version argument is not working. It can be set by hardcoding
# it in PyMechanical.
# Note: batch = True is working as well.
script_dir = pathlib.Path(__file__).resolve().parent
mechanical1 = pymechanical.launch_mechanical(batch=False, version=ANSYS_VERSION)

mesh_path = script_dir / "output" / "mesh.h5"
mesh_path.unlink(missing_ok=True)
result = mechanical1.run_python_script_from_file("generate_mesh_noshim.py", enable_logging=True)
assert mesh_path.exists()
mechanical1.exit(force=True)

mechanical2 = pymechanical.launch_mechanical(batch=False, version=ANSYS_VERSION)

SETUP_FOLDER_NAME = "Setup"
output_path = pathlib.Path(mechanical2.project_directory) / SETUP_FOLDER_NAME
os.mkdir(output_path)

acp_model = setup_and_update_acp_model(output_path, mesh_path)

assert (output_path / MATML_FILE).exists()
assert (output_path / COMPOSITE_DEFINITIONS_H5).exists()
assert (output_path / SOLID_MODEL_COMPOSITE_DEFINITIONS_H5).exists()

cdb_path = output_path / SOLID_MODEL_CDB_FILE
h5_path = output_path / SOLID_MODEL_COMPOSITE_DEFINITIONS_H5

with open(cdb_path, "r+", encoding="utf-8") as f:
    cdb_content = f.read()
    cdb_content = cdb_content.replace(",_ACP_", ",ACP_")
    f.seek(0)
    f.write(cdb_content)

# Import geometry, mesh, and named selections into Mechanical
mechanical2.run_python_script(
    textwrap.dedent(
        f"""\
        model_import = Model.AddGeometryImportGroup().AddModelImport()
        model_import.ModelImportSourceFilePath = r"{cdb_path}"
        model_import.ProcessValidBlockedCDBFile = False
        model_import.ProcessModelData = False
        model_import.Import()

        solid_body = Model.Geometry.Children[0].Children[0]
        solid_body.AddCommandSnippet().Input = "keyo,matid,3,1\\nkeyo,matid,8,1"
        """
    )
)

# Import materials into Mechanical
mechanical2.run_python_script(f"Model.Materials.Import({str(output_path / MATML_FILE)!r})")

# Import plies into Mechanical
hdf_file = (
    rf"{SETUP_FOLDER_NAME}::{str((output_path / SOLID_MODEL_COMPOSITE_DEFINITIONS_H5).resolve())}"
)
hdf_file = hdf_file.replace("\\", "\\\\")
hdf_file = hdf_file.replace("\\", "\\\\")
mechanical2.run_python_script(
    textwrap.dedent(
        f"""\
        import clr
        clr.AddReference("Ansys.Common.Interop.{ANSYS_VERSION}")
        filename = r"{hdf_file}"
        composite_definition_paths_coll = Ansys.Common.Interop.AnsCoreObjects.AnsBSTRColl()
        composite_definition_paths_coll.Add(filename)
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

# Set boundary condition and solve
result = mechanical2.run_python_script_from_file("set_bc_solid.py", enable_logging=True)
result = mechanical2.run_python_script("Model.Analyses[0].Solution.Solve(True)")

rst_file = [filename for filename in mechanical2.list_files() if filename.endswith(".rst")][0]
matml_out = [filename for filename in mechanical2.list_files() if filename.endswith("MatML.xml")][0]

postprocess_results(
    rst_file=rst_file,
    matml_file=matml_out,
    composite_definitions_path=output_path / COMPOSITE_DEFINITIONS_H5,
    solid_composite_definitions_path=output_path / SOLID_MODEL_COMPOSITE_DEFINITIONS_H5,
)
