"""
.. _basic_sandwich_panel:

Basic sandwich panel
====================

Define a Composite Lay-up for a sandwich panel with PyACP. This example shows just the
pyACP part of the setup. For a complete Composite analysis,
see the :ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py` example
"""


# %%
# Import standard library and third-party dependencies
import pathlib
import tempfile

# %%
# Import pyACP dependencies
from ansys.acp.core import (
    ACPWorkflow,
    FabricWithAngle,
    Lamina,
    PlyType,
    get_directions_plotter,
    launch_acp,
)
from ansys.acp.core.example_helpers import ExampleKeys, get_example_file, run_analysis
from ansys.acp.core.material_property_sets import ConstantEngineeringConstants, ConstantStrainLimits

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

ud_fabric = model.create_fabric(name="UD", material=ud_material, thickness=0.002)

# %%
# Create a multi-axial Stackup and a Sublaminate. Sublaminates and Stackups help to quickly
# build repeating laminates.

biax_carbon_ud = model.create_stackup(
    name="Biax_Carbon_UD",
    fabrics=(
        FabricWithAngle(ud_fabric, -45),
        FabricWithAngle(ud_fabric, 45),
    ),
)

fabric_with_angle = biax_carbon_ud.fabrics[0]
fabric_with_angle.angle = 20
assert fabric_with_angle.angle == biax_carbon_ud.fabrics[0].angle


sublaminate = model.create_sublaminate(
    name="Sublaminate",
    materials=(
        Lamina(biax_carbon_ud, 0),
        Lamina(ud_fabric, 90),
        Lamina(biax_carbon_ud, 0),
    ),
)


# Todo: it looks like the arguments for isotropic materials are missing
engineering_constants_core = ConstantEngineeringConstants(
    E1=5e10, E2=1e10, E3=1e10, nu12=0.28, nu13=0.28, nu23=0.3, G12=5e9, G23=4e9, G31=4e9
)

# engineering_constants_core.E = 8.5E7
# engineering_constants_core.nu = 0.3

# %%
# Create the Core Material and its corresponding Fabric
core = model.create_material(
    name="Core",
    # ply_type=PlyType.ISOTROPIC_HOMOGENEOUS_CORE,
    ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants_core,
    strain_limits=strain_limits,
)

core_fabric = model.create_fabric(name="core", material=ud_material, thickness=0.015)

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
assert oss.elemental_data.orientation is not None
plotter = get_directions_plotter(model=model, components=[oss.elemental_data.orientation])
plotter.show()

# %%
# Create the modeling plies which define the layup of the sandwich panel.
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

# Just to make sure the analysis actually runs. Todo: remove
run_analysis(workflow)
