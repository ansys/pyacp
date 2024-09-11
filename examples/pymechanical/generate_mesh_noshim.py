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

import Ansys

"""
Generate the mesh based on a geometry and export it. Used in remote_workflow.py.
"""

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

bsMeshFilePath = os.path.join(script_dir, "output", "mesh.h5")
unit = Ansys.Mechanical.DataModel.Enums.WBUnitSystemType.ConsistentMKS
geometry_type = Ansys.Mechanical.DataModel.Enums.GeometryType.Sheet
dsid = 0

Model.InternalObject.WriteHDF5TransferFile(geometry_type, bsMeshFilePath, unit, dsid)
