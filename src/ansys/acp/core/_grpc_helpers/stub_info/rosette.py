from ansys.api.acp.v0.rosette_pb2 import (
    CreateRosetteRequest,
    DeleteRosetteRequest,
    ListRosettesRequest,
)
from ansys.api.acp.v0.rosette_pb2_grpc import RosetteStub

from .base import SimpleStubInfo, SimpleStubWrapper

ROSETTE_STUB_INFO = SimpleStubInfo(
    stub_class=RosetteStub,
    list_attribute="rosettes",
    list_request_class=ListRosettesRequest,
    create_request_class=CreateRosetteRequest,
    delete_request_class=DeleteRosetteRequest,
)


class RosetteStubWrapper(SimpleStubWrapper):
    _STUB_INFO = ROSETTE_STUB_INFO
