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

"""Helper functions for converting ACP data to PyVista data structures."""

from enum import IntEnum

import numpy as np
import numpy.typing as npt
from pyvista.core.celltype import CellType as pv_CellType


class ElementType(IntEnum):
    """Enumeration of ACP element types."""

    VERTEX_ELEMENT = 100
    LINK2N3D = 101
    BEAM2N3D = 111

    SHELL3N = 121
    SHELL4N = 122
    LAYERED_SHELL4N = 123
    LAYERED_SHELL8N = 124
    LAYERED_SHELL3N = 125
    LAYERED_SHELL4N_QM6 = 126
    LAYERED_SHELL6N = 128
    LAYERED_SHELL4N_SIMPSON = 129

    TETRA4N = 131
    TETRA10N = 132
    PYRAMID5N = 133
    PYRAMID13N = 134

    HEXA8N = 141
    HEXA20N = 142
    PRISM6N = 143
    PRISM15N = 144

    PLANE6N_PLANE_STRAIN = 150
    PLANE6N_PLANE_STRESS = 151
    PLANE8N_PLANE_STRAIN = 152
    PLANE8N_PLANE_STRESS = 153

    LAYERED_HEXA8N = 161
    LAYERED_HEXA20N = 162
    LAYERED_PRISM6N = 163
    LAYERED_PRISM15N = 164

    DRAPING_SHELL4N = 170

    INTERFACE_ELEMENT6N = 180
    INTERFACE_ELEMENT8N = 181
    INTERFACE_ELEMENT12N = 182
    INTERFACE_ELEMENT16N = 183

    LAYERED_POLYHEDRON = 190


ELEMENT_TO_PYVISTA_TYPE = {
    ElementType.VERTEX_ELEMENT: pv_CellType.VERTEX,
    ElementType.LINK2N3D: pv_CellType.LINE,
    ElementType.BEAM2N3D: pv_CellType.LINE,
    ElementType.SHELL3N: pv_CellType.TRIANGLE,
    ElementType.SHELL4N: pv_CellType.QUAD,
    ElementType.LAYERED_SHELL4N: pv_CellType.QUAD,
    ElementType.LAYERED_SHELL8N: pv_CellType.QUADRATIC_QUAD,
    ElementType.LAYERED_SHELL3N: pv_CellType.TRIANGLE,
    ElementType.LAYERED_SHELL4N_QM6: pv_CellType.QUAD,
    ElementType.LAYERED_SHELL6N: pv_CellType.QUADRATIC_TRIANGLE,
    ElementType.LAYERED_SHELL4N_SIMPSON: pv_CellType.QUAD,
    ElementType.TETRA4N: pv_CellType.TETRA,
    ElementType.TETRA10N: pv_CellType.QUADRATIC_TETRA,
    ElementType.PYRAMID5N: pv_CellType.PYRAMID,
    ElementType.PYRAMID13N: pv_CellType.QUADRATIC_PYRAMID,
    ElementType.HEXA8N: pv_CellType.HEXAHEDRON,
    ElementType.HEXA20N: pv_CellType.QUADRATIC_HEXAHEDRON,
    ElementType.PRISM6N: pv_CellType.WEDGE,
    ElementType.PRISM15N: pv_CellType.QUADRATIC_WEDGE,
    ElementType.PLANE6N_PLANE_STRAIN: pv_CellType.QUADRATIC_TRIANGLE,
    ElementType.PLANE6N_PLANE_STRESS: pv_CellType.QUADRATIC_TRIANGLE,
    ElementType.PLANE8N_PLANE_STRAIN: pv_CellType.QUADRATIC_QUAD,
    ElementType.PLANE8N_PLANE_STRESS: pv_CellType.QUADRATIC_QUAD,
    ElementType.LAYERED_HEXA8N: pv_CellType.HEXAHEDRON,
    ElementType.LAYERED_HEXA20N: pv_CellType.QUADRATIC_HEXAHEDRON,
    ElementType.LAYERED_PRISM6N: pv_CellType.WEDGE,
    ElementType.LAYERED_PRISM15N: pv_CellType.QUADRATIC_WEDGE,
    ElementType.DRAPING_SHELL4N: pv_CellType.QUAD,
    ElementType.INTERFACE_ELEMENT6N: pv_CellType.WEDGE,
    ElementType.INTERFACE_ELEMENT8N: pv_CellType.HEXAHEDRON,
    ElementType.INTERFACE_ELEMENT12N: pv_CellType.TRIANGLE,
    ElementType.INTERFACE_ELEMENT16N: pv_CellType.QUAD,
    ElementType.LAYERED_POLYHEDRON: pv_CellType.POLYHEDRON,
}


def to_pyvista_faces(
    *,
    element_types: npt.NDArray[np.int32],
    element_nodes: npt.NDArray[np.int32],
    element_nodes_offsets: npt.NDArray[np.int32],
) -> npt.NDArray[np.int32]:
    """Convert ACP element data to PyVista faces."""
    target_size = element_types.size + element_nodes.size
    # InterfaceElement12N and InterfaceElement16N are not supported by VTK;
    # they are shown as shell 3n and 4n, respectively.
    INTERFACE_ELEMENT_12N = 182
    INTERFACE_ELEMENT_16N = 183
    target_size -= 9 * np.sum(element_types == INTERFACE_ELEMENT_12N)
    target_size -= 12 * np.sum(element_types == INTERFACE_ELEMENT_16N)

    faces = np.empty(target_size, dtype=np.int32)

    target_idx = 0
    for i, element_type in enumerate(element_types):
        start_idx = element_nodes_offsets[i]

        if element_type == INTERFACE_ELEMENT_12N:
            end_idx = start_idx + 3
        elif element_type == INTERFACE_ELEMENT_16N:
            end_idx = start_idx + 4
        else:
            try:
                end_idx = element_nodes_offsets[i + 1]
            except IndexError:
                end_idx = element_nodes.size

        current_size = end_idx - start_idx
        faces[target_idx] = current_size
        target_idx += 1
        faces[target_idx : target_idx + current_size] = element_nodes[start_idx:end_idx]
        target_idx += current_size
    return faces


def to_pyvista_types(element_types: npt.NDArray[np.int32]) -> npt.NDArray[np.int32]:
    """Convert ACP element types to PyVista cell types."""
    return np.array([ELEMENT_TO_PYVISTA_TYPE[el_type] for el_type in element_types])
