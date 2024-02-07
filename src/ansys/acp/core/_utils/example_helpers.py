import dataclasses
from enum import Enum, auto
import pathlib
import urllib.request

__all__ = ["ExampleKeys", "get_example_file"]

from typing import TYPE_CHECKING

from ansys.mapdl.core import launch_mapdl

if TYPE_CHECKING:
    from ansys.acp.core import ACPWorkflow

_EXAMPLE_REPO = "https://github.com/ansys/example-data/raw/master/pyacp/"


@dataclasses.dataclass
class _ExampleLocation:
    directory: str
    filename: str


class ExampleKeys(Enum):
    """Keys for the example files."""

    BASIC_FLAT_PLATE_CDB = auto()
    BASIC_FLAT_PLATE_ACPH5 = auto()


EXAMPLE_FILES: dict[ExampleKeys, _ExampleLocation] = {
    ExampleKeys.BASIC_FLAT_PLATE_CDB: _ExampleLocation(
        directory="basic_flat_plate_example", filename="flat_plate_input.dat"
    ),
    ExampleKeys.BASIC_FLAT_PLATE_ACPH5: _ExampleLocation(
        directory="basic_flat_plate_example", filename="flat_plate.acph5"
    ),
}


def get_example_file(example_key: ExampleKeys, working_directory: pathlib.Path) -> pathlib.Path:
    """Download an example file from the example-data repo to the working directory.

    Parameters
    ----------
    example_key
        Key for the example file.
    working_directory
        Working directory to download the example file to.
    """
    example_location = EXAMPLE_FILES[example_key]
    _download_file(example_location, working_directory / example_location.filename)
    return working_directory / example_location.filename


def _get_file_url(example_location: _ExampleLocation) -> str:
    return _EXAMPLE_REPO + "/".join([example_location.directory, example_location.filename])


def _download_file(example_location: _ExampleLocation, local_path: pathlib.Path) -> None:
    file_url = _get_file_url(example_location)
    urllib.request.urlretrieve(file_url, local_path)


def run_analysis(workflow: "ACPWorkflow"):
    model = workflow.model
    model.update()

    # %%
    # Solve the model with MAPDL
    # --------------------------
    #
    # Launch the MAPDL instance
    mapdl = launch_mapdl()
    mapdl.clear()

    # %%
    # Load the CDB file into PyMAPDL
    mapdl.input(str(workflow.get_local_cdb_file()))

    # %%
    # Solve the model
    mapdl.allsel()
    mapdl.slashsolu()
    mapdl.solve()

    # %%
    # Post-processing: show displacements
    mapdl.post1()
    mapdl.set("last")
    mapdl.post_processing.plot_nodal_displacement(component="NORM")

    # %%
    # Download the rst file for composite specific post-processing
    rstfile_name = f"{mapdl.jobname}.rst"
    rst_file_local_path = workflow.working_directory.path / rstfile_name
    mapdl.download(rstfile_name, str(workflow.working_directory.path))

    # %%
    # Post-Processing with DPF composites
    # -----------------------------------
    #
    # Setup: configure imports and connect to the pyDPF Composites server
    # and load the dpf composites plugin

    from ansys.acp.core import get_composite_post_processing_files, get_dpf_unit_system
    from ansys.dpf.composites.composite_model import CompositeModel
    from ansys.dpf.composites.constants import FailureOutput
    from ansys.dpf.composites.failure_criteria import CombinedFailureCriterion, MaxStrainCriterion
    from ansys.dpf.composites.server_helpers import connect_to_or_start_server

    # %%
    # Connect to the server. The ``connect_to_or_start_server`` function
    # automatically loads the composites plugin.
    dpf_server = connect_to_or_start_server()

    # %%
    # Specify the Combined Failure Criterion
    max_strain = MaxStrainCriterion()

    cfc = CombinedFailureCriterion(
        name="Combined Failure Criterion",
        failure_criteria=[max_strain],
    )

    # %%
    # Create the CompositeModel and configure its input
    composite_model = CompositeModel(
        get_composite_post_processing_files(workflow, rst_file_local_path),
        default_unit_system=get_dpf_unit_system(model.unit_system),
        server=dpf_server,
    )

    # %%
    # Evaluate the failure criteria and plot it
    output_all_elements = composite_model.evaluate_failure_criteria(cfc)
    irf_field = output_all_elements.get_field({"failure_label": FailureOutput.FAILURE_VALUE})
    irf_field.plot()

    # %%
    # Release composite model to close open streams to result file.
    composite_model = None  # type: ignore
