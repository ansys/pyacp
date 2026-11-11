thickness_data = model.elemental_data.thickness
pyvista_mesh = thickness_data.get_pyvista_mesh(mesh=model.mesh)
pyvista_mesh.plot()
