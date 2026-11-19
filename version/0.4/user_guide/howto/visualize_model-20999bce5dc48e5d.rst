import tempfile
import pathlib
import ansys.acp.core as pyacp
from ansys.acp.core.extras import ExampleKeys, get_example_file
#
acp = pyacp.launch_acp()
tempdir = tempfile.TemporaryDirectory()
input_file = get_example_file(
    ExampleKeys.RACE_CAR_NOSE_ACPH5, pathlib.Path(tempdir.name)
)
model = acp.import_model(input_file)
#
input_file_geometry = get_example_file(
    ExampleKeys.RACE_CAR_NOSE_STEP, pathlib.Path(tempdir.name)
)
cad_geometry = model.create_cad_geometry(name="nose_geometry")
cad_geometry.refresh(input_file_geometry)
#
model.update()
