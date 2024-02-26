modeling_ply = model.modeling_groups['nose'].modeling_plies['mp.nose.4']
elemental_data = modeling_ply.elemental_data
directions_plotter = pyacp.get_directions_plotter(
    model=model,
    components=[
        elemental_data.orientation,
        elemental_data.fiber_direction
    ],
    length_factor=10.,
    culling_factor=10,
)
directions_plotter.show()
