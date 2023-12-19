from __future__ import annotations

from collections.abc import Iterable
import typing

from ansys.api.acp.v0 import virtual_geometry_pb2, virtual_geometry_pb2_grpc

from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb, virtual_geometry_dimension_from_pb
from .object_registry import register

if typing.TYPE_CHECKING:
    from .cad_component import CADComponent


@mark_grpc_properties
@register
class VirtualGeometry(CreatableTreeObject, IdTreeObject):
    """Instantiate a Virtual Geometry.

    Parameters
    ----------
    name :
        Name of the Virtual Geometry.
    dimension :
        Dimension of the Virtual Geometry, if it is uniquely defined.
    sub_shapes :
        Paths of the CAD Components that make up the Virtual Geometry.
    """

    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "virtual_geometries"
    OBJECT_INFO_TYPE = virtual_geometry_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = virtual_geometry_pb2.CreateRequest

    def __init__(
        self,
        name: str = "VirtualGeometry",
        sub_shapes: Iterable[str] = (),
    ):
        super().__init__(
            name=name,
        )
        self.sub_shapes = sub_shapes

    def _create_stub(self) -> virtual_geometry_pb2_grpc.ObjectServiceStub:
        return virtual_geometry_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    dimension = grpc_data_property_read_only(
        "properties.dimension", from_protobuf=virtual_geometry_dimension_from_pb
    )
    sub_shapes = grpc_data_property("properties.sub_shapes")

    def set_cad_components(self, cad_components: Iterable[CADComponent]) -> None:
        sub_shapes = [component.path for component in cad_components]
        self.sub_shapes = sub_shapes
