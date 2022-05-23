from typing import Any
from typing import Optional

from ansys.api.acp.v0.base_pb2 import BasicInfo
from ansys.api.acp.v0.base_pb2 import ResourcePath
from ansys.api.acp.v0.modeling_group_pb2 import ModelingGroupRequest
from ansys.api.acp.v0.modeling_group_pb2 import PutModelingGroupRequest
from ansys.api.acp.v0.modeling_group_pb2_grpc import ModelingGroupStub

from ._data_objects.modeling_group import ModelingGroup as _ModelingGroupData
from ._launcher import ServerProtocol
from ._property_helper import grpc_data_property

__all__ = ["ModelingGroup"]


class ModelingGroup:
    COLLECTION_LABEL = "modeling_groups"

    def __init__(self, *, resource_path: str, server: ServerProtocol):
        self._resource_path = resource_path
        self._server = server
        self._stub = ModelingGroupStub(self._server.channel)
        self._data_object: Optional[_ModelingGroupData] = None

    def _get_pb_resource_path(self) -> ResourcePath:
        return ResourcePath(value=self._resource_path)

    def _get(self) -> None:
        reply = self._stub.Get(ModelingGroupRequest(resource_path=self._get_pb_resource_path()))
        self._data_object = _ModelingGroupData(
            name=reply.info.name,
            version=reply.info.version,
        )

    def _put(self) -> None:
        if self._data_object is None:
            raise RuntimeError("Cannot create PUT request, the data_object is uninitialized.")
        request = PutModelingGroupRequest(
            info=BasicInfo(resource_path=self._get_pb_resource_path(), name=self._data_object.name)
        )
        self._stub.Put(request)

    def _get_data_attribute(self, name: str) -> Any:
        return getattr(self._data_object, name)

    def _set_data_attribute(self, name: str, value: Any) -> None:
        setattr(self._data_object, name, value)

    name = grpc_data_property("name")
