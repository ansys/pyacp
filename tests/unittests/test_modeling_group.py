import pytest

from ansys.acp.core import ModelingGroup

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    modeling_group = ModelingGroup()
    parent_object.add_modeling_group(modeling_group)
    return modeling_group


class TestModelingGroup(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "modeling_groups"
    DEFAULT_PROPERTIES = {}
    ADD_METHOD_NAME = "add_modeling_group"
    OBJECT_CLS = ModelingGroup

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
            ],
            read_only=[
                ("id", "some_id"),
            ],
        )
