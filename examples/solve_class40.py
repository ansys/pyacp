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

import ansys.acp.core as pyacp

#%%
# Import Ansys libraries
from ansys.utilities.filetransfer import Client as FileTransferClient

#%%
# Instantiate clients: The ``filetransfer_client`` will be used to up- and download
# files to the server. The ``pyacp_client`` connects to the main PyACP server.
filetransfer_client = FileTransferClient(grpc.insecure_channel("0.0.0.0:50556"))

pyacp_server = pyacp.RemoteAcpServer(hostname="0.0.0.0", port=50555)
pyacp.wait_for_server(pyacp_server, timeout=30)  # ensure the server is running
pyacp_client = pyacp.Client(pyacp_server)

#%%
#
# Load Mesh and Materials from CDB file
# -------------------------------------

#%%
# Define the directory in which the input files are stored.
EXAMPLE_DATA_DIR = pathlib.Path(os.environ["REPO_ROOT"]) / "examples" / "data" / "class40"

#%%
# Send ``class40.cdb`` to the server.
CDB_FILENAME = "class40.cdb"
filetransfer_client.upload_file(
    local_filename=str(EXAMPLE_DATA_DIR / CDB_FILENAME), remote_filename=CDB_FILENAME
)

#%%
# Load CDB file into PyACP
model = pyacp_client.import_model(path="class40.cdb", format="ansys:cdb")
model

#%%
#
# Build Composite Lay-up
# ----------------------
#
# Create the model (unit system is SI)

#%%
# Fabrics
# '''''''

corecell_81kg_5mm = model.create_fabric(
    name="Corecell 81kg", thickness=0.005, material=model.materials["1"]
)
corecell_103kg_10mm = model.create_fabric(
    name="Corecell 103kg", thickness=0.01, material=model.materials["2"]
)
eglass_ud_02mm = model.create_fabric(
    name="eglass UD", thickness=0.0002, material=model.materials["3"]
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


angles = [-90.0, -60.0, -45.0 - 30.0, 0.0, 0.0, 30.0, 45.0, 60.0, 90.0]

#%%
# Define plies for the HULL, DECK and BULKHEAD

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
filetransfer_client.download_file(CDB_FILENAME_OUT, str(WORKING_DIR / CDB_FILENAME_OUT))

#%%
# Solve with PyMAPDL
# ------------------

#%%
from ansys.mapdl.core import Mapdl

#%%
mapdl = Mapdl(ip="0.0.0.0", port=50557, timeout=30)

#%%
mapdl.input(str(WORKING_DIR / CDB_FILENAME_OUT))

#%%
mapdl.allsel()
mapdl.slashsolu()
mapdl.solve()

#%%
mapdl.post1()
mapdl.set("last")
mapdl.post_processing.plot_nodal_displacement(component="NORM")

#%%
mapdl.post_processing.plot_element_stress("X")
