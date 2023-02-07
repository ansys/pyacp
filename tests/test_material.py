import pytest


def get_structural_steel(model):
    return model.materials["Structural Steel"]


def test_create_material(load_model_from_tempfile):
    """Test the creation of a material."""
    with load_model_from_tempfile() as model:
        material_names = ["New Material", "New Material", "üñıçよð€"]
        for ref_name in material_names:
            material = model.create_material(name=ref_name)
            assert material.name == ref_name


def test_material_properties(load_model_from_tempfile):
    """Test the put request of a Material."""
    with load_model_from_tempfile() as model:
        material = model.create_material(name="test_properties")
        properties = {
            "name": "new_name",
        }

        for prop, value in properties.items():
            setattr(material, prop, value)
            assert getattr(material, prop) == value

        # test read only property
        readonly_props = ["id", "status", "locked"]
        for prop in readonly_props:
            value = getattr(material, prop)
            with pytest.raises(AttributeError):
                setattr(material, prop, value)


def test_collection_access(load_model_from_tempfile):
    """Basic test of the Model.materials collection."""
    with load_model_from_tempfile() as model:
        initial_num_mats = len(model.materials)
        assert initial_num_mats == 1

        mat_names = ["Material.1", "Material.1", "üñıçよð€"]
        mat_ids = []
        for ref_name in mat_names:
            material = model.create_material(name=ref_name)
            assert material.id not in mat_ids
            mat_ids.append(material.id)

        assert len(model.materials) == len(mat_names) + initial_num_mats

        for name in mat_names:
            assert name in [mat.name for mat in model.materials.values()]

        for id in mat_ids:
            assert id in model.materials
            assert id in model.materials.keys()
