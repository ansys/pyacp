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

from ansys.acp.core import ElementalDataType, UnitSystemType
from ansys.acp.core.mesh_data import VectorData

from .helpers import check_property


def test_unittest(acp_instance, model_data_dir):
    """
    Test basic properties of the model object
    """
    input_file_path = model_data_dir / "ACP-Pre.h5"
    model = acp_instance.import_model(name="kiteboard", path=input_file_path, format="ansys:h5")

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

        with tempfile.TemporaryDirectory() as local_working_dir:
            save_path = pathlib.Path(local_working_dir) / "test_model_serialization.acph5"
            model.save(save_path, save_cache=True)
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
    model = acp_instance.import_model(
        name="minimal_model", path=input_file_path, format="ansys:cdb", unit_system="mpa"
    )

    with tempfile.TemporaryDirectory() as tmp_dir:
        local_file_path = pathlib.Path(tmp_dir) / "out_file.cdb"
        model.export_analysis_model(local_file_path)
        assert local_file_path.exists()


def test_string_representation(acp_instance, model_data_dir):
    input_file_path = model_data_dir / "ACP-Pre.h5"
    model = acp_instance.import_model(
        name="minimal_model",
        path=input_file_path,
        format="ansys:cdb",
        unit_system=UnitSystemType.MKS,
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


@pytest.mark.plotting
def test_mesh_data_to_pyvista(minimal_complete_model):
    import pyvista

    pv_mesh = minimal_complete_model.mesh.to_pyvista()
    assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
    assert pv_mesh.n_points == 4
    assert pv_mesh.n_cells == 1


@pytest.mark.plotting
def test_elemental_data_to_pyvista(minimal_complete_model):
    import pyvista

    data = minimal_complete_model.elemental_data
    pv_mesh = data.get_pyvista_mesh(mesh=minimal_complete_model.mesh)
    assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
    assert pv_mesh.n_points == 4
    assert pv_mesh.n_cells == 1


@pytest.mark.plotting
@pytest.mark.parametrize("component", [e.value for e in ElementalDataType])
def test_elemental_data_to_pyvista_with_component(minimal_complete_model, component):
    import pyvista

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


def test_modeling_ply_export(acp_instance, minimal_complete_model, raises_before_version):
    """
    Test that the 'export_modeling_ply_geometries' method produces a file.
    The contents of the file are not checked.
    """
    out_filename = "modeling_ply_export.step"

    with tempfile.TemporaryDirectory() as tmp_dir:
        out_file_path = pathlib.Path(tmp_dir) / out_filename

        with raises_before_version("25.1"):
            minimal_complete_model.export_modeling_ply_geometries(out_file_path)
            assert out_file_path.exists()


def test_parent_access_raises(minimal_complete_model):
    with pytest.raises(RuntimeError) as exc:
        minimal_complete_model.parent
    assert "parent" in str(exc.value)


@pytest.mark.parametrize("unit_system", UnitSystemType)
def test_change_unit_system(minimal_complete_model, unit_system, raises_before_version):
    assert minimal_complete_model.unit_system == UnitSystemType.MPA

    initial_node_coords = minimal_complete_model.mesh.node_coordinates
    initial_minimum_analysis_ply_thickness = minimal_complete_model.minimum_analysis_ply_thickness

    conversion_factor_by_us = {
        "mpa": 1.0,
        "mks": 1e-3,
        "cgs": 0.1,
        "si": 1e-3,
        "bin": 0.03937008,
        "bft": 0.00328084,
        "umks": 1e3,
    }

    with raises_before_version("25.1"):
        if unit_system in (UnitSystemType.UNDEFINED, UnitSystemType.FROM_FILE):
            with pytest.raises(ValueError):
                minimal_complete_model.unit_system = unit_system
        else:
            minimal_complete_model.unit_system = unit_system
            assert minimal_complete_model.unit_system == unit_system
            minimal_complete_model.update()

            np.testing.assert_allclose(
                minimal_complete_model.mesh.node_coordinates,
                initial_node_coords * conversion_factor_by_us[unit_system.value],
            )
            np.testing.assert_allclose(
                minimal_complete_model.minimum_analysis_ply_thickness,
                initial_minimum_analysis_ply_thickness * conversion_factor_by_us[unit_system.value],
            )


def test_material_export(minimal_complete_model):
    """Check that the 'export_materials' method produces a file."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        export_path = pathlib.Path(tmp_dir) / "material_exported.xml"
        minimal_complete_model.export_materials(export_path)

        assert export_path.exists()
        assert os.stat(export_path).st_size > 0


def test_material_import(minimal_complete_model, raises_before_version):
    # GIVEN: a model, and a material XML file containing a material which is
    # not present in the model

    with tempfile.TemporaryDirectory() as export_dir:
        new_mat_id = "New Material"
        export_file_path = pathlib.Path(export_dir) / "material_exported.xml"
        mat = minimal_complete_model.materials["Structural Steel"].clone()
        mat.name = new_mat_id
        mat.store(parent=minimal_complete_model)
        minimal_complete_model.export_materials(export_file_path)
        del minimal_complete_model.materials[new_mat_id]
        assert new_mat_id not in minimal_complete_model.materials

        with raises_before_version("25.1"):
            # WHEN: the materials are imported
            minimal_complete_model.import_materials(export_file_path)

            # THEN: the new material should be present in the model
            assert new_mat_id in minimal_complete_model.materials


@pytest.mark.parametrize(
    "layup_representation_3d",
    [True, False],
)
@pytest.mark.parametrize(
    "offset_type",
    ["bottom_offset", "middle_offset", "top_offset"],
)
def test_hdf5_composite_cae_export(
    acp_instance,
    minimal_complete_model,
    raises_before_version,
    layup_representation_3d,
    offset_type,
):
    with raises_before_version("25.1"):
        with tempfile.TemporaryDirectory() as tmp_dir:
            export_file = pathlib.Path(tmp_dir) / "model_export.h5"
            minimal_complete_model.export_hdf5_composite_cae(
                export_file,
                layup_representation_3d=layup_representation_3d,
                offset_type=offset_type,
            )

            assert export_file.exists()
            assert os.stat(export_file).st_size > 0


def test_hdf5_composite_cae_export_with_scope(
    acp_instance, minimal_complete_model, raises_before_version
):
    with raises_before_version("25.1"):
        with tempfile.TemporaryDirectory() as tmp_dir:
            export_file = pathlib.Path(tmp_dir) / "model_export.h5"
            minimal_complete_model.export_hdf5_composite_cae(
                export_file,
                all_elements=False,
                element_sets=minimal_complete_model.element_sets.values(),
                all_plies=False,
                plies=minimal_complete_model.modeling_groups[
                    "ModelingGroup.1"
                ].modeling_plies.values(),
            )

            assert export_file.exists()
            assert os.stat(export_file).st_size > 0


@pytest.mark.parametrize(
    "import_mode",
    ["append", "overwrite"],
)
@pytest.mark.parametrize(
    "projection_mode",
    ["shell", "solid"],
)
def test_hdf5_composite_cae_export_import(
    minimal_complete_model,
    raises_before_version,
    import_mode,
    projection_mode,
):
    with raises_before_version("25.1"):
        with tempfile.TemporaryDirectory() as tmp_dir:
            export_file = pathlib.Path(tmp_dir) / "model_export.h5"
            minimal_complete_model.export_hdf5_composite_cae(export_file)
            minimal_complete_model.import_hdf5_composite_cae(
                export_file,
                import_mode=import_mode,
                projection_mode=projection_mode,
            )
