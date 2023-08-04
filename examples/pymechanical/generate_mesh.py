import os
import Ansys
clr.AddReference("Ansys.Common.Interop.241")

script_dir = os.path.dirname(os.path.abspath(__file__))

geometry_import_group = Model.GeometryImportGroup
geometry_import = geometry_import_group.AddGeometryImport()

import_format = Ansys.Mechanical.DataModel.Enums.GeometryImportPreference.Format.Automatic
import_preferences = Ansys.ACT.Mechanical.Utilities.GeometryImportPreferences()
import_preferences.ProcessNamedSelections = True
import_preferences.ProcessCoordinateSystems = True

geometry_import.Import(os.path.join(script_dir, "geometry", "flat_plate.agdb"), import_format, import_preferences)

body = Model.Geometry.GetChildren(
        Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body, True
    )[0]
body.Thickness = Quantity(0.001, "m")

Model.Mesh.GenerateMesh()

geometry_type = Ansys.Common.Interop.DSObjectTypes.DSGeometryType.kSheetGeometry
bsMeshFilePath = os.path.join(script_dir, "output", "mesh.h5")
unit = Ansys.Common.Interop.WBUnitTypes.WBUnitSystemType.WBUST_StandardMKS


import clr
import sys
sys.path.append(os.path.join(script_dir, "acp_future", "bin", "x64", "Debug"))
clr.AddReference(r"ACPFuture.dll")
import ACPFuture
ACPFuture.Shims.ModelExportHDF5TransferFile(Model, bsMeshFilePath, geometry_type, unit)

