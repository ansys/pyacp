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

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:  # pragma: no cover
    import pyvista
    from ansys.acp.core import Model
    from ansys.acp.core.mesh_data import MeshData
    from ansys.acp.core.mesh_data import VectorData

from ._utils.pyvista_import_check import requires_pyvista
from ._utils.string_manipulation import replace_underscores_and_capitalize

__all__ = ["get_directions_plotter"]

_acp_direction_colors = {
    "normal": (1.0, 0.6, 0.0),
    "orientation": (1.0, 0, 1.0),
    "reference_direction": (1.0, 1.0, 0),
    "fiber_direction": (0.0, 1.0, 0.0),
    "transverse_direction": (0.0, 0.64, 0.11),
    "draped_fiber_direction": (0.0, 1.0, 1.0),
    "draped_transverse_direction": (0.0, 0.0, 1.0),
    "material_1_direction": (1.0, 0.0, 0.0),
}


@requires_pyvista
def get_directions_plotter(
    *,
    model: "Model",
    mesh: "MeshData | None" = None,
    components: Sequence[Optional["VectorData"]],
    culling_factor: int = 1,
    length_factor: float = 1.0,
    **kwargs: Any,
) -> "pyvista.Plotter":
    """Get a pyvista plotter that shows the specified directions on the mesh.

    Parameters
    ----------
    model :
        ACP model. Determines the average element size used for scaling the
        arrows. Unless explicitly specified, the model also determines the
        mesh to plot.
    mesh :
        Mesh defining the scope of the plot. If not provided, the full mesh
        of the model is used.
    components:
        List of components to plot.
    culling_factor :
        If set to a value other than ``1``, add only every n-th data
        point to the PyVista object. This is useful especially for
        vector data, where the arrows can be too dense.
    length_factor:
        Factor to scale the length of the arrows.
    kwargs :
        Keyword arguments passed to the PyVista object constructor.
    """
    import pyvista

    if mesh is None:
        mesh = model.mesh

    plotter = pyvista.Plotter()
    plotter.add_mesh(mesh.to_pyvista(), color="white", show_edges=True)

    for vector_data in components:
        if vector_data is None:
            continue
        color = _acp_direction_colors.get(vector_data.component_name, "black")
        plotter.add_mesh(
            vector_data.get_pyvista_glyphs(
                mesh=mesh,
                factor=model.average_element_size * length_factor,
                culling_factor=culling_factor,
                **kwargs,
            ),
            color=color,
            label=replace_underscores_and_capitalize(vector_data.component_name),
        )
        plotter.add_legend(face=None, bcolor=[0.2, 0.2, 0.2], size=(0.25, 0.25))
    return plotter
