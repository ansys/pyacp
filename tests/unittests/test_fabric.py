import pytest

from ansys.acp.core import CutoffMaterialType, DrapingMaterialType, DropoffMaterialType

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_fabric()


class TestFabric(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "fabrics"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "thickness": 0.0,
            "area_price": 0.0,
            "ignore_for_postprocessing": False,
            "drop_off_material_handling": DropoffMaterialType.GLOBAL,
            "cut_off_material_handling": CutoffMaterialType.COMPUTED,
            "draping_material_model": DrapingMaterialType.WOVEN,
            "draping_ud_coefficient": 0.0,
            "material": None,
        }

    CREATE_METHOD_NAME = "create_fabric"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        material = model.create_material()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Fabric name"),
                ("thickness", 1e-6),
                ("area_price", 5.98),
                ("ignore_for_postprocessing", True),
                ("drop_off_material_handling", DropoffMaterialType.CUSTOM),
                ("cut_off_material_handling", CutoffMaterialType.GLOBAL),
                ("draping_material_model", DrapingMaterialType.UD),
                ("draping_ud_coefficient", 0.55),
                ("material", material),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("area_weight", 0.0),
                # ("draping_ud_coefficient", 4.32), # TODO: enable this check, see backend issue #778698
            ],
        )
