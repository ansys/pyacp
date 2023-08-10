import pathlib

from examples.pymechanical.setup_acp_model import setup_and_update_acp_model

from ansys.dpf.composites.composite_model import CompositeModel
from ansys.dpf.composites.constants import FailureOutput
from ansys.dpf.composites.data_sources import (
    CompositeDefinitionFiles,
    ContinuousFiberCompositesFiles,
)
from ansys.dpf.composites.failure_criteria import CombinedFailureCriterion, MaxStrainCriterion
from ansys.dpf.composites.server_helpers import connect_to_or_start_server
from ansys.mechanical.core import App, global_variables

app = App(version=241)
# The following line extracts the global API entry points and merges them into your global
# Python global variables.
globals().update(global_variables(app))

import os

script_dir = os.path.dirname(os.path.abspath(__file__))

geometry_import_group = Model.GeometryImportGroup
geometry_import = geometry_import_group.AddGeometryImport()

import_format = Ansys.Mechanical.DataModel.Enums.GeometryImportPreference.Format.Automatic
import_preferences = Ansys.ACT.Mechanical.Utilities.GeometryImportPreferences()
import_preferences.ProcessNamedSelections = True
import_preferences.ProcessCoordinateSystems = True

geometry_import.Import(
    os.path.join(script_dir, "geometry", "flat_plate.agdb"), import_format, import_preferences
)

body = Model.Geometry.GetChildren(
    Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body, True
)[0]
body.Thickness = Quantity(0.001, "m")

Model.Mesh.GenerateMesh()


import sys

# Todo: unclear why this works only with dsid 0
# dsid=Model.Analyses[0].ObjectId
import clr

# sys.path.append()


clr.AddReference(os.path.join(script_dir, "acp_future", "bin", "x64", "Debug", "ACPFuture.dll"))
import ACPFuture

bsMeshFilePath = os.path.join(script_dir, "output", "mesh.h5")
unit = Ansys.Mechanical.DataModel.Enums.WBUnitSystemType.ConsistentMKS
geometry_type = ACPFuture.Shims.GeometryType.Sheet
ACPFuture.Shims.ModelExportHDF5TransferFile(Model, bsMeshFilePath, geometry_type, unit)
analysis = Model.AddStaticStructuralAnalysis()

solver_files_directory = Model.Analyses[0].Children[0].SolverFilesDirectory

# ACPH5_FILE = "acp.acph5"
# CDB_FILENAME_OUT = "class40_analysis_model.cdb"


SETUP_FOLDER_NAME = "Setup"
output_path = pathlib.Path(solver_files_directory) / SETUP_FOLDER_NAME
os.mkdir(output_path)

acp_model = setup_and_update_acp_model(output_path)

COMPOSITE_DEFINITIONS_H5 = "ACPCompositeDefinitions.h5"
MATML_FILE = "materials.xml"
file_list = [rf"{SETUP_FOLDER_NAME}::{str((output_path / COMPOSITE_DEFINITIONS_H5).resolve())}"]
ACPFuture.Shims.ImportPlies(Model, file_list, [])


# Geometry has 4 named selctions the
# NS2 is xmin and NS2 is xmax
NS2 = Model.NamedSelections.Children[1]
NS3 = Model.NamedSelections.Children[2]

fixed_support_48 = analysis.AddFixedSupport()
fixed_support_48.Location = NS2

force_37 = analysis.AddForce()
force_37.DefineBy = Ansys.Mechanical.DataModel.Enums.LoadDefineBy.Components
force_37.XComponent.Output.SetDiscreteValue(0, Quantity(1000, "N"))
force_37.Location = NS3

Model.Analyses[0].Solution.Solve(True)

rst_file = [
    filename
    for filename in pathlib.Path(solver_files_directory).iterdir()
    if filename.parts[-1].endswith(".rst")
][0]
matml_out = [
    filename
    for filename in pathlib.Path(solver_files_directory).iterdir()
    if filename.parts[-1].endswith("MatML.xml")
][0]

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

assert composite_model.get_element_info(1).n_layers == 3
irf_field.plot()
