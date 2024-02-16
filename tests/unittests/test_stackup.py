import pytest

from ansys.acp.core import (
    CutoffMaterialType,
    DrapingMaterialType,
    DropoffMaterialType,
    FabricWithAngle,
    SymmetryType,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_stackup()


class TestStackup(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "stackups"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "area_price": 0.0,
        "topdown": True,
        "fabrics": [],
        "symmetry": SymmetryType.NO_SYMMETRY,
        "drop_off_material_handling": DropoffMaterialType.GLOBAL,
        "drop_off_material": None,
        "cut_off_material_handling": CutoffMaterialType.COMPUTED,
        "cut_off_material": None,
        "draping_material_model": DrapingMaterialType.WOVEN,
        "draping_ud_coefficient": 0.0,
    }

    CREATE_METHOD_NAME = "create_stackup"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        material = model.create_material()
        f1 = model.create_fabric(name="fabric 1", thickness=0.1, material=material)
        f2 = model.create_fabric(name="fabric 2", thickness=0.25, material=material)
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Stackup name"),
                ("topdown", False),
                ("area_price", 6.45),
                (
                    "fabrics",
                    [
                        FabricWithAngle(fabric=f1, angle=30.0),
                        FabricWithAngle(fabric=f2, angle=-60.0),
                    ],
                ),
                ("symmetry", SymmetryType.EVEN_SYMMETRY),
                ("drop_off_material_handling", DropoffMaterialType.CUSTOM),
                ("drop_off_material", material),
                ("cut_off_material_handling", CutoffMaterialType.CUSTOM),
                ("cut_off_material", material),
                ("draping_material_model", DrapingMaterialType.UD),
                ("draping_ud_coefficient", 0.55),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("area_weight", 0.0),
                ("thickness", 0.35),
                # ("draping_ud_coefficient", 4.32), # TODO: enable this check, see backend issue #778698
            ],
        )


def test_regression_413(parent_object):
    """
    Regression test for issue #413:
    Modifying the linked fabrics from two instances of the EdgePropertyList
    produces inconsistent results.
    """
    model = parent_object

    material = model.create_material()
    fabric_1 = model.create_fabric(material=material)
    fabric_2 = model.create_fabric(material=material)

    stackup = model.create_stackup(
        fabrics=[
            FabricWithAngle(fabric=fabric_1, angle=0.0),
            FabricWithAngle(fabric=fabric_2, angle=0.0),
        ]
    )
    edge_property_list_1 = stackup.fabrics
    edge_property_list_2 = stackup.fabrics

    edge_property_list_1[0].angle = 45.0
    edge_property_list_2[1].angle = 90.0

    assert edge_property_list_1[0].angle == 45.0
    assert edge_property_list_1[1].angle == 90.0

    assert edge_property_list_2[0].angle == 45.0
    assert edge_property_list_2[1].angle == 90.0


def test_regression_413_v2(parent_object):
    """
    Regression test for issue #413:
    Modifying the linked fabrics from two instances of the EdgePropertyList
    produces inconsistent results.
    """
    model = parent_object

    material = model.create_material()
    fabric_1 = model.create_fabric(material=material)
    fabric_2 = model.create_fabric(material=material)

    stackup = model.create_stackup(
        fabrics=[
            FabricWithAngle(fabric=fabric_1, angle=0.0),
            FabricWithAngle(fabric=fabric_2, angle=0.0),
        ]
    )
    edge_property_list_1 = stackup.fabrics
    # Stricter test: also get the stackup instance independently
    edge_property_list_2 = model.stackups[stackup.id].fabrics

    edge_property_list_1[0].angle = 45.0
    edge_property_list_2[1].angle = 90.0

    assert edge_property_list_1[0].angle == 45.0
    assert edge_property_list_1[1].angle == 90.0

    assert edge_property_list_2[0].angle == 45.0
    assert edge_property_list_2[1].angle == 90.0


def test_wrong_fabrics_type_error_message(parent_object):
    stackup = parent_object.create_stackup()
    modeling_group = parent_object.create_modeling_group()
    with pytest.raises(TypeError) as exc:
        stackup.fabrics = [modeling_group]
    assert "FabricWithAngle" in str(exc.value)
    assert "ModelingGroup" in str(exc.value)


def test_fabrics_autoconversion(parent_object):
    stackup = parent_object.create_stackup()
    fabric = parent_object.create_fabric()
    fabric.material = parent_object.create_material()
    stackup.fabrics = [fabric]
    assert stackup.fabrics[0].fabric == fabric
