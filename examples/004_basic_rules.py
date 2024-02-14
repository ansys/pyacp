"""
.. _basic_rules_example:

Basic rule example
==================

Shows the basic usage of selection rules. This example shows just the
pyACP part of the setup. See the :ref:`sphx_glr_examples_gallery_examples_005_advanced_rules.py`
for more advanced rule examples. For a complete Composite analysis,
see the :ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py` example
"""


# %%
# Import standard library and third-party dependencies
import pathlib
import tempfile

# %%
# Import pyACP dependencies
from ansys.acp.core import ACPWorkflow, LinkedSelectionRule, PlyType, launch_acp
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

parallel_rule = model.create_parallel_selection_rule(
    name="parallel_rule",
    origin=(0, 0, 0),
    direction=(1, 0, 0),
    lower_limit=0.005,
    upper_limit=1,
)

modeling_group = model.create_modeling_group(name="modeling_group")

partial_ply = modeling_group.create_modeling_ply(
    name="partial_ply",
    ply_angle=90,
    ply_material=ud_fabric,
    oriented_selection_sets=[oss],
    selection_rules=[LinkedSelectionRule(parallel_rule)],
    number_of_layers=10,
)

model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Create a cylindrical selection rule and add it to the ply. This will intersect the two rules.
cylindrical_rule = model.create_cylindrical_selection_rule(
    name="cylindrical_rule",
    origin=(0.005, 0, 0.005),
    direction=(0, 1, 0),
    radius=0.002,
)

partial_ply.selection_rules.append(LinkedSelectionRule(cylindrical_rule))

model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

# %%
# Create a spherical selection rule and assign it to the ply. Now only the spherical rule is
# active.
spherical_rule = model.create_spherical_selection_rule(
    name="spherical_rule",
    origin=(0.003, 0, 0.005),
    radius=0.002,
)

partial_ply.selection_rules = [LinkedSelectionRule(spherical_rule)]

model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)

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

partial_ply.selection_rules = [LinkedSelectionRule(tube_rule)]

model.update()
assert model.elemental_data.thickness is not None
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot(show_edges=True)
