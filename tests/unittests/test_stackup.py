import pytest

from ansys.acp.core import Fabric, FabricWithAngle, Material, Stackup
from ansys.acp.core._tree_objects.enums import (
    CutoffMaterialType,
    DrapingMaterialType,
    DropoffMaterialType,
    SymmetryType,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    stackup = Stackup()
    parent_object.add_stackup(stackup)
    return stackup


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
    OBJECT_CLS = Stackup
    ADD_METHOD_NAME = "add_stackup"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        material = Material()
        model.add_material(material)

        f1 = Fabric(name="fabric 1", thickness=0.1, material=material)
        f2 = Fabric(name="fabric 2", thickness=0.25, material=material)
        model.add_fabric(f1)
        model.add_fabric(f2)
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
