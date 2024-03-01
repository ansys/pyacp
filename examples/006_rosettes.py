"""
.. _rosette_example:

Rosette example
===============

This example shows how rosettes can be used to define the reference directions of a ply. Note
that only parallel rosettes are supported in pyACP.
This example shows just the pyACP part of the setup.  For a complete Composite analysis,
see the :ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py` example
"""


# %%
# Import standard library and third-party dependencies.
import pathlib
import tempfile

import numpy as np

# %%
# Import pyACP dependencies
from ansys.acp.core import (
    ACPWorkflow,
    PlyType,
    RosetteSelectionMethod,
    RosetteType,
    get_directions_plotter,
    launch_acp,
)
from ansys.acp.core.example_helpers import ExampleKeys, get_example_file

# %%
# Start ACP and load the model
# ----------------------------

# %%
# Get example file from server
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_DAT, WORKING_DIR)

# %%
# Launch the PyACP server and connect to it.
acp = launch_acp()

# %%
# Define the input file and instantiate an ACPWorkflow.
# The ACPWorkflow class provides convenience methods which simplify the file handling.
# It automatically creates a model based on the input file.
# The input file contains a flat plate with a single ply.
workflow = ACPWorkflow.from_cdb_or_dat_file(
    acp=acp,
    cdb_or_dat_file_path=input_file,
    local_working_directory=WORKING_DIR,
)

model = workflow.model
print(workflow.working_directory.path)
print(model.unit_system)

# %%
# Define directions with a parallel rosette
# -----------------------------------------

# %%
# Create a material and a fabric
ud_material = model.create_material(
    name="UD",
    ply_type=PlyType.REGULAR,
)

fabric = model.create_fabric(name="UD", material=ud_material, thickness=0.1)

# %%
# Create a parallel rosette where the first direction is rotated by 45 degrees around the y-axis.
parallel_rosette_45_deg = model.create_rosette(
    name="ParallelRosette",
    rosette_type=RosetteType.PARALLEL,
    origin=(0, 0, 0),
    dir1=(np.sqrt(2) / 2, 0, np.sqrt(2) / 2),
    dir2=(-np.sqrt(2) / 2, 0, np.sqrt(2) / 2),
)

# %%
# Create an oriented selection set and assign the rosette.
oss = model.create_oriented_selection_set(
    name="oss",
    orientation_point=(0.0, 0.0, 0.0),
    orientation_direction=(0.0, 1.0, 0),
    element_sets=[model.element_sets["All_Elements"]],
    rosettes=[parallel_rosette_45_deg],
)

model.update()

# %%
# Plot the orientation and the reference direction of the oriented selection set.
plotter = get_directions_plotter(
    model=model, components=[oss.elemental_data.orientation, oss.elemental_data.reference_direction]
)
plotter.show()

# %%
# Create a ply with which uses the reference direction defined by the rosette.
# The ply angle is set to 20 degrees, which means the fiber direction is rotated by 20 degrees
# from the reference direction.
modeling_group = model.create_modeling_group(name="modeling_group")
modeling_ply = modeling_group.create_modeling_ply(
    name="ply",
    ply_angle=20,
    ply_material=fabric,
    oriented_selection_sets=[oss],
)

# %%
# Plot the reference direction, the fiber direction and the transverse direction of the ply.
plotter = get_directions_plotter(
    model=model,
    components=[
        modeling_ply.elemental_data.reference_direction,
        modeling_ply.elemental_data.fiber_direction,
        modeling_ply.elemental_data.transverse_direction,
    ],
)
plotter.show()

# %%
# Define directions with a radial rosette
# ---------------------------------------
# %%
# Create a radial rosette and plot the resulting reference direction.
# For a radial rosette, a line is constructed that goes through the origin and its
# direction vector is normal to a plane spanned by ``dir1`` and ``dir2``.
# The reference direction are then parallel to the shortest connection from the line to each point
# for which the reference direction is computed.
radial_rosette = model.create_rosette(
    name="RadialRosette",
    rosette_type=RosetteType.RADIAL,
    origin=(0.005, 0, 0.005),
    dir1=(1, 0, 0),
    dir2=(0, 0, 1),
)

oss.rosettes = [radial_rosette]
model.update()

plotter = get_directions_plotter(model=model, components=[oss.elemental_data.reference_direction])
plotter.show()

# %%
# Define directions with a cylindrical rosette
# --------------------------------------------
# %%
# Create a cylindrical rosette and plot the resulting reference direction.
# For a cylindrical rosette, the reference directions are tangential to circles around the origin
# that lie in a plane spanned by ``dir1`` and ``dir2``.
cylindrical_rosette = model.create_rosette(
    name="CylindricalRosette",
    rosette_type=RosetteType.CYLINDRICAL,
    origin=(0.005, 0, 0.005),
    dir1=(1, 0, 0),
    dir2=(0, 0, 1),
)

oss.rosettes = [cylindrical_rosette]
model.update()

plotter = get_directions_plotter(model=model, components=[oss.elemental_data.reference_direction])
plotter.show()

# %%
# Define directions with a spherical rosette
# ------------------------------------------
# %%
# Create a spherical rosette and plot the resulting reference direction.
# For a spherical rosette, the reference directions are tangential to a sphere around the origin.
# Note: This is the same as the cylindrical rosette for the current example.
spherical_rosette = model.create_rosette(
    name="SphericalRosette",
    rosette_type=RosetteType.SPHERICAL,
    origin=(0.005, 0, 0.005),
    dir1=(1, 0, 0),
    dir2=(0, 0, 1),
)

oss.rosettes = [spherical_rosette]
model.update()

plotter = get_directions_plotter(model=model, components=[oss.elemental_data.reference_direction])
plotter.show()


# %%
# Combine rosettes
# ----------------

# %%
# Create and additional parallel rosette which points along the x direction and has its origin
# at (0.01, 0, 0.01).
parallel_rosette_0_deg = model.create_rosette(
    name="ParallelRosette",
    rosette_type=RosetteType.PARALLEL,
    origin=(0.01, 0, 0.01),
    dir1=(1, 0, 0),
    dir2=(0, 0, 1),
)

# %%
# Assign both rosettes to the oriented selection set and set the rosette selection method to
# ``RosetteSelectionMethod.MINIMUM_DISTANCE_SUPERPOSED``. This implies that the reference direction
# is weighted by the inverse distance to each rosette. Note that the origin of
# the rotated rosette is at (0,0,0).
oss.rosettes = [parallel_rosette_45_deg, parallel_rosette_0_deg]
oss.rosette_selection_method = RosetteSelectionMethod.MINIMUM_DISTANCE_SUPERPOSED

# %%
# Plot the resulting reference direction.
model.update()
plotter = get_directions_plotter(model=model, components=[oss.elemental_data.reference_direction])
plotter.show()

workflow.get_local_acp_h5_file()

pass
