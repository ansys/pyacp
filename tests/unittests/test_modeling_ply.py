import numpy as np
import numpy.testing
import pytest
import pyvista

from ansys.acp.core import ElementalDataType, LinkedSelectionRule, NodalDataType, Fabric, Stackup, SubLaminate
from ansys.acp.core._tree_objects.enums import BooleanOperationType

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
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "oriented_selection_sets": [],
        "ply_material": None,
        "ply_angle": 0.0,
        "active": True,
        "global_ply_nr": AnyThing(),
    }
    CREATE_METHOD_NAME = "create_modeling_ply"

    @staticmethod
    @pytest.fixture(params=["create_fabric", "create_stackup", "create_sublaminate"])
    def object_properties(request, parent_model):
        oriented_selection_sets = [parent_model.create_oriented_selection_set() for _ in range(3)]
        create_method = getattr(parent_model, request.param, None)
        ply_material = create_method()
        if not isinstance(ply_material, (Fabric, Stackup, SubLaminate)):
            raise RuntimeError("Unsupported ply material!")
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
                            selection_rule=parent_model.create_boolean_selection_rule(),
                            operation_type=BooleanOperationType.REMOVE,
                            template_rule=False,
                            parameter_1=4.0,
                            parameter_2=9.2,
                        ),
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
    numpy.testing.assert_allclose(data.element_labels, np.array([1]))
    numpy.testing.assert_allclose(data.normal, np.array([[0.0, 0.0, 1.0]]))

    numpy.testing.assert_allclose(
        data.orientation,
        np.array([[0.0, 0.0, 1.0]]),
        atol=1e-12,
    )
    numpy.testing.assert_allclose(
        data.reference_direction,
        np.array([[1.0, 0.0, 0.0]]),
        atol=1e-12,
    )
    numpy.testing.assert_allclose(
        data.fiber_direction,
        np.array([[1.0, 0.0, 0.0]]),
        atol=1e-12,
    )
    numpy.testing.assert_allclose(
        data.draped_fiber_direction,
        np.array([[1.0, 0.0, 0.0]]),
        atol=1e-12,
    )
    numpy.testing.assert_allclose(
        data.transverse_direction,
        np.array([[0.0, 1.0, 0.0]]),
        atol=1e-12,
    )
    numpy.testing.assert_allclose(
        data.draped_transverse_direction,
        np.array([[0.0, 1.0, 0.0]]),
        atol=1e-12,
    )

    numpy.testing.assert_allclose(data.thickness, np.array([1e-4]))
    numpy.testing.assert_allclose(data.relative_thickness_correction, np.array([1.0]))

    numpy.testing.assert_allclose(data.design_angle, np.array([0.0]))
    numpy.testing.assert_allclose(data.shear_angle, np.array([0.0]))
    numpy.testing.assert_allclose(data.draped_fiber_angle, np.array([0.0]))
    numpy.testing.assert_allclose(data.draped_transverse_angle, np.array([90.0]))

    numpy.testing.assert_allclose(data.area, np.array([9e4]))
    numpy.testing.assert_allclose(data.price, np.array([0.0]))
    numpy.testing.assert_allclose(data.volume, np.array([9.0]))
    numpy.testing.assert_allclose(data.mass, np.array([7.065e-08]))
    numpy.testing.assert_allclose(data.offset, np.array([5e-5]))
    numpy.testing.assert_allclose(data.cog, np.array([[0.0, 0.0, 5e-5]]))


def test_nodal_data(simple_modeling_ply):
    data = simple_modeling_ply.nodal_data
    numpy.testing.assert_allclose(data.node_labels, np.array([1, 2, 3, 4]))
    numpy.testing.assert_allclose(
        data.ply_offset,
        np.array([[0.0, 0.0, 5e-5], [0.0, 0.0, 5e-5], [0.0, 0.0, 5e-5], [0.0, 0.0, 5e-5]]),
    )


def test_elemental_data_to_pyvista(minimal_complete_model, simple_modeling_ply):
    elemental_data = simple_modeling_ply.elemental_data
    pv_mesh = elemental_data.to_pyvista(mesh=minimal_complete_model.mesh)
    assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
    assert pv_mesh.n_points == 4
    assert pv_mesh.n_cells == 1


@pytest.mark.parametrize("component", [e.value for e in ElementalDataType])
def test_elemental_data_to_pyvista_with_component(
    minimal_complete_model, simple_modeling_ply, component
):
    data = simple_modeling_ply.elemental_data
    if not hasattr(data, component):
        pytest.skip(f"Modeling Ply elemental data does not contain component '{component}'")
    pv_mesh = data.to_pyvista(mesh=minimal_complete_model.mesh, component=component)
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
    data = simple_modeling_ply.nodal_data
    pv_mesh = data.to_pyvista(mesh=minimal_complete_model.mesh)
    assert isinstance(pv_mesh, pyvista.core.pointset.UnstructuredGrid)
    assert pv_mesh.n_points == 4
    assert pv_mesh.n_cells == 1


@pytest.mark.parametrize("component", [e.value for e in NodalDataType])
def test_nodal_data_to_pyvista_with_component(
    minimal_complete_model, simple_modeling_ply, component
):
    data = simple_modeling_ply.nodal_data
    if not hasattr(data, component):
        pytest.skip(f"Modeling Ply nodal data does not contain component '{component}'")
    pv_mesh = data.to_pyvista(mesh=minimal_complete_model.mesh, component=component)
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
