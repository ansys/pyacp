import ansys.mechanical.core as pymechanical
import ansys.acp.core as pyacp

mechanical = pymechanical.launch_mechanical(batch=False)

print(mechanical.project_directory)
result = mechanical.run_python_script_from_file("generate_mesh.py", enable_logging=True)

#result = mechanical.run_python_script_from_file("print_tree.py", enable_logging=True)

#result = mechanical.run_python_script("Model.GeometryImportGroup[0].Import('D:\\ANSYSDev\pymechanical_install\\flat_plate.stp')", enable_logging=True)

# %%
# Launch the PyACP server and connect to it.
pyacp_server = pyacp.launch_acp()
pyacp_server.wait(timeout=30)
pyacp_client = pyacp.Client(pyacp_server)

MESH_FILE_NAME = r"D:\\ANSYSDev\\pyacp-private\\examples\\pymechanical\\output\\mesh.h5"
model = pyacp_client.import_model(path=MESH_FILE_NAME,format="ansys:h5")

mat = model.create_material(name="mat")


mat.ply_type = "regular"

# %%
# Fabrics
# '''''''

corecell_81kg_5mm = model.create_fabric(
    name="Corecell 81kg", thickness=0.005, material=mat
)


''''''

ros = model.create_rosette(name="ros", origin=(0, 0, 0))


# %%
# Oriented Selection Sets
# '''''''''''''''''''''''
#
# Note: the element sets are imported from the initial mesh (CDB)

oss = model.create_oriented_selection_set(
    name="oss",
    orientation_point=(-0, 0, 0),
    orientation_direction=(0.0, 1, 0.0),
    element_sets=[model.element_sets["All_Elements"]],
    rosettes=[ros],
)

mg = model.create_modeling_group(name="group")
mg.create_modeling_ply(
        name="ply",
        ply_material=corecell_81kg_5mm,
        oriented_selection_sets=[oss],
        ply_angle=45,
        number_of_layers=1,
        global_ply_nr=0,  # add at the end
    )


ACPH5_FILE = "acp.acph5"
CDB_FILENAME_OUT = "class40_analysis_model.cdb"
COMPOSITE_DEFINITIONS_H5 = "ACPCompositeDefinitions.h5"
MATML_FILE = "materials.xml"

# %%
# Update and Save the ACP model
model.update()
model.save(ACPH5_FILE, save_cache=True)

model.export_shell_composite_definitions(COMPOSITE_DEFINITIONS_H5)
model.export_materials(MATML_FILE)
result = mechanical.run_python_script_from_file("import_materials.py", enable_logging=True)
result = mechanical.run_python_script_from_file("set_bc.py", enable_logging=True)

result = mechanical.run_python_script_from_file("load_composite_definitions.py", enable_logging=True)


result = mechanical.run_python_script_from_file("solve.py", enable_logging=True)
#result = mechanical.run_python_script("Tree.Find(name='P1L1__ModelingPly.1')", enable_logging=True)

print(mechanical.project_directory)