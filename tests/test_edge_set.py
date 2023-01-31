import pytest

from ansys.acp.core import EdgeSetType


def test_create_edge_set(load_model_from_tempfile):
    """Test the creation of Edge Sets."""
    with load_model_from_tempfile() as model:
        edge_set_names = ["EdgeSet.1", "EdgeSet.1", "üñıçよð€"]
        for ref_name in edge_set_names:
            edge_set = model.create_edge_set(name=ref_name)
            assert edge_set.name == ref_name


def test_edge_set_properties(load_model_from_tempfile):
    """Test the put request of an Edge Set."""
    with load_model_from_tempfile() as model:

        edge_set = model.create_edge_set(name="test_properties")
        properties = {
            "name": "new_name",
            "edge_set_type": EdgeSetType.BY_REFERENCE,
            "defining_node_labels": (1, 2, 5),
            "limit_angle": 3.21,
            "origin": (2.0, 3.0, 1.0),
        }

        for prop, value in properties.items():
            setattr(edge_set, prop, value)
            assert getattr(edge_set, prop) == value

        # test read only property
        readonly_props = ["id", "status", "locked"]
        for prop in readonly_props:
            value = getattr(edge_set, prop)
            with pytest.raises(AttributeError):
                setattr(edge_set, prop, value)


def test_collection_access(load_model_from_tempfile):
    """Basic test of the Model.edge_sets collection."""
    with load_model_from_tempfile() as model:
        initial_num_esets = len(model.edge_sets)
        assert initial_num_esets == 1

        edge_set_names = ["EdgeSet.1", "EdgeSet.1", "üñıçよð€"]
        edge_set_ids = []
        for ref_name in edge_set_names:
            edge_set = model.create_edge_set(name=ref_name)
            edge_set_ids.append(edge_set.id)

        assert len(model.edge_sets) == len(edge_set_names) + initial_num_esets

        for name in edge_set_names:
            assert name in [eset.name for eset in model.edge_sets.values()]

        for id in edge_set_ids:
            assert id in model.edge_sets
            assert id in model.edge_sets.keys()

        edge_set_names_fromitems = []
        edge_set_ids_fromitems = []
        for key, value in model.edge_sets.items():
            edge_set_names_fromitems.append(value.name)
            edge_set_ids_fromitems.append(key)
            assert key == value.id

        for name in edge_set_names:
            assert name in edge_set_names_fromitems
        for id in edge_set_ids:
            assert id in edge_set_ids_fromitems

        REF_ID = edge_set_ids[0]
        INEXISTENT_ID = "Inexistent ID"

        assert model.edge_sets[REF_ID].id == REF_ID
        assert model.edge_sets.get(REF_ID).id == REF_ID

        with pytest.raises(KeyError):
            model.edge_sets[INEXISTENT_ID]
        assert model.edge_sets.get(INEXISTENT_ID) is None
