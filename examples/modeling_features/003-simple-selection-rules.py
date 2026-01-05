# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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
.. _basic_selection_rules_example:

Basic selection rules
=====================

This example shows the basic usage of selection rules, which enable you to select elements through
geometrical operations and thus to shape plies. The example only shows the PyACP part of the setup.
For more advanced selection rule usage, see
:ref:`advanced_selection_rules_example`. For a complete composite
analysis, see :ref:`pymapdl_workflow_example`.
"""


# %%
# Import modules
# --------------
#
# Import the standard library and third-party dependencies.
import pathlib
import tempfile

# %%
# Import the PyACP dependencies.
from ansys.acp.core import LinkedSelectionRule, launch_acp
from ansys.acp.core.extras import ExampleKeys, get_example_file, set_plot_theme

# sphinx_gallery_thumbnail_number = -1

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
model = acp.import_model(input_file)
print(model.unit_system)

# %%
# Visualize the loaded mesh.
mesh = model.mesh.to_pyvista()
mesh.plot(show_edges=True)


# %%
# Create a Parallel Rule
# ----------------------

# %%
# Create parallel selection rule and assign it to the existing ply.

parallel_rule = model.create_parallel_selection_rule(
    name="parallel_rule",
    origin=(0, 0, 0),
    direction=(1, 0, 0),
    lower_limit=0.005,
    upper_limit=1,
)

modeling_ply = model.modeling_groups["modeling_group"].modeling_plies["ply"]
modeling_ply.selection_rules = [LinkedSelectionRule(parallel_rule)]

# %%
# Plot the ply thickness.
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Create a Cylindrical Rule
# -------------------------

# %%
# Create a cylindrical selection rule and add it to the ply. This will intersect the two rules.
cylindrical_rule = model.create_cylindrical_selection_rule(
    name="cylindrical_rule",
    origin=(0.005, 0, 0.005),
    direction=(0, 1, 0),
    radius=0.002,
)

modeling_ply.selection_rules.append(LinkedSelectionRule(cylindrical_rule))

# %%
# Plot the ply thickness.
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)


# %%
# Create a Spherical Rule
# -----------------------

# %%
# Create a spherical selection rule and assign it to the ply. Now, only the spherical rule is
# active.
spherical_rule = model.create_spherical_selection_rule(
    name="spherical_rule",
    origin=(0.003, 0, 0.005),
    radius=0.002,
)

modeling_ply.selection_rules = [LinkedSelectionRule(spherical_rule)]

# %%
# Plot the ply thickness.
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Create a Tube Rule
# ------------------

# %%
# Create a tube selection rule and assign it to the ply. Now, only the tube rule is
# active.
tube_rule = model.create_tube_selection_rule(
    name="spherical_rule",
    # Select the pre-exsting _FIXEDSU edge which is the edge at x=0
    edge_set=model.edge_sets["_FIXEDSU"],
    inner_radius=0.001,
    outer_radius=0.003,
)

modeling_ply.selection_rules = [LinkedSelectionRule(tube_rule)]

# %%
# Plot the ply thickness.
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)
