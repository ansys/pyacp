# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

from collections.abc import Iterable
import dataclasses
from typing import TYPE_CHECKING, cast

import numpy as np
import numpy.typing as npt
from typing_extensions import Self

if TYPE_CHECKING:  # pragma: no cover
    import pyvista

from ansys.api.acp.v0 import (
    base_pb2,
    cad_component_pb2_grpc,
    cad_geometry_pb2,
    cad_geometry_pb2_grpc,
)

from .._utils.array_conversions import to_numpy
from .._utils.path_to_str import path_to_str_checked
from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from .._utils.pyvista_import_check import requires_pyvista
from .._utils.typing_helper import PATH
from ._grpc_helpers.exceptions import wrap_grpc_errors
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

    @requires_pyvista
    def to_pyvista(
        self,
    ) -> pyvista.PolyData:
        """Convert the mesh data to a PyVista object."""
        import pyvista

        return pyvista.PolyData.from_regular_faces(
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
    _OBJECT_INFO_TYPE = cad_geometry_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = cad_geometry_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
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
    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")

    external_path: ReadWriteProperty[PATH, PATH] = grpc_data_property(
        "properties.external_path", to_protobuf=path_to_str_checked
    )
    scale_factor: ReadWriteProperty[float, float] = grpc_data_property("properties.scale_factor")
    use_default_precision: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_default_precision"
    )
    precision: ReadWriteProperty[float, float] = grpc_data_property("properties.precision")
    use_default_offset: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_default_offset"
    )
    offset: ReadWriteProperty[float, float] = grpc_data_property("properties.offset")

    @property
    def visualization_mesh(self) -> TriangleMesh:
        """Surface mesh for visualization.

        The CAD Geometry's surface represented as a triangle mesh.
        """
        if not self._is_stored:
            raise RuntimeError("Cannot get mesh data from an unstored object")
        stub = cast(cad_geometry_pb2_grpc.ObjectServiceStub, self._get_stub())
        with wrap_grpc_errors():
            response = stub.GetMesh(
                request=base_pb2.GetRequest(
                    resource_path=self._resource_path,
                ),
            )
        return TriangleMesh._from_pb(response)

    root_shapes = get_read_only_collection_property(
        object_class=CADComponent,
        stub_class=cad_component_pb2_grpc.ObjectServiceStub,
        requires_uptodate=True,
    )

    def refresh(self, path: PATH) -> None:
        """Reload the geometry from its external source.

        Parameters
        ----------
        path :
            Path of the new input file.
        """
        self.external_path = self._server_wrapper.auto_upload(path)
        stub = cast(cad_geometry_pb2_grpc.ObjectServiceStub, self._get_stub())
        with wrap_grpc_errors():
            stub.Refresh(
                request=cad_geometry_pb2.RefreshRequest(
                    resource_path=self._resource_path,
                ),
            )
