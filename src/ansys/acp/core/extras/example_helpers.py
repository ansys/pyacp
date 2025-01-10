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

"""Helpers used in the PyACP examples.

These utilities can download the input files used in the PyACP examples.
"""
import dataclasses
from enum import Enum, auto
import pathlib
import shutil
import sys
import tempfile
import urllib.parse
import urllib.request

__all__ = [
    "ExampleKeys",
    "get_example_file",
    "FLAT_PLATE_SHELL_CAMERA",
    "FLAT_PLATE_SOLID_CAMERA",
    "RACE_CARE_NOSE_CAMERA_METER",
]

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from ansys.acp.core import Model

_EXAMPLE_REPO = "https://github.com/ansys/example-data/raw/master/pyacp/"


# _EXAMPLE_REPO = "D:\\ANSYSDev\\pyansys-example-data\\pyacp\\"


# Order of inputs: position, rotation point, orientation
FLAT_PLATE_SHELL_CAMERA = [
    (-0.0053, 0.0168, 0.0220),
    (0.0022, 0.0041, 0.0104),
    (0.3510, 0.7368, -0.5779),
]
FLAT_PLATE_SOLID_CAMERA = [
    (0.0251, 0.0144, 0.0256),
    (0.0086, 0.0041, 0.0089),
    (-0.2895, 0.9160, -0.2776),
]

# Order of inputs: position, rotation point, orientation
RACE_CARE_NOSE_CAMERA_METER = [
    (1.614, 1.154, 2.243),
    (0.450, 0.238, -0.181),
    (-0.1094, 0.9460, -0.3050),
]


@dataclasses.dataclass
class _ExampleLocation:
    directory: str
    filename: str


class ExampleKeys(Enum):
    """Keys for the example files."""

    BASIC_FLAT_PLATE_DAT = auto()
    BASIC_FLAT_PLATE_REFINED_DAT = auto()
    BASIC_FLAT_PLATE_ACPH5 = auto()
    BASIC_FLAT_PLATE_SOLID_MESH_CDB = auto()
    RACE_CAR_NOSE_ACPH5 = auto()
    RACE_CAR_NOSE_STEP = auto()
    CUT_OFF_GEOMETRY = auto()
    RULE_GEOMETRY_TRIANGLE = auto()
    THICKNESS_GEOMETRY = auto()
    MINIMAL_FLAT_PLATE = auto()
    OPTIMIZATION_EXAMPLE_DAT = auto()
    CLASS40_AGDB = auto()
    CLASS40_CDB = auto()
    MATERIALS_XML = auto()
    IMPORTED_SOLID_MODEL_ACPH5 = auto()
    IMPORTED_SOLID_MODEL_SOLID_MESH = auto()
    SNAP_TO_GEOMETRY = auto()
    CUT_OFF_GEOMETRY_SOLID_MODEL = auto()


EXAMPLE_FILES: dict[ExampleKeys, _ExampleLocation] = {
    ExampleKeys.BASIC_FLAT_PLATE_DAT: _ExampleLocation(
        directory="basic_flat_plate_example", filename="flat_plate_input.dat"
    ),
    ExampleKeys.BASIC_FLAT_PLATE_REFINED_DAT: _ExampleLocation(
        directory="basic_flat_plate_example", filename="flat_plate_input_refined.dat"
    ),
    ExampleKeys.BASIC_FLAT_PLATE_ACPH5: _ExampleLocation(
        directory="basic_flat_plate_example", filename="flat_plate.acph5"
    ),
    ExampleKeys.BASIC_FLAT_PLATE_SOLID_MESH_CDB: _ExampleLocation(
        directory="basic_flat_plate_example", filename="solid_mesh.cdb"
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
    ExampleKeys.CLASS40_AGDB: _ExampleLocation(directory="class40", filename="class40.agdb"),
    ExampleKeys.CLASS40_CDB: _ExampleLocation(directory="class40", filename="class40.cdb"),
    ExampleKeys.MATERIALS_XML: _ExampleLocation(directory="materials", filename="materials.engd"),
    ExampleKeys.IMPORTED_SOLID_MODEL_ACPH5: _ExampleLocation(
        directory="imported_solid_model", filename="t-joint-ACP-Pre.acph5"
    ),
    ExampleKeys.IMPORTED_SOLID_MODEL_SOLID_MESH: _ExampleLocation(
        directory="imported_solid_model", filename="t-joint.solid.h5"
    ),
    ExampleKeys.SNAP_TO_GEOMETRY: _ExampleLocation(
        directory="geometries", filename="snap_to_geometry.stp"
    ),
    ExampleKeys.CUT_OFF_GEOMETRY_SOLID_MODEL: _ExampleLocation(
        directory="geometries", filename="cut_off_geometry_solid_model.stp"
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


def _is_url(path_url: str) -> bool:  # pragma: no cover
    return urllib.parse.urlparse(path_url).scheme in ["http", "https"]


def _get_file_url(example_location: _ExampleLocation) -> str:  # pragma: no cover
    if sys.platform == "win32" and not _is_url(_EXAMPLE_REPO):
        return _EXAMPLE_REPO + "\\".join([example_location.directory, example_location.filename])
    else:
        return _EXAMPLE_REPO + "/".join([example_location.directory, example_location.filename])


def _download_file(
    example_location: _ExampleLocation, local_path: pathlib.Path
) -> None:  # pragma: no cover
    file_url = _get_file_url(example_location)
    # The URL is hard-coded to start with the example repository URL, so it is safe to use
    if _is_url(file_url):
        urllib.request.urlretrieve(file_url, local_path)  # nosec: B310
    else:
        shutil.copyfile(file_url, local_path)


def _run_analysis(model: "Model") -> None:
    """Run the model with mapdl and do a post-processing analysis.

    Uses a max strain criteria, which means strain limits have to be defined.
    This function can be called at the end of examples to verify the prepared model
    actually solves and can be postprocessed.
    """
    from ansys.mapdl.core import launch_mapdl

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir_path = pathlib.Path(tmp_dir)
        model.update()
        cdb_out_path = tmp_dir_path / "model.cdb"
        model.export_analysis_model(cdb_out_path)

        # Launch the MAPDL instance
        mapdl = launch_mapdl()
        mapdl.clear()

        # Load the CDB file into PyMAPDL
        mapdl.input(str(cdb_out_path))

        # Solve the model
        mapdl.allsel()
        mapdl.slashsolu()
        mapdl.solve()

        # Download the rst file for composite specific post-processing
        rstfile_name = f"{mapdl.jobname}.rst"
        rst_file_local_path = tmp_dir_path / rstfile_name
        mapdl.download(rstfile_name, str(tmp_dir_path))

        from ansys.acp.core.dpf_integration_helpers import get_dpf_unit_system
        from ansys.dpf.composites.composite_model import CompositeModel
        from ansys.dpf.composites.constants import FailureOutput
        from ansys.dpf.composites.data_sources import (
            CompositeDefinitionFiles,
            ContinuousFiberCompositesFiles,
        )
        from ansys.dpf.composites.failure_criteria import (
            CombinedFailureCriterion,
            MaxStrainCriterion,
        )
        from ansys.dpf.composites.server_helpers import connect_to_or_start_server

        dpf_server = connect_to_or_start_server()

        max_strain = MaxStrainCriterion()

        cfc = CombinedFailureCriterion(
            name="Combined Failure Criterion",
            failure_criteria=[max_strain],
        )

        materials_file_path = tmp_dir_path / "materials.xml"
        model.export_materials(materials_file_path)
        composite_definitions_file_path = tmp_dir_path / "ACPCompositeDefinitions.h5"
        model.export_shell_composite_definitions(composite_definitions_file_path)
        composite_model = CompositeModel(
            composite_files=ContinuousFiberCompositesFiles(
                rst=rst_file_local_path,
                composite={"shell": CompositeDefinitionFiles(composite_definitions_file_path)},
                engineering_data=materials_file_path,
            ),
            default_unit_system=get_dpf_unit_system(model.unit_system),
            server=dpf_server,
        )

        output_all_elements = composite_model.evaluate_failure_criteria(cfc)
        irf_field = output_all_elements.get_field({"failure_label": FailureOutput.FAILURE_VALUE})

        # %%
        # Release composite model to close open streams to result file.
        composite_model = None  # type: ignore

        # Close MAPDL instance
        mapdl.exit()
