import os
from typing import Any
from typing import cast
from typing import Dict
from typing import Tuple
from typing import Union

from ansys.api.acp.v0.base_pb2 import BasicInfo
from ansys.api.acp.v0.base_pb2 import CollectionPath
from ansys.api.acp.v0.base_pb2 import ResourcePath
from ansys.api.acp.v0.model_pb2 import LoadModelRequest
from ansys.api.acp.v0.model_pb2 import ModelRequest
from ansys.api.acp.v0.model_pb2 import PutModelRequest
from ansys.api.acp.v0.model_pb2 import SaveModelRequest
from ansys.api.acp.v0.model_pb2 import UpdateModelRequest
from ansys.api.acp.v0.model_pb2_grpc import ModelStub
from ansys.api.acp.v0.modeling_group_pb2 import CreateModelingGroupRequest
from ansys.api.acp.v0.modeling_group_pb2 import ListModelingGroupsRequest
from ansys.api.acp.v0.modeling_group_pb2_grpc import ModelingGroupStub

from ._launcher import ServerProtocol
from ._modeling_group import ModelingGroup
from ._resource_paths import join as _rp_join

__all__ = ["Model"]

_PATH = Union[str, os.PathLike]


class Model:
    # TODO: make resource_path have a non-str type?
    def __init__(self, *, resource_path: str, server: ServerProtocol):
        self._resource_path = resource_path
        # self._has_unsynced_writes = False
        self._server = server
        self._stub = ModelStub(self._server.channel)
        self._property_cache: Dict[str, Any] = {}

    @classmethod
    def from_file(cls, path: _PATH, server: ServerProtocol) -> "Model":
        # Send absolute paths to the server, since its CWD may not match
        # the Python CWD.
        request = LoadModelRequest(path=os.path.abspath(path))
        response = ModelStub(server.channel).LoadFromFile(request)
        return cls(resource_path=response.info.resource_path.value, server=server)

    @property
    def name(self) -> str:
        request = ModelRequest(resource_path=self._get_pb_resource_path())
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
            request = PutModelRequest(
                info=BasicInfo(resource_path=self._get_pb_resource_path(), name=value)
            )
            # TODO: handle case where Put is rejected
            res = self._stub.Put(request)
            self._property_cache = {
                "name": res.info.name,
                "version": res.info.version,
            }

    def update(self, *, relations_only: bool = False) -> None:
        self._stub.Update(
            UpdateModelRequest(
                resource_path=self._get_pb_resource_path(), relations_only=relations_only
            )
        )

    def save(self, path: _PATH) -> None:
        self._stub.SaveToFile(
            SaveModelRequest(resource_path=self._get_pb_resource_path(), path=os.path.abspath(path))
        )

    def _get_pb_resource_path(self) -> ResourcePath:
        return ResourcePath(value=self._resource_path)

    def _get_pb_model_request(self) -> ModelRequest:
        return ModelRequest(resource_path=self._get_pb_resource_path())

    def create_modeling_group(self, name: str) -> ModelingGroup:
        collection_path = CollectionPath(
            value=_rp_join(self._resource_path, ModelingGroup.COLLECTION_LABEL)
        )
        stub = ModelingGroupStub(self._server.channel)
        request = CreateModelingGroupRequest(collection_path=collection_path, name=name)
        reply = stub.Create(request)
        return ModelingGroup(resource_path=reply.info.resource_path.value, server=self._server)

    @property
    def modeling_groups(self) -> Tuple[ModelingGroup, ...]:
        collection_path = CollectionPath(
            value=_rp_join(self._resource_path, ModelingGroup.COLLECTION_LABEL)
        )
        stub = ModelingGroupStub(self._server.channel)
        request = ListModelingGroupsRequest(collection_path=collection_path)
        reply = stub.List(request)
        return tuple(
            ModelingGroup(resource_path=mg.info.resource_path.value, server=self._server)
            for mg in reply.modeling_groups
        )
