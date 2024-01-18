import pytest
from pytest_cases import fixture, parametrize_with_cases

from ansys.acp.core import (
    BooleanSelectionRule,
    CylindricalSelectionRule,
    ElementSet,
    OrientedSelectionSet,
    ParallelSelectionRule,
    Rosette,
    SphericalSelectionRule,
    TubeSelectionRule,
    VariableOffsetSelectionRule,
)
from ansys.acp.core._tree_objects.enums import RosetteSelectionMethod

from .common.linked_object_list_tester import LinkedObjectListTestCase, LinkedObjectListTester
from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    oriented_selection_set = OrientedSelectionSet()
    parent_object.add_oriented_selection_set(oriented_selection_set)
    return oriented_selection_set


class TestOrientedSelectionSet(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "oriented_selection_sets"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "element_sets": [],
        "rosettes": [],
        "orientation_point": (0.0, 0.0, 0.0),
        "orientation_direction": (0.0, 0.0, 0.0),
        "rosette_selection_method": "minimum_angle",
        "draping": False,
        "draping_seed_point": (0.0, 0.0, 0.0),
        "auto_draping_direction": True,
        "draping_direction": (0.0, 0.0, 1.0),
        "use_default_draping_mesh_size": True,
        "draping_mesh_size": 0.0,
        "draping_material_model": "woven",
        "draping_ud_coefficient": 0.0,
        "rotation_angle": 0.0,
    }
    OBJECT_CLS = OrientedSelectionSet
    ADD_METHOD_NAME = "add_oriented_selection_set"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        element_sets = [ElementSet() for _ in range(3)]
        for elset in element_sets:
            model.add_element_set(elset)
        rosettes = [Rosette() for _ in range(4)]
        for rosette in rosettes:
            model.add_rosette(rosette)

        tube_selection_rule = TubeSelectionRule()
        model.add_tube_selection_rule(tube_selection_rule)
        parallel_selection_rule = ParallelSelectionRule()
        model.add_parallel_selection_rule(parallel_selection_rule)
        spherical_selection_rule = SphericalSelectionRule()
        model.add_spherical_selection_rule(spherical_selection_rule)
        cylindrical_selection_rule = CylindricalSelectionRule()
        model.add_cylindrical_selection_rule(cylindrical_selection_rule)
        variable_offset_selection_rule = VariableOffsetSelectionRule()
        model.add_variable_offset_selection_rule(variable_offset_selection_rule)
        boolean_selection_rule = BooleanSelectionRule()
        model.add_boolean_selection_rule(boolean_selection_rule)
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
                ("element_sets", element_sets),
                ("orientation_point", (1.2, 6.3, -2.4)),
                ("orientation_direction", (1.0, -0.4, 0.9)),
                ("rosettes", rosettes),
                ("rosette_selection_method", RosetteSelectionMethod.MINIMUM_DISTANCE_SUPERPOSED),
                (
                    "selection_rules",
                    [
                        tube_selection_rule,
                        parallel_selection_rule,
                        spherical_selection_rule,
                        cylindrical_selection_rule,
                        variable_offset_selection_rule,
                        boolean_selection_rule,
                    ],
                ),
                ("draping", True),
                ("draping_seed_point", (0.0, 0.1, 0.0)),
                ("auto_draping_direction", False),
                ("draping_direction", (1.0, 0.0, 0.0)),
                ("use_default_draping_mesh_size", False),
                ("draping_mesh_size", 0.1),
                ("draping_material_model", "ud"),
                ("draping_ud_coefficient", 0.5),
                ("rotation_angle", 22.35),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def case_link_to_elset_one_existing(parent_object):
    oss = parent_object.oriented_selection_sets["OrientedSelectionSet.1"]

    def _create_elset(name="ElementSet"):
        element_set = ElementSet(name=name)
        parent_object.add_element_set(element_set)
        return element_set

    yield LinkedObjectListTestCase(
        parent_object=oss,
        linked_attribute_name="element_sets",
        existing_linked_object_names=tuple(["All_Elements"]),
        linked_object_constructor=_create_elset,
    )


def case_link_to_elset_empty(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = OrientedSelectionSet()
        model.add_oriented_selection_set(oss)

        def _create_elset(name="ElementSet"):
            element_set = ElementSet(name=name)
            model.add_element_set(element_set)
            return element_set

        yield LinkedObjectListTestCase(
            parent_object=oss,
            linked_attribute_name="element_sets",
            existing_linked_object_names=tuple(),
            linked_object_constructor=_create_elset,
        )


def case_link_to_rosette_empty(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = OrientedSelectionSet()
        model.add_oriented_selection_set(oss)

        def _create_rosette(name="Rosette"):
            rosette = Rosette(name=name)
            model.add_rosette(rosette)
            return rosette

        yield LinkedObjectListTestCase(
            parent_object=oss,
            linked_attribute_name="rosettes",
            existing_linked_object_names=tuple(),
            linked_object_constructor=_create_rosette,
        )


def case_link_to_rosette_one_existing(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = model.oriented_selection_sets["OrientedSelectionSet.1"]

        def _create_rosette(name="Rosette"):
            rosette = Rosette(name=name)
            model.add_rosette(rosette)
            return rosette

        yield LinkedObjectListTestCase(
            parent_object=oss,
            linked_attribute_name="rosettes",
            existing_linked_object_names=tuple(["Global Coordinate System"]),
            linked_object_constructor=_create_rosette,
        )


@fixture
@parametrize_with_cases("linked_case", cases=".", glob="link_*")
def linked_object_case(linked_case):
    return linked_case


@fixture
@parametrize_with_cases("linked_case", cases=".", glob="link_*_existing")
def linked_object_case_nonempty(linked_case):
    return linked_case


@fixture
@parametrize_with_cases("linked_case", cases=".", glob="link_*_empty")
def linked_object_case_empty(linked_case):
    return linked_case


class TestLinkedObjectLists(LinkedObjectListTester):
    pass
