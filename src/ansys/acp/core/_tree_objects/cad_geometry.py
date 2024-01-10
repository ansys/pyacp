from __future__ import annotations

from collections.abc import Iterable
import dataclasses

import numpy as np
import numpy.typing as npt
import pyvista as pv
from typing_extensions import Self

from ansys.api.acp.v0 import (
    base_pb2,
    cad_component_pb2_grpc,
    cad_geometry_pb2,
    cad_geometry_pb2_grpc,
)

from .._utils.array_conversions import to_numpy
from .._utils.path_to_str import path_to_str_checked
from ._grpc_helpers.mapping import get_read_only_collection_property
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .cad_component import CADComponent
from .enums import status_type_from_pb
from .object_registry import register


@dataclasses.dataclass
class TriangleMesh:
    """Represents a mesh consisting of triangle faces only."""

    node_coordinates: npt.NDArray[np.float64]
    element_nodes: npt.NDArray[np.int64]

    @classmethod
    def _from_pb(cls, response: cad_geometry_pb2.TriangleMeshData) -> Self:
        """Construct a triangle mesh object from a protobuf response."""

        return cls(
            to_numpy(response.node_coordinates),
            to_numpy(response.element_nodes),
        )

    def to_pyvista(
        self,
    ) -> pv.PolyData:
        """Convert the mesh data to a PyVista object."""
        return pv.PolyData.from_regular_faces(
            points=self.node_coordinates,
            faces=self.element_nodes,
        )


@mark_grpc_properties
@register
class CADGeometry(CreatableTreeObject, IdTreeObject):
    """Instantiate a CAD Geometry.

    Parameters
    ----------
    name :
        Name of the CAD Geometry.
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

    external_path = grpc_data_property("properties.external_path", to_protobuf=path_to_str_checked)
    scale_factor = grpc_data_property("properties.scale_factor")
    use_default_precision = grpc_data_property("properties.use_default_precision")
    precision = grpc_data_property("properties.precision")
    use_default_offset = grpc_data_property("properties.use_default_offset")
    offset = grpc_data_property("properties.offset")

    @property
    def visualization_mesh(self) -> TriangleMesh:
        """The CAD Geometry's surface represented as a triangle mesh."""
        if not self._is_stored:
            raise RuntimeError("Cannot get mesh data from an unstored object")
        stub = cad_geometry_pb2_grpc.ObjectServiceStub(self._channel)
        response = stub.GetMesh(
            request=base_pb2.GetRequest(
                resource_path=self._resource_path,
            ),
        )
        return TriangleMesh._from_pb(response)

    root_shapes = property(
        get_read_only_collection_property(CADComponent, cad_component_pb2_grpc.ObjectServiceStub)
    )

    def refresh(self) -> None:
        """Reload the geometry from its external source."""
        stub = cad_geometry_pb2_grpc.ObjectServiceStub(self._channel)
        stub.Refresh(
            request=cad_geometry_pb2.RefreshRequest(
                resource_path=self._resource_path,
            ),
        )
