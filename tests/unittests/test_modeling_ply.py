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

from ansys.acp.core import (
    BooleanOperationType,
    CutoffSelectionRule,
    DrapingType,
    ElementalDataType,
    Fabric,
    LinkedSelectionRule,
    NodalDataType,
    Stackup,
    SubLaminate,
    TaperEdge,
    ThicknessFieldType,
    ThicknessType,
)
from ansys.acp.core.mesh_data import VectorData

from .common.linked_object_list_tester import LinkedObjectListTestCase, LinkedObjectListTester
from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester
from .common.utils import AnyThing


@pytest.fixture
def parent_model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def parent_object(parent_model):
    return parent_model.modeling_groups["ModelingGroup.1"]


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_modeling_ply()


class TestModelingPly(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "modeling_plies"
    CREATE_METHOD_NAME = "create_modeling_ply"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "oriented_selection_sets": [],
            "ply_material": None,
            "ply_angle": 0.0,
            "active": True,
            "global_ply_nr": AnyThing(),
            "draping_type": DrapingType.NO_DRAPING,
            "draping_seed_point": (0.0, 0.0, 0.0),
            "auto_draping_direction": True,
            "draping_direction": (1.0, 0.0, 0.0),
            "use_default_draping_mesh_size": True,
            "draping_mesh_size": 0.0,
            "draping_thickness_correction": True,
            "draping_angle_1_field": None,
            "draping_angle_2_field": None,
            "thickness_type": ThicknessType.NOMINAL,
            "thickness_geometry": None,
            "thickness_field": None,
            "thickness_field_type": ThicknessFieldType.ABSOLUTE_VALUES,
            "taper_edges": [],
        }

    @staticmethod
    @pytest.fixture(params=["create_fabric", "create_stackup", "create_sublaminate"])
    def object_properties(request, parent_model):
        oriented_selection_sets = [parent_model.create_oriented_selection_set() for _ in range(3)]
        create_method = getattr(parent_model, request.param)
        ply_material = create_method()
        if not isinstance(ply_material, (Fabric, Stackup, SubLaminate)):
            raise RuntimeError("Unsupported ply material!")
        lookup_table = parent_model.create_lookup_table_1d()
        column_1 = lookup_table.create_column()
        column_2 = lookup_table.create_column()
        return ObjectPropertiesToTest(
            read_write=[
                ("oriented_selection_sets", oriented_selection_sets),
                ("ply_material", ply_material),
                ("ply_angle", 0.5),
                ("active", False),
                ("global_ply_nr", AnyThing()),
                (
                    "selection_rules",
                    [
                        LinkedSelectionRule(
                            selection_rule=parent_model.create_parallel_selection_rule(),
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=False,
                            parameter_1=1.0,
                            parameter_2=2.0,
                        ),
                        LinkedSelectionRule(
                            selection_rule=parent_model.create_cylindrical_selection_rule(),
                            operation_type=BooleanOperationType.ADD,
                            template_rule=True,
                            parameter_1=1.1,
                            parameter_2=2.2,
                        ),
                        LinkedSelectionRule(
                            selection_rule=parent_model.create_spherical_selection_rule(),
                            operation_type=BooleanOperationType.REMOVE,
                            template_rule=True,
                            parameter_1=2.3,
                            parameter_2=-1.3,
                        ),
                        LinkedSelectionRule(
                            selection_rule=parent_model.create_tube_selection_rule(),
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=False,
                            parameter_1=1.3,
                            parameter_2=2.9,
                        ),
                        LinkedSelectionRule(
                            selection_rule=parent_model.create_variable_offset_selection_rule(),
                            operation_type=BooleanOperationType.ADD,
                            template_rule=False,
                            parameter_1=0.0,
                            parameter_2=0.0,
                        ),
                        LinkedSelectionRule(
                            selection_rule=parent_model.create_cutoff_selection_rule(),
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=True,
                            parameter_1=1.2,
                            parameter_2=3.9,
                        ),
                        LinkedSelectionRule(
                            selection_rule=parent_model.create_boolean_selection_rule(),
                            operation_type=BooleanOperationType.REMOVE,
                            template_rule=False,
                            parameter_1=4.0,
                            parameter_2=9.2,
                        ),
                    ],
                ),
                ("draping_seed_point", (0.0, 0.1, 0.2)),
                ("auto_draping_direction", False),
                ("draping_direction", (0.0, -1.0, 0.0)),
                ("use_default_draping_mesh_size", False),
                ("draping_mesh_size", 20.0),
                ("draping_thickness_correction", False),
                ("draping_angle_1_field", column_1),
                ("draping_angle_2_field", column_2),
                ("thickness_type", ThicknessType.FROM_GEOMETRY),
                ("thickness_geometry", parent_model.create_virtual_geometry()),
                ("thickness_type", ThicknessType.FROM_TABLE),
                ("thickness_field", column_1),
                ("thickness_field_type", ThicknessFieldType.RELATIVE_SCALING_FACTOR),
                (
                    "taper_edges",
                    [
                        TaperEdge(edge_set=parent_model.create_edge_set(), angle=1.2, offset=2.3),
                        TaperEdge(edge_set=parent_model.create_edge_set(), angle=3.4, offset=4.5),
                    ],
                ),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


@pytest.fixture
def linked_object_case(tree_object, parent_model):
    return LinkedObjectListTestCase(
        parent_object=tree_object,
        linked_attribute_name="oriented_selection_sets",
        existing_linked_object_names=(),
        linked_object_constructor=parent_model.create_oriented_selection_set,
    )


linked_object_case_empty = linked_object_case


@pytest.fixture
def linked_object_case_nonempty(tree_object, parent_model):
    tree_object.oriented_selection_sets = [parent_model.create_oriented_selection_set(name="OSS.1")]
    return LinkedObjectListTestCase(
        parent_object=tree_object,
        linked_attribute_name="oriented_selection_sets",
        existing_linked_object_names=("OSS.1",),
        linked_object_constructor=parent_model.create_oriented_selection_set,
    )


class TestLinkedObjectLists(LinkedObjectListTester):
    pass


@pytest.fixture
def minimal_complete_model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def simple_modeling_ply(minimal_complete_model):
    return minimal_complete_model.modeling_groups["ModelingGroup.1"].modeling_plies["ModelingPly.1"]


def test_elemental_data(simple_modeling_ply):
    data = simple_modeling_ply.elemental_data
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


def test_elemental_data_incomplete(simple_modeling_ply, minimal_complete_model):
    """Test the elemental data when draping properties are missing."""
    # draping-related properties are not propagated up to the modeling ply
    # when it has more than one production ply
    simple_modeling_ply.number_of_layers = 2
    minimal_complete_model.update()

    data = simple_modeling_ply.elemental_data
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
    assert data.draped_fiber_direction is None
    numpy.testing.assert_allclose(
        data.transverse_direction.values,
        np.array([[0.0, 1.0, 0.0]]),
        atol=1e-12,
    )
    assert data.draped_transverse_direction is None

    numpy.testing.assert_allclose(data.thickness.values, np.array([2e-4]))
    numpy.testing.assert_allclose(data.relative_thickness_correction.values, np.array([1.0]))

    numpy.testing.assert_allclose(data.design_angle.values, np.array([0.0]))
    assert data.shear_angle is None
    assert data.draped_fiber_angle is None
    assert data.draped_transverse_angle is None

    numpy.testing.assert_allclose(data.area.values, np.array([9e4]))
    numpy.testing.assert_allclose(data.price.values, np.array([0.0]))
    numpy.testing.assert_allclose(data.volume.values, np.array([18.0]))
    numpy.testing.assert_allclose(data.mass.values, np.array([14.130e-08]))
    numpy.testing.assert_allclose(data.offset.values, np.array([1e-4]))
    numpy.testing.assert_allclose(data.cog.values, np.array([[0.0, 0.0, 1e-4]]))


def test_nodal_data(simple_modeling_ply):
    data = simple_modeling_ply.nodal_data
    numpy.testing.assert_allclose(data.node_labels.values, np.array([1, 2, 3, 4]))
    numpy.testing.assert_allclose(
        data.ply_offset.values,
        np.array([[0.0, 0.0, 5e-5], [0.0, 0.0, 5e-5], [0.0, 0.0, 5e-5], [0.0, 0.0, 5e-5]]),
    )


@pytest.mark.plotting
def test_elemental_data_to_pyvista(minimal_complete_model, simple_modeling_ply):
    import pyvista

    elemental_data = simple_modeling_ply.elemental_data
    pv_mesh = elemental_data.get_pyvista_mesh(mesh=minimal_complete_model.mesh)
    assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
    assert pv_mesh.n_points == 4
    assert pv_mesh.n_cells == 1


@pytest.mark.plotting
@pytest.mark.parametrize("component", [e.value for e in ElementalDataType])
def test_elemental_data_to_pyvista_with_component(
    minimal_complete_model, simple_modeling_ply, component
):
    import pyvista

    data = simple_modeling_ply.elemental_data
    if not hasattr(data, component):
        pytest.skip(f"Modeling Ply elemental data does not contain component '{component}'")
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


def test_nodal_data_to_pyvista(minimal_complete_model, simple_modeling_ply):
    import pyvista

    data = simple_modeling_ply.nodal_data
    pv_mesh = data.get_pyvista_mesh(mesh=minimal_complete_model.mesh)
    assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
    assert pv_mesh.n_points == 4
    assert pv_mesh.n_cells == 1


@pytest.mark.plotting
@pytest.mark.parametrize("component", [e.value for e in NodalDataType])
def test_nodal_data_to_pyvista_with_component(
    minimal_complete_model, simple_modeling_ply, component
):
    import pyvista

    data = simple_modeling_ply.nodal_data
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


def test_linked_selection_rule_parameters(simple_modeling_ply, minimal_complete_model):
    parallel_selection_rule = minimal_complete_model.create_parallel_selection_rule(
        origin=(0.0, 0.0, 0.0), direction=(1.0, 0.0, 0.0), lower_limit=0.005, upper_limit=1.0
    )
    linked_parallel_rule = LinkedSelectionRule(parallel_selection_rule, template_rule=True)
    simple_modeling_ply.selection_rules = [linked_parallel_rule]

    linked_parallel_rule.parameter_1 = 1.0
    minimal_complete_model.update()

    assert linked_parallel_rule.parameter_1 == simple_modeling_ply.selection_rules[0].parameter_1

    linked_rule_in_ply = simple_modeling_ply.selection_rules[0]
    linked_rule_in_ply.parameter_1 = 1
    assert linked_parallel_rule.parameter_1 == simple_modeling_ply.selection_rules[0].parameter_1


@pytest.mark.parametrize(
    "operation_type", [e for e in BooleanOperationType if e != BooleanOperationType.INTERSECT]
)
def test_linked_cutoff_selection_rule_operation_type(operation_type):
    """Check that CutoffSelectionRule only allows INTERSECT operation type."""
    with pytest.raises(ValueError) as exc:
        LinkedSelectionRule(
            selection_rule=CutoffSelectionRule(),
            operation_type=operation_type,
        )
    assert "INTERSECT" in str(exc.value)
