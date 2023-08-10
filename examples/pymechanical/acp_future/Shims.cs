using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Ansys.Common.Interop.DSObjectTypes;
using Ansys.Mechanical.DataModel.Enums;
using Ansys.Common.Interop.AnsCoreObjects;
using Ansys.Common.Interop.DSObjectsAuto;
using Ansys.ACT.Automation.Mechanical;

namespace ACPFuture
{
    public static class Shims
    {
        public enum GeometryType
        {
            Solid = DSGeometryType.kSolidGeometry,
            Sheet = DSGeometryType.kSheetGeometry
        }

        public static void ModelExportHDF5TransferFile(Ansys.ACT.Automation.Mechanical.Model model, string filename, GeometryType geomType, WBUnitSystemType unitSystemType)
        {
            // Todo: unclear why this works only with dsid 0
            // dsid=Model.Analyses[0].ObjectId
            uint dsid = 0;
            model.InternalObject.WriteHDF5TransferFile((DSGeometryType)geomType, filename, (int)unitSystemType, 0);
        }
        
        public static void ImportPlies(Ansys.ACT.Automation.Mechanical.Model model, string composite_defintion_paths)
        {
  
            // Note: Currently supports only a single composite definition file and no
            // mapping files because I'm not sure what is the best way
            // to pass lists from IronPython to C#
            var composite_definition_paths_coll = new AnsBSTRColl();
            var mapping_paths_coll = new AnsVARIANTColl();

            composite_definition_paths_coll.Add(composite_defintion_paths);
            mapping_paths_coll.Add(null);

            /*
            foreach (var str in composite_defintion_paths){
                 composite_definition_paths_coll.Add(str);
             }
             foreach (var str in mapping_paths)
             {
                 mapping_paths_coll.Add(str);
             }
             */

            var external_model = (IDSExternalEnhancedModelAuto)model.InternalObject.AddExternalEnhancedModel(DSExternalEnhancedModelType.kEXTERNAL_ENHANCEDMODEL_ASSEMBLEDLAYEREDSECTION);
            external_model.Import(composite_definition_paths_coll, mapping_paths_coll);
            external_model.Update();
        }
    }
}
