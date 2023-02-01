import pytest

from ansys.acp.core._tree_objects.enums import (
    CutoffMaterialType,
    DrapingMaterialType,
    DropoffMaterialType,
)


def test_create_fabric(load_model_from_tempfile):
    """Test the creation."""
    with load_model_from_tempfile() as model:
        fabric_names = ["New Fabric.1", "New Fabric.1", "üñıçよð€"]
        for i, ref_name in enumerate(fabric_names):
            fabric = model.create_fabric(name=ref_name)
            assert fabric.name == ref_name
            if i == 1:
                assert fabric.id == "New Fabric.2"
            else:
                assert fabric.id == ref_name
            assert fabric.status == "NOTUPTODATE"
            assert fabric.thickness == 0.0
            assert fabric.area_price == 0.0
            assert not fabric.ignore_for_postprocessing
            assert fabric.drop_off_material_handling == DropoffMaterialType.GLOBAL
            assert fabric.cut_off_material_handling == CutoffMaterialType.COMPUTED
            assert fabric.draping_material_model == DrapingMaterialType.WOVEN
            assert fabric.draping_ud_coefficient == 0.0
            assert fabric.material is None


def test_fabric_properties(load_model_from_tempfile):
    """Test the put request."""
    with load_model_from_tempfile() as model:
        fabric = model.create_fabric(name="test_properties")
        properties = {
            "name": "new_name",
            "thickness": 0.23,
            "area_price": 12.3,
            "ignore_for_postprocessing": True,
            "drop_off_material_handling": DropoffMaterialType.CUSTOM,
            "cut_off_material_handling": CutoffMaterialType.GLOBAL,
            "draping_material_model": DrapingMaterialType.UD,
            "draping_ud_coefficient": 0.55,
            "material": model.materials["Structural Steel"],
        }

        for prop, value in properties.items():
            setattr(fabric, prop, value)
            assert getattr(fabric, prop) == value

        # test read only property
        readonly_props = ["id", "status"]
        for prop in readonly_props:
            value = getattr(fabric, prop)
            with pytest.raises(AttributeError):
                setattr(fabric, prop, value)


def test_collection_access(load_model_from_tempfile):
    """Basic test of the Model.fabrics collection."""
    with load_model_from_tempfile() as model:
        initial_num_fabric = len(model.fabrics)
        assert initial_num_fabric == 1

        fabric_names = ["Fabric.1", "Fabric.1", "üñıçよð€"]
        fabric_ids = []
        for ref_name in fabric_names:
            fabric = model.create_fabric(name=ref_name)
            assert fabric.id not in fabric_ids
            fabric_ids.append(fabric.id)

        assert len(model.fabrics) == len(fabric_names) + initial_num_fabric

        for name in fabric_names:
            assert name in [mg.name for mg in model.fabrics.values()]

        for id in fabric_ids:
            assert id in model.fabrics
            assert id in model.fabrics.keys()
