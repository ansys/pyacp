import pytest

from ansys.acp.core import (
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
    return parent_object.create_variable_offset_selection_rule()


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

    CREATE_METHOD_NAME = "create_variable_offset_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        edge_set = model.create_edge_set()
        lookup_table = model.create_lookup_table_1d()
        column_1 = lookup_table.create_column()
        column_2 = lookup_table.create_column()
        element_set = model.create_element_set()
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
    rule = parent_object.create_variable_offset_selection_rule()
    assert isinstance(rule.elemental_data, VariableOffsetSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, VariableOffsetSelectionRuleNodalData)
