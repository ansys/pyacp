import os
import pathlib

from examples.pymechanical.postprocess_results import postprocess_results
from examples.pymechanical.setup_acp_model import setup_and_update_acp_model

from ansys.mechanical.core import App, global_variables

app = App(version=241)
# The following line extracts the global API entry points and merges them into your global
# Python global variables.
globals().update(global_variables(app))

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

import clr

clr.AddReference(os.path.join(script_dir, "acp_future", "bin", "x64", "Debug", "ACPFuture.dll"))
import ACPFuture

bsMeshFilePath = os.path.join(script_dir, "output", "mesh.h5")
unit = Ansys.Mechanical.DataModel.Enums.WBUnitSystemType.ConsistentMKS
geometry_type = ACPFuture.Shims.GeometryType.Sheet
ACPFuture.Shims.ModelExportHDF5TransferFile(Model, bsMeshFilePath, geometry_type, unit)

analysis = Model.AddStaticStructuralAnalysis()
solver_files_directory = Model.Analyses[0].Children[0].SolverFilesDirectory

SETUP_FOLDER_NAME = "Setup"
output_path = pathlib.Path(solver_files_directory) / SETUP_FOLDER_NAME
os.mkdir(output_path)

acp_model = setup_and_update_acp_model(output_path)

COMPOSITE_DEFINITIONS_H5 = "ACPCompositeDefinitions.h5"
MATML_FILE = "materials.xml"

material_output_path = str((output_path / MATML_FILE).resolve())
material_output_path = material_output_path.replace("\\", "\\\\")
Model.Materials.Import(material_output_path)

hdf_file = rf"{SETUP_FOLDER_NAME}::{str((output_path / COMPOSITE_DEFINITIONS_H5).resolve())}"
hdf_file = hdf_file.replace("\\", "\\\\")
hdf_file = hdf_file.replace("\\", "\\\\")
ACPFuture.Shims.ImportPlies(Model, hdf_file)


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

postprocess_results(rst_file, matml_out, output_path / COMPOSITE_DEFINITIONS_H5)
