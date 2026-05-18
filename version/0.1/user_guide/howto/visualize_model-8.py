production_ply = model.modeling_groups['nose'].modeling_plies['mp.nose.6'].production_plies['ProductionPly.20']
ply_offset = production_ply.nodal_data.ply_offset
ply_offset.get_pyvista_glyphs(mesh=model.mesh, scaling_factor=6., culling_factor=5).plot()
