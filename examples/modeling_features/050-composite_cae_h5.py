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
.. _composite_cae_h5_example:

HDF5 Composite CAE
==================

This example shows how to write and read layup data to and from
a HDF5 Composite CAE file, respectively. The HDF5 Composite CAE format
is a vendor independent format to exchange composite layup information
between CAE tools. PyACP can read and write this format.

This examples demonstrates how to:
- Export data to a HDF5 Composite CAE file
- Import a layup onto a different model (model)
- Export data with offsets (3D plies)
- Import a layup as :class:`.ImportedModelingPly`
- Map the imported layup onto an :class:`.ImportedSolidModel`

"""

# %%
# Import the standard library and third-party dependencies.
import pathlib
import tempfile

import pyvista

# %%
# Import the PyACP dependencies.
from ansys.acp.core import (
    HDF5CompositeCAEProjectionMode,
    LinkedSelectionRule,
    OffsetType,
    launch_acp,
)
from ansys.acp.core.extras import (
    FLAT_PLATE_SHELL_CAMERA,
    FLAT_PLATE_SOLID_CAMERA,
    ExampleKeys,
    get_example_file,
)

# sphinx_gallery_thumbnail_number = 2


# %%
# Start ACP and load the model
# ----------------------------
# %%
# Get the example file from the server.
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
acph5_input_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_ACPH5, WORKING_DIR)

# %%
# Launch the PyACP server and connect to it.
acp = launch_acp()

# %%
# Load the model from an acph5 file
model = acp.import_model(acph5_input_file)

# %%
# Crop some plies in order to generate a variable laminate
pr_x = model.create_parallel_selection_rule(
    name="x axis",
    direction=(1, 0, 0),
    lower_limit=0.0025,
    upper_limit=0.0075,
)
pr_z = model.create_parallel_selection_rule(
    name="z axis",
    direction=(0, 0, 1),
    lower_limit=0.0015,
    upper_limit=0.0085,
)
boolean_rule = model.create_boolean_selection_rule(
    name="boolean rule",
    selection_rules=[LinkedSelectionRule(pr_x), LinkedSelectionRule(pr_z)],
)

for ply_name in ["ply_1_45_UD", "ply_2_-45_UD", "ply_3_45_UD", "ply_4_-45_UD"]:
    ply = model.modeling_groups["modeling_group"].modeling_plies[ply_name]
    ply.selection_rules = [LinkedSelectionRule(boolean_rule)]

model.update()

# %%
# some plies only cover the inner part of the plate
thickness = model.elemental_data.thickness
assert thickness is not None
thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Write HDF5 Composite CAE
# ------------------------
#
# Export the entire layup to a HDF5 Composite CAE file
# There are options to export only a certain area and/or
# certain plies.
h5_output_file = WORKING_DIR / "hdf5_composite_cae.h5"
model.export_hdf5_composite_cae(
    path=h5_output_file,
)

# %%
# Map HDF5 Composite CAE to a different model
# -------------------------------------------
#
# The same plate with a refined mesh is used as target model.
# Both meshes (initial mesh in blue, refined one in red) are shown below.
dat_input_file_refined = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_REFINED_DAT, WORKING_DIR)
refined_model = acp.import_model(path=dat_input_file_refined, format="ansys:dat")

plotter = pyvista.Plotter()
plotter.add_mesh(
    model.shell_mesh.to_pyvista(),
    color="blue",
    edge_color="blue",
    show_edges=True,
    style="wireframe",
    line_width=4,
)
plotter.add_mesh(
    refined_model.shell_mesh.to_pyvista(),
    color="red",
    edge_color="red",
    show_edges=True,
    style="wireframe",
    line_width=2,
)
plotter.camera_position = FLAT_PLATE_SHELL_CAMERA
plotter.show()

# %%
# Import and map the layup from the HDF5 Composite CAE file
# The default settings (tolerances, etc.) are used.
refined_model.import_hdf5_composite_cae(
    path=h5_output_file,
)
refined_model.update()

# %%
# Plot the thickness distribution of the refined model
thickness = refined_model.elemental_data.thickness
assert thickness is not None
thickness.get_pyvista_mesh(mesh=refined_model.mesh).plot(show_edges=True)

# %%
# 3D plies with ply-offsets
# -------------------------
#
# The interface also allows to export the 3D plies
# which can then be used to create imported modeling plies.
# Therefore, the data is written to a HDF5 Composite CAE file
# again with the offset option enabled.
h5_output_file_3D = WORKING_DIR / "hdf5_composite_cae_3D.h5"
model.export_hdf5_composite_cae(
    path=h5_output_file_3D,
    layup_representation_3d=True,
    offset_type=OffsetType.BOTTOM_OFFSET,
)

# %%
# The generated HDF5 composite CAE is now imported and the data is converted into
# imported modeling plies.
refined_model_3D = acp.import_model(path=dat_input_file_refined, format="ansys:dat")
refined_model_3D.import_hdf5_composite_cae(
    path=h5_output_file_3D, projection_mode=HDF5CompositeCAEProjectionMode.SOLID
)

# %%
# Import a solid mesh to map the imported modeling plies. Details about the imported solid
# model and imported plies can be found in the examples :ref:`imported_solid_model_example` and
# :ref:`imported_plies_example`.
solid_mesh_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_SOLID_MESH_CDB, WORKING_DIR)
imported_solid_model = refined_model_3D.create_imported_solid_model(
    name="Imported Solid Model",
    external_path=solid_mesh_file,
    format="ansys:cdb",
)
imported_solid_model.create_layup_mapping_object(
    name="Map imported plies",
    use_imported_plies=True,  # enable imported plies
    select_all_plies=True,  # select all plies
    scale_ply_thicknesses=True,
    entire_solid_mesh=True,
    delete_lost_elements=True,  # elements without plies are deleted
)
refined_model_3D.update()

# %%
# Show the mapped top layer of the imported laminate. Note that the
# solid elements which do not intersect with the layup are deleted.
imported_analysis_ply = (
    refined_model_3D.imported_modeling_groups["modeling_group"]
    .imported_modeling_plies["ply_5_0_UD"]
    .imported_production_plies["ImportedProductionPly.6"]
    .imported_analysis_plies["P1L1__ply_5_0_UD"]
)
plotter = pyvista.Plotter()
plotter.add_mesh(imported_analysis_ply.solid_mesh.to_pyvista(), show_edges=True)
plotter.add_mesh(refined_model_3D.solid_mesh.to_pyvista(), opacity=0.2, show_edges=False)
plotter.camera_position = FLAT_PLATE_SOLID_CAMERA
plotter.show()
