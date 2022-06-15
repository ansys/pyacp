from typing import Any, Optional

from ansys.api.acp.v0.base_pb2 import BasicInfo, ResourcePath
from ansys.api.acp.v0.rosette_pb2 import PutRosetteRequest, RosetteProperties, RosetteRequest
from ansys.api.acp.v0.rosette_pb2_grpc import RosetteStub

from ._data_objects.rosette import Rosette as _RosetteData
from ._log import LOGGER
from ._property_helper import ResourceProtocol, grpc_data_property, grpc_data_property_read_only
from ._server import ServerProtocol
from .utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .utils.enum_conversions import status_type_to_string

__all__ = ["Rosette"]


class Rosette(ResourceProtocol):
    COLLECTION_LABEL = "rosettes"

    def __init__(self, *, resource_path: str, server: ServerProtocol):
        self._resource_path = resource_path
        self._server = server
        self._stub = RosetteStub(self._server.channel)
        self._data_object: Optional[_RosetteData] = None

    def _get_pb_resource_path(self) -> ResourcePath:
        return ResourcePath(value=self._resource_path)

    def _get(self) -> None:
        LOGGER.debug("Rosette Get request.")
        reply = self._stub.Get(RosetteRequest(resource_path=self._get_pb_resource_path()))
        self._data_object = _RosetteData(
            name=reply.info.name,
            id=reply.info.id,
            version=reply.info.version,
            locked=reply.properties.locked,
            status=status_type_to_string(reply.properties.status),
            origin=to_tuple_from_1D_array(reply.properties.origin),
            dir1=to_tuple_from_1D_array(reply.properties.dir1),
            dir2=to_tuple_from_1D_array(reply.properties.dir2),
        )

    def _put(self) -> None:
        if self._data_object is None:
            raise RuntimeError("Cannot create PUT request, the data_object is uninitialized.")
        request = PutRosetteRequest(
            info=BasicInfo(
                resource_path=self._get_pb_resource_path(),
                name=self._data_object.name,
                version=self._data_object.version,
            ),
            properties=RosetteProperties(
                origin=to_1D_double_array(self._data_object.origin),
                dir1=to_1D_double_array(self._data_object.dir1),
                dir2=to_1D_double_array(self._data_object.dir2),
            ),
        )
        LOGGER.debug("Rosette Put request.")
        self._stub.Put(request)

    def _get_data_attribute(self, name: str) -> Any:
        return getattr(self._data_object, name)

    def _set_data_attribute(self, name: str, value: Any) -> None:
        setattr(self._data_object, name, value)

    name = grpc_data_property("name")
    id = grpc_data_property_read_only("id")

    locked = grpc_data_property_read_only("locked")
    status = grpc_data_property_read_only("status")
    origin = grpc_data_property("origin")
    dir1 = grpc_data_property("dir1")
    dir2 = grpc_data_property("dir2")
