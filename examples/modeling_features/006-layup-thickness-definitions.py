# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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
.. _thickness_definition_example:

Thickness definition
====================

This example shows how the thickness of a ply can be defined by a geometry or a lookup table.
The example only shows the PyACP part of the setup. For a complete composite analysis,
see :ref:`pymapdl_workflow_example`.
"""


# %%
# Import modules
# --------------
#
# Import the standard library and third-party dependencies.
import pathlib
import tempfile

import numpy as np
import pyvista

# %%
# Import the PyACP dependencies.
from ansys.acp.core import PhysicalDimension, ThicknessType, launch_acp
from ansys.acp.core.extras import (
    FLAT_PLATE_SOLID_CAMERA,
    ExampleKeys,
    get_example_file,
    set_plot_theme,
)

# sphinx_gallery_thumbnail_number = 2

# %%
# Set the plot theme for the example. This is optional, and ensures that you get the
# same plot style (theme, color map, etc.) as in the online documentation.
set_plot_theme()

# %%
# Start ACP and load the model
# ----------------------------

# %%
# Get the example file from the server.
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_file = get_example_file(ExampleKeys.MINIMAL_FLAT_PLATE, WORKING_DIR)

# %%
# Launch the PyACP server and connect to it.
acp = launch_acp()

# %%
# Load the model from the input file.
# This example's input file contains a flat plate with a single ply.
model = acp.import_model(input_file)
print(model.unit_system)


# Plot the nominal ply thickness.
modeling_ply = model.modeling_groups["modeling_group"].modeling_plies["ply"]
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Define the thickness from a geometry
# ------------------------------------

# %%
# Add the solid geometry to the model that defines the thickness.
thickness_geometry_file = get_example_file(ExampleKeys.THICKNESS_GEOMETRY, WORKING_DIR)
thickness_geometry = model.create_cad_geometry()
thickness_geometry.refresh(thickness_geometry_file)

# Note: It is important to update the model here, because the root_shapes of the
# cad_geometry are not available until the model is updated.
model.update()

# %%
# Create a virtual geometry from the CAD geometry.
thickness_virtual_geometry = model.create_virtual_geometry(
    name="thickness_virtual_geometry", cad_components=thickness_geometry.root_shapes.values()
)

# %%
# Set the thickness type to ``FROM_GEOMETRY`` and define the virtual geometry.
modeling_ply.thickness_type = ThicknessType.FROM_GEOMETRY
modeling_ply.thickness_geometry = thickness_virtual_geometry

# %%
# Plot the ply thickness together with the geometry defining the thickness.
model.update()
assert model.elemental_data.thickness is not None
plotter = pyvista.Plotter()
# Plot the surface of the geometry
geometry_polydata = thickness_geometry.visualization_mesh.to_pyvista()
plotter.add_mesh(geometry_polydata, color="grey", opacity=0.05)
# Plot the edges of the geometry
edges = geometry_polydata.extract_feature_edges()
plotter.add_mesh(edges, color="white", line_width=4)
plotter.add_mesh(edges, color="black", line_width=2)
# Plot the ply thickness
plotter.add_mesh(model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh), show_edges=True)
plotter.camera_position = FLAT_PLATE_SOLID_CAMERA
plotter.show()

# %%
# Define the thickness from a lookup table
# ----------------------------------------

# %%
# Create the data for the lookup table.
# Make a 20x20 grid of points to define a thickness function on. In this example,
# the mesh of the lookup table is finer than the finite element mesh, and the thickness
# is interpolated onto the finite element mesh.
# Note that the plate lies in the xz plane and the thickness is defined in the y direction.
plate_side_length = 0.01
num_points = 3
x_coordinates = np.linspace(0, plate_side_length, num_points)
z_coordinates = np.linspace(0, plate_side_length, num_points)
xx, zz = np.meshgrid(x_coordinates, z_coordinates)

# %%
# Create a thickness that equals the distance to the center of the plate.
center_x = 0.005
center_z = 0.005
thickness = np.sqrt((xx - center_x) ** 2 + (zz - center_z) ** 2).ravel()

# %%
# Create the point coordinates for the lookup table.
# The y coordinate is always zero.
points = np.stack(
    [
        xx.ravel(),
        np.zeros(xx.ravel().shape),
        zz.ravel(),
    ],
    axis=1,
)

# %%
# Now you have a list of point coordinates:
print(points)

# %%
# And the corresponding thickness values.
print(thickness)

# %%
# Create the lookup table and add the coordinates and thickness data.
lookup_table = model.create_lookup_table_3d()
lookup_table.columns["Location"].data = points
thickness_column = lookup_table.create_column(
    data=thickness, physical_dimension=PhysicalDimension.LENGTH
)

# %%
# Set the thickness type to ``FROM_TABLE`` and assign the thickness column.
modeling_ply.thickness_type = ThicknessType.FROM_TABLE
modeling_ply.thickness_field = thickness_column

# %%
# Plot the ply thickness.
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)
