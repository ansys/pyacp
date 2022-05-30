import os
import pathlib
import tempfile

from ansys.acp.core import DB
from helpers import check_property
from helpers import relpath_if_possible
from helpers import suppress_for_pyacp


def test_unittest(db_kwargs, model_data_dir_server, convert_temp_path):
    """
    Test basic properties of the model object
    """
    db = DB(**db_kwargs)
    db.clear()

    input_file_path = model_data_dir_server / "ACP-Pre.h5"
    db.import_model(name="kiteboard", path=input_file_path, format="ansys:h5")
    model = db.active_model

    with suppress_for_pyacp():
        assert model.unit_system.type == "mks"

    check_property(model, name="name", value="kiteboard", set_value="kiteboard_renamed")
    with suppress_for_pyacp():
        check_property(model, name="save_path", value="")
        check_property(model, name="format", value="ansys:h5")
        check_property(model, name="cache_update_results", value=True, set_value=False),
        check_property(model, name="path", value=input_file_path),
    check_property(model, name="use_nodal_thicknesses", value=False, set_value=True),
    check_property(model, name="draping_offset_correction", value=False, set_value=True),
    check_property(model, name="use_default_section_tolerances", value=True, set_value=False),
    check_property(model, name="angle_tolerance", value=1.0, set_value=2.0),
    check_property(model, name="relative_thickness_tolerance", value=0.01, set_value=0.03)

    with suppress_for_pyacp():
        # The minimum analysis ply thickness is an absolute value, and depends on the
        # unit system being set. This is currently not implemented in PyACP, hence the
        # values are wrong (it's not using the expected unit system).
        check_property(model, name="minimum_analysis_ply_thickness", value=1e-09, set_value=2e-09)
    with suppress_for_pyacp():
        check_property(
            model,
            name="reference_surface_bounding_box",
            value=(
                (-0.6750000000000003, -0.2, 0.0005419999999999998),
                (0.6750000000000003, 0.20000000000000007, 0.0005420000000000003),
            ),
        )

    with tempfile.TemporaryDirectory() as tmp_dir:
        working_dir = pathlib.Path(tmp_dir) / "workdir"
        os.makedirs(working_dir)
        # model.solver.working_dir = str(working_dir)

        save_path = convert_temp_path(pathlib.Path(tmp_dir) / "test_model_serialization.acph5")
        model.save(save_path, save_cache=True)

        db.clear()

        # TODO: originally used db.open(save_path)
        db.import_model(path=save_path)

        model = db.active_model
        with suppress_for_pyacp():
            assert model.unit_system.type == "mks"

        check_property(model, name="name", value="kiteboard_renamed")
        with suppress_for_pyacp():
            check_property(model, name="save_path", value=save_path)
            check_property(model, name="format", value="ansys:h5")
            check_property(model, name="cache_update_results", value=False)
            check_property(model, name="path", value=input_file_path)
        check_property(model, name="use_nodal_thicknesses", value=True)
        check_property(model, name="draping_offset_correction", value=True)
        check_property(model, name="use_default_section_tolerances", value=False)
        check_property(model, name="angle_tolerance", value=2.0)
        check_property(model, name="relative_thickness_tolerance", value=0.03)
        with suppress_for_pyacp():
            check_property(model, name="minimum_analysis_ply_thickness", value=2e-09)
            check_property(
                model,
                name="reference_surface_bounding_box",
                value=(
                    (-0.6750000000000003, -0.2, 0.0005419999999999998),
                    (0.6750000000000003, 0.20000000000000007, 0.0005420000000000003),
                ),
            )

            rel_path_posix = pathlib.Path(relpath_if_possible(model.solver.working_dir)).as_posix()
            # To ensure platform independency we store file paths using POSIX format
            assert model.solver.working_dir == rel_path_posix
