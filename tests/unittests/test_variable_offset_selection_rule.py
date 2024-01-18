import pytest

from ansys.acp.core import (
    EdgeSet,
    ElementSet,
    LookUpTable1D,
    LookUpTable1DColumn,
    VariableOffsetSelectionRule,
)
from ansys.acp.core._tree_objects.variable_offset_selection_rule import (
    VariableOffsetSelectionRuleElementalData,
    VariableOffsetSelectionRuleNodalData,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    rule = VariableOffsetSelectionRule()
    parent_object.add_variable_offset_selection_rule(rule)
    return rule


class TestVariableOffsetSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "variable_offset_selection_rules"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "edge_set": None,
        "offsets": None,
        "angles": None,
        "include_rule_type": True,
        "use_offset_correction": False,
        "element_set": None,
        "inherit_from_lookup_table": True,
        "radius_origin": (0.0, 0.0, 0.0),
        "radius_direction": (1.0, 0.0, 0.0),
        "distance_along_edge": False,
    }
    OBJECT_CLS = VariableOffsetSelectionRule
    ADD_METHOD_NAME = "add_variable_offset_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        edge_set = EdgeSet()
        model.add_edge_set(edge_set)
        lookup_table = LookUpTable1D()
        model.add_lookup_table_1d(lookup_table)

        column_1 = LookUpTable1DColumn()
        column_2 = LookUpTable1DColumn()
        lookup_table.add_column(column_1)
        lookup_table.add_column(column_2)

        element_set = ElementSet()
        model.add_element_set(element_set)
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Variable Offset Selection Rule name"),
                ("edge_set", edge_set),
                ("offsets", column_1),
                ("angles", column_2),
                ("include_rule_type", False),
                ("use_offset_correction", True),
                ("element_set", element_set),
                ("inherit_from_lookup_table", False),
                ("radius_origin", (0.1, 0.2, 0.3)),
                ("radius_direction", (0.4, 0.5, 0.6)),
                ("distance_along_edge", True),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = VariableOffsetSelectionRule()
    parent_object.add_variable_offset_selection_rule(rule)
    assert isinstance(rule.elemental_data, VariableOffsetSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, VariableOffsetSelectionRuleNodalData)
