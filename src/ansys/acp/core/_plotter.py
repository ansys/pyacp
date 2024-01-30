from collections.abc import Sequence

import pyvista

from ansys.acp.core import Model, VectorData

colors = {
    "normal": "orange",
    "orientation": "purple",
    "reference_direction": "yellow",
    "fiber_direction": "green",
    "draped_fiber_direction": "blue"
    # todo add all colors
}


def get_directions_on_mesh_plotter(
    model: Model, vector_datas: Sequence[VectorData]
) -> pyvista.Plotter:
    plotter = pyvista.Plotter()
    plotter.add_mesh(model.mesh.to_pyvista(), color="white", show_edges=True)
    avg_element_size = 0.001
    for vector_data in vector_datas:
        color = colors.get(vector_data.component_name, "black")
        plotter.add_mesh(
            vector_data.get_pyvista_glyphs(mesh=model.mesh, factor=avg_element_size), color=color
        )
    return plotter
