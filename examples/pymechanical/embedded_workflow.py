# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# type: ignore
import os
import pathlib

from constants import COMPOSITE_DEFINITIONS_H5, MATML_FILE
from postprocess_results import postprocess_results
from setup_acp_model import setup_and_update_acp_model

from ansys.mechanical.core import App, global_variables

"""
 Full composites workflow that uses 'embedded' PyMechanical.
 These are the main steps:
    * Load geometry (with named selections) in PyMechanical
    * Mesh in PyMechanical
    * Export mesh to HDF5 file
    * Load mesh in PyACP and build lay-up
    * Export composite definitions and material data from PyACP
    * Import lay-up and material in PyMechanical (imported plies)
    * Define boundary condition in PyMechanical
    * Postprocess results with PyDPF Composites (using the materials file and the RST
      file generated by PyMechanical)

 The workflow currently uses a Docker container for PyACP and PyDPF Composites. For PyMechanical,
 the local installer is used. There is no known issue that prevents us from using the PyMechanical
 container. This was just not yet implemented due to time restrictions.
"""

app = App(version=241)
# The following line extracts the global API entry points and merges them into your global
# Python variables
globals().update(global_variables(app))

script_dir = os.path.dirname(os.path.abspath(__file__))

# Import the geometry
# An agdb (Design modeler) file is used because it enables specifying named selections
# directly in the geometry that can be imported into Mechanical.
# The agdb geometry file was created by loading a Spaceclaim geometry in DesignModeler (without
# further modification).
# When directly importing the Spaceclaim geometry in Mechanical, the named selections where not
# imported.
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

# Generate mesh
Model.Mesh.GenerateMesh()

# Load ACPFuture Shim
# Note: In the embedded PyMechanical, the Shim has to be loaded with an
# absolute path. In the remote workflow, it is loaded by adding the containing folder
# to the path and then just passing the file name. This does not work for the embedded case
# (and vice versa).
import clr

clr.AddReference(os.path.join(script_dir, "acp_future", "bin", "x64", "Debug", "ACPFuture.dll"))
import ACPFuture

# Export the hdf5 file from Mechanical
mesh_path = os.path.join(script_dir, "output", "mesh.h5")
unit = Ansys.Mechanical.DataModel.Enums.WBUnitSystemType.ConsistentMKS
geometry_type = ACPFuture.Shims.GeometryType.Sheet
ACPFuture.Shims.ModelExportHDF5TransferFile(Model, mesh_path, geometry_type, unit)

# Create a structural analysis. This is done here
# to the solver_files_directory.
analysis = Model.AddStaticStructuralAnalysis()
solver_files_directory = Model.Analyses[0].Children[0].SolverFilesDirectory

# Create a setup folder for the composite definitions file.
# It is important to save the composite definitions file in a location where a
# relative path to the solver_files_directory can be computed. The "Setup" folder is
# probably unnecessary, but we keep it to have a similar folder structure as in the
# Workbench project.
# Note: If something fails during the import, no imported plies are generated. There is no
# error message.
SETUP_FOLDER_NAME = "Setup"
output_path = pathlib.Path(solver_files_directory) / SETUP_FOLDER_NAME
os.mkdir(output_path)

acp_model = setup_and_update_acp_model(output_path, mesh_path)

# Import materials
material_output_path = str((output_path / MATML_FILE).resolve())
material_output_path = material_output_path.replace("\\", "\\\\")
Model.Materials.Import(material_output_path)

# The prefix before the filen ame and :: is necessary, but it looks like the actual value is
# ignored.
hdf_file = rf"{SETUP_FOLDER_NAME}::{str((output_path / COMPOSITE_DEFINITIONS_H5).resolve())}"
# backslashes need to be escaped twice because when
# passing the path to the Shim, one escape is undone
hdf_file = hdf_file.replace("\\", "\\\\")
hdf_file = hdf_file.replace("\\", "\\\\")
ACPFuture.Shims.ImportPlies(Model, hdf_file)

# Define boundary conditions
# Geometry has 4 named selections the
# NS2 is xmin and NS3 is xmax
NS2 = Model.NamedSelections.Children[1]
NS3 = Model.NamedSelections.Children[2]

fixed_support_48 = analysis.AddFixedSupport()
fixed_support_48.Location = NS2

force_37 = analysis.AddForce()
force_37.DefineBy = Ansys.Mechanical.DataModel.Enums.LoadDefineBy.Components
force_37.XComponent.Output.SetDiscreteValue(0, Quantity(1000, "N"))
force_37.Location = NS3

# Solve
Model.Analyses[0].Solution.Solve(True)

# Identify result and material files
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
