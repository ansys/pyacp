cad_geometry = model.cad_geometries['nose_geometry']
tessellated_mesh = cad_geometry.visualization_mesh
tessellated_mesh.to_pyvista().plot(show_edges=True)
