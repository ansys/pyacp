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
            /*
             * Export Shell Mesh from Mechanical in hdf5 format. 
             */
            // Todo: unclear why this works only with dsid 0
            // dsid=Model.Analyses[0].ObjectId
            uint dsid = 0;
            model.InternalObject.WriteHDF5TransferFile((DSGeometryType)geomType, filename, (int)unitSystemType, 0);
        }
        
        public static void ImportPlies(Ansys.ACT.Automation.Mechanical.Model model, string composite_defintion_paths)
        {
            /*
             * Import CompositeDefinitions.h5 in Mechanical and generate the ImportedPlies object.
             */
  
            // Note: Currently supports only a single composite definition file and no
            // mapping files because I'm not sure what is the best way
            // to pass lists from IronPython to C#
            // Note: it is not clear if multiple CompositeDefinition files are actually supported.
            var composite_definition_paths_coll = new AnsBSTRColl();
            var mapping_paths_coll = new AnsVARIANTColl();

            composite_definition_paths_coll.Add(composite_defintion_paths);
            mapping_paths_coll.Add(null);

            var external_model = (IDSExternalEnhancedModelAuto)model.InternalObject.AddExternalEnhancedModel(DSExternalEnhancedModelType.kEXTERNAL_ENHANCEDMODEL_ASSEMBLEDLAYEREDSECTION);

            // The second argument for Import is probably the list of mapping files. It is required
            // to pass a container with a single null entry if no mapping files are present, otherwise Import will fail.
            external_model.Import(composite_definition_paths_coll, mapping_paths_coll);
            // Note: If plies cannot be imported, Update will remove the whole
            // Imported Plies object from the tree.
            external_model.Update();
        }
    }
}
