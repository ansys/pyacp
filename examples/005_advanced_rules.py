"""
.. _advanced_rules_example:

Advanced rules example
======================

This example shows the usage of advanced rules such as geometrical rule,
cut-off rule and variable offset rule. It also demonstrates how rules can be templated
and reused with different parameters.
See the :ref:`sphx_glr_examples_gallery_examples_004_basic_rules.py` for more basic rule examples.
This example shows just the pyACP part of the setup.  For a complete Composite analysis,
see the :ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py` example
"""


# %%
# Import standard library and third-party dependencies
import pathlib
import tempfile

import numpy as np
import pyvista

# %%
# Import pyACP dependencies
from ansys.acp.core import (
    ACPWorkflow,
    BooleanOperationType,
    DimensionType,
    EdgeSetType,
    LinkedSelectionRule,
    PlyType,
    example_helpers,
    launch_acp,
)
from ansys.acp.core.example_helpers import ExampleKeys, get_example_file
from ansys.acp.core.material_property_sets import ConstantEngineeringConstants

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
engineering_constants_ud = ConstantEngineeringConstants.from_orthotropic_constants(
    E1=5e10, E2=1e10, E3=1e10, nu12=0.28, nu13=0.28, nu23=0.3, G12=5e9, G23=4e9, G31=4e9
)

ud_material = model.create_material(
    name="UD",
    ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants_ud,
)

ud_fabric = model.create_fabric(name="UD", material=ud_material, thickness=0.002)

# %%
# Define a rosette and an oriented selection set
rosette = model.create_rosette(origin=(0.0, 0.0, 0.0), dir1=(1.0, 0.0, 0.0), dir2=(0.0, 1.0, 0.0))

oss = model.create_oriented_selection_set(
    name="oss",
    orientation_point=(0.0, 0.0, 0.0),
    orientation_direction=(0.0, 1.0, 0),
    element_sets=[model.element_sets["All_Elements"]],
    rosettes=[rosette],
)

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
    selection_rules=[linked_parallel_rule],
    number_of_layers=10,
)

model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)


# %%
# Rules can be parametrized. This makes sense when a rule is used multiple times with different
# parameters. :class:`.LinkedSelectionRule` shows what parameters are available for each rule.
# Here, the extent of the parallel rule modified.
linked_parallel_rule.template_rule = True
linked_parallel_rule.parameter_1 = 0.002
linked_parallel_rule.parameter_2 = 0.1

model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)


# %%
# Create a geometrical selection rule

# Add CAD geometry to the model.
triangle_path = example_helpers.get_example_file(
    example_helpers.ExampleKeys.RULE_GEOMETRY_TRIANGLE, WORKING_DIR
)
triangle = workflow.add_cad_geometry_from_local_file(triangle_path)


# Note: It is important to update the model here, because the root_shapes of the
# cad_geometry are not available until the model is updated.
model.update()

# Create a virtual geometry from the CAD geometry
triangle_virtual_geometry = model.create_virtual_geometry(
    name="triangle_virtual_geometry", cad_components=triangle.root_shapes.values()
)

# Create the geometrical selection rule
geometrical_selection_rule = model.create_geometrical_selection_rule(
    name="geometrical_rule",
    geometry=triangle_virtual_geometry,
)

# Assign the geometrical selection rule to the ply and plot the ply extend with
# the outline of the geometry
partial_ply.selection_rules = [LinkedSelectionRule(geometrical_selection_rule)]
model.update()
assert model.elemental_data.thickness is not None

plotter = pyvista.Plotter()
plotter.add_mesh(
    triangle.visualization_mesh.to_pyvista(), style="wireframe", line_width=4, color="white"
)
plotter.add_mesh(model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh), show_edges=True)
plotter.show()

# %%
# Create a cutoff selection rule

# Add the cutoff CAD geometry to the model
cutoff_plane_path = example_helpers.get_example_file(
    example_helpers.ExampleKeys.CUT_OFF_GEOMETRY, WORKING_DIR
)
cut_off_plane = workflow.add_cad_geometry_from_local_file(cutoff_plane_path)

# Note: It is important to update the model here, because the root_shapes of the
# cad_geometry are not available until the model is updated.
model.update()

# Create a virtual geometry from the CAD geometry
cutoff_virtual_geometry = model.create_virtual_geometry(
    name="cutoff_virtual_geometry", cad_components=cut_off_plane.root_shapes.values()
)

# Create the cutoff selection rule
cutoff_selection_rule = model.create_cutoff_selection_rule(
    name="cutoff_rule",
    cutoff_geometry=cutoff_virtual_geometry,
)

partial_ply.selection_rules = [LinkedSelectionRule(cutoff_selection_rule)]

model.update()
assert model.elemental_data.thickness is not None

# Plot the ply extent together with the cutoff geometry
plotter = pyvista.Plotter()
plotter.add_mesh(cut_off_plane.visualization_mesh.to_pyvista(), color="white")
plotter.add_mesh(model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh))
plotter.camera_position = [(-0.05, 0.01, 0), (0.005, 0.005, 0.005), (0, 1, 0)]

plotter.show()

# %%
# Create a variable offset selection rule

# Create the lookup table
lookup_table = model.create_lookup_table_1d(
    name="lookup_table",
    origin=(0, 0, 0),
    direction=(0, 0, 1),
)

# Add the location data. The "Location" column of the lookup table
# is always created by default.
lookup_table.columns["Location"].data = np.array([0, 0.005, 0.01])

# Create the offset column that defines the offsets from the edge.
offsets_column = lookup_table.create_column(
    name="offset",
    dimension_type=DimensionType.LENGTH,
    data=np.array([0.00, 0.004, 0]),
)

# Create the edge set from the "All_Elements" element set. Because we set
# the limit angle to 30°, only one edge at x=0 will be selected.
edge_set = model.create_edge_set(
    name="edge_set",
    edge_set_type=EdgeSetType.BY_REFERENCE,
    limit_angle=30,
    element_set=model.element_sets["All_Elements"],
    origin=(0, 0, 0),
)

# Create the variable offset rule and assign it to the ply
variable_offset_rule = model.create_variable_offset_selection_rule(
    name="variable_offset_rule", edge_set=edge_set, offsets=offsets_column, distance_along_edge=True
)

partial_ply.selection_rules = [LinkedSelectionRule(variable_offset_rule)]

# Plot the ply extent
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Create a boolean selection rule.
# Note: Creating a boolean selection rule and assigning it to a ply has the same
# effect as linking the individual rules to the ply directly. Boolean rules are still useful
# because they help to organize the rules and can be used to create more complex rules.

# Create a cylindrical selection rule which will be combined with the parallel rule.
cylindrical_rule_boolean = model.create_cylindrical_selection_rule(
    name="cylindrical_rule",
    origin=(0.005, 0, 0.005),
    direction=(0, 1, 0),
    radius=0.002,
)

parallel_rule_boolean = model.create_parallel_selection_rule(
    name="parallel_rule",
    origin=(0, 0, 0),
    direction=(1, 0, 0),
    lower_limit=0.005,
    upper_limit=1,
)

linked_cylindrical_rule_boolean = LinkedSelectionRule(cylindrical_rule_boolean)
linked_parallel_rule_boolean = LinkedSelectionRule(parallel_rule_boolean)

boolean_selection_rule = model.create_boolean_selection_rule(
    name="boolean_rule",
    selection_rules=[linked_parallel_rule_boolean, linked_cylindrical_rule_boolean],
)

partial_ply.selection_rules = [LinkedSelectionRule(boolean_selection_rule)]

# Plot the ply extent
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Modify the operation type of the boolean selection rule
linked_parallel_rule_boolean.operation_type = BooleanOperationType.INTERSECT
linked_cylindrical_rule_boolean.operation_type = BooleanOperationType.ADD

# Plot the ply extent
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)
