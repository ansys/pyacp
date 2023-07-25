from ansys.mechanical.core import App, global_variables

app = App()
# The following line extracts the global API entry points and merges them into your global
# Python global variables.
globals().update(global_variables(app))

import os
import Ansys
#clr.AddReference("Ansys.Common.Interop.241")

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

internal_model = Model.InternalObject
geometry_type = Ansys.Common.Interop.DSObjectTypes.DSGeometryType.kSheetGeometry
bsMeshFilePath=os.path.join(script_dir,"output", "mesh.h5")
unit = Ansys.Common.Interop.WBUnitTypes.WBUnitSystemType.WBUST_StandardMKS
# Todo: unclear why this works only with dsid 0
#dsid=Model.Analyses[0].ObjectId
dsid = 0
internal_model.WriteHDF5TransferFile(geometry_type, bsMeshFilePath, unit, 0)

external_model_type=Ansys.Common.Interop.DSObjectTypes.DSExternalEnhancedModelType.kEXTERNAL_ENHANCEDMODEL_ASSEMBLEDLAYEREDSECTION

external_model = internal_model.AddExternalEnhancedModel(external_model_type)


str_cont = Ansys.Common.Interop.AnsCoreObjects.AnsBSTRColl()
str_cont.Add(r"{SETUP_FOLDER_NAME}::{str((output_path / COMPOSITE_DEFINITIONS_H5).resolve())}")

null_cont = Ansys.Common.Interop.AnsCoreObjects.AnsVARIANTColl()
null_cont.Add(None)

external_model.Import(str_cont, null_cont)

external_model.Update()
