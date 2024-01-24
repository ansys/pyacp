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

The MAPDL and DPF services are run in docker containers which share a volume (working
directory).
"""

# %%
# Import standard library and third-party dependencies
import pathlib

import pyvista

# %%
import ansys.acp.core as pyacp
from ansys.acp.core import OrientedSelectionSet
from ansys.acp.core._tree_objects.enums import PlyType
from ansys.acp.core._tree_objects.material.property_sets import (
    ConstantEngineeringConstants,
    ConstantStrainLimits,
)
from ansys.acp.core.model_printer import print_model
from ansys.acp.core.workflow import ACPWorkflow, get_composite_post_processing_files

# Note: It is important to import mapdl before dpf, otherwise the plot defaults are messed up
# https://github.com/ansys/pydpf-core/issues/1363
from ansys.mapdl.core import launch_mapdl

# Todo get example from example-data repo
EXAMPLES_DIR = pathlib.Path(__file__).parent
EXAMPLE_DATA_DIR = EXAMPLES_DIR / "data" / "flat_plate"

WORKING_DIR = pathlib.Path(EXAMPLE_DATA_DIR)

# Use temp directory
# WORKING_DIR = None

# %%
# Launch the PyACP server and connect to it.
pyacp_server = pyacp.launch_acp()
pyacp_server.wait(timeout=30)
pyacp_client = pyacp.Client(pyacp_server)

CDB_FILENAME = "flat_plate_input.dat"
local_file_path = str(EXAMPLE_DATA_DIR / CDB_FILENAME)
print(local_file_path)
workflow = ACPWorkflow(
    acp_client=pyacp_client,
    cdb_file_path=str(EXAMPLE_DATA_DIR / "flat_plate_input.dat"),
    local_working_directory=WORKING_DIR,
)

model = workflow.model
print(workflow.working_directory.path)
print(model.unit_system)

# %%
# Visualize the loaded mesh
mesh = model.mesh.to_pyvista()
mesh.plot(show_edges=True)
rosette = model.create_rosette(origin=(0.0, 0.0, 0.0), dir1=(1.0, 0.0, 0.0), dir2=(0.0, 0.0, 1.0))

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

# Deletes the StructuralSteel Todo should we remove it from the input cdb
# model.materials["1"]

ud_material = model.create_material(
    name="UD",
    ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants,
    strain_limits=strain_limits,
)

fabric = model.create_fabric(name="UD", material=ud_material, thickness=0.1)

oss: OrientedSelectionSet = model.create_oriented_selection_set(
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

modeling_ply = model.modeling_groups["modeling_group"].modeling_plies["ply_4_-45_UD"]


# %%
# Show the ply offsets, scaled by a factor of 200
plotter = pyvista.Plotter()
plotter.add_mesh(model.mesh.to_pyvista(), color="white")
plotter.add_mesh(
    modeling_ply.nodal_data.ply_offset.get_pyvista_glyphs(mesh=model.mesh, factor=0.01),
)
plotter.show()

print_model(model)

mapdl = launch_mapdl()

# This is important because otherwise definitions from previous runs are still present
# in the mapdl instance (for instance materials)
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

# Download RST FILE for further post-processing
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
from ansys.dpf.core.unit_system import unit_systems

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
    default_unit_system=unit_systems.solver_nmm,
    server=dpf_server,
)

# %%
# Evaluate the failure criteria
output_all_elements = composite_model.evaluate_failure_criteria(cfc)

# %%
# Query and plot the results
irf_field = output_all_elements.get_field({"failure_label": FailureOutput.FAILURE_VALUE})
irf_field.plot()

# There is a failure on exit when using a temp directory:
# See https://github.com/ansys/pydpf-core/issues/1373
