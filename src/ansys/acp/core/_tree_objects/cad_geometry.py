from __future__ import annotations

from collections.abc import Iterable

from ansys.api.acp.v0 import cad_geometry_pb2, cad_geometry_pb2_grpc

from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .object_registry import register


@mark_grpc_properties
@register
class CADGeometry(CreatableTreeObject, IdTreeObject):
    """Instantiate an edge set.

    Parameters
    ----------
    name :
        Name of the edge set.
    external_path :
        Path to the CAD file.
    scale_factor :
        Scale factor applied to the CAD geometry.
    use_default_precision :
        Whether to use the default precision value.
    precision :
        Precision of geometrical operations such as intersection points, thickness sampling, etc.
    use_default_offset :
        Whether to use the default offset value.
    offset :
        Offset value used to analyze the surface's coverage regarding the mesh.
    """

    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "cad_geometries"
    OBJECT_INFO_TYPE = cad_geometry_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = cad_geometry_pb2.CreateRequest

    def __init__(
        self,
        name: str = "CADGeometry",
        external_path: str = "",
        scale_factor: float = 1.0,
        use_default_precision: bool = True,
        precision: float = 1e-3,
        use_default_offset: bool = True,
        offset: float = 0.0,
    ):
        super().__init__(
            name=name,
        )
        self.external_path = external_path
        self.scale_factor = scale_factor
        self.use_default_precision = use_default_precision
        self.precision = precision
        self.use_default_offset = use_default_offset
        self.offset = offset

    def _create_stub(self) -> cad_geometry_pb2_grpc.ObjectServiceStub:
        return cad_geometry_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    locked = grpc_data_property_read_only("properties.locked")

    external_path = grpc_data_property("properties.external_path")
    scale_factor = grpc_data_property("properties.scale_factor")
    use_default_precision = grpc_data_property("properties.use_default_precision")
    precision = grpc_data_property("properties.precision")
    use_default_offset = grpc_data_property("properties.use_default_offset")
    offset = grpc_data_property("properties.offset")
