import tempfile
import pathlib
import ansys.acp.core as pyacp
from ansys.acp.core import example_helpers
#
acp = pyacp.launch_acp()
tempdir = tempfile.TemporaryDirectory()
input_file = example_helpers.get_example_file(
    example_helpers.ExampleKeys.RACE_CAR_NOSE_ACPH5, pathlib.Path(tempdir.name)
)
path = acp.upload_file(input_file)
model = acp.import_model(path=path)
#
input_file_geometry = example_helpers.get_example_file(
    example_helpers.ExampleKeys.RACE_CAR_NOSE_STEP, pathlib.Path(tempdir.name)
)
path_geometry = acp.upload_file(input_file_geometry)
model.create_cad_geometry(name="nose_geometry", external_path=path_geometry)
#
model.update()
