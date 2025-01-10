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

# type: ignore
import os
import pathlib

from constants import COMPOSITE_DEFINITIONS_H5, MATML_FILE
from postprocess_results import postprocess_results
from setup_acp_model import setup_and_update_acp_model

import ansys.mechanical.core as pymechanical

"""
 Full composites workflow that uses 'remote' PyMechanical.
 See embedded_workflow.py for more comments.
"""

# The following lines show how to start the PyMechanical container, currently disabled because
# a local instance is used.
# Run the Mechanical Docker container: docker run
# -e ANSYSLMD_LICENSE_FILE=1055@example@example.com -p 50054:10000 ghcr.io/ansys/mechanical:24.1.0
# mechanical = pymechanical.launch_mechanical(batch=False, port=50054, start_instance=False)

# Note: It looks like the version argument is not working. It can be set by hardcoding
# it in PyMechanical.
# Note: batch = True is working as well.
mechanical = pymechanical.launch_mechanical(batch=False, version="241")
print(mechanical.project_directory)
script_dir = os.path.dirname(os.path.abspath(__file__))

result = mechanical.run_python_script_from_file("generate_mesh.py", enable_logging=True)

SETUP_FOLDER_NAME = "Setup"
output_path = pathlib.Path(mechanical.project_directory) / SETUP_FOLDER_NAME
os.mkdir(output_path)

mesh_path = os.path.join(script_dir, "output", "mesh.h5")
acp_model = setup_and_update_acp_model(output_path, mesh_path)

# Import materials into Mechanical
material_output_path = str((output_path / MATML_FILE).resolve())
material_output_path = material_output_path.replace("\\", "\\\\")
import_material_cmd = f"Model.Materials.Import('{material_output_path}')"
result = mechanical.run_python_script(import_material_cmd)

# Import plies into Mechanical
hdf_file = rf"{SETUP_FOLDER_NAME}::{str((output_path / COMPOSITE_DEFINITIONS_H5).resolve())}"
hdf_file = hdf_file.replace("\\", "\\\\")
hdf_file = hdf_file.replace("\\", "\\\\")
import_plies_str = f"""
filename = r"{hdf_file}"
ACPFuture.Shims.ImportPlies(Model, filename)
"""

result = mechanical.run_python_script(import_plies_str)

# Set boundary condition and solve
result = mechanical.run_python_script_from_file("set_bc.py", enable_logging=True)
result = mechanical.run_python_script("Model.Analyses[0].Solution.Solve(True)")

print(mechanical.list_files())
print(mechanical.project_directory)

rst_file = [filename for filename in mechanical.list_files() if filename.endswith(".rst")][0]
matml_out = [filename for filename in mechanical.list_files() if filename.endswith("MatML.xml")][0]

postprocess_results(rst_file, matml_out, output_path / COMPOSITE_DEFINITIONS_H5)
