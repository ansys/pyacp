def test_server_version(acp_instance):
    version = acp_instance.server_version
    assert isinstance(version, str)
    assert version != ""


def test_models(acp_instance, load_model_from_tempfile):
    with load_model_from_tempfile() as m1:
        assert acp_instance.models == (m1,)

        with load_model_from_tempfile() as m2:
            # the order of models is not guaranteed
            current_models = acp_instance.models
            assert len(current_models) == 2
            assert m1 in current_models
            assert m2 in current_models

            acp_instance.clear()
            assert acp_instance.models == ()
