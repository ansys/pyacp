import pathlib

from ansys.acp.core.workflow import ACPWorkflow, print_model
import ansys.acp.core as pyacp

EXAMPLES_DIR = pathlib.Path(__file__).parent
EXAMPLE_DATA_DIR = EXAMPLES_DIR / "data" / "flat_plate"

WORKING_DIR = pathlib.Path(EXAMPLE_DATA_DIR)

# Launch the PyACP server and connect to it.
pyacp_server = pyacp.launch_acp()
pyacp_server.wait(timeout=30)
pyacp_client = pyacp.Client(pyacp_server, local_working_dir=WORKING_DIR)

class40_path = pathlib.Path(r"D:\ANSYSDev\acp_test_model_data\model_data\class40")

workflow_reload = ACPWorkflow(acp_client=pyacp_client,
                       h5_file_path=str(class40_path / "class40.acph5"),
                       cdb_file_path=str(class40_path / "class40.cdb")
                       )
print_model(workflow_reload.model)
workflow_reload.model.update()
workflow_reload.get_local_cdb_file()