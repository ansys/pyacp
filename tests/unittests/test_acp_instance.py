def test_server_version(acp_instance):
    version = acp_instance.server_version
    assert isinstance(version, str)
    assert version != ""
