import pytest

from ansys.acp.core import FabricWithAngle, Lamina, SymmetryType

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_sublaminate()


class TestSubLaminate(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "sublaminates"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "topdown": True,
            "materials": [],
            "symmetry": SymmetryType.NO_SYMMETRY,
        }

    CREATE_METHOD_NAME = "create_sublaminate"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        material = model.create_material()
        fabric = model.create_fabric(
            name="fabric 1", thickness=0.1, material=material, area_price=15.0
        )
        fabric_stack = [
            FabricWithAngle(fabric=fabric, angle=30.0),
            FabricWithAngle(fabric=fabric, angle=-30.0),
        ]
        stackup = model.create_stackup(name="stackup 1", fabrics=fabric_stack, area_price=32.5)
        sublaminat_stack = [
            Lamina(material=fabric, angle=45.0),
            Lamina(material=stackup, angle=-60.0),
        ]
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Sub-laminate name"),
                ("topdown", False),
                ("materials", sublaminat_stack),
                ("symmetry", SymmetryType.EVEN_SYMMETRY),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("thickness", 0.3),
                ("area_weight", 0.0),
                ("area_price", 47.5),
            ],
        )


def test_add_lamina(parent_object):
    """Verify add method for lamina."""
    fabric1 = parent_object.create_fabric()
    fabric1.material = parent_object.create_material()
    stackup = parent_object.create_stackup()
    stackup.add_fabric(fabric1, angle=30.0)
    stackup.add_fabric(fabric1, angle=-30.0)

    sublaminate = parent_object.create_sublaminate()
    sublaminate.add_material(fabric1, angle=45.0)
    sublaminate.add_material(stackup, angle=0.0)
    sublaminate.add_material(fabric1, angle=-45.0)
    assert len(sublaminate.materials) == 3
    assert sublaminate.materials[1].material == stackup
    assert sublaminate.materials[1].angle == 0.0
    assert sublaminate.materials[2].material == fabric1
    assert sublaminate.materials[2].angle == -45.0
