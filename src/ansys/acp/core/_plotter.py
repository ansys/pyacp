from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

import pyvista

if TYPE_CHECKING:
    from ansys.acp.core import Model
    from ansys.acp.core import VectorData

from ansys.acp.core._utils.visualization import _replace_underscores_and_capitalize

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


def get_directions_plotter(
    *,
    model: "Model",
    components: Sequence["VectorData"],
    culling_factor: int = 1,
    length_factor: float = 1.0,
    **kwargs: Any,
) -> pyvista.Plotter:
    """

    Parameters
    ----------
    model:
        ACP Model.
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

    plotter = pyvista.Plotter()
    plotter.add_mesh(model.mesh.to_pyvista(), color="white", show_edges=True)

    for vector_data in components:
        color = _acp_direction_colors.get(vector_data.component_name, "black")
        plotter.add_mesh(
            vector_data.get_pyvista_glyphs(
                mesh=model.mesh,
                factor=model.average_element_size * length_factor,
                culling_factor=culling_factor,
                **kwargs,
            ),
            color=color,
            label=_replace_underscores_and_capitalize(vector_data.component_name),
        )
        plotter.add_legend(face=None, bcolor=[0.2, 0.2, 0.2], size=(0.25, 0.25))
    return plotter
