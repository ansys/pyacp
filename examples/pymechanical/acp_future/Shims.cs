using Ansys.Common.Interop.DSObjectTypes;
using Ansys.Common.Interop.AnsCoreObjects;

using Ansys.Common.Interop.WBUnitTypes;
using Ansys.Common.Interop.DSObjectsAuto;

namespace ACPFuture
{
    public static class Shims
    {


        public static void ModelExportHDF5TransferFile(Ansys.ACT.Automation.Mechanical.Model model, string filename, DSGeometryType geomType, WBUnitSystemType unitSystemType)
        {
            // Todo: unclear why this works only with dsid 0
            // dsid=Model.Analyses[0].ObjectId
            uint dsid = 0;
            model.InternalObject.WriteHDF5TransferFile(geomType, filename, (int)unitSystemType, dsid);
        }

        public static void ImportPlies(Ansys.ACT.Automation.Mechanical.Model model, AnsBSTRColl composite_defintion_paths, AnsVARIANTColl mapping_paths)
        {

            var external_model = model.InternalObject.AddExternalEnhancedModel(DSExternalEnhancedModelType.kEXTERNAL_ENHANCEDMODEL_ASSEMBLEDLAYEREDSECTION);
            var external_model_cast = (IDSExternalEnhancedModelAuto)external_model;
            external_model_cast.Import(composite_defintion_paths, mapping_paths);
            external_model_cast.Update();
        }
    }
}
