import pytest


def test_create_element_set(load_model_from_tempfile):
    """Test the creation of Element Sets."""
    with load_model_from_tempfile() as model:
        eset_names = ["ElementSet.1", "ElementSet.1", "üñıçよð€"]
        for ref_name in eset_names:
            element_set = model.create_element_set(name=ref_name)
            assert element_set.name == ref_name

            assert element_set.status == "NOTUPTODATE"
            assert not element_set.locked
            assert not element_set.middle_offset
            assert element_set.element_labels == []


def test_element_set_properties(load_model_from_tempfile):
    """Test the put request of a ElementSet."""
    with load_model_from_tempfile() as model:

        element_set = model.create_element_set(name="test_properties")
        properties = {"name": "new_name", "element_labels": [1, 2, 3], "middle_offset": True}

        for prop, value in properties.items():
            setattr(element_set, prop, value)
            assert getattr(element_set, prop) == value

        # test read only property
        readonly_props = ["id", "status", "locked"]
        for prop in readonly_props:
            value = getattr(element_set, prop)
            with pytest.raises(AttributeError):
                setattr(element_set, prop, value)


def test_collection_access(load_model_from_tempfile):
    """Basic test of the Model.element_sets collection."""
    with load_model_from_tempfile() as model:
        initial_num_esets = len(model.element_sets)
        assert initial_num_esets == 1

        eset_names = ["ElementSet.1", "ElementSet.1", "üñıçよð€"]
        eset_ids = []
        for ref_name in eset_names:
            element_set = model.create_element_set(name=ref_name)
            eset_ids.append(element_set.id)

        assert len(model.element_sets) == len(eset_names) + initial_num_esets

        for name in eset_names:
            assert name in [eset.name for eset in model.element_sets.values()]

        for id in eset_ids:
            assert id in model.element_sets
            assert id in model.element_sets.keys()

        eset_names_fromitems = []
        eset_ids_fromitems = []
        for key, value in model.element_sets.items():
            eset_names_fromitems.append(value.name)
            eset_ids_fromitems.append(key)
            assert key == value.id

        for name in eset_names:
            assert name in eset_names_fromitems
        for id in eset_ids:
            assert id in eset_ids_fromitems

        REF_ID = eset_ids[0]
        INEXISTENT_ID = "Inexistent ID"

        assert model.element_sets[REF_ID].id == REF_ID
        assert model.element_sets.get(REF_ID).id == REF_ID

        with pytest.raises(KeyError):
            model.element_sets[INEXISTENT_ID]
        assert model.element_sets.get(INEXISTENT_ID) is None
