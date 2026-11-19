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
.. _sandwich_panel_example:

Sandwich panel
==============

This example defines a composite lay-up for a sandwich panel using PyACP.
It only shows the PyACP part of the setup. For a complete composite analysis,
see :ref:`pymapdl_workflow_example`.
"""

# %%# Import modules
# ------------------
#
# Import the standard library and third-party dependencies.
import pathlib
import tempfile

# %%
# Import the PyACP dependencies.
from ansys.acp.core import (
    FabricWithAngle,
    Lamina,
    PlyType,
    get_directions_plotter,
    launch_acp,
    print_model,
)
from ansys.acp.core.extras import ExampleKeys, get_example_file, set_plot_theme
from ansys.acp.core.material_property_sets import ConstantEngineeringConstants, ConstantStrainLimits

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
input_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_DAT, WORKING_DIR)

# %%
# Launch the ACP server and connect to it.
acp = launch_acp()

# %%
# Define the input file and import it into ACP.

model = acp.import_model(
    input_file,
    format="ansys:cdb",
)
print(model.unit_system)

# %%
# Visualize the loaded mesh.
mesh = model.mesh.to_pyvista()
mesh.plot(show_edges=True)

# %%
# Create the sandwich materials
# -----------------------------

# %%
# Create the UD material and  its corresponding fabric.
engineering_constants_ud = ConstantEngineeringConstants.from_orthotropic_constants(
    E1=5e10, E2=1e10, E3=1e10, nu12=0.28, nu13=0.28, nu23=0.3, G12=5e9, G23=4e9, G31=4e9
)

strain_limit = 0.01
strain_limits = ConstantStrainLimits.from_orthotropic_constants(
    eXc=-strain_limit,
    eYc=-strain_limit,
    eZc=-strain_limit,
    eXt=strain_limit,
    eYt=strain_limit,
    eZt=strain_limit,
    eSxy=strain_limit,
    eSyz=strain_limit,
    eSxz=strain_limit,
)

ud_material = model.create_material(
    name="UD",
    ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants_ud,
    strain_limits=strain_limits,
)

ud_fabric = model.create_fabric(name="UD", material=ud_material, thickness=0.002)


# %%
# Create a multi-axial stackup and a sublaminate. Stackups and sublaminates help quickly
# build repeating laminates.

biax_carbon_ud = model.create_stackup(
    name="Biax_Carbon_UD",
    fabrics=(
        FabricWithAngle(ud_fabric, -45),
        FabricWithAngle(ud_fabric, 45),
    ),
)


sublaminate = model.create_sublaminate(
    name="Sublaminate",
    materials=(
        Lamina(biax_carbon_ud, 0),
        Lamina(ud_fabric, 90),
        Lamina(biax_carbon_ud, 0),
    ),
)


# %%
# Create the core material and its corresponding fabric.
engineering_constants_core = ConstantEngineeringConstants.from_isotropic_constants(E=8.5e7, nu=0.3)

core = model.create_material(
    name="Core",
    ply_type=PlyType.ISOTROPIC_HOMOGENEOUS_CORE,
    engineering_constants=engineering_constants_core,
    strain_limits=strain_limits,
)

core_fabric = model.create_fabric(name="core", material=ud_material, thickness=0.015)

# %%
# Create the Lay-up
# -----------------

# %%
# Define a rosette and oriented selection set. Plot the orientations.
rosette = model.create_rosette(origin=(0.0, 0.0, 0.0), dir1=(1.0, 0.0, 0.0), dir2=(0.0, 1.0, 0.0))

oss = model.create_oriented_selection_set(
    name="oss",
    orientation_point=(0.0, 0.0, 0.0),
    orientation_direction=(0.0, 1.0, 0),
    element_sets=[model.element_sets["All_Elements"]],
    rosettes=[rosette],
)

model.update()
plotter = get_directions_plotter(model=model, components=[oss.elemental_data.orientation])
plotter.show()

# %%
# Create the modeling plies which define the lay-up of the sandwich panel.
modeling_group = model.create_modeling_group(name="modeling_group")

bottom_ply = modeling_group.create_modeling_ply(
    name="bottom_ply",
    ply_angle=0,
    ply_material=sublaminate,
    oriented_selection_sets=[oss],
)

core_ply = modeling_group.create_modeling_ply(
    name="core_ply",
    ply_angle=0,
    ply_material=core_fabric,
    oriented_selection_sets=[oss],
)


top_ply = modeling_group.create_modeling_ply(
    name="top_ply",
    ply_angle=90,
    ply_material=ud_fabric,
    oriented_selection_sets=[oss],
    number_of_layers=3,
)

# %%
# Update and print the model.
model.update()
print_model(model)
# sphinx_gallery_start_ignore
from ansys.acp.core.extras.example_helpers import _run_analysis

# Run the analysis to ensure that all the material properties have been correctly
# defined.
_run_analysis(model)
# sphinx_gallery_end_ignore
