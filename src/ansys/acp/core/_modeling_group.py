from typing import Any, Optional

from ansys.api.acp.v0.base_pb2 import BasicInfo, ResourcePath
from ansys.api.acp.v0.modeling_group_pb2 import ModelingGroupRequest, PutModelingGroupRequest
from ansys.api.acp.v0.modeling_group_pb2_grpc import ModelingGroupStub

from ._data_objects.modeling_group import ModelingGroup as _ModelingGroupData
from ._log import LOGGER
from ._property_helper import ResourceProtocol, grpc_data_property
from ._server import ServerProtocol

__all__ = ["ModelingGroup"]


class ModelingGroup(ResourceProtocol):
    COLLECTION_LABEL = "modeling_groups"

    def __init__(self, *, resource_path: str, server: ServerProtocol):
        self._resource_path = resource_path
        self._server = server
        self._stub = ModelingGroupStub(self._server.channel)
        self._data_object: Optional[_ModelingGroupData] = None

    def _get_pb_resource_path(self) -> ResourcePath:
        return ResourcePath(value=self._resource_path)

    def _get(self) -> None:
        LOGGER.debug("ModelingGroup Get request.")
        reply = self._stub.Get(ModelingGroupRequest(resource_path=self._get_pb_resource_path()))
        self._data_object = _ModelingGroupData(
            name=reply.info.name,
            id=reply.info.id,
            version=reply.info.version,
        )

    def _put(self) -> None:
        if self._data_object is None:
            raise RuntimeError("Cannot create PUT request, the data_object is uninitialized.")
        request = PutModelingGroupRequest(
            info=BasicInfo(
                resource_path=self._get_pb_resource_path(),
                name=self._data_object.name,
                version=self._data_object.version,
            )
        )
        LOGGER.debug("ModelingGroup Put request.")
        self._stub.Put(request)

    def _get_data_attribute(self, name: str) -> Any:
        return getattr(self._data_object, name)

    def _set_data_attribute(self, name: str, value: Any) -> None:
        setattr(self._data_object, name, value)

    name = grpc_data_property("name")
    id = grpc_data_property("id")
