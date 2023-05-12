import pytest

from .common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_element_set()


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
    CREATE_METHOD_NAME = "create_element_set"
    INITIAL_OBJECT_NAMES = ("All_Elements",)
