"""
.. _start from existing acph5 project:

Start from existing acph5 project
=================================

    TODO: Write descriptions
"""

import pathlib
import tempfile

import ansys.acp.core as pyacp
from ansys.acp.core import ACPWorkflow, ExampleKeys, get_example_file, print_model

# %%
# Get example file from server
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_cdb_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_CDB, WORKING_DIR)
input_acph5_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_ACPH5, WORKING_DIR)

# Launch the PyACP server and connect to it.
pyacp_server = pyacp.launch_acp()
pyacp_server.wait(timeout=30)
pyacp_client = pyacp.Client(pyacp_server)

workflow_reload = ACPWorkflow(
    acp_client=pyacp_client,
    h5_file_path=input_acph5_file,
    cdb_file_path=input_cdb_file,
)
print_model(workflow_reload.model)
workflow_reload.model.update()
workflow_reload.get_local_cdb_file()
