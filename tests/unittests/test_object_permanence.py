import gc


def test_object_identity(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        mg_0 = model.create_modeling_group()
        mg_1 = model.modeling_groups[mg_0.id]
        mg_2 = model.modeling_groups[mg_0.id]
        assert mg_0 is mg_1 is mg_2


def test_object_identity_after_deletion(load_model_from_tempfile):
    """Check that objects are deleted when no longer referenced."""
    with load_model_from_tempfile() as model:
        key = list(model.modeling_groups.keys())[0]

        # Immediately consume the objects via 'id' to ensure no references
        # are kept by the test infrastructure.
        id1 = id(model.modeling_groups[key])
        gc.collect()
        id2 = id(model.modeling_groups[key])
        assert id1 != id2

        # test the inverse: keep a reference alive explicitly
        _ = model.modeling_groups[key]
        id1 = id(model.modeling_groups[key])
        gc.collect()
        id2 = id(model.modeling_groups[key])
        assert id1 == id2
