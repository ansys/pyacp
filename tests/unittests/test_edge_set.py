import pytest

from ansys.acp.core import EdgeSetType

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_edge_set()


class TestEdgeSet(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "edge_sets"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "edge_set_type": EdgeSetType.BY_REFERENCE,
        "element_set": None,
        "defining_node_labels": tuple(),
        "limit_angle": -1.0,
        "origin": (0.0, 0.0, 0.0),
    }

    CREATE_METHOD_NAME = "create_edge_set"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        element_set = model.create_element_set()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Edge set name"),
                ("edge_set_type", EdgeSetType.BY_NODES),
                ("element_set", element_set),
                ("limit_angle", 3.21),
                ("origin", (2.0, 3.0, 1.0)),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )
