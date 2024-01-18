import pytest

from ansys.acp.core import ElementSet, GeometricalSelectionRule, VirtualGeometry
from ansys.acp.core._tree_objects.enums import GeometricalRuleType
from ansys.acp.core._tree_objects.geometrical_selection_rule import (
    GeometricalSelectionRuleElementalData,
    GeometricalSelectionRuleNodalData,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    res = GeometricalSelectionRule()
    parent_object.add_geometrical_selection_rule(res)
    return res


class TestGeometricalSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "geometrical_selection_rules"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "geometrical_rule_type": GeometricalRuleType.GEOMETRY,
        "geometry": None,
        "element_sets": [],
        "include_rule_type": True,
        "use_default_tolerances": True,
        "in_plane_capture_tolerance": 0.0,
        "negative_capture_tolerance": 0.0,
        "positive_capture_tolerance": 0.0,
    }
    OBJECT_CLS = GeometricalSelectionRule
    ADD_METHOD_NAME = "add_geometrical_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        virtual_geometry = VirtualGeometry()
        model.add_virtual_geometry(virtual_geometry)
        element_sets = [ElementSet() for _ in range(3)]
        for element_set in element_sets:
            model.add_element_set(element_set)
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Geometrical Selection Rule name"),
                ("geometrical_rule_type", GeometricalRuleType.ELEMENT_SETS),
                ("geometry", virtual_geometry),
                ("element_sets", element_sets),
                ("include_rule_type", False),
                ("use_default_tolerances", False),
                ("in_plane_capture_tolerance", 1.2),
                ("negative_capture_tolerance", 2.3),
                ("positive_capture_tolerance", 3.4),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = GeometricalSelectionRule()
    parent_object.add_geometrical_selection_rule(rule)
    assert isinstance(rule.elemental_data, GeometricalSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, GeometricalSelectionRuleNodalData)
