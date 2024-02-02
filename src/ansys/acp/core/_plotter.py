from collections.abc import Sequence

import pyvista

from ansys.acp.core import Model, VectorData
from ansys.acp.core._utils.visualization import _replace_underscores_and_capitalize

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

# Todo StrEnum type for component_name
# todo: docs
# add culling factor, factor and kwargs


def get_directions_on_mesh_plotter(
    model: Model, vector_datas: Sequence[VectorData]
) -> pyvista.Plotter:
    plotter = pyvista.Plotter()
    plotter.add_mesh(model.mesh.to_pyvista(), color="white", show_edges=True)

    for vector_data in vector_datas:
        color = _acp_direction_colors.get(vector_data.component_name, "black")
        plotter.add_mesh(
            vector_data.get_pyvista_glyphs(mesh=model.mesh, factor=model.average_element_size),
            color=color,
            label=_replace_underscores_and_capitalize(vector_data.component_name),
        )
        plotter.add_legend(face=None, bcolor="w")
    return plotter
