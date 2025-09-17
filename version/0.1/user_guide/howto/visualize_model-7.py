pyvista_mesh = thickness_data.get_pyvista_mesh(mesh=model.element_sets["els_wing_assembly"].mesh)
pyvista_mesh.plot()
