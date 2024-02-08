"""
.. _start from existing acph5 project:

Start from existing acph5 project
=================================

    TODO: Write descriptions
"""

import pathlib
import tempfile

import ansys.acp.core as pyacp
from ansys.acp.core import ACPWorkflow, example_helpers, print_model

# %%
# Get example file from server
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_acph5_file = example_helpers.get_example_file(
    example_helpers.ExampleKeys.BASIC_FLAT_PLATE_ACPH5, WORKING_DIR
)

# Launch the PyACP server and connect to it.
acp = pyacp.launch_acp()

workflow_reload = ACPWorkflow.from_acph5_file(acp=acp, acph5_file_path=input_acph5_file)
print_model(workflow_reload.model)
workflow_reload.model.update()
workflow_reload.get_local_cdb_file()
