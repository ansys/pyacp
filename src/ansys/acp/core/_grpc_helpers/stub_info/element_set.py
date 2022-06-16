from ansys.api.acp.v0.element_set_pb2 import (
    CreateElementSetRequest,
    DeleteElementSetRequest,
    ListElementSetsRequest,
)
from ansys.api.acp.v0.element_set_pb2_grpc import ElementSetStub

from .base import SimpleStubInfo, SimpleStubWrapper

ELEMENT_SET_STUB_INFO = SimpleStubInfo(
    stub_class=ElementSetStub,
    list_attribute="element_sets",
    list_request_class=ListElementSetsRequest,
    create_request_class=CreateElementSetRequest,
    delete_request_class=DeleteElementSetRequest,
)


class ElementSetStubWrapper(SimpleStubWrapper):
    _STUB_INFO = ELEMENT_SET_STUB_INFO
