import pytest


def test_create_rosette(load_model_from_tempfile):
    """Test the creation of a Rosette."""
    with load_model_from_tempfile() as model:
        ros_names = ["Rosette.1", "Rosette.1", "üñıçよð€"]
        for ref_name in ros_names:
            rosette = model.create_rosette(name=ref_name)
            assert rosette.name == ref_name


def test_collection_access(load_model_from_tempfile):
    """Basic test of the Model.rosettes collection."""
    with load_model_from_tempfile() as model:
        initial_num_ros = len(model.rosettes)
        assert initial_num_mg == 1

        ros_names = ["Rosette.1", "Rosette.1", "üñıçよð€"]
        ros_ids = []
        for ref_name in ros_names:
            rosette = model.create_rosette(name=ref_name)
            ros_ids.append(rosette.id)

        assert len(model.rosettes) == len(ros_names) + initial_num_mg

        for name in ros_names:
            assert name in [mg.name for mg in model.rosettes.values()]

        for id in ros_ids:
            assert id in model.rosettes
            assert id in model.rosettes.keys()

        ros_names_fromitems = []
        ros_ids_fromitems = []
        for key, value in model.rosettes.items():
            ros_names_fromitems.append(value.name)
            ros_ids_fromitems.append(key)
            assert key == value.id

        for name in ros_names:
            assert name in ros_names_fromitems
        for id in ros_ids_fromitems:
            assert id in ros_ids_fromitems

        REF_ID = ros_ids[0]
        INEXISTENT_ID = "Inexistent ID"

        assert model.rosettes[REF_ID].id == REF_ID
        assert model.rosettes.get(REF_ID).id == REF_ID

        with pytest.raises(KeyError):
            model.rosettes[INEXISTENT_ID]
        assert model.rosettes.get(INEXISTENT_ID) is None
