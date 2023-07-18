import pathlib

import ansys.mechanical.core as pymechanical
from ansys.dpf.composites.composite_model import CompositeModel
from ansys.dpf.composites.constants import FailureOutput
from ansys.dpf.composites.data_sources import ContinuousFiberCompositesFiles, \
    CompositeDefinitionFiles

import ansys.acp.core as pyacp
from ansys.acp.core._tree_objects.material.property_sets import ConstantStrainLimits

from ansys.dpf.composites.failure_criteria import (
    CombinedFailureCriterion,
    MaxStrainCriterion
)
from ansys.dpf.composites.server_helpers import connect_to_or_start_server

mechanical = pymechanical.launch_mechanical(batch=False)
print(mechanical.project_directory)

result = mechanical.run_python_script_from_file("generate_mesh.py", enable_logging=True)


pyacp_server = pyacp.launch_acp()
pyacp_server.wait(timeout=30)
pyacp_client = pyacp.Client(pyacp_server)

current_file_location = pathlib.Path(__file__).parent

MESH_FILE_NAME = str((current_file_location / "output" / "mesh.h5").resolve())
model = pyacp_client.import_model(path=MESH_FILE_NAME,format="ansys:h5")

mat = model.create_material(name="mat")

mat.ply_type = "regular"
mat.engineering_constants.E1 = 1E12
mat.engineering_constants.E2 = 1E11
mat.engineering_constants.E3 = 1E11
mat.engineering_constants.G12 = 1E10
mat.engineering_constants.G23 = 1E10
mat.engineering_constants.G31 = 1E10
mat.engineering_constants.nu12 = 0.3
mat.engineering_constants.nu13 = 0.3
mat.engineering_constants.nu23 = 0.3

mat.strain_limits = ConstantStrainLimits(
    eXc=-0.01,
    eYc=-0.01,
    eZc=-0.01,
    eXt=0.01,
    eYt=0.01,
    eZt=0.01,
    eSxy=0.01,
    eSyz=0.01,
    eSxz=0.01
)

corecell_81kg_5mm = model.create_fabric(
    name="Corecell 81kg", thickness=0.005, material=mat
)

ros = model.create_rosette(name="ros", origin=(0, 0, 0))

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

output_path = pathlib.Path(mechanical.project_directory)

# %%
# Update and Save the ACP model
model.update()
#model.save(ACPH5_FILE, save_cache=True)

model.export_shell_composite_definitions(output_path / COMPOSITE_DEFINITIONS_H5)
model.export_materials(output_path / MATML_FILE)

material_output_path = str((output_path / MATML_FILE).resolve())
import_material_cmd = f"Model.Materials.Import('{material_output_path}')"
result = mechanical.run_python_script(import_material_cmd)

import_plies_str = f"""
clr.AddReference("Ansys.Common.Interop.241")
external_model_type=Ansys.Common.Interop.DSObjectTypes.DSExternalEnhancedModelType.kEXTERNAL_ENHANCEDMODEL_ASSEMBLEDLAYEREDSECTION

m=Model.InternalObject
em= m.AddExternalEnhancedModel(external_model_type)

str_cont = Ansys.Common.Interop.AnsCoreObjects.AnsBSTRColl()
str_cont.Add(r"System::{str((output_path / COMPOSITE_DEFINITIONS_H5).resolve())}")

null_cont = Ansys.Common.Interop.AnsCoreObjects.AnsVARIANTColl()
null_cont.Add(None)

em.Import(str_cont, null_cont)

em.Update()
    """

result = mechanical.run_python_script(import_plies_str)

# Set bc's and solve
result = mechanical.run_python_script_from_file("set_bc.py", enable_logging=True)
result = mechanical.run_python_script("Model.Analyses[0].Solution.Solve(True)")

print(mechanical.list_files())
print(mechanical.project_directory)

rst_file = [filename for filename in  mechanical.list_files() if filename.endswith(".rst")][0]
matml_out = [filename for filename in  mechanical.list_files() if filename.endswith("MatML.xml")][0]

dpf_server = connect_to_or_start_server(ip="127.0.0.1", port=50052)

max_strain = MaxStrainCriterion()
cfc = CombinedFailureCriterion(
    name="Combined Failure Criterion",
    failure_criteria=[max_strain],
)

composite_model = CompositeModel(
    composite_files=ContinuousFiberCompositesFiles(
        rst=rst_file,
        composite={
            "shell": CompositeDefinitionFiles(definition=output_path / COMPOSITE_DEFINITIONS_H5),
        },
        engineering_data=matml_out,
    ),
    server=dpf_server,
)

# %%
# Evaluate the failure criteria
output_all_elements = composite_model.evaluate_failure_criteria(cfc)

# %%
# Query and plot the results
irf_field = output_all_elements.get_field({"failure_label": FailureOutput.FAILURE_VALUE})
irf_field.plot()