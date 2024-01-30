"""
.. _solve_class40_example:

Class 40 example
================

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
# Setup: Connect to PyACP Server
# ------------------------------

# %%
# Import standard library and third-party dependencies
import os
import pathlib
import tempfile

import pyvista

# %%
# Import Ansys libraries
import ansys.acp.core as pyacp

# %%
# Launch the PyACP server and connect to it.
acp = pyacp.launch_acp()

# %%
#
# Load Mesh and Materials from CDB file
# -------------------------------------

# %%
# Define the directory in which the input files are stored.
try:
    EXAMPLES_DIR = pathlib.Path(os.environ["REPO_ROOT"]) / "examples"
except KeyError:
    EXAMPLES_DIR = pathlib.Path(__file__).parent
EXAMPLE_DATA_DIR = EXAMPLES_DIR / "data" / "class40"

# %%
# Send ``class40.cdb`` to the server.
CDB_FILENAME = "class40.cdb"
local_file_path = str(EXAMPLE_DATA_DIR / CDB_FILENAME)
print(local_file_path)
cdb_file_path = acp.upload_file(local_path=local_file_path)

# %%
# Load CDB file into PyACP and set the unit system
model = acp.import_model(
    path=cdb_file_path, format="ansys:cdb", unit_system=pyacp.UnitSystemType.MPA
)
model


# %%
# Visualize the loaded mesh
mesh = model.mesh.to_pyvista()
mesh.plot()

# %%
#
# Build Composite Lay-up
# ----------------------
#
# Create the model (unit system is MPA)

# %%
# Materials
# '''''''''

mat_corecell_81kg = model.materials["1"]
mat_corecell_81kg.name = "Core Cell 81kg"
mat_corecell_81kg.ply_type = "isotropic_homogeneous_core"

mat_corecell_103kg = model.materials["2"]
mat_corecell_103kg.name = "Core Cell 103kg"
mat_corecell_103kg.ply_type = "isotropic_homogeneous_core"

mat_eglass_ud = model.materials["3"]
mat_eglass_ud.name = "E-Glass (uni-directional)"
mat_eglass_ud.ply_type = "regular"

# %%
# Fabrics
# '''''''

corecell_81kg_5mm = model.create_fabric(
    name="Corecell 81kg", thickness=0.005, material=mat_corecell_81kg
)
corecell_103kg_10mm = model.create_fabric(
    name="Corecell 103kg", thickness=0.01, material=mat_corecell_103kg
)
eglass_ud_02mm = model.create_fabric(name="eglass UD", thickness=0.0002, material=mat_eglass_ud)

# %%
# Rosettes
# ''''''''

ros_deck = model.create_rosette(name="ros_deck", origin=(-5.9334, -0.0481, 1.693))
ros_hull = model.create_rosette(name="ros_hull", origin=(-5.3711, -0.0506, -0.2551))
ros_bulkhead = model.create_rosette(
    name="ros_bulkhead", origin=(-5.622, 0.0022, 0.0847), dir1=(0.0, 1.0, 0.0), dir2=(0.0, 0.0, 1.0)
)
ros_keeltower = model.create_rosette(
    name="ros_keeltower", origin=(-6.0699, -0.0502, 0.623), dir1=(0.0, 0.0, 1.0)
)

# %%
# Oriented Selection Sets
# '''''''''''''''''''''''
#
# Note: the element sets are imported from the initial mesh (CDB)

oss_deck = model.create_oriented_selection_set(
    name="oss_deck",
    orientation_point=(-5.3806, -0.0016, 1.6449),
    orientation_direction=(0.0, 0.0, -1.0),
    element_sets=[model.element_sets["DECK"]],
    rosettes=[ros_deck],
)

oss_hull = model.create_oriented_selection_set(
    name="oss_hull",
    orientation_point=(-5.12, 0.1949, -0.2487),
    orientation_direction=(0.0, 0.0, 1.0),
    element_sets=[model.element_sets["HULL_ALL"]],
    rosettes=[ros_hull],
)

oss_bulkhead = model.create_oriented_selection_set(
    name="oss_bulkhead",
    orientation_point=(-5.622, -0.0465, -0.094),
    orientation_direction=(1.0, 0.0, 0.0),
    element_sets=[model.element_sets["BULKHEAD_ALL"]],
    rosettes=[ros_bulkhead],
)

esets = [
    model.element_sets["KEELTOWER_AFT"],
    model.element_sets["KEELTOWER_FRONT"],
    model.element_sets["KEELTOWER_PORT"],
    model.element_sets["KEELTOWER_STB"],
]

oss_keeltower = model.create_oriented_selection_set(
    name="oss_keeltower",
    orientation_point=(-6.1019, 0.0001, 1.162),
    orientation_direction=(-1.0, 0.0, 0.0),
    element_sets=esets,
    rosettes=[ros_keeltower],
)

# %%
# Show the orientations on the hull OSS.
#
# Note that the Model must be updated before the orientations are available.

model.update()

plotter = pyvista.Plotter()
plotter.add_mesh(model.mesh.to_pyvista(), color="white")
plotter.add_mesh(
    oss_hull.elemental_data.orientation.get_pyvista_glyphs(
        mesh=model.mesh, factor=0.2, culling_factor=5
    ),
    color="blue",
)
plotter.show()


# %%
# Modeling Plies
# ''''''''''''''


def add_ply(mg, name, ply_material, angle, oss):
    return mg.create_modeling_ply(
        name=name,
        ply_material=ply_material,
        oriented_selection_sets=oss,
        ply_angle=angle,
        number_of_layers=1,
        global_ply_nr=0,  # add at the end
    )


# %%
# Define plies for the HULL, DECK and BULKHEAD

angles = [-90.0, -60.0, -45.0 - 30.0, 0.0, 0.0, 30.0, 45.0, 60.0, 90.0]
for mg_name in ["hull", "deck", "bulkhead"]:
    mg = model.create_modeling_group(name=mg_name)
    oss_list = [model.oriented_selection_sets["oss_" + mg_name]]
    for angle in angles:
        add_ply(mg, "eglass_ud_02mm_" + str(angle), eglass_ud_02mm, angle, oss_list)
    add_ply(mg, "corecell_103kg_10mm", corecell_103kg_10mm, 0.0, oss_list)
    for angle in angles:
        add_ply(mg, "eglass_ud_02mm_" + str(angle), eglass_ud_02mm, angle, oss_list)

# %%
# Add plies to the keeltower
mg = model.create_modeling_group(name="keeltower")
oss_list = [model.oriented_selection_sets["oss_keeltower"]]
for angle in angles:
    add_ply(mg, "eglass_ud_02mm_" + str(angle), eglass_ud_02mm, angle, oss_list)

add_ply(mg, "corecell_81kg_5mm", corecell_81kg_5mm, 0.0, oss_list)

for angle in angles:
    add_ply(mg, "eglass_ud_02mm_" + str(angle), eglass_ud_02mm, angle, oss_list)

# %%
# Inspect the number of modeling groups and plies
print(len(model.modeling_groups))
print(len(model.modeling_groups["hull"].modeling_plies))
print(len(model.modeling_groups["deck"].modeling_plies))
print(len(model.modeling_groups["bulkhead"].modeling_plies))
print(len(model.modeling_groups["keeltower"].modeling_plies))


# %%
# Show the thickness of one of the plies
model.update()
modeling_ply = model.modeling_groups["deck"].modeling_plies["eglass_ud_02mm_0.5"]
modeling_ply.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot()

# %%
# Show the ply offsets, scaled by a factor of 200
plotter = pyvista.Plotter()
plotter.add_mesh(model.mesh.to_pyvista(), color="white")
plotter.add_mesh(
    modeling_ply.nodal_data.ply_offset.get_pyvista_glyphs(mesh=model.mesh, factor=200),
)
plotter.show()

# %%
# Show the thickness of the entire lay-up
model.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot()

# %%
#
# Write out ACP Model
# -------------------

ACPH5_FILE = "class40.acph5"
CDB_FILENAME_OUT = "class40_analysis_model.cdb"
COMPOSITE_DEFINITIONS_H5 = "ACPCompositeDefinitions.h5"
MATML_FILE = "materials.xml"

# %%
# Update and Save the ACP model
model.update()
model.save(ACPH5_FILE, save_cache=True)

# %%
# Save the model as CDB for solving with PyMAPDL
model.save_analysis_model(CDB_FILENAME_OUT)
# Export the shell lay-up and material file for DPF Composites
model.export_shell_composite_definitions(COMPOSITE_DEFINITIONS_H5)
model.export_materials(MATML_FILE)

# %%
# Download files from ACP server to a local directory
tmp_dir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tmp_dir.name)
cdb_file_local_path = pathlib.Path(WORKING_DIR) / CDB_FILENAME_OUT
matml_file_local_path = pathlib.Path(WORKING_DIR) / MATML_FILE
composite_definitions_local_path = pathlib.Path(WORKING_DIR) / COMPOSITE_DEFINITIONS_H5
acp.download_file(remote_filename=CDB_FILENAME_OUT, local_path=str(cdb_file_local_path))
acp.download_file(remote_filename=MATML_FILE, local_path=str(matml_file_local_path))
acp.download_file(
    remote_filename=COMPOSITE_DEFINITIONS_H5, local_path=str(composite_definitions_local_path)
)

# %%
# Solve with PyMAPDL
# ------------------

# %%
# Import PyMAPDL and connect to its server
from ansys.mapdl.core import launch_mapdl

mapdl = launch_mapdl()
mapdl.clear()
# %%
# Load the CDB file into PyMAPDL
mapdl.input(str(cdb_file_local_path))

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
rst_file_local_path = pathlib.Path(tmp_dir.name) / rstfile_name
mapdl.download(rstfile_name, tmp_dir.name)

# %%
# Post-Processing with DPF composites
# -----------------------------------
#
# Setup: configure imports and connect to the pyDPF Composites server
# and load the dpf composites plugin

from ansys.dpf.composites.composite_model import CompositeModel
from ansys.dpf.composites.constants import FailureOutput
from ansys.dpf.composites.data_sources import (
    CompositeDefinitionFiles,
    ContinuousFiberCompositesFiles,
)
from ansys.dpf.composites.failure_criteria import (
    CombinedFailureCriterion,
    CoreFailureCriterion,
    MaxStrainCriterion,
    MaxStressCriterion,
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
max_stress = MaxStressCriterion()
core_failure = CoreFailureCriterion()

cfc = CombinedFailureCriterion(
    name="Combined Failure Criterion",
    failure_criteria=[max_strain, max_stress, core_failure],
)

# %%
# Create the CompositeModel and configure its input
composite_model = CompositeModel(
    composite_files=ContinuousFiberCompositesFiles(
        rst=rst_file_local_path,
        composite={
            "shell": CompositeDefinitionFiles(definition=composite_definitions_local_path),
        },
        engineering_data=matml_file_local_path,
    ),
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
