import pytest

from ansys.acp.core import (
    BooleanSelectionRule,
    CylindricalSelectionRule,
    GeometricalSelectionRule,
    LinkedSelectionRule,
    ParallelSelectionRule,
    SphericalSelectionRule,
    TubeSelectionRule,
    VariableOffsetSelectionRule,
)
from ansys.acp.core._tree_objects.boolean_selection_rule import (
    BooleanSelectionRuleElementalData,
    BooleanSelectionRuleNodalData,
)
from ansys.acp.core._tree_objects.enums import BooleanOperationType

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    res = BooleanSelectionRule()
    parent_object.add_boolean_selection_rule(res)
    return res


class TestBooleanSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "boolean_selection_rules"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "selection_rules": [],
        "include_rule_type": True,
    }
    OBJECT_CLS = BooleanSelectionRule
    ADD_METHOD_NAME = "add_boolean_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object

        parallel_sr = ParallelSelectionRule()
        model.add_parallel_selection_rule(parallel_sr)

        cylindrical_sr = CylindricalSelectionRule()
        model.add_cylindrical_selection_rule(cylindrical_sr)

        spherical_sr = SphericalSelectionRule()
        model.add_spherical_selection_rule(spherical_sr)

        tube_sr = TubeSelectionRule()
        model.add_tube_selection_rule(tube_sr)

        geometrical_sr = GeometricalSelectionRule()
        model.add_geometrical_selection_rule(geometrical_sr)

        variable_offset_sr = VariableOffsetSelectionRule()
        model.add_variable_offset_selection_rule(variable_offset_sr)
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Boolean Selection Rule name"),
                (
                    "selection_rules",
                    [
                        LinkedSelectionRule(
                            selection_rule=parallel_sr,
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=False,
                            parameter_1=1.0,
                            parameter_2=2.0,
                        ),
                        LinkedSelectionRule(
                            selection_rule=cylindrical_sr,
                            operation_type=BooleanOperationType.ADD,
                            template_rule=True,
                            parameter_1=1.1,
                            parameter_2=2.2,
                        ),
                        LinkedSelectionRule(
                            selection_rule=spherical_sr,
                            operation_type=BooleanOperationType.REMOVE,
                            template_rule=True,
                            parameter_1=2.3,
                            parameter_2=-1.3,
                        ),
                        LinkedSelectionRule(
                            selection_rule=tube_sr,
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=False,
                            parameter_1=1.3,
                            parameter_2=2.9,
                        ),
                        LinkedSelectionRule(
                            selection_rule=geometrical_sr,
                            operation_type=BooleanOperationType.REMOVE,
                            template_rule=False,
                            parameter_1=1.5,
                            parameter_2=2.5,
                        ),
                        LinkedSelectionRule(
                            selection_rule=variable_offset_sr,
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
    rule = BooleanSelectionRule()
    parent_object.add_boolean_selection_rule(rule)
    assert isinstance(rule.elemental_data, BooleanSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, BooleanSelectionRuleNodalData)
