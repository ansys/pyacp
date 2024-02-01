import pytest

from ansys.acp.core import TubeSelectionRuleElementalData, TubeSelectionRuleNodalData

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_tube_selection_rule()


class TestTubeSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "tube_selection_rules"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "edge_set": None,
        "outer_radius": 1.0,
        "inner_radius": 0.0,
        "include_rule_type": True,
        "extend_endings": False,
        "symmetrical_extension": True,
        "head": (0.0, 0.0, 0.0),
        "head_extension": 0.0,
        "tail_extension": 0.0,
    }

    CREATE_METHOD_NAME = "create_tube_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        edge_set = model.create_edge_set()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Tube Selection Rule name"),
                ("edge_set", edge_set),
                ("outer_radius", 1.3),
                ("inner_radius", 0.3),
                ("include_rule_type", False),
                ("extend_endings", True),
                ("symmetrical_extension", False),
                ("head", (1.0, 2.0, 3.0)),
                ("head_extension", 4.0),
                ("tail_extension", 5.0),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = parent_object.create_tube_selection_rule()
    assert isinstance(rule.elemental_data, TubeSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, TubeSelectionRuleNodalData)
