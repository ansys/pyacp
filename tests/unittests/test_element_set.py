import pytest

from ansys.acp.core import ElementSet

from .common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    element_set = ElementSet()
    parent_object.add_element_set(element_set)
    return element_set


@pytest.fixture
def object_properties():
    return ObjectPropertiesToTest(
        read_write=[
            ("name", "new_name"),
            ("middle_offset", True),
            ("element_labels", (1, 2, 3, 4)),
        ],
        read_only=[
            ("id", "some_id"),
            ("status", "UPTODATE"),
        ],
    )


class TestElementSet(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "element_sets"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "locked": False,
        "middle_offset": False,
        "element_labels": tuple(),
    }
    ADD_METHOD_NAME = "add_element_set"
    OBJECT_CLS = ElementSet
    INITIAL_OBJECT_NAMES = ("All_Elements",)
