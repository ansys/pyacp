# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
.. _imported_plies_example:

Imported ply example
============================

The definition and use of imported plies is demonstrated in this example.
In a nutshell, the difference between :class:`.ImportedModelingPly` and a
:class:`.ModelingPly` is that the surface mesh of an :class:`.ImportedModelingPly`
is defined by an external source, such as a CAD surface, where a :class:`.ModelingPly`
is always defined on the initial loaded shell mesh.
Therefore, an imported ply can only be used in combination with an
:class:`.ImportedSolidModel`.

This examples shows hot to:

- Load an initial mesh
- Add a :class:`.Material` and :class:`.Fabric`
- Import geometries which will be used to define the surface of the :class:`.ImportedModelingPly`
- Add two imported modeling plies
- Create an :class:`.ImportedSolidModel`
- Map the imported plies to the solid model
- Visualized the mapped plies.
"""

# %%
# Import modules
# --------------
#
# Import the standard library and third-party dependencies.
import pathlib
import tempfile
import os
import pyvista

# %%
# Import the PyACP dependencies.
from ansys.acp.core import launch_acp, ImportedPlyOffsetType, CADGeometry, \
    VirtualGeometry, PlyType
from ansys.acp.core.extras import ExampleKeys, get_example_file
from ansys.acp.core.material_property_sets import ConstantEngineeringConstants, ConstantDensity

# sphinx_gallery_thumbnail_number = 3


# %%
# Start ACP and load the model
# ----------------------------

# %%
# Get the example file from the server.
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_DAT, WORKING_DIR)

# %%
# Launch the PyACP server and connect to it.
acp = launch_acp()

# %%
# Create a model by loading a shell mesh
model = acp.import_model(path=input_file, format="ansys:dat")

# %%
# Add a material and a fabric with 1mm thickness.
# The fabric is used for the imported modeling ply.
engineering_constants_ud = ConstantEngineeringConstants.from_orthotropic_constants(
    E1=5e10, E2=1e10, E3=1e10, nu12=0.28, nu13=0.28, nu23=0.3, G12=5e9, G23=4e9, G31=4e9
)
density_ud = ConstantDensity(rho=2700)

ud_material = model.create_material(
    name="E-Glass UD",
    ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants_ud,
    density=density_ud,
)

engineering_resin = ConstantEngineeringConstants.from_isotropic_constants(
    E=5e9, nu=0.3
)
density_resin = ConstantDensity(rho=1200)

void_material = model.create_material(
    name="Void material",
    ply_type=PlyType.ISOTROPIC,
    engineering_constants=engineering_resin,
    density=density_resin,
)
filler_material = model.create_material(
    name="Filler material",
    ply_type=PlyType.ISOTROPIC,
    engineering_constants=engineering_resin,
    density=density_resin,
)

fabric = model.create_fabric(name="E-Glass Fabric", material=ud_material, thickness=0.001)


# %%
# Import two cad surfaces to define the surface of the imported modeling plies.
def create_virtual_geometry_from_file(
        example_key: ExampleKeys,
) -> tuple[CADGeometry, VirtualGeometry]:
    """Create a CAD geometry and virtual geometry."""
    geometry_file = get_example_file(example_key, WORKING_DIR)
    geometry_obj = model.create_cad_geometry()
    geometry_obj.refresh(geometry_file)  # upload and load the geometry file
    model.update()
    virtual_geometry = model.create_virtual_geometry(
        name=os.path.basename(geometry_file), cad_components=geometry_obj.root_shapes.values()
    )
    return geometry_obj, virtual_geometry


triangle_surf_cad, triangle_surf_vcad = create_virtual_geometry_from_file(ExampleKeys.RULE_GEOMETRY_TRIANGLE)
top_surf_cad, top_surf_vcad = create_virtual_geometry_from_file(ExampleKeys.SNAP_TO_GEOMETRY)

imported_ply_group = model.create_imported_modeling_group(name="Imported Ply Group")
imported_ply_triangle = imported_ply_group.create_imported_modeling_ply(
    name="Triangle Ply",
    offset_type=ImportedPlyOffsetType.BOTTOM_OFFSET,
    ply_material=fabric,
    mesh_geometry=triangle_surf_vcad,
    ply_angle=0,
    rosettes=[model.rosettes["12"]],
)

imported_ply_top = imported_ply_group.create_imported_modeling_ply(
    name="Triangle Ply",
    offset_type=ImportedPlyOffsetType.MIDDLE_OFFSET,
    ply_material=fabric,
    mesh_geometry=top_surf_vcad,
    ply_angle=45,
    rosettes=[model.rosettes["12"]],
)
model.update()


# %%
# Imported plies cannot be visualized directly but the cad geometries are
# shown here instead.
def plotter_with_all_geometries(cad_geometries):
    colors = ["green", "yellow", "blue", "red"]
    plotter = pyvista.Plotter()
    for index, cad in enumerate(cad_geometries):
        geom_mesh = cad.visualization_mesh.to_pyvista()
        plotter.add_mesh(geom_mesh, color=colors[index], opacity=0.1)
        edges = geom_mesh.extract_feature_edges()
        plotter.add_mesh(edges, color="white", line_width=4)
        plotter.add_mesh(edges, color="black", line_width=2)
    return plotter


plotter = plotter_with_all_geometries([triangle_surf_cad, top_surf_cad])
plotter.show()

# %%
# An external solid mesh is loaded now to map the imported plies
# onto the solid model.
solid_mesh_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_SOLID_MESH_CDB, WORKING_DIR)
imported_solid_model = model.create_imported_solid_model(
    name="Imported Solid Model",
    external_path=solid_mesh_file,
    format="ansys:cdb",
)
imported_solid_model.import_initial_mesh()
plotter = plotter_with_all_geometries([triangle_surf_cad, top_surf_cad])
plotter.add_mesh(imported_solid_model.solid_mesh.to_pyvista(), show_edges=True, opacity=0.5)
plotter.show()

# %%
# Add a mapping object to link the imported plies with the solid model.
# In this example, all imported plies are mapped in one go.
# The remaining elemental volume and elements which do not intersect
# with the imported plies are filled with a void and filler material,
# respectively.
imported_solid_model.create_layup_mapping_object(
    name="Map imported plies",
    use_imported_plies=True,  # enable imported plies
    select_all_plies=True,  # select all plies
    entire_solid_mesh=True,
    scale_ply_thicknesses=False,
    void_material=void_material,
    delete_lost_elements=False,
    filler_material=filler_material,
    rosettes=[model.rosettes["12"]],
)
model.update()

# %%
# Show the imported ply geometries and mapped plies on the solid model.
# Note that the analysis plies are not yet directly accessible via
# the API of the imported solid model. Also, elemental data such as
# thicknesses are not yet implemented for imported plies.
plotter = plotter_with_all_geometries([triangle_surf_cad, top_surf_cad])
for imported_ply in [imported_ply_triangle, imported_ply_top]:
    for pp in imported_ply.imported_production_plies.values():
        for ap in pp.imported_analysis_plies.values():
            plotter.add_mesh(ap.solid_mesh.to_pyvista(), show_edges=True, opacity=1)
plotter.add_mesh(mesh=imported_solid_model.solid_mesh.to_pyvista(), show_edges=False, opacity=0.2)
plotter.show()

# %%
# Show the elemental mass for the entire solid model
"""
!!! This does not work yet.
assert model.elemental_data.mass is not None
model.elemental_data.mass.get_pyvista_mesh(mesh=model.solid_mesh).plot(show_edges=True)
"""

# %%
# The imported solid model could be now passed to Mechanical or MAPDL as shown
# in the examples :ref:`pymechanical_solid_example` and
# :ref:`pymapdl_workflow_example`.
