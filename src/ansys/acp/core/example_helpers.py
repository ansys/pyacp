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

"""Helpers used in the PyACP examples.

These utilities can download the input files used in the PyACP examples.
"""


import dataclasses
from enum import Enum, auto
import pathlib
import urllib.request

__all__ = ["ExampleKeys", "get_example_file"]

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansys.acp.core import ACPWorkflow

_EXAMPLE_REPO = "https://github.com/ansys/example-data/raw/master/pyacp/"


@dataclasses.dataclass
class _ExampleLocation:
    directory: str
    filename: str


class ExampleKeys(Enum):
    """Keys for the example files."""

    BASIC_FLAT_PLATE_DAT = auto()
    BASIC_FLAT_PLATE_ACPH5 = auto()
    RACE_CAR_NOSE_ACPH5 = auto()
    RACE_CAR_NOSE_STEP = auto()
    CUT_OFF_GEOMETRY = auto()
    RULE_GEOMETRY_TRIANGLE = auto()
    THICKNESS_GEOMETRY = auto()
    MINIMAL_FLAT_PLATE = auto()
    OPTIMIZATION_EXAMPLE_DAT = auto()


EXAMPLE_FILES: dict[ExampleKeys, _ExampleLocation] = {
    ExampleKeys.BASIC_FLAT_PLATE_DAT: _ExampleLocation(
        directory="basic_flat_plate_example", filename="flat_plate_input.dat"
    ),
    ExampleKeys.BASIC_FLAT_PLATE_ACPH5: _ExampleLocation(
        directory="basic_flat_plate_example", filename="flat_plate.acph5"
    ),
    ExampleKeys.RACE_CAR_NOSE_ACPH5: _ExampleLocation(
        directory="race_car_nose", filename="race_car_nose.acph5"
    ),
    ExampleKeys.RACE_CAR_NOSE_STEP: _ExampleLocation(
        directory="race_car_nose", filename="race_car_nose.stp"
    ),
    ExampleKeys.CUT_OFF_GEOMETRY: _ExampleLocation(
        directory="geometries", filename="cut_off_geometry.stp"
    ),
    ExampleKeys.RULE_GEOMETRY_TRIANGLE: _ExampleLocation(
        directory="geometries", filename="rule_geometry_triangle.stp"
    ),
    ExampleKeys.THICKNESS_GEOMETRY: _ExampleLocation(
        directory="geometries", filename="thickness_geometry.stp"
    ),
    ExampleKeys.MINIMAL_FLAT_PLATE: _ExampleLocation(
        directory="basic_flat_plate_example", filename="minimal_model_single_ply.acph5"
    ),
    ExampleKeys.OPTIMIZATION_EXAMPLE_DAT: _ExampleLocation(
        directory="optimization_example", filename="optimization_model.dat"
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


def _run_analysis(workflow: "ACPWorkflow") -> None:
    """Run the model with mapdl and do a post-processing analysis.

    Uses a max strain criteria, which means strain limits have to be defined.
    This function can be called at the end of examples to verify the prepared model
    actually solves and can be postprocessed.
    """
    from ansys.mapdl.core import launch_mapdl

    model = workflow.model
    model.update()

    # Launch the MAPDL instance
    mapdl = launch_mapdl()
    mapdl.clear()

    # Load the CDB file into PyMAPDL
    mapdl.input(str(workflow.get_local_cdb_file()))

    # Solve the model
    mapdl.allsel()
    mapdl.slashsolu()
    mapdl.solve()

    # Download the rst file for composite specific post-processing
    rstfile_name = f"{mapdl.jobname}.rst"
    rst_file_local_path = workflow.working_directory.path / rstfile_name
    mapdl.download(rstfile_name, str(workflow.working_directory.path))

    from ansys.acp.core import get_composite_post_processing_files, get_dpf_unit_system
    from ansys.dpf.composites.composite_model import CompositeModel
    from ansys.dpf.composites.constants import FailureOutput
    from ansys.dpf.composites.failure_criteria import CombinedFailureCriterion, MaxStrainCriterion
    from ansys.dpf.composites.server_helpers import connect_to_or_start_server

    dpf_server = connect_to_or_start_server()

    max_strain = MaxStrainCriterion()

    cfc = CombinedFailureCriterion(
        name="Combined Failure Criterion",
        failure_criteria=[max_strain],
    )

    composite_model = CompositeModel(
        get_composite_post_processing_files(workflow, rst_file_local_path),
        default_unit_system=get_dpf_unit_system(model.unit_system),
        server=dpf_server,
    )

    output_all_elements = composite_model.evaluate_failure_criteria(cfc)
    irf_field = output_all_elements.get_field({"failure_label": FailureOutput.FAILURE_VALUE})

    # %%
    # Release composite model to close open streams to result file.
    composite_model = None  # type: ignore
