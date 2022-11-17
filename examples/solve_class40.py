"""
.. _solve_class40_example:

Basic PyACP Example
===================

Define a Composite Lay-up with PyACP and solve the resulting model with PyMAPDL.

"""

#%%
# Setup: Connect to PyACP Server
# ------------------------------

#%%
# Import standard library and third-party dependencies
import os
import pathlib
import tempfile

import grpc

#%%
# Import Ansys libraries
import ansys.acp.core as pyacp
from ansys.utilities.filetransfer import Client as FileTransferClient

#%%
# Instantiate clients: The ``filetransfer_client`` will be used to up- and download
# files to the server. The ``pyacp_client`` connects to the main PyACP server.
filetransfer_client = FileTransferClient(grpc.insecure_channel("localhost:50556"))

pyacp_server = pyacp.RemoteAcpServer(hostname="localhost", port=50555)
pyacp.wait_for_server(pyacp_server, timeout=30)  # ensure the server is running
pyacp_client = pyacp.Client(pyacp_server)

#%%
#
# Load Mesh and Materials from CDB file
# -------------------------------------

#%%
# Define the directory in which the input files are stored.
#EXAMPLE_DATA_DIR = pathlib.Path(r'D:\ANSYSDev\pyacp-private') / "examples" / "data" / "class40"
EXAMPLE_DATA_DIR = pathlib.Path(os.environ["REPO_ROOT"]) / "examples" / "data" / "class40"

#%%
# Send ``class40.cdb`` to the server.
CDB_FILENAME = "class40.cdb"
filetransfer_client.upload_file(
    local_filename=str(EXAMPLE_DATA_DIR / CDB_FILENAME), remote_filename=CDB_FILENAME
)

#%%
# Load CDB file into PyACP
model = pyacp_client.import_model(path=CDB_FILENAME, format="ansys:cdb")
model

#%%
#
# Build Composite Lay-up
# ----------------------
#
# Create the model (unit system is SI)

#%%
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

#%%
# Fabrics
# '''''''

corecell_81kg_5mm = model.create_fabric(
    name="Corecell 81kg", thickness=0.005, material=mat_corecell_81kg
)
corecell_103kg_10mm = model.create_fabric(
    name="Corecell 103kg", thickness=0.01, material=mat_corecell_103kg
)
eglass_ud_02mm = model.create_fabric(
    name="eglass UD", thickness=0.0002, material=mat_eglass_ud
)

#%%
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

#%%
# Oriented Selection Sets
# '''''''''''''''''''''''

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


#%%
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


#%%
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

#%%
# Add plies to the keeltower
mg = model.create_modeling_group(name="keeltower")
oss_list = [model.oriented_selection_sets["oss_keeltower"]]
for angle in angles:
    add_ply(mg, "eglass_ud_02mm_" + str(angle), eglass_ud_02mm, angle, oss_list)

add_ply(mg, "corecell_81kg_5mm", corecell_81kg_5mm, 0.0, oss_list)

for angle in angles:
    add_ply(mg, "eglass_ud_02mm_" + str(angle), eglass_ud_02mm, angle, oss_list)

#%%
# Inspect the number of plies
print(len(model.modeling_groups))
print(len(model.modeling_groups["hull"].modeling_plies))
print(len(model.modeling_groups["deck"].modeling_plies))
print(len(model.modeling_groups["bulkhead"].modeling_plies))
print(len(model.modeling_groups["keeltower"].modeling_plies))

#%%
#
# Write out ACP Model
# -------------------

#%%
# Update and Save the ACP model
model.update()
model.save("class40.acph5", save_cache=True)

#%%
# Save the model as CDB for solving with PyMAPDL
model.save_analysis_model("class40_analysis_model.cdb")

#%%
# Download analysis CDB file
tmp_dir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tmp_dir.name)
CDB_FILENAME_OUT = "class40_analysis_model.cdb"
CDB_FILEPATH = pathlib.Path(WORKING_DIR) / CDB_FILENAME_OUT
filetransfer_client.download_file(CDB_FILENAME_OUT, str(CDB_FILEPATH))

#%%
# Solve with PyMAPDL
# ------------------

#%%
# Import PyMAPDL and connect to its server
from ansys.mapdl.core import Mapdl

mapdl = Mapdl(ip="localhost", port=50557, timeout=30)

#%%
# Load the CDB file into PyMAPDL
mapdl.input(str(CDB_FILEPATH))

#%%
# Solve the model
mapdl.allsel()
mapdl.slashsolu()
mapdl.solve()

#%%
# Post-processing: show displacements
mapdl.post1()
mapdl.set("last")
mapdl.post_processing.plot_nodal_displacement(component="NORM")

#%%
# Post-Processing with DPF composites
# -----------------------------------

import ansys.dpf.core as dpf
server = dpf.server.connect_to_server("127.0.0.1", port=50558)

from ansys.dpf.composites.failure_criteria import (
    CombinedFailureCriterion,
    MaxStrainCriterion,
)
from ansys.dpf.composites.load_plugin import load_composites_plugin

def get_combined_failure_criterion() -> CombinedFailureCriterion:
    max_strain = MaxStrainCriterion()
    #max_stress = MaxStressCriterion()
    #core_failure = CoreFailureCriterion()
    
    return CombinedFailureCriterion(
        name="Combined Failure Criterion",
        failure_criteria=[max_strain],
    )

#rd = ResultDefinition(
#    name="combined failure criteria",
#    rst_files=[rst_server_path],
#    material_files=[material_server_path],
#    composite_definitions=[h5_server_path],
#    combined_failure_criterion=get_combined_failure_criterion(),
#)
#
#fc_op = dpf.Operator("composite::composite_failure_operator")
#fc_op.inputs.result_definition(rd.to_json())