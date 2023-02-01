import pytest

from common.tree_object_tester import NoLockedMixin, ObjectProperties, TreeObjectTester
from common.utils import AnyThing


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


class TestOrientedSelectionSet(NoLockedMixin, TreeObjectTester):
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
    @pytest.fixture
    def object_properties(parent_model):
        oriented_selection_sets = [parent_model.create_oriented_selection_set() for _ in range(3)]
        fabric = parent_model.create_fabric()
        return ObjectProperties(
            read_write={
                "oriented_selection_sets": oriented_selection_sets,
                "ply_material": fabric,
                "ply_angle": 0.5,
                "active": False,
                "global_ply_nr": AnyThing(),
            },
            read_only={
                "id": "some_id",
                "status": "UPTODATE",
            },
        )
