directions_plotter = pyacp.get_directions_plotter(
    model=model,
    mesh=modeling_ply.mesh,
    components=[
        elemental_data.orientation,
        elemental_data.fiber_direction
    ],
    length_factor=10.,
    culling_factor=10,
)
directions_plotter.show()
