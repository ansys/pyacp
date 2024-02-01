import pytest

from ansys.acp.core import (
    BooleanOperationType,
    BooleanSelectionRuleElementalData,
    BooleanSelectionRuleNodalData,
    LinkedSelectionRule,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_boolean_selection_rule()


class TestBooleanSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "boolean_selection_rules"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "selection_rules": [],
        "include_rule_type": True,
    }

    CREATE_METHOD_NAME = "create_boolean_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        material = model.create_material()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Boolean Selection Rule name"),
                (
                    "selection_rules",
                    [
                        LinkedSelectionRule(
                            selection_rule=model.create_parallel_selection_rule(),
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=False,
                            parameter_1=1.0,
                            parameter_2=2.0,
                        ),
                        LinkedSelectionRule(
                            selection_rule=model.create_cylindrical_selection_rule(),
                            operation_type=BooleanOperationType.ADD,
                            template_rule=True,
                            parameter_1=1.1,
                            parameter_2=2.2,
                        ),
                        LinkedSelectionRule(
                            selection_rule=model.create_spherical_selection_rule(),
                            operation_type=BooleanOperationType.REMOVE,
                            template_rule=True,
                            parameter_1=2.3,
                            parameter_2=-1.3,
                        ),
                        LinkedSelectionRule(
                            selection_rule=model.create_tube_selection_rule(),
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=False,
                            parameter_1=1.3,
                            parameter_2=2.9,
                        ),
                        LinkedSelectionRule(
                            selection_rule=model.create_geometrical_selection_rule(),
                            operation_type=BooleanOperationType.REMOVE,
                            template_rule=False,
                            parameter_1=1.5,
                            parameter_2=2.5,
                        ),
                        LinkedSelectionRule(
                            selection_rule=model.create_variable_offset_selection_rule(),
                            operation_type=BooleanOperationType.ADD,
                            template_rule=False,
                            parameter_1=0.0,
                            parameter_2=0.0,
                        ),
                    ],
                ),
                ("include_rule_type", False),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = parent_object.create_boolean_selection_rule()
    assert isinstance(rule.elemental_data, BooleanSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, BooleanSelectionRuleNodalData)
