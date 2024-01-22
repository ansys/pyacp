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

# Note: It is important to import mapdl before dpf, otherwise the plot defaults are messed up
# https://github.com/ansys/pydpf-core/issues/1363
from ansys.mapdl.core import Mapdl, launch_mapdl


# %%
# Import standard library and third-party dependencies
import os
import pathlib
import tempfile
from typing import Callable, Optional

import pyvista

# %%
import ansys.acp.core as pyacp
from ansys.acp.core import OrientedSelectionSet, Rosette, ModelingPly, Fabric, Material
from ansys.acp.core._tree_objects.enums import PlyType
from ansys.acp.core._tree_objects.material.property_sets import ConstantEngineeringConstants, \
    ConstantStrainLimits
from ansys.acp.core._tree_objects.modeling_ply import ModelingPlyElementalData
from ansys.acp.core._tree_objects.oriented_selection_set import OrientedSelectionSetElementalData
from ansys.acp.core.workflow import ACPWorkflow, get_composite_post_processing_files, print_model

"""
We currently support the following setups:



Input files are all files to load an write a model.

Actual input files (from which a model is created):
* acph5
* cdb

General note on linked files: Linked files are stored in the acph5 with a relative
path if possible.

Linked files which are needed to save and update a model:
* cdb (original cdb from which the acph5 was created)
* other?

Linked files which are needed to refresh the model
* geometries 

Local server, user defined working directory:
* Input files are not copied
* Output files end up in working directory (server writes it directly to the right location)
* Linked files: No extra work needed
* End result: Input and output files are in user defined working directory

Local server, temp directory:
* Input files are copied to the temp directory (not strictly needed)
* Output files are copied to the temp directory
* Linked files: No extra work needed if the input file is still in its original location
* End result: Input and output files are in the temp directory 

Remote server, temp directory
* Input files are copied to the server
* Output files are copied to the temp directory (first stored on server and then downloaded)
* Linked files: Input file needs to be uploaded again, to the same location that is 
specified in the model. We probably need to pass the local path again to the workflow. Probably
it also makes sense to overwrite the "external_path" defined in the object. 
* End result: Only output files are in the temp directory (we could also copy the input files to
the temp directory to be "consistent")

Remote server, user defined directory
* Input files are copied to the server
* Output files are downloaded to the local directory (first stored on the server and then downloaded)
* Linked files: Input file needs to be uploaded again, to the same location that is 
specified in the model. We probably need to pass the local path again to the workflow. Probably
it also makes sense to overwrite the "external_path" defined in the object. 
End result: Input and output files are in the local directory


Scenarios:

Reopen a project with a local server that was last edited on a remote server
* We need to edit the linked paths with the workflow input files

Reopen a project with a remote server that was last edited on a local server
* We need to edit the linked paths with the workflow input files

Move a project:
* We need to edit the linked paths with the workflow input files

Possible solution:
* We always ask the user to specify all the paths (cdb, acph5, geometries, etc.) when creating
a workflow.
* We create a project file that contains everything (maybe just as binary blobs in the h5)
* We lookup the file paths in the acph5 file (preferred)
* We only support projects with relative paths that keep their directory structor


"""


# Todo get example from example-data repo
EXAMPLES_DIR = pathlib.Path(__file__).parent
EXAMPLE_DATA_DIR = EXAMPLES_DIR / "data" / "flat_plate"

#tmp_dir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(EXAMPLE_DATA_DIR)
# %%
# Launch the PyACP server and connect to it.
pyacp_server = pyacp.launch_acp()
pyacp_server.wait(timeout=30)
pyacp_client = pyacp.Client(pyacp_server, local_working_dir=WORKING_DIR)


CDB_FILENAME = "flat_plate_input.dat"
local_file_path = str(EXAMPLE_DATA_DIR / CDB_FILENAME)
print(local_file_path)
workflow = ACPWorkflow(
    acp_client=pyacp_client,
    cdb_file_path=str(EXAMPLE_DATA_DIR / "flat_plate_input.dat")
)

model = workflow.model

print(model.unit_system)

# %%
# Visualize the loaded mesh
mesh = model.mesh.to_pyvista()
mesh.plot(show_edges=True)
rosette = model.create_rosette(origin=(0.0, 0.0, 0.0), dir1=(1.0, 0.0, 0.0), dir2=(0.0, 0.0, 1.0))


engineering_constants = ConstantEngineeringConstants(
    E1=5E10, E2=1E10, E3=1E10, nu12=0.28, nu13=0.28, nu23=0.3, G12=5E9, G23=4E9, G31=4E9
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
#model.materials["1"]

ud_material: Material = model.create_material(
    name="UD", ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants,
    strain_limits=strain_limits,
)

fabric: Fabric = model.create_fabric(name="UD", material=ud_material, thickness=0.1)

oss: OrientedSelectionSet = model.create_oriented_selection_set(
    name="oss",
    orientation_point=(0.0, 0.0, 0.0),
    orientation_direction=(0.0, 1.0, 0),
    element_sets=[model.element_sets["All_Elements"]],
    rosettes=[rosette],
)

elemental_data: OrientedSelectionSetElementalData = oss.elemental_data

model.update()



plotter = pyvista.Plotter()
plotter.add_mesh(model.mesh.to_pyvista(), color="white")
plotter.add_mesh(
    oss.elemental_data.orientation.to_pyvista(
        mesh=model.mesh, factor=0.01, culling_factor=5
    ),
    color="blue",
)


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

modeling_ply: ModelingPly = model.modeling_groups["modeling_group"].modeling_plies["ply_4_-45_UD"]
modeling_ply.elemental_data.normal.to_pyvista(
    mesh=model.mesh,
    factor=0.01
).plot()



# %%
# Show the ply offsets, scaled by a factor of 200
plotter = pyvista.Plotter()
plotter.add_mesh(model.mesh.to_pyvista(), color="white")
plotter.add_mesh(
    modeling_ply.nodal_data.ply_offset.to_pyvista(
        mesh=model.mesh, factor=0.01
    ),
)
plotter.show()

print_model(model)

mapdl = launch_mapdl()
#mapdl = Mapdl(ip="localhost", port=50557, timeout=30)

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
rst_file_local_path = WORKING_DIR / rstfile_name
mapdl.download(rstfile_name, str(WORKING_DIR))


# %%
# Post-Processing with DPF composites
# -----------------------------------
#
# Setup: configure imports and connect to the pyDPF Composites server
# and load the dpf composites plugin

from ansys.dpf.composites.composite_model import CompositeModel
from ansys.dpf.composites.constants import FailureOutput

from ansys.dpf.composites.failure_criteria import (
    CombinedFailureCriterion,
    MaxStrainCriterion,
)
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


