import os
import pathlib

from postprocess_results import postprocess_results
from setup_acp_model import setup_and_update_acp_model

import ansys.mechanical.core as pymechanical

# Run mechanical docker container: docker run -e ANSYSLMD_LICENSE_FILE=1055@milwinlicense1.win.ansys.com -p 50054:10000 ghcr.io/ansys/mechanical:24.1.0
# mechanical = pymechanical.launch_mechanical(batch=False, port=50054, start_instance=False)
mechanical = pymechanical.launch_mechanical(batch=False, version="232")
print(mechanical.project_directory)

result = mechanical.run_python_script_from_file("generate_mesh.py", enable_logging=True)


SETUP_FOLDER_NAME = "Setup"
output_path = pathlib.Path(mechanical.project_directory) / SETUP_FOLDER_NAME
os.mkdir(output_path)

acp_model = setup_and_update_acp_model(output_path)

COMPOSITE_DEFINITIONS_H5 = "ACPCompositeDefinitions.h5"
MATML_FILE = "materials.xml"

material_output_path = str((output_path / MATML_FILE).resolve())
material_output_path = material_output_path.replace("\\", "\\\\")
import_material_cmd = f"Model.Materials.Import('{material_output_path}')"
result = mechanical.run_python_script(import_material_cmd)

# The composite definitions file needs to be copied into
# a folder from which a relative path to the solver files directory
# can be constructed. Otherwise, the material assignment fails.
# The prefix before the filename and :: is necessary, but it looks like the actual value is
# ignored.
# The second argument for Import is probably the list of mapping files. It is required
# to pass an empty container if no mapping files are present, otherwise Import will fail.

hdf_file = rf"{SETUP_FOLDER_NAME}::{str((output_path / COMPOSITE_DEFINITIONS_H5).resolve())}"
hdf_file = hdf_file.replace("\\", "\\\\")
hdf_file = hdf_file.replace("\\", "\\\\")
import_plies_str = f"""
filename = r"{hdf_file}"
ACPFuture.Shims.ImportPlies(Model, filename) 
"""

result = mechanical.run_python_script(import_plies_str)

# Set bc's and solve
result = mechanical.run_python_script_from_file("set_bc.py", enable_logging=True)
result = mechanical.run_python_script("Model.Analyses[0].Solution.Solve(True)")

print(mechanical.list_files())
print(mechanical.project_directory)

rst_file = [filename for filename in mechanical.list_files() if filename.endswith(".rst")][0]
matml_out = [filename for filename in mechanical.list_files() if filename.endswith("MatML.xml")][0]

postprocess_results(rst_file, matml_out, output_path / COMPOSITE_DEFINITIONS_H5)
