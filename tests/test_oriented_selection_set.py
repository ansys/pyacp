import pytest

from ansys.acp.core._tree_objects.enums import RosetteSelectionMethod


def test_create_oriented_selection_set(load_model_from_tempfile):
    """Test the creation of Oriented Selection Sets."""
    with load_model_from_tempfile() as model:
        oss_names = ["OrientedSelectionSet.1", "OrientedSelectionSet.1", "üñıçよð€"]
        for ref_name in oss_names:
            oriented_selection_set = model.create_oriented_selection_set(name=ref_name)
            assert oriented_selection_set.name == ref_name
            assert oriented_selection_set.status == "NOTUPTODATE"
            assert oriented_selection_set.element_sets == []
            assert oriented_selection_set.rosettes == []
            assert oriented_selection_set.orientation_point == (0.0, 0.0, 0.0)
            assert oriented_selection_set.orientation_direction == (0.0, 0.0, 0.0)
            assert oriented_selection_set.rosette_selection_method == "minimum_angle"
            assert (
                oriented_selection_set.rosette_selection_method
                == RosetteSelectionMethod.MINIMUM_ANGLE
            )


def test_oriented_selection_set_properties(load_model_from_tempfile):
    """Test the put request of a Rosette."""
    with load_model_from_tempfile() as model:
        element_sets = [model.create_element_set() for _ in range(3)]
        rosettes = [model.create_rosette() for _ in range(4)]

        oriented_selection_set = model.create_oriented_selection_set(name="test_properties")
        properties = {
            "name": "new_name",
            "element_sets": element_sets,
            "orientation_point": (1.2, 6.3, -2.4),
            "orientation_direction": (1.0, -0.4, 0.9),
            "rosettes": rosettes,
            "rosette_selection_method": RosetteSelectionMethod.MINIMUM_DISTANCE_SUPERPOSED,
        }

        for prop, value in properties.items():
            setattr(oriented_selection_set, prop, value)
            assert getattr(oriented_selection_set, prop) == value

        # test read only property
        readonly_props = ["id", "status"]
        for prop in readonly_props:
            value = getattr(oriented_selection_set, prop)
            with pytest.raises(AttributeError):
                setattr(oriented_selection_set, prop, value)


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

        assert set(mg_names) == {mg.name for mg in model.oriented_selection_sets.values()}
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
