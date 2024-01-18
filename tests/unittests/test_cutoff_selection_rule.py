import pytest

from ansys.acp.core import CutoffSelectionRule, EdgeSet, VirtualGeometry
from ansys.acp.core._tree_objects.cutoff_selection_rule import (
    CutoffSelectionRuleElementalData,
    CutoffSelectionRuleNodalData,
)
from ansys.acp.core._tree_objects.enums import CutoffRuleType, PlyCutoffType

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    res = CutoffSelectionRule()
    parent_object.add_cutoff_selection_rule(res)
    return res


class TestCutoffSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "cutoff_selection_rules"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "cutoff_rule_type": CutoffRuleType.GEOMETRY,
        "cutoff_geometry": None,
        "taper_edge_set": None,
        "offset": 0.0,
        "angle": 0.0,
        "ply_cutoff_type": PlyCutoffType.PRODUCTION_PLY_CUTOFF,
        "ply_tapering": False,
    }
    OBJECT_CLS = CutoffSelectionRule
    ADD_METHOD_NAME = "add_cutoff_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        geometry = VirtualGeometry()
        model.add_virtual_geometry(geometry)
        edge_set = EdgeSet()
        model.add_edge_set(edge_set)
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
    rule = CutoffSelectionRule()
    parent_object.add_cutoff_selection_rule(rule)
    assert isinstance(rule.elemental_data, CutoffSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, CutoffSelectionRuleNodalData)
