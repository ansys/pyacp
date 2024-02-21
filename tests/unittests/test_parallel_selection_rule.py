import pytest

from ansys.acp.core import (
    LinkedSelectionRule,
    ParallelSelectionRuleElementalData,
    ParallelSelectionRuleNodalData,
)

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


def test_regression_413(parent_object):
    """
    Regression test for issue #413:
    Setting property on linked rule removes it from the modeling ply
    """
    model = parent_object

    parallel_rule = model.create_parallel_selection_rule()

    linked_parallel_rule = LinkedSelectionRule(parallel_rule)

    modeling_group = model.create_modeling_group()
    modeling_ply = modeling_group.create_modeling_ply(selection_rules=[linked_parallel_rule])

    cylindrical_rule = model.create_cylindrical_selection_rule()
    linked_cylindrical_rule = LinkedSelectionRule(cylindrical_rule)
    modeling_ply.selection_rules.append(linked_cylindrical_rule)

    assert len(modeling_ply.selection_rules) == 2

    # Original bug: changing a property on the linked rule
    # removes it from the modeling ply, making the assertion fail.
    linked_parallel_rule.parameter_1 = 0.002
    assert len(modeling_ply.selection_rules) == 2
