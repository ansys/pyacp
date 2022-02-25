from typing import Any
from typing import cast
from typing import Dict

from ansys.api.acp.v0.base_pb2 import BasicInfo
from ansys.api.acp.v0.base_pb2 import ResourcePath
from ansys.api.acp.v0.modeling_group_pb2 import ModelingGroupRequest
from ansys.api.acp.v0.modeling_group_pb2 import PutModelingGroupRequest
from ansys.api.acp.v0.modeling_group_pb2_grpc import ModelingGroupStub

from ._launcher import ServerProtocol

__all__ = ["ModelingGroup"]


class ModelingGroup:
    COLLECTION_LABEL = "modeling_groups"

    def __init__(self, *, resource_path: str, server: ServerProtocol):
        self._resource_path = resource_path
        self._server = server
        self._stub = ModelingGroupStub(self._server.channel)
        self._property_cache: Dict[str, Any] = {}

    @property
    def name(self) -> str:
        request = ModelingGroupRequest(resource_path=self._get_pb_resource_path())
        res = self._stub.Get(request)
        self._property_cache = {
            "name": res.info.name,
            "version": res.info.version,
        }
        return cast(str, self._property_cache["name"])

    @name.setter
    def name(self, value: str) -> None:
        if value != self._property_cache["name"]:
            # TODO: add version to Put request
            request = PutModelingGroupRequest(
                info=BasicInfo(resource_path=self._get_pb_resource_path(), name=value)
            )
            # TODO: handle case where Put is rejected
            res = self._stub.Put(request)
            self._property_cache = {
                "name": res.info.name,
                "version": res.info.version,
            }

    def _get_pb_resource_path(self) -> ResourcePath:
        return ResourcePath(value=self._resource_path)
