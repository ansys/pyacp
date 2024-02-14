import pytest

from ansys.acp.core import (
    CutoffRuleType,
    CutoffSelectionRuleElementalData,
    CutoffSelectionRuleNodalData,
    PlyCutoffType,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_cutoff_selection_rule()


class TestCutoffSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "cutoff_selection_rules"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "cutoff_rule_type": CutoffRuleType.GEOMETRY,
            "cutoff_geometry": None,
            "taper_edge_set": None,
            "offset": 0.0,
            "angle": 0.0,
            "ply_cutoff_type": PlyCutoffType.PRODUCTION_PLY_CUTOFF,
            "ply_tapering": False,
        }

    CREATE_METHOD_NAME = "create_cutoff_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        geometry = model.create_virtual_geometry()
        edge_set = model.create_edge_set()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Cutoff Selection Rule name"),
                ("cutoff_rule_type", CutoffRuleType.TAPER),
                ("cutoff_geometry", geometry),
                ("taper_edge_set", edge_set),
                ("offset", 1.2),
                ("angle", 2.3),
                ("ply_cutoff_type", PlyCutoffType.ANALYSIS_PLY_CUTOFF),
                ("ply_tapering", True),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = parent_object.create_cutoff_selection_rule()
    assert isinstance(rule.elemental_data, CutoffSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, CutoffSelectionRuleNodalData)
