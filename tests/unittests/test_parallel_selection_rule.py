import pytest

from ansys.acp.core import ParallelSelectionRuleElementalData, ParallelSelectionRuleNodalData

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_parallel_selection_rule()


class TestParallelSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "parallel_selection_rules"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "use_global_coordinate_system": True,
            "rosette": None,
            "origin": (0.0, 0.0, 0.0),
            "direction": (1.0, 0.0, 0.0),
            "lower_limit": 0.0,
            "upper_limit": 0.0,
            "relative_rule_type": False,
            "include_rule_type": True,
        }

    CREATE_METHOD_NAME = "create_parallel_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        rosette = model.create_rosette()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Parallel Selection Rule name"),
                ("use_global_coordinate_system", False),
                ("rosette", rosette),
                ("origin", (1.0, 2.0, 3.0)),
                ("direction", (4.0, 5.0, 6.0)),
                ("lower_limit", 7.0),
                ("upper_limit", 8.0),
                ("relative_rule_type", True),
                ("include_rule_type", False),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    model = parent_object
    rule = model.create_parallel_selection_rule(
        use_global_coordinate_system=True,
        origin=(0.0, 0.0, 0.0),
        direction=(1.0, 0.0, 0.0),
        lower_limit=-1.0,
        upper_limit=1.0,
    )
    assert isinstance(rule.elemental_data, ParallelSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, ParallelSelectionRuleNodalData)
