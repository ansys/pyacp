from ansys.acp.core import Client


def test_server_version(grpc_server):
    client = Client(server=grpc_server)
    version = client.server_version
    assert isinstance(version, str)
    assert version != ""
