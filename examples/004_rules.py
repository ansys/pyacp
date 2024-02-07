"""
.. _basic_sandwich_panel:

Basic rule example
==================

Shows basic usage of selection rules. This example shows just the
pyACP part of the setup. For a complete Composite analysis, see the :ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py` example
"""


# %%
# Import standard library and third-party dependencies
import pathlib
import tempfile

import pyvista

# %%
# Import pyACP dependencies
from ansys.acp.core import (
    ACPWorkflow,
    ConstantEngineeringConstants,
    ConstantStrainLimits,
    ExampleKeys,
    FabricWithAngle,
    Lamina,
    LinkedSelectionRule,
    PlyType,
    get_composite_post_processing_files,
    get_dpf_unit_system,
    get_example_file,
    launch_acp,
    print_model,
)

# from ansys.acp.core._utils.example_helpers import run_analysis

# Note: It is important to import mapdl before dpf, otherwise the plot defaults are messed up
# https://github.com/ansys/pydpf-core/issues/1363
# from ansys.mapdl.core import launch_mapdl


# %%
# Get example file from server
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_CDB, WORKING_DIR)

# %%
# Launch the PyACP server and connect to it.
acp = launch_acp()

# %%
# Define the input file and instantiate an ACPWorkflow
# The ACPWorkflow class provides convenience methods which simplify the file handling.
# It automatically creates a model based on the input file.

workflow = ACPWorkflow.from_cdb_file(
    acp=acp,
    cdb_file_path=input_file,
    local_working_directory=WORKING_DIR,
)

model = workflow.model
print(workflow.working_directory.path)
print(model.unit_system)

# %%
# Visualize the loaded mesh
mesh = model.mesh.to_pyvista()
mesh.plot(show_edges=True)


# %%
# Create the UD material and  its corresponding fabric
engineering_constants_ud = ConstantEngineeringConstants(
    E1=5e10, E2=1e10, E3=1e10, nu12=0.28, nu13=0.28, nu23=0.3, G12=5e9, G23=4e9, G31=4e9
)

strain_limit = 0.01
strain_limits = ConstantStrainLimits(
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
# TBD: Should we add strain limits?
ud_material = model.create_material(
    name="UD",
    ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants_ud,
    strain_limits=strain_limits,
)

ud_fabric = model.create_fabric(name="UD", material=ud_material, thickness=0.2)

# %%
# Define a rosette and an oriented selection set and plot the orientations
rosette = model.create_rosette(origin=(0.0, 0.0, 0.0), dir1=(1.0, 0.0, 0.0), dir2=(0.0, 1.0, 0.0))

oss = model.create_oriented_selection_set(
    name="oss",
    orientation_point=(0.0, 0.0, 0.0),
    orientation_direction=(0.0, 1.0, 0),
    element_sets=[model.element_sets["All_Elements"]],
    rosettes=[rosette],
)

model.update()

plotter = pyvista.Plotter()
plotter.add_mesh(model.mesh.to_pyvista(), color="white")
plotter.add_mesh(
    oss.elemental_data.orientation.get_pyvista_glyphs(mesh=model.mesh, factor=0.01),
    color="blue",
)
plotter.show()


# %%
# Create a ply with an attached parallel selection rule and plot the ply extent
modeling_group = model.create_modeling_group(name="modeling_group")

parallel_rule = model.create_parallel_selection_rule(
    name="parallel_rule",
    origin=(0, 0, 0),
    direction=(1, 0, 0),
    lower_limit=0.005,
    upper_limit=1,
)

linked_parallel_rule = LinkedSelectionRule(parallel_rule)
partial_ply = modeling_group.create_modeling_ply(
    name="partial_ply",
    ply_angle=90,
    ply_material=ud_fabric,
    oriented_selection_sets=[oss],
    # Todo: error message when passing plain SelectionRules is cryptic for the user.
    # Should we allow to pass plain selection rules?
    selection_rules=[linked_parallel_rule],
)

# partial_ply.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Create a cylindrical selection rule and add it to the ply
cylindrical_rule = model.create_cylindrical_selection_rule(
    name="cylindrical_rule",
    origin=(0.005, 0, 0.005),
    direction=(0, 1, 0),
    radius=0.002,
)

linked_cylindrical_rule = LinkedSelectionRule(cylindrical_rule)
# partial_ply.selection_rules.append(linked_cylindrical_rule)

# todo: should we automatically update the model when plotting (at least up to the entity
# that gets plotted
model.update()

partial_ply.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

linked_parallel_rule.template_rule = True
linked_parallel_rule.parameter_1 = 0.002
linked_parallel_rule.parameter_2 = 0.1

model.update()
partial_ply.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)


# %%
# Create a geometrical selection rule

workflow.add_cad
model.create_geometrical_selection_rule(
    name="geometrical_rule",
)

pass
# Just to make sure the analysis actually runs. Todo: remove
# run_analysis(workflow)
