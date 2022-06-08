import pytest


def test_create_element_set(load_model_from_tempfile):
    """Test the creation of Modeling Groups."""
    with load_model_from_tempfile() as model:
        eset_names = ["ElementSet.1", "ElementSet.1", "üñıçよð€"]
        for ref_name in eset_names:
            element_set = model.create_element_set(name=ref_name)
            assert element_set.name == ref_name


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
