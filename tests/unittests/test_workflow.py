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

import pathlib
import shutil
import tempfile

import pytest

from ansys.acp.core import ACPWorkflow, UnitSystemType


@pytest.mark.parametrize("explict_temp_dir", [None, tempfile.TemporaryDirectory()])
def test_workflow(acp_instance, model_data_dir, explict_temp_dir):
    """Test that workflow can be initialized and files can be retrieved."""
    input_file_path = model_data_dir / "minimal_model_2.cdb"

    if explict_temp_dir is not None:
        working_dir = pathlib.Path(explict_temp_dir.name)
    else:
        working_dir = None

    workflow = ACPWorkflow.from_cdb_or_dat_file(
        acp=acp_instance,
        cdb_or_dat_file_path=input_file_path,
        local_working_directory=working_dir,
        unit_system=UnitSystemType.MPA,
    )
    workflow.model.update()

    cbd_path = workflow.get_local_cdb_file()
    assert cbd_path == workflow.working_directory.path / f"{workflow.model.name}.cdb"
    assert cbd_path.is_file()

    acph5_path = workflow.get_local_acph5_file()
    assert acph5_path == workflow.working_directory.path / f"{workflow.model.name}.acph5"
    assert acph5_path.is_file()

    materials_path = workflow.get_local_materials_file()
    assert materials_path == workflow.working_directory.path / "materials.xml"
    assert materials_path.is_file()

    composite_definitions = workflow.get_local_composite_definitions_file()
    assert composite_definitions == workflow.working_directory.path / "ACPCompositeDefinitions.h5"
    assert composite_definitions.is_file()


def test_reload_cad_geometry(acp_instance, model_data_dir, load_cad_geometry):
    input_file_path = model_data_dir / "minimal_model_2.cdb"

    workflow = ACPWorkflow.from_cdb_or_dat_file(
        acp=acp_instance,
        cdb_or_dat_file_path=input_file_path,
        unit_system=UnitSystemType.MPA,
    )
    workflow.model.update()

    cad_geometry_file_path = model_data_dir / "square_and_solid.stp"
    cad_geometry = workflow.add_cad_geometry_from_local_file(cad_geometry_file_path)

    with tempfile.TemporaryDirectory() as tempdir:
        copied_path = pathlib.Path(shutil.copy(cad_geometry_file_path, tempdir))

        workflow.refresh_cad_geometry_from_local_file(copied_path, cad_geometry)
        if acp_instance.is_remote:
            assert cad_geometry.external_path == str(copied_path.name)
        else:
            assert cad_geometry.external_path == str(copied_path)

        # Test that refresh works twice with the same local file.
        workflow.refresh_cad_geometry_from_local_file(copied_path, cad_geometry)

        # Test error when local file does not exist.
        pathlib.Path.unlink(copied_path)
        with pytest.raises(FileNotFoundError) as excinfo:
            workflow.refresh_cad_geometry_from_local_file(copied_path, cad_geometry)
            assert "No such file or directory" in str(excinfo.value)


@pytest.mark.parametrize("unit_system", UnitSystemType)
def test_workflow_unit_system_dat(acp_instance, model_data_dir, unit_system):
    """Test that workflow can be initialized and files can be retrieved."""

    input_file_path = model_data_dir / "flat_plate_input.dat"

    if unit_system != UnitSystemType.UNDEFINED:
        with pytest.raises(ValueError) as ex:
            # Initializing a workflow with a defined unit system is not allowed
            # if the input file does contain the unit system.
            ACPWorkflow.from_cdb_or_dat_file(
                acp=acp_instance,
                cdb_or_dat_file_path=input_file_path,
                unit_system=unit_system,
            )
    else:
        workflow = ACPWorkflow.from_cdb_or_dat_file(
            acp=acp_instance,
            cdb_or_dat_file_path=input_file_path,
            unit_system=unit_system,
        )
        # Unit system in the dat file is MKS
        assert workflow.model.unit_system == UnitSystemType.MKS


@pytest.mark.parametrize("unit_system", UnitSystemType)
def test_workflow_unit_system_cdb(acp_instance, model_data_dir, unit_system):
    """Test that workflow can be initialized and files can be retrieved."""

    input_file_path = model_data_dir / "minimal_model_2.cdb"

    if unit_system == UnitSystemType.UNDEFINED:
        with pytest.raises(ValueError) as ex:
            # Initializing a workflow with an undefined unit system is not allowed
            # if the input file does not contain the unit system.
            ACPWorkflow.from_cdb_or_dat_file(
                acp=acp_instance,
                cdb_or_dat_file_path=input_file_path,
                unit_system=unit_system,
            )
    else:
        workflow = ACPWorkflow.from_cdb_or_dat_file(
            acp=acp_instance,
            cdb_or_dat_file_path=input_file_path,
            unit_system=unit_system,
        )
        assert workflow.model.unit_system == unit_system
