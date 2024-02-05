"""
.. _basic_flat_plate:

Basic PyACP Example
===================

Define a Composite Lay-up with PyACP, solve the resulting model with PyMAPDL, and run
a failure analysis with PyDPF-Composites.

The starting point is a MAPDL CDB file which contains the mesh, material data and
the boundary conditions. This model is imported in PyACP to define the lay-up.
PyACP exports the resulting model for PyMAPDL. Once the results are available,
the RST file is loaded in PyDPF composites. The additional input files (material.xml
and ACPCompositeDefinitions.h5) can also be stored with PyACP and passed to PyDPF Composites.
"""


# %%
# Import standard library and third-party dependencies
import pathlib
import tempfile

# %%
# Import pyACP dependencies
from ansys.acp.core import (
    ACPWorkflow,
    ConstantEngineeringConstants,
    ConstantStrainLimits,
    ExampleKeys,
    PlyType,
    get_composite_post_processing_files,
    get_directions_plotter,
    get_dpf_unit_system,
    get_example_file,
    launch_acp,
    print_model,
)

# Note: It is important to import mapdl before dpf, otherwise the plot defaults are messed up
# https://github.com/ansys/pydpf-core/issues/1363
from ansys.mapdl.core import launch_mapdl

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

workflow = ACPWorkflow(
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
# Create an orthotropic material and fabric including strain limits, which are later
# used to post-process the simulation.
engineering_constants = ConstantEngineeringConstants(
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

ud_material = model.create_material(
    name="UD",
    ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants,
    strain_limits=strain_limits,
)

fabric = model.create_fabric(name="UD", material=ud_material, thickness=0.1)


# %%
# Define a rosette and an oriented selection set and plot the orientations
rosette = model.create_rosette(origin=(0.0, 0.0, 0.0), dir1=(1.0, 0.0, 0.0), dir2=(0.0, 0.0, 1.0))

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
# Create various plies with different angles and add them to a modeling group
modeling_group = model.create_modeling_group(name="modeling_group")
angles = [0, 45, -45, 45, -45, 0]
for idx, angle in enumerate(angles):
    modeling_group.create_modeling_ply(
        name=f"ply_{idx}_{angle}_{fabric.name}",
        ply_angle=angle,
        ply_material=fabric,
        oriented_selection_sets=[oss],
    )

model.update()


# %%
# Show the fiber directions of a specific ply
modeling_ply = model.modeling_groups["modeling_group"].modeling_plies["ply_4_-45_UD"]


plotter = get_directions_plotter(
    model=model,
    components=[modeling_ply.elemental_data.fiber_direction],
)

plotter.show()


# %%
# Print the model tree for a quick overview
print_model(model)

# %%
# Solve the model with MAPDL
# --------------------------
#
# Launch the MAPDL instance
mapdl = launch_mapdl()
mapdl.clear()

# %%
# Load the CDB file into PyMAPDL
mapdl.input(str(workflow.get_local_cdb_file()))

# %%
# Solve the model
mapdl.allsel()
mapdl.slashsolu()
mapdl.solve()

# %%
# Post-processing: show displacements
mapdl.post1()
mapdl.set("last")
mapdl.post_processing.plot_nodal_displacement(component="NORM")

# %%
# Download the rst file for composite specific post-processing
rstfile_name = f"{mapdl.jobname}.rst"
rst_file_local_path = workflow.working_directory.path / rstfile_name
mapdl.download(rstfile_name, str(workflow.working_directory.path))

# %%
# Post-Processing with DPF composites
# -----------------------------------
#
# Setup: configure imports and connect to the pyDPF Composites server
# and load the dpf composites plugin

from ansys.dpf.composites.composite_model import CompositeModel
from ansys.dpf.composites.constants import FailureOutput
from ansys.dpf.composites.failure_criteria import CombinedFailureCriterion, MaxStrainCriterion
from ansys.dpf.composites.server_helpers import connect_to_or_start_server

# %%
# Connect to the server. The ``connect_to_or_start_server`` function
# automatically loads the composites plugin.
dpf_server = connect_to_or_start_server()

# %%
# Specify the Combined Failure Criterion
max_strain = MaxStrainCriterion()

cfc = CombinedFailureCriterion(
    name="Combined Failure Criterion",
    failure_criteria=[max_strain],
)

# %%
# Create the CompositeModel and configure its input
composite_model = CompositeModel(
    get_composite_post_processing_files(workflow, rst_file_local_path),
    default_unit_system=get_dpf_unit_system(model.unit_system),
    server=dpf_server,
)

# %%
# Evaluate the failure criteria and plot it
output_all_elements = composite_model.evaluate_failure_criteria(cfc)
irf_field = output_all_elements.get_field({"failure_label": FailureOutput.FAILURE_VALUE})
irf_field.plot()

# %%
# Release composite model to close open streams to result file.
composite_model = None  # type: ignore
