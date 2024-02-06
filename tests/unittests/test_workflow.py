import pathlib
import shutil
import tempfile

import pytest

from ansys.acp.core import ACPWorkflow


@pytest.mark.parametrize("explict_temp_dir", [None, tempfile.TemporaryDirectory()])
def test_workflow(acp_instance, model_data_dir, explict_temp_dir):
    """Test that workflow can be initialized and files can be retrieved."""
    input_file_path = model_data_dir / "minimal_model_2.cdb"

    if explict_temp_dir is not None:
        working_dir = pathlib.Path(explict_temp_dir.name)
    else:
        working_dir = None

    workflow = ACPWorkflow(
        acp=acp_instance,
        cdb_file_path=input_file_path,
        local_working_directory=working_dir,
    )
    workflow.model.update()

    cbd_path = workflow.get_local_cdb_file()
    assert cbd_path == workflow.working_directory.path / f"{workflow.model.name}.cdb"
    assert cbd_path.is_file()

    acph5_path = workflow.get_local_acp_h5_file()
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

    workflow = ACPWorkflow(
        acp=acp_instance,
        cdb_file_path=input_file_path,
    )
    workflow.model.update()

    cad_geometry_file_path = model_data_dir / "square_and_solid.stp"
    cad_geometry = workflow.load_cad_geometry_from_local_file(cad_geometry_file_path)

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
