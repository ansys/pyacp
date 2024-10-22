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

import numpy as np
import numpy.testing
import pytest
import pyvista

from ansys.acp.core import (
    ImportedPlyDrapingType,
    ImportedPlyOffsetType,
    ImportedPlyThicknessType,
    RosetteSelectionMethod,
    MeshImportType,
    ElementalDataType,
    NodalDataType,
    ThicknessFieldType,
    VectorData,
)

from .common.linked_object_list_tester import LinkedObjectListTestCase, LinkedObjectListTester
from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def minimal_complete_model(load_model_imported_plies_from_tempfile):
    with load_model_imported_plies_from_tempfile() as model:
        yield model


@pytest.fixture
def parent_object(minimal_complete_model):
    return minimal_complete_model.imported_modeling_groups["by hdf5"]


@pytest.fixture
def existing_imported_modeling_ply(minimal_complete_model):
    return minimal_complete_model.imported_modeling_groups["by hdf5"].imported_modeling_plies["ud"]

@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_imported_modeling_ply()


class TestImportedModelingPly(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "imported_modeling_plies"
    CREATE_METHOD_NAME = "create_imported_modeling_ply"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "active": True,
            "offset_type": ImportedPlyOffsetType.MIDDLE_OFFSET,
            "mesh_import_type": MeshImportType.FROM_GEOMETRY,
            "rosette_selection_method": "minimum_angle",
            "rosettes": [],
            "reference_direction_field": None,
            "rotation_angle": 0.0,
            "ply_material": None,
            "ply_angle": 0.0,
            "draping": ImportedPlyDrapingType.NO_DRAPING,
            "draping_angle_1_field": None,
            "draping_angle_2_field": None,
            "thickness_type": ImportedPlyThicknessType.NOMINAL,
            "thickness_field": None,
            "thickness_field_type": ThicknessFieldType.ABSOLUTE_VALUES,
        }

    @staticmethod
    @pytest.fixture(params=[v.value for v in ImportedPlyOffsetType])
    def object_properties(request, minimal_complete_model):
        ply_material = minimal_complete_model.create_fabric()
        create_lut_method = getattr(minimal_complete_model, "create_lookup_table_1d")
        lookup_table = create_lut_method()
        column_1 = lookup_table.create_column()
        column_2 = lookup_table.create_column()
        rosette = minimal_complete_model.create_rosette()
        virtual_geometry = minimal_complete_model.create_virtual_geometry()

        return ObjectPropertiesToTest(
            read_write=[
                ("active", False),
                ("offset_type", request.param),
                ("mesh_import_type", MeshImportType.FROM_GEOMETRY),
                ("mesh_geometry", virtual_geometry),
                ("rosette_selection_method", RosetteSelectionMethod.MINIMUM_DISTANCE),
                ("rosettes", [rosette]),
                ("reference_direction_field", column_1),
                ("rotation_angle", 67.2),
                ("ply_material", ply_material),
                ("ply_angle", 34.5),
                ("draping", ImportedPlyDrapingType.TABULAR_VALUES),
                ("draping_angle_1_field", column_1),
                ("draping_angle_2_field", column_2),
                ("thickness_type", ImportedPlyThicknessType.FROM_TABLE),
                ("thickness_field", column_1),
                ("thickness_field_type", ThicknessFieldType.RELATIVE_SCALING_FACTOR),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


@pytest.fixture
def linked_object_case(tree_object, minimal_complete_model):
    return LinkedObjectListTestCase(
        parent_object=tree_object,
        linked_attribute_name="rosettes",
        existing_linked_object_names=(),
        linked_object_constructor=minimal_complete_model.create_rosette,
    )


linked_object_case_empty = linked_object_case


@pytest.fixture
def linked_object_case_nonempty(tree_object, minimal_complete_model):
    tree_object.rosettes = [minimal_complete_model.create_rosette(name="rosette 32")]
    return LinkedObjectListTestCase(
        parent_object=tree_object,
        linked_attribute_name="rosettes",
        existing_linked_object_names=("rosette 32",),
        linked_object_constructor=minimal_complete_model.create_rosette,
    )

class TestLinkedObjectLists(LinkedObjectListTester):
    pass


#@pytest.fixture
#def minimal_complete_model(load_model_from_tempfile):
#    with load_model_from_tempfile() as model:
#        yield model


#@pytest.fixture
#def simple_imported_modeling_ply(minimal_complete_model):
#    return minimal_complete_model.modeling_groups["ModelingGroup.1"].modeling_plies["ModelingPly.1"]


def test_elemental_data(existing_imported_modeling_ply):
    data = existing_imported_modeling_ply.elemental_data
    numpy.testing.assert_allclose(data.element_labels.values, np.array([1]))
    numpy.testing.assert_allclose(data.normal.values, np.array([[0.0, 0.0, 1.0]]))

    numpy.testing.assert_allclose(
        data.orientation.values,
        np.array([[0.0, 0.0, 1.0]]),
        atol=1e-12,
    )
    numpy.testing.assert_allclose(
        data.reference_direction.values,
        np.array([[1.0, 0.0, 0.0]]),
        atol=1e-12,
    )
    numpy.testing.assert_allclose(
        data.fiber_direction.values,
        np.array([[1.0, 0.0, 0.0]]),
        atol=1e-12,
    )
    numpy.testing.assert_allclose(
        data.draped_fiber_direction.values,
        np.array([[1.0, 0.0, 0.0]]),
        atol=1e-12,
    )
    numpy.testing.assert_allclose(
        data.transverse_direction.values,
        np.array([[0.0, 1.0, 0.0]]),
        atol=1e-12,
    )
    numpy.testing.assert_allclose(
        data.draped_transverse_direction.values,
        np.array([[0.0, 1.0, 0.0]]),
        atol=1e-12,
    )

    numpy.testing.assert_allclose(data.thickness.values, np.array([1e-4]))
    numpy.testing.assert_allclose(data.relative_thickness_correction.values, np.array([1.0]))

    numpy.testing.assert_allclose(data.design_angle.values, np.array([0.0]))
    numpy.testing.assert_allclose(data.shear_angle.values, np.array([0.0]))
    numpy.testing.assert_allclose(data.draped_fiber_angle.values, np.array([0.0]))
    numpy.testing.assert_allclose(data.draped_transverse_angle.values, np.array([90.0]))

    numpy.testing.assert_allclose(data.area.values, np.array([9e4]))
    numpy.testing.assert_allclose(data.price.values, np.array([0.0]))
    numpy.testing.assert_allclose(data.volume.values, np.array([9.0]))
    numpy.testing.assert_allclose(data.mass.values, np.array([7.065e-08]))
    numpy.testing.assert_allclose(data.offset.values, np.array([5e-5]))
    numpy.testing.assert_allclose(data.cog.values, np.array([[0.0, 0.0, 5e-5]]))


def test_nodal_data(existing_imported_modeling_ply):
    data = existing_imported_modeling_ply.nodal_data
    numpy.testing.assert_allclose(data.node_labels.values, np.array([1, 2, 3, 4]))
    numpy.testing.assert_allclose(
        data.ply_offset.values,
        np.array([[0.0, 0.0, 5e-5], [0.0, 0.0, 5e-5], [0.0, 0.0, 5e-5], [0.0, 0.0, 5e-5]]),
    )


def test_elemental_data_to_pyvista(minimal_complete_model, existing_imported_modeling_ply):
    elemental_data = existing_imported_modeling_ply.elemental_data
    pv_mesh = elemental_data.get_pyvista_mesh(mesh=existing_imported_modeling_ply.mesh)
    assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
    assert pv_mesh.n_points == 4
    assert pv_mesh.n_cells == 1


@pytest.mark.parametrize("component", [e.value for e in ElementalDataType])
def test_elemental_data_to_pyvista_with_component(
    minimal_complete_model, existing_imported_modeling_ply, component
):
    data = existing_imported_modeling_ply.elemental_data
    if not hasattr(data, component):
        pytest.skip(f"Imported Modeling Ply elemental data does not contain component '{component}'")
    component_data = getattr(data, component)
    if isinstance(component_data, VectorData):
        pv_mesh = component_data.get_pyvista_glyphs(mesh=minimal_complete_model.mesh, factor=0.01)
    else:
        pv_mesh = component_data.get_pyvista_mesh(mesh=minimal_complete_model.mesh)
    if component in [
        "normal",
        "orientation",
        "reference_direction",
        "fiber_direction",
        "draped_fiber_direction",
        "transverse_direction",
        "draped_transverse_direction",
        "cog",
    ]:
        assert isinstance(
            pv_mesh, pyvista.core.pointset.PolyData
        ), f"Created wrong mesh type PolyData for component '{component}'"
    else:
        assert isinstance(
            pv_mesh, pyvista.core.pointset.UnstructuredGrid
        ), f"Created wrong mesh type UnstructuredGrid for component '{component}'"
        assert pv_mesh.n_points == 4
        assert pv_mesh.n_cells == 1


def test_nodal_data_to_pyvista(minimal_complete_model, existing_imported_modeling_ply):
    data = existing_imported_modeling_ply.nodal_data
    pv_mesh = data.get_pyvista_mesh(mesh=minimal_complete_model.mesh)
    assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
    assert pv_mesh.n_points == 4
    assert pv_mesh.n_cells == 1


@pytest.mark.parametrize("component", [e.value for e in NodalDataType])
def test_nodal_data_to_pyvista_with_component(
    minimal_complete_model, existing_imported_modeling_ply, component
):
    data = existing_imported_modeling_ply.nodal_data
    if not hasattr(data, component):
        pytest.skip(f"Modeling Ply nodal data does not contain component '{component}'")

    component_data = getattr(data, component)
    if isinstance(component_data, VectorData):
        pv_mesh = component_data.get_pyvista_glyphs(mesh=minimal_complete_model.mesh, factor=0.01)
    else:
        pv_mesh = component_data.get_pyvista_mesh(mesh=minimal_complete_model.mesh)
    if component in ["ply_offset"]:
        assert isinstance(
            pv_mesh, pyvista.core.pointset.PolyData
        ), f"Created wrong mesh type PolyData for component '{component}'"
    else:
        assert isinstance(
            pv_mesh, pyvista.core.pointset.UnstructuredGrid
        ), f"Created wrong mesh type UnstructuredGrid for component '{component}'"
        assert pv_mesh.n_points == 4
        assert pv_mesh.n_cells == 1

