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
.. _thickness_definition_example:

Thickness definition example
============================

This example shows how the thickness of a ply can be defined by a geometry or a lookup table.
This example shows just the pyACP part of the setup.  For a complete Composite analysis,
see the :ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py` example
"""


# %%
# Import standard library and third-party dependencies.
import pathlib
import tempfile

import numpy as np
import pyvista

# %%
# Import pyACP dependencies
from ansys.acp.core import ACPWorkflow, DimensionType, ThicknessType, example_helpers, launch_acp
from ansys.acp.core.example_helpers import ExampleKeys, get_example_file

# %%
# Start ACP and load the model
# ----------------------------

# %%
# Get example file from server
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_file = get_example_file(ExampleKeys.MINIMAL_FLAT_PLATE, WORKING_DIR)

# %%
# Launch the PyACP server and connect to it.
acp = launch_acp()

# %%
# Define the input file and instantiate an ACPWorkflow.
# The ACPWorkflow class provides convenience methods which simplify the file handling.
# It automatically creates a model based on the input file.
# The input file contains a flat plate with a single ply.
workflow = ACPWorkflow.from_acph5_file(
    acp=acp,
    acph5_file_path=input_file,
    local_working_directory=WORKING_DIR,
)

model = workflow.model
print(workflow.working_directory.path)
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
thickness_geometry_file = example_helpers.get_example_file(
    example_helpers.ExampleKeys.THICKNESS_GEOMETRY, WORKING_DIR
)
thickness_geometry = workflow.add_cad_geometry_from_local_file(thickness_geometry_file)

# Note: It is important to update the model here, because the root_shapes of the
# cad_geometry are not available until the model is updated.
model.update()

# %%
# Create a virtual geometry from the CAD geometry.
thickness_virtual_geometry = model.create_virtual_geometry(
    name="thickness_virtual_geometry", cad_components=thickness_geometry.root_shapes.values()
)

# %%
# Set the thickness type to "from geometry" and define the virtual geometry.
modeling_ply.thickness_type = ThicknessType.FROM_GEOMETRY
modeling_ply.thickness_geometry = thickness_virtual_geometry

# %%
# Plot the ply thickness together with the geometry that defines the thickness.
model.update()
assert model.elemental_data.thickness is not None
plotter = pyvista.Plotter()
plotter.add_mesh(
    thickness_geometry.visualization_mesh.to_pyvista(), color="white", style="wireframe"
)
plotter.add_mesh(model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh), show_edges=True)

plotter.show()

# %%
# Define the thickness from a lookup table
# ----------------------------------------

# %%
# Create the data for the lookup table.
# Create a 20x20 grid of points on which a thickness function is defined. In this case
# the mesh of the lookup table is finer than the Finite Element mesh and the thickness
# is interpolated onto the Finite Element mesh.
# Note: the plate lies in the x-z plane and the thickness is defined in the y direction.
plate_side_length = 0.01
num_points = 3
x_coordinates = np.linspace(0, plate_side_length, num_points)
z_coordinates = np.linspace(0, plate_side_length, num_points)
xx, zz = np.meshgrid(x_coordinates, z_coordinates)

# %%
# Create a thickness equal to the distance to the center of the plate.
center_x = 0.005
center_z = 0.005
thickness = np.sqrt((xx - center_x) ** 2 + (zz - center_z) ** 2).ravel()

# %%
# Create the point coordinates for the lookup table
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
# We have now a list of point coordinates:
print(points)

# %%
# And the corresponding thickness values.
print(thickness)

# %%
# Create the lookup table and add the coordinates and thickness data.
lookup_table = model.create_lookup_table_3d()
lookup_table.columns["Location"].data = points
thickness_column = lookup_table.create_column(data=thickness, dimension_type=DimensionType.LENGTH)

# %%
# Set the thickness type to "from table" and assign the thickness column.
modeling_ply.thickness_type = ThicknessType.FROM_TABLE
modeling_ply.thickness_field = thickness_column

# %%
# Plot the ply thickness
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)
