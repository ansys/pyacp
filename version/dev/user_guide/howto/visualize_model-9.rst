import pyvista
plotter = pyvista.Plotter()
_ = plotter.add_mesh(model.mesh.to_pyvista(), color="white", opacity=0.5)
_ = plotter.add_mesh(
    ply_offset.get_pyvista_glyphs(mesh=model.mesh, scaling_factor=6., culling_factor=5),
    color="blue"
)
plotter.show()
