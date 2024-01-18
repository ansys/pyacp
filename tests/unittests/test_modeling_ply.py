import numpy as np
import numpy.testing
import pytest
import pyvista

from ansys.acp.core import (
    BooleanSelectionRule,
    CylindricalSelectionRule,
    EdgeSet,
    ElementalDataType,
    Fabric,
    LinkedSelectionRule,
    LookUpTable1D,
    LookUpTable1DColumn,
    ModelingPly,
    NodalDataType,
    OrientedSelectionSet,
    ParallelSelectionRule,
    SphericalSelectionRule,
    Stackup,
    SubLaminate,
    TaperEdge,
    TubeSelectionRule,
    VariableOffsetSelectionRule,
    VirtualGeometry,
)
from ansys.acp.core._tree_objects.enums import (
    BooleanOperationType,
    DrapingType,
    ThicknessFieldType,
    ThicknessType,
)

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
    modeling_ply = ModelingPly()
    parent_object.add_modeling_ply(modeling_ply)
    return modeling_ply


class TestModelingPly(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "modeling_plies"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "oriented_selection_sets": [],
        "ply_material": None,
        "ply_angle": 0.0,
        "active": True,
        "global_ply_nr": AnyThing(),
        "draping": DrapingType.NO_DRAPING,
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
    OBJECT_CLS = ModelingPly
    ADD_METHOD_NAME = "add_modeling_ply"

    @staticmethod
    @pytest.fixture(
        params=[("add_fabric", Fabric), ("add_stackup", Stackup), ("add_sublaminate", SubLaminate)]
    )
    def object_properties(request, parent_model):
        oriented_selection_sets = [OrientedSelectionSet() for _ in range(3)]
        for oss in oriented_selection_sets:
            parent_model.add_oriented_selection_set(oss)
        add_method_name, material_cls = request.param
        ply_material = material_cls()
        getattr(parent_model, add_method_name)(ply_material)
        if not isinstance(ply_material, (Fabric, Stackup, SubLaminate)):
            raise RuntimeError("Unsupported ply material!")

        lookup_table = LookUpTable1D()
        parent_model.add_lookup_table_1d(lookup_table)

        column_1 = LookUpTable1DColumn()
        lookup_table.add_column(column_1)
        column_2 = LookUpTable1DColumn()
        lookup_table.add_column(column_2)

        parallel_selection_rule = ParallelSelectionRule()
        parent_model.add_parallel_selection_rule(parallel_selection_rule)
        cylindrical_selection_rule = CylindricalSelectionRule()
        parent_model.add_cylindrical_selection_rule(cylindrical_selection_rule)
        spherical_selection_rule = SphericalSelectionRule()
        parent_model.add_spherical_selection_rule(spherical_selection_rule)
        tube_selection_rule = TubeSelectionRule()
        parent_model.add_tube_selection_rule(tube_selection_rule)
        variable_offset_selection_rule = VariableOffsetSelectionRule()
        parent_model.add_variable_offset_selection_rule(variable_offset_selection_rule)
        boolean_selection_rule = BooleanSelectionRule()
        parent_model.add_boolean_selection_rule(boolean_selection_rule)

        virtual_geometry = VirtualGeometry()
        parent_model.add_virtual_geometry(virtual_geometry)

        edge_set_1 = EdgeSet()
        parent_model.add_edge_set(edge_set_1)
        edge_set_2 = EdgeSet()
        parent_model.add_edge_set(edge_set_2)

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
                            selection_rule=parallel_selection_rule,
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=False,
                            parameter_1=1.0,
                            parameter_2=2.0,
                        ),
                        LinkedSelectionRule(
                            selection_rule=cylindrical_selection_rule,
                            operation_type=BooleanOperationType.ADD,
                            template_rule=True,
                            parameter_1=1.1,
                            parameter_2=2.2,
                        ),
                        LinkedSelectionRule(
                            selection_rule=spherical_selection_rule,
                            operation_type=BooleanOperationType.REMOVE,
                            template_rule=True,
                            parameter_1=2.3,
                            parameter_2=-1.3,
                        ),
                        LinkedSelectionRule(
                            selection_rule=tube_selection_rule,
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=False,
                            parameter_1=1.3,
                            parameter_2=2.9,
                        ),
                        LinkedSelectionRule(
                            selection_rule=variable_offset_selection_rule,
                            operation_type=BooleanOperationType.ADD,
                            template_rule=False,
                            parameter_1=0.0,
                            parameter_2=0.0,
                        ),
                        LinkedSelectionRule(
                            selection_rule=boolean_selection_rule,
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
                ("thickness_geometry", virtual_geometry),
                ("thickness_type", ThicknessType.FROM_TABLE),
                ("thickness_field", column_1),
                ("thickness_field_type", ThicknessFieldType.RELATIVE_SCALING_FACTOR),
                (
                    "taper_edges",
                    [
                        TaperEdge(edge_set=edge_set_1, angle=1.2, offset=2.3),
                        TaperEdge(edge_set=edge_set_2, angle=3.4, offset=4.5),
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
    def _create_oss(name="OrientedSelectionSet"):
        oss = OrientedSelectionSet(name=name)
        parent_model.add_oriented_selection_set(oss)
        return oss

    return LinkedObjectListTestCase(
        parent_object=tree_object,
        linked_attribute_name="oriented_selection_sets",
        existing_linked_object_names=(),
        linked_object_constructor=_create_oss,
    )


linked_object_case_empty = linked_object_case


@pytest.fixture
def linked_object_case_nonempty(tree_object, parent_model):
    def _create_oss(name="OrientedSelectionSet"):
        oss = OrientedSelectionSet(name=name)
        parent_model.add_oriented_selection_set(oss)
        return oss

    oss = OrientedSelectionSet(name="OSS.1")
    parent_model.add_oriented_selection_set(oss)
    tree_object.oriented_selection_sets = [oss]
    return LinkedObjectListTestCase(
        parent_object=tree_object,
        linked_attribute_name="oriented_selection_sets",
        existing_linked_object_names=("OSS.1",),
        linked_object_constructor=_create_oss,
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
