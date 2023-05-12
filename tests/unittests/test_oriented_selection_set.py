import pytest
from pytest_cases import fixture, parametrize_with_cases

from ansys.acp.core._tree_objects.enums import RosetteSelectionMethod

from .common.linked_object_list_tester import LinkedObjectListTestCase, LinkedObjectListTester
from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_oriented_selection_set()


class TestOrientedSelectionSet(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "oriented_selection_sets"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "element_sets": [],
        "rosettes": [],
        "orientation_point": (0.0, 0.0, 0.0),
        "orientation_direction": (0.0, 0.0, 0.0),
        "rosette_selection_method": "minimum_angle",
    }
    CREATE_METHOD_NAME = "create_oriented_selection_set"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        element_sets = [model.create_element_set() for _ in range(3)]
        rosettes = [model.create_rosette() for _ in range(4)]
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
                ("element_sets", element_sets),
                ("orientation_point", (1.2, 6.3, -2.4)),
                ("orientation_direction", (1.0, -0.4, 0.9)),
                ("rosettes", rosettes),
                ("rosette_selection_method", RosetteSelectionMethod.MINIMUM_DISTANCE_SUPERPOSED),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def case_link_to_elset_one_existing(parent_object):
    oss = parent_object.oriented_selection_sets["OrientedSelectionSet.1"]
    yield LinkedObjectListTestCase(
        parent_object=oss,
        linked_attribute_name="element_sets",
        existing_linked_object_names=tuple(["All_Elements"]),
        linked_object_constructor=parent_object.create_element_set,
    )


def case_link_to_elset_empty(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = model.create_oriented_selection_set()
        yield LinkedObjectListTestCase(
            parent_object=oss,
            linked_attribute_name="element_sets",
            existing_linked_object_names=tuple(),
            linked_object_constructor=model.create_element_set,
        )


def case_link_to_rosette_empty(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = model.create_oriented_selection_set()
        yield LinkedObjectListTestCase(
            parent_object=oss,
            linked_attribute_name="rosettes",
            existing_linked_object_names=tuple(),
            linked_object_constructor=model.create_rosette,
        )


def case_link_to_rosette_one_existing(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = model.oriented_selection_sets["OrientedSelectionSet.1"]
        yield LinkedObjectListTestCase(
            parent_object=oss,
            linked_attribute_name="rosettes",
            existing_linked_object_names=tuple(["Global Coordinate System"]),
            linked_object_constructor=model.create_rosette,
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