import pytest


def test_create_modeling_group(load_model_from_tempfile):
    """Test the creation of Modeling Groups."""
    with load_model_from_tempfile() as model:
        mg_names = ["ModelingGroup.1", "ModelingGroup.1", "üñıçよð€"]
        for ref_name in mg_names:
            modeling_group = model.create_modeling_group(name=ref_name)
            assert modeling_group.name == ref_name


def test_collection_access(load_model_from_tempfile):
    """Basic test of the Model.modeling_groups collection."""
    with load_model_from_tempfile() as model:
        initial_num_mg = len(model.modeling_groups)
        assert initial_num_mg == 1

        mg_names = ["ModelingGroup.1", "ModelingGroup.1", "üñıçよð€"]
        mg_ids = []
        for ref_name in mg_names:
            modeling_group = model.create_modeling_group(name=ref_name)
            mg_ids.append(modeling_group.id)

        assert len(model.modeling_groups) == len(mg_names) + initial_num_mg

        for name in mg_names:
            assert name in [mg.name for mg in model.modeling_groups.values()]

        for id in mg_ids:
            assert id in model.modeling_groups
            assert id in model.modeling_groups.keys()

        mg_names_fromitems = []
        mg_ids_fromitems = []
        for key, value in model.modeling_groups.items():
            mg_names_fromitems.append(value.name)
            mg_ids_fromitems.append(key)
            assert key == value.id

        for name in mg_names:
            assert name in mg_names_fromitems
        for id in mg_ids:
            assert id in mg_ids_fromitems

        REF_ID = mg_ids[0]
        INEXISTENT_ID = "Inexistent ID"

        assert model.modeling_groups[REF_ID].id == REF_ID
        assert model.modeling_groups.get(REF_ID).id == REF_ID

        with pytest.raises(KeyError):
            model.modeling_groups[INEXISTENT_ID]
        assert model.modeling_groups.get(INEXISTENT_ID) is None
