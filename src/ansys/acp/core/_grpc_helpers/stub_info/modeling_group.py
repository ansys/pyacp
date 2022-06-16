from ansys.api.acp.v0.modeling_group_pb2 import (
    CreateModelingGroupRequest,
    DeleteModelingGroupRequest,
    ListModelingGroupsRequest,
)
from ansys.api.acp.v0.modeling_group_pb2_grpc import ModelingGroupStub

from .base import SimpleStubInfo, SimpleStubWrapper

MODELING_GROUP_STUB_INFO = SimpleStubInfo(
    stub_class=ModelingGroupStub,
    list_attribute="modeling_groups",
    list_request_class=ListModelingGroupsRequest,
    create_request_class=CreateModelingGroupRequest,
    delete_request_class=DeleteModelingGroupRequest,
)


class ModelingGroupStubWrapper(SimpleStubWrapper):
    _STUB_INFO = MODELING_GROUP_STUB_INFO
