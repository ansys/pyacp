import pytest


def get_first_modeling_group(model):
    return model.modeling_groups["ModelingGroup.1"]


def test_get_existing(load_model_from_tempfile):
    """Test the creation of Modeling Ply."""
    with load_model_from_tempfile() as model:
        modeling_ply_names = ["ModelingPly.1", "ModelingPly.1", "üñıçよð€"]
        for ref_name in modeling_ply_names:
            modeling_ply = get_first_modeling_group(model).create_modeling_ply(name=ref_name)
            assert modeling_ply.name == ref_name


def test_properties(load_model_from_tempfile):
    """Basic test of the Model.modeling_groups.modeling_plies collection."""
    # TODO: split into separate tests for each mode of access.
    with load_model_from_tempfile() as model:
        modeling_ply = get_first_modeling_group(model).modeling_plies["ModelingPly.1"]
        oriented_selection_sets = modeling_ply.oriented_selection_sets
        assert len(oriented_selection_sets) == 1
        modeling_ply.oriented_selection_sets.append(
            model.create_oriented_selection_set(name="test")
        )
        assert len(oriented_selection_sets) == 2

        fabric = modeling_ply.ply_material
        assert fabric.name == "Fabric.1"
        new_fabric = model.create_fabric(name="Fabric.2")
        modeling_ply.ply_material = new_fabric
        assert modeling_ply.ply_material.name == "Fabric.2"

        modeling_ply.ply_angle = 20.0
        assert modeling_ply.ply_angle == pytest.approx(20.0)

        modeling_ply.number_of_layers = 3
        assert modeling_ply.number_of_layers == 3

        modeling_ply.active = False
        assert not modeling_ply.active

        modeling_ply.global_ply_nr = 3
        assert modeling_ply.global_ply_nr == 3


def test_collection_access(load_model_from_tempfile):
    """Basic test of the Model.modeling_groups.modeling_plies collection."""
    # TODO: split into separate tests for each mode of access.
    with load_model_from_tempfile() as model:
        get_first_modeling_group(model).modeling_plies.clear()
        assert len(get_first_modeling_group(model).modeling_plies) == 0

        mp_names = ["ModellingPly.1", "ModellingPly.1", "üñıçよð€"]
        mp_ids = []
        for ref_name in mp_names:
            modeling_ply = get_first_modeling_group(model).create_modeling_ply(name=ref_name)
            assert modeling_ply.id not in mp_ids  # check uniqueness
            mp_ids.append(modeling_ply.id)

        assert len(get_first_modeling_group(model).modeling_plies) == len(mp_names)

        assert set(mp_names) == set(
            mp.name for mp in get_first_modeling_group(model).modeling_plies.values()
        )
        assert (
            set(mp_ids)
            == set(get_first_modeling_group(model).modeling_plies)
            == set(get_first_modeling_group(model).modeling_plies.keys())
        )

        for id in mp_ids:
            assert id in get_first_modeling_group(model).modeling_plies

        mp_names = []
        mp_ids_fromitems = []
        for key, value in get_first_modeling_group(model).modeling_plies.items():
            mp_names.append(value.name)
            mp_ids_fromitems.append(key)
            assert key == value.id

        for name in mp_names:
            assert name in mp_names
        for id in mp_ids:
            assert id in mp_ids_fromitems

        REF_ID = mp_ids[0]
        INEXISTENT_ID = "Inexistent ID"

        assert get_first_modeling_group(model).modeling_plies[REF_ID].id == REF_ID
        assert get_first_modeling_group(model).modeling_plies.get(REF_ID).id == REF_ID

        with pytest.raises(KeyError):
            get_first_modeling_group(model).modeling_plies[INEXISTENT_ID]
        assert model.oriented_selection_sets.get(INEXISTENT_ID) is None

        del get_first_modeling_group(model).modeling_plies[REF_ID]
        with pytest.raises(KeyError):
            get_first_modeling_group(model).modeling_plies[REF_ID]
