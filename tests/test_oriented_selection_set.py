import pytest


def test_create_oriented_selection_set(load_model_from_tempfile):
    """Test the creation of Oriented Selection Sets."""
    with load_model_from_tempfile() as model:
        mg_names = ["OrientedSelectionSet.1", "OrientedSelectionSet.1", "üñıçよð€"]
        for ref_name in mg_names:
            oriented_selection_set = model.create_oriented_selection_set(name=ref_name)
            assert oriented_selection_set.name == ref_name


def test_collection_access(load_model_from_tempfile):
    """Basic test of the Model.oriented_selection_sets collection."""
    # TODO: split into separate tests for each mode of access.
    with load_model_from_tempfile() as model:
        model.oriented_selection_sets.clear()
        assert len(model.oriented_selection_sets) == 0

        mg_names = ["OrientedSelectionSet.1", "OrientedSelectionSet.1", "üñıçよð€"]
        mg_ids = []
        for ref_name in mg_names:
            oriented_selection_set = model.create_oriented_selection_set(name=ref_name)
            assert oriented_selection_set.id not in mg_ids  # check uniqueness
            mg_ids.append(oriented_selection_set.id)

        assert len(model.oriented_selection_sets) == len(mg_names)

        assert set(mg_names) == set(mg.name for mg in model.oriented_selection_sets.values())
        assert (
            set(mg_ids)
            == set(model.oriented_selection_sets)
            == set(model.oriented_selection_sets.keys())
        )

        for id in mg_ids:
            assert id in model.oriented_selection_sets

        mg_names_fromitems = []
        mg_ids_fromitems = []
        for key, value in model.oriented_selection_sets.items():
            mg_names_fromitems.append(value.name)
            mg_ids_fromitems.append(key)
            assert key == value.id

        for name in mg_names:
            assert name in mg_names_fromitems
        for id in mg_ids:
            assert id in mg_ids_fromitems

        REF_ID = mg_ids[0]
        INEXISTENT_ID = "Inexistent ID"

        assert model.oriented_selection_sets[REF_ID].id == REF_ID
        assert model.oriented_selection_sets.get(REF_ID).id == REF_ID

        with pytest.raises(KeyError):
            model.oriented_selection_sets[INEXISTENT_ID]
        assert model.oriented_selection_sets.get(INEXISTENT_ID) is None

        del model.oriented_selection_sets[REF_ID]
        with pytest.raises(KeyError):
            model.oriented_selection_sets[REF_ID]
