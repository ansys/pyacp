"""
.. _basic_rules_example:

Basic selection rules example
=============================

Shows the basic usage of selection rules. This example shows just the
pyACP part of the setup. See the :ref:`sphx_glr_examples_gallery_examples_004_advanced_rules.py`
for more advanced rule examples. For a complete Composite analysis,
see the :ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py` example
"""


# %%
# Import standard library and third-party dependencies.
import pathlib
import tempfile

# %%
# Import pyACP dependencies.
from ansys.acp.core import ACPWorkflow, LinkedSelectionRule, launch_acp
from ansys.acp.core.example_helpers import ExampleKeys, get_example_file

# %%
# Start ACP and load the model
# ----------------------------


# %%
# Get example file from server.
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
# Create a spherical selection rule and assign it to the ply. Now only the spherical rule is
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
# Create a tube selection rule and assign it to the ply. Now only the tube rule is
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
