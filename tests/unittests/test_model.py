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

from __future__ import annotations

import os
import pathlib
import tempfile

import numpy as np
import numpy.testing
import pytest
import pyvista

from ansys.acp.core import ElementalDataType, VectorData

from .helpers import check_property


def test_unittest(acp_instance, model_data_dir):
    """
    Test basic properties of the model object
    """
    input_file_path = model_data_dir / "ACP-Pre.h5"
    remote_path = acp_instance.upload_file(input_file_path)

    model = acp_instance.import_model(name="kiteboard", path=remote_path, format="ansys:h5")

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

        if acp_instance.is_remote:
            save_path: str | pathlib.Path = os.path.join(
                os.path.dirname(remote_path), "test_model_serialization.acph5"
            )
            model.save(save_path, save_cache=True)
            acp_instance.clear()
            model = acp_instance.import_model(path=save_path)
        else:
            with tempfile.TemporaryDirectory() as local_working_dir:
                save_path = pathlib.Path(local_working_dir) / "test_model_serialization.acph5"
                acp_instance.save(save_path, save_cache=True)
                acp_instance.clear()
                model = acp_instance.import_model(path=save_path)

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


def test_export_analysis_model(acp_instance, model_data_dir):
    """
    Test that 'export_analysis_model' produces a file. The contents of the file
    are not checked.
    """
    input_file_path = model_data_dir / "minimal_model_2.cdb"
    remote_file_path = acp_instance.upload_file(input_file_path)
    remote_workdir = remote_file_path.parent
    model = acp_instance.import_model(
        name="minimal_model", path=remote_file_path, format="ansys:cdb", unit_system="mpa"
    )

    if acp_instance.is_remote:
        out_file_path = remote_workdir / "out_file.cdb"
        model.export_analysis_model(out_file_path)
        with tempfile.TemporaryDirectory() as tmp_dir:
            local_file_path = pathlib.Path(tmp_dir, "out_file.cdb")
            acp_instance.download_file(out_file_path, local_file_path)
            assert local_file_path.exists()
    else:
        with tempfile.TemporaryDirectory() as tmp_dir:
            local_file_path = pathlib.Path(tmp_dir) / "out_file.cdb"
            model.export_analysis_model(local_file_path)
            assert local_file_path.exists()


def test_string_representation(acp_instance, model_data_dir):
    input_file_path = model_data_dir / "ACP-Pre.h5"
    remote_file_path = acp_instance.upload_file(input_file_path)
    model = acp_instance.import_model(
        name="minimal_model", path=remote_file_path, format="ansys:cdb"
    )

    assert repr(model) == "<Model with name 'minimal_model'>"

    model_str = str(model)
    assert model_str.startswith("Model(")
    assert f"name='{model.name}'" in model_str


@pytest.fixture
def minimal_complete_model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


def test_mesh_data(minimal_complete_model):
    mesh = minimal_complete_model.mesh

    numpy.testing.assert_equal(mesh.node_labels, np.array([1, 2, 3, 4]))
    numpy.testing.assert_allclose(
        mesh.node_coordinates,
        np.array(
            [
                [-150.0, 150.0, 0.0],
                [-150.0, -150.0, 0.0],
                [150.0, -150.0, 0.0],
                [150.0, 150.0, 0.0],
            ]
        ),
    )
    numpy.testing.assert_equal(mesh.element_labels, np.array([1]))
    numpy.testing.assert_equal(mesh.element_types, np.array([126]))
    numpy.testing.assert_equal(mesh.element_nodes, np.array([0, 1, 2, 3]))
    numpy.testing.assert_equal(mesh.element_nodes_offsets, np.array([0]))


def test_elemental_data(minimal_complete_model):
    data = minimal_complete_model.elemental_data
    numpy.testing.assert_allclose(data.element_labels.values, np.array([1]))
    numpy.testing.assert_allclose(data.normal.values, np.array([[0.0, 0.0, 1.0]]))
    numpy.testing.assert_allclose(data.thickness.values, np.array([1e-4]))
    numpy.testing.assert_allclose(data.relative_thickness_correction.values, np.array([1.0]))
    numpy.testing.assert_allclose(data.area.values, np.array([9e4]))
    numpy.testing.assert_allclose(data.price.values, np.array([0.0]))
    numpy.testing.assert_allclose(data.volume.values, np.array([9.0]))
    numpy.testing.assert_allclose(data.mass.values, np.array([7.065e-08]))
    numpy.testing.assert_allclose(data.offset.values, np.array([5e-5]))
    numpy.testing.assert_allclose(data.cog.values, np.array([[0.0, 0.0, 5e-5]]))


def test_nodal_data(minimal_complete_model):
    data = minimal_complete_model.nodal_data
    numpy.testing.assert_allclose(data.node_labels.values, np.array([1, 2, 3, 4]))


def test_mesh_data_to_pyvista(minimal_complete_model):
    pv_mesh = minimal_complete_model.mesh.to_pyvista()
    assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
    assert pv_mesh.n_points == 4
    assert pv_mesh.n_cells == 1


def test_elemental_data_to_pyvista(minimal_complete_model):
    data = minimal_complete_model.elemental_data
    pv_mesh = data.get_pyvista_mesh(mesh=minimal_complete_model.mesh)
    assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
    assert pv_mesh.n_points == 4
    assert pv_mesh.n_cells == 1


@pytest.mark.parametrize("component", [e.value for e in ElementalDataType])
def test_elemental_data_to_pyvista_with_component(minimal_complete_model, component):
    data = minimal_complete_model.elemental_data
    if not hasattr(data, component):
        pytest.skip(f"Model elemental data does not contain component '{component}'")
    component_data = getattr(data, component)
    if isinstance(component_data, VectorData):
        pv_mesh = component_data.get_pyvista_glyphs(mesh=minimal_complete_model.mesh)
    else:
        pv_mesh = component_data.get_pyvista_mesh(mesh=minimal_complete_model.mesh)
    if component in ["normal", "cog"]:
        assert isinstance(pv_mesh, pyvista.core.pointset.PolyData)
    else:
        assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
        assert pv_mesh.n_points == 4
        assert pv_mesh.n_cells == 1


def test_regression_454(minimal_complete_model):
    """
    Regression test for issue #454
    The 'Model' object should not be clonable, as it is not directly
    constructible from its client-side representation.
    """
    assert not hasattr(minimal_complete_model, "clone")
    assert not hasattr(minimal_complete_model, "store")


def test_modeling_ply_export(acp_instance, minimal_complete_model):
    """
    Test that the 'export_modeling_ply_geometries' method produces a file.
    The contents of the file are not checked.
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        output_path = pathlib.Path(tmp_dir) / "modeling_ply_export.step"
        minimal_complete_model.export_modeling_ply_geometries(output_path)
        assert output_path.exists()

    out_filename = "modeling_ply_export.step"

    if acp_instance.is_remote:
        out_file_path = out_filename
        minimal_complete_model.export_modeling_ply_geometries(out_file_path)
        with tempfile.TemporaryDirectory() as tmp_dir:
            local_file_path = pathlib.Path(tmp_dir, out_filename)
            acp_instance.download_file(out_file_path, local_file_path)
            assert local_file_path.exists()
    else:
        with tempfile.TemporaryDirectory() as tmp_dir:
            local_file_path = pathlib.Path(tmp_dir) / out_filename
            minimal_complete_model.export_modeling_ply_geometries(local_file_path)
            assert local_file_path.exists()
