import pytest

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_oriented_selection_set()


class TestModelingGroup(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "modeling_groups"
    DEFAULT_PROPERTIES = {}
    CREATE_METHOD_NAME = "create_modeling_group"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        element_sets = [model.create_element_set() for _ in range(3)]
        rosettes = [model.create_rosette() for _ in range(4)]
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
            ],
            read_only=[
                ("id", "some_id"),
            ],
        )
