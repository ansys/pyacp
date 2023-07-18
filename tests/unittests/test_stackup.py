import pytest

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
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Stackup name"),
                ("topdown", False),
                ("area_price", 6.45),
                ("fabrics", []),
                ("symmetry", SymmetryType.EVEN_SYMMETRY),
                ("drop_off_material_handling", DropoffMaterialType.CUSTOM),
                ("drop_off_material", material),
                ("cut_off_material_handling", CutoffMaterialType.GLOBAL),
                ("cut_off_material", material),
                ("draping_material_model", DrapingMaterialType.UD),
                ("draping_ud_coefficient", 0.55),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                # ("draping_ud_coefficient", 4.32), # TODO: enable this check, see backend issue #778698
            ],
        )
