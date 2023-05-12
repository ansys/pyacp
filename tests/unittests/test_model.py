import os
import pathlib
import tempfile

from ansys.acp.core import Client

from .helpers import check_property


def test_unittest(grpc_server, model_data_dir):
    """
    Test basic properties of the model object
    """
    client = Client(server=grpc_server)

    input_file_path = model_data_dir / "ACP-Pre.h5"
    remote_path = client.upload_file(input_file_path)

    model = client.import_model(name="kiteboard", path=remote_path, format="ansys:h5")

    # TODO: re-activate these tests when the respective features are implemented
    # assert model.unit_system.type == "mks"

    check_property(model, name="name", value="kiteboard", set_value="kiteboard_renamed")
    # TODO: re-activate these tests when the respective features are implemented
    # check_property(model, name="save_path", value="")
    # check_property(model, name="format", value="ansys:h5")
    # check_property(model, name="cache_update_results", value=True, set_value=False),
    # check_property(model, name="path", value=input_file_path),
    check_property(model, name="use_nodal_thicknesses", value=False, set_value=True),
    check_property(model, name="draping_offset_correction", value=False, set_value=True),
    check_property(model, name="angle_tolerance", value=1.0, set_value=2.0),
    check_property(model, name="relative_thickness_tolerance", value=0.01, set_value=0.03)

    # TODO: re-activate these tests when the respective features are implemented
    # The minimum analysis ply thickness is an absolute value, and depends on the
    # unit system being set. This is currently not implemented in PyACP, hence the
    # values are wrong (it's not using the expected unit system).
    # check_property(model, name="minimum_analysis_ply_thickness", value=1e-09, set_value=2e-09)
    # check_property(
    #     model,
    #     name="reference_surface_bounding_box",
    #     value=(
    #         (-0.6750000000000003, -0.2, 0.0005419999999999998),
    #         (0.6750000000000003, 0.20000000000000007, 0.0005420000000000003),
    #     ),
    # )

    with tempfile.TemporaryDirectory() as tmp_dir:
        working_dir = pathlib.Path(tmp_dir) / "workdir"
        os.makedirs(working_dir)
        # model.solver.working_dir = str(working_dir)

        save_path = os.path.join(os.path.dirname(remote_path), "test_model_serialization.acph5")
        model.save(save_path, save_cache=True)

        client.clear()

        model = client.import_model(path=save_path)

        # TODO: re-activate these tests when the respective features are implemented
        # assert model.unit_system.type == "mks"

        check_property(model, name="name", value="kiteboard_renamed")
        # TODO: re-activate these tests when the respective features are implemented
        # check_property(model, name="save_path", value=save_path)
        # check_property(model, name="format", value="ansys:h5")
        # check_property(model, name="cache_update_results", value=False)
        # check_property(model, name="path", value=input_file_path)
        check_property(model, name="use_nodal_thicknesses", value=True)
        check_property(model, name="draping_offset_correction", value=True)
        check_property(model, name="angle_tolerance", value=2.0)
        check_property(model, name="relative_thickness_tolerance", value=0.03)

        # TODO: re-activate these tests when the respective features are implemented
        # check_property(model, name="minimum_analysis_ply_thickness", value=2e-09)
        # check_property(
        #     model,
        #     name="reference_surface_bounding_box",
        #     value=(
        #         (-0.6750000000000003, -0.2, 0.0005419999999999998),
        #         (0.6750000000000003, 0.20000000000000007, 0.0005420000000000003),
        #     ),
        # )

        # rel_path_posix = pathlib.Path(relpath_if_possible(model.solver.working_dir)).as_posix()
        # # To ensure platform independency we store file paths using POSIX format
        # assert model.solver.working_dir == rel_path_posix


def test_save_analysis_model(grpc_server, model_data_dir):
    """
    Test that 'save_analysis_model' produces a file. The contents of the file
    are not checked.
    """
    client = Client(server=grpc_server)
    input_file_path = model_data_dir / "minimal_model_2.cdb"
    remote_file_path = client.upload_file(input_file_path)
    remote_workdir = remote_file_path.parent
    model = client.import_model(
        name="minimal_model", path=remote_file_path, format="ansys:cdb", unit_system="mpa"
    )

    out_file_path = remote_workdir / "out_file.cdb"
    model.save_analysis_model(out_file_path)
    with tempfile.TemporaryDirectory() as tmp_dir:
        local_file_path = pathlib.Path(tmp_dir, "out_file.cdb")
        client.download_file(out_file_path, local_file_path)
        assert local_file_path.exists()


def test_string_representation(grpc_server, model_data_dir):
    client = Client(server=grpc_server)
    input_file_path = model_data_dir / "ACP-Pre.h5"
    remote_file_path = client.upload_file(input_file_path)
    model = client.import_model(name="minimal_model", path=remote_file_path, format="ansys:cdb")

    assert repr(model) == "<Model with name 'minimal_model'>"

    model_str = str(model)
    assert model_str.startswith("Model(")
    assert f"name='{model.name}'" in model_str
