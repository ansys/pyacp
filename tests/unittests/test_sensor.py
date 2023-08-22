import pytest

from ansys.acp.core._tree_objects.enums import SensorType

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_sensor()


class TestSensor(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "sensors"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "active": True,
        "entities": [],
        "covered_area": None,
        "modeling_ply_area": None,
        "production_ply_area": None,
        "price": None,
        "weight": None,
        "center_of_gravity": None,
    }

    CREATE_METHOD_NAME = "create_sensor"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        elset = model.create_element_set()
        oriented_selection_set = model.create_oriented_selection_set()
        modeling_ply = model.create_modeling_group().create_modeling_ply()
        fabric = model.create_fabric()
        stackup = model.create_stackup()
        sublaminate = model.create_sublaminate()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Sensor name"),
                ("sensor_type", SensorType.SENSOR_BY_AREA),
                ("entities", [elset, modeling_ply, oriented_selection_set]),
                ("sensor_type", SensorType.SENSOR_BY_MATERIAL),
                ("entities", [stackup, fabric, sublaminate]),
                ("sensor_type", SensorType.SENSOR_BY_PLIES),
                ("entities", [modeling_ply]),
                ("sensor_type", SensorType.SENSOR_BY_SOLID_MODEL),
                ("active", False),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("locked", True),
                ("covered_area", 0.3),
                ("modeling_ply_area", 0.3),
                ("production_ply_area", 0.3),
                ("price", 0.3),
                ("weight", 0.3),
                ("center_of_gravity", (0.1, 0.2, 0.3)),
            ],
        )
