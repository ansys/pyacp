import pytest

from ansys.acp.core._tree_objects.cylindrical_selection_rule import (
    CylindricalSelectionRuleElementalData,
    CylindricalSelectionRuleNodalData,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_cylindrical_selection_rule()


class TestCylindricalSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "cylindrical_selection_rules"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "use_global_coordinate_system": True,
        "rosette": None,
        "origin": (0.0, 0.0, 0.0),
        "direction": (0.0, 0.0, 1.0),
        "radius": 0.0,
        "relative_rule_type": False,
        "include_rule_type": True,
    }

    CREATE_METHOD_NAME = "create_cylindrical_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        rosette = model.create_rosette()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Cylindrical Selection Rule name"),
                ("use_global_coordinate_system", False),
                ("rosette", rosette),
                ("origin", (1.0, 2.0, 3.0)),
                ("direction", (4.0, 5.0, 6.0)),
                ("radius", 7.0),
                ("relative_rule_type", True),
                ("include_rule_type", False),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = parent_object.create_cylindrical_selection_rule()
    assert isinstance(rule.elemental_data, CylindricalSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, CylindricalSelectionRuleNodalData)