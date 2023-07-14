geometry_import_group_11 = Model.GeometryImportGroup
geometry_import_28 = geometry_import_group_11.AddGeometryImport()


geometry_import_28_format = Ansys.Mechanical.DataModel.Enums.GeometryImportPreference.Format.Automatic
geometry_import_28_preferences = Ansys.ACT.Mechanical.Utilities.GeometryImportPreferences()

geometry_import_28_preferences.ProcessNamedSelections = True
geometry_import_28_preferences.ProcessCoordinateSystems = True
geometry_import_28.Import(r"D:\ANSYSDev\pyacp-private\examples\pymechanical\geometry\\flat_plate.agdb", geometry_import_28_format, geometry_import_28_preferences)


body = Model.Geometry.GetChildren(
        Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body, True
    )[0]
body.Thickness = Quantity(0.001, "m")

Model.Mesh.GenerateMesh()

m=Model.InternalObject
clr.AddReference("Ansys.Common.Interop.241")
import Ansys
t=Ansys.Common.Interop.DSObjectTypes.DSGeometryType.kSheetGeometry
#dsid=Model.Analyses[0].ObjectId

bsMeshFilePath="D:\\ANSYSDev\\pyacp-private\\examples\\pymechanical\\output\\mesh.h5"
unit=Ansys.Common.Interop.WBUnitTypes.WBUnitSystemType.WBUST_StandardMKS
m.WriteHDF5TransferFile(t, bsMeshFilePath, unit, 0)