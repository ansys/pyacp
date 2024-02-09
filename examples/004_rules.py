"""
.. _rules_example:

Basic rule example
==================

Shows basic usage of selection rules. This example shows just the
pyACP part of the setup. For a complete Composite analysis,
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
# Todo: reset to tempdir
WORKING_DIR = pathlib.Path(r"D:\ANSYSDev\pyacp-private\tests\data")
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

ud_material = model.create_material(
    name="UD",
    ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants_ud,
)

ud_fabric = model.create_fabric(name="UD", material=ud_material, thickness=0.002)

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
    number_of_layers=10,
)

model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Create a cylindrical selection rule and add it to the ply
cylindrical_rule = model.create_cylindrical_selection_rule(
    name="cylindrical_rule",
    origin=(0.005, 0, 0.005),
    direction=(0, 1, 0),
    radius=0.002,
)

linked_cylindrical_rule = LinkedSelectionRule(cylindrical_rule)
partial_ply.selection_rules.append(linked_cylindrical_rule)
# todo: should we automatically update the model when plotting (at least up to the entity
# that gets plotted
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# We can parametrize the rules
# linked_parallel_rule.template_rule = True
linked_parallel_rule.parameter_1 = 0.002
# linked_parallel_rule.parameter_2 = 0.1

# Todo: Extend example once #413 is fixed
assert len(partial_ply.selection_rules) == 1
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)


# %%
# Create a geometrical selection rule
triangle_path = example_helpers.get_example_file(
    example_helpers.ExampleKeys.RULE_GEOMETRY_TRIANGLE, WORKING_DIR
)
triangle = workflow.add_cad_geometry_from_local_file(triangle_path)


# TBD should we update the geometry automatically before we request root shapes?
model.update()

triangle_virtual_geometry = model.create_virtual_geometry(
    name="triangle_virtual_geometry", cad_components=triangle.root_shapes.values()
)


geometrical_selection_rule = model.create_geometrical_selection_rule(
    name="geometrical_rule",
    geometry=triangle_virtual_geometry,
)

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

cutoff_plane_path = example_helpers.get_example_file(
    example_helpers.ExampleKeys.CUT_OFF_GEOMETRY, WORKING_DIR
)
cut_off_plane = workflow.add_cad_geometry_from_local_file(cutoff_plane_path)

model.update()

cutoff_virtual_geometry = model.create_virtual_geometry(
    name="cutoff_virtual_geometry", cad_components=cut_off_plane.root_shapes.values()
)

cutoff_selection_rule = model.create_cutoff_selection_rule(
    name="cutoff_rule",
    cutoff_geometry=cutoff_virtual_geometry,
)

partial_ply.selection_rules = [LinkedSelectionRule(cutoff_selection_rule)]

model.update()
assert model.elemental_data.thickness is not None

plotter = pyvista.Plotter()
plotter.add_mesh(cut_off_plane.visualization_mesh.to_pyvista(), color="white")
plotter.add_mesh(model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh))
plotter.camera_position = [(-0.05, 0.01, 0), (0.005, 0.005, 0.005), (0, 1, 0)]

plotter.show()

# %%
# Create a variable offset selection rule

lookup_table = model.create_lookup_table_1d(
    name="lookup_table",
    origin=(0, 0, 0),
    direction=(0, 0, 1),
)

# Todo: should we allow setting the data from a list
lookup_table.columns["Location"].data = np.array([0, 0.005, 0.01])

offsets_column = lookup_table.create_column(
    name="offset",
    dimension_type=DimensionType.LENGTH,
    data=np.array([0.00, 0.004, 0]),
)

edge_set = model.create_edge_set(
    name="edge_set",
    edge_set_type=EdgeSetType.BY_REFERENCE,
    limit_angle=30,
    element_set=model.element_sets["All_Elements"],
    origin=(0, 0, 0),
)

variable_offset_rule = model.create_variable_offset_selection_rule(
    name="variable_offset_rule", edge_set=edge_set, offsets=offsets_column, distance_along_edge=True
)

partial_ply.selection_rules = [LinkedSelectionRule(variable_offset_rule)]
model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Create a boolean selection rule.
# Note: Creating a boolean selection rule and assigning it to a ply has the same
# effect as linking the individual rules to the ply directly. Boolean rules are still useful
# because they help to organize the rules and can be used to create more complex rules.

boolean_selection_rule = model.create_boolean_selection_rule(
    name="boolean_rule",
    selection_rules=[linked_parallel_rule, linked_cylindrical_rule],
)

partial_ply.selection_rules = [LinkedSelectionRule(boolean_selection_rule)]
model.update()
assert model.elemental_data.thickness is not None

model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# We can modify the operation type of the boolean selection rule
linked_parallel_rule.operation_type = BooleanOperationType.INTERSECT
linked_cylindrical_rule.operation_type = BooleanOperationType.ADD
model.update()
assert model.elemental_data.thickness is not None

model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

pass
# Todo: remove
#  Just to make sure the analysis actually runs.
# run_analysis(workflow)
workflow.get_local_acp_h5_file()
