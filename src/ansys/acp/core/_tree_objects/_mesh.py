# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
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

import dataclasses

import numpy as np
import numpy.typing as npt
from pyvista.core.pointset import UnstructuredGrid

from ansys.api.acp.v0 import mesh_query_pb2, mesh_query_pb2_grpc

from .._utils.array_conversions import to_numpy
from .._utils.property_protocols import ReadOnlyProperty
from .._utils.visualization import to_pyvista_faces, to_pyvista_types
from .base import TreeObject

__all__ = [
    "MeshData",
    "mesh_property",
    "shell_mesh_property",
    "solid_mesh_property",
]


@dataclasses.dataclass
class MeshData:
    """Container for the mesh data of an ACP Model."""

    node_labels: npt.NDArray[np.int32]
    node_coordinates: npt.NDArray[np.float64]
    element_labels: npt.NDArray[np.int32]
    element_types: npt.NDArray[np.int32]
    element_nodes: npt.NDArray[np.int32]
    element_nodes_offsets: npt.NDArray[np.int32]

    def to_pyvista(self) -> UnstructuredGrid:
        """Convert the mesh data to a PyVista mesh."""
        return UnstructuredGrid(
            to_pyvista_faces(
                element_types=self.element_types,
                element_nodes=self.element_nodes,
                element_nodes_offsets=self.element_nodes_offsets,
            ),
            to_pyvista_types(self.element_types),
            self.node_coordinates,
        )


def _mesh_property_impl(
    element_scoping: mesh_query_pb2.ElementScopingType.ValueType, doc: str
) -> ReadOnlyProperty[MeshData]:
    def getter(self: TreeObject) -> MeshData:
        mesh_query_stub = mesh_query_pb2_grpc.MeshQueryServiceStub(self._channel)
        reply = mesh_query_stub.GetMeshData(
            mesh_query_pb2.GetMeshDataRequest(
                resource_path=self._resource_path, element_scoping=element_scoping
            )
        )
        return MeshData(
            node_labels=to_numpy(reply.node_labels),
            node_coordinates=to_numpy(reply.node_coordinates),
            element_labels=to_numpy(reply.element_labels),
            element_types=to_numpy(reply.element_types),
            element_nodes=to_numpy(reply.element_nodes),
            element_nodes_offsets=to_numpy(reply.element_nodes_offsets),
        )

    return property(getter, doc=doc)


mesh_property = _mesh_property_impl(
    mesh_query_pb2.ElementScopingType.ALL, doc="Full mesh associated with the object."
)
shell_mesh_property = _mesh_property_impl(
    mesh_query_pb2.ElementScopingType.SHELL, doc="Shell mesh associated with the object."
)
solid_mesh_property = _mesh_property_impl(
    mesh_query_pb2.ElementScopingType.SOLID, doc="Solid mesh associated with the object."
)
