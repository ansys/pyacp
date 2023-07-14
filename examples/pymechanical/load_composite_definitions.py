clr.AddReference("Ansys.Common.Interop.241")
#t=Ansys.Common.Interop.DSObjectTypes.DSExternalEnhancedModelType.kEXTERNAL_ENHANCEDMODEL_LAYEREDSECTION
t=Ansys.Common.Interop.DSObjectTypes.DSExternalEnhancedModelType.kEXTERNAL_ENHANCEDMODEL_ASSEMBLEDLAYEREDSECTION


m=Model.InternalObject
em= m.AddExternalEnhancedModel(t)

str_cont = Ansys.Common.Interop.AnsCoreObjects.AnsBSTRColl()

#str_cont.Add("D:\\ANSYSDev\\pyacp-private\\examples\\ACPCompositeDefinitions.h5")
str_cont.Add("ACP-Pre::D:\\ANSYSDev\\pyacp-private\\examples\\workbench_project\\flat_plat_files\\dp0\\ACP-Pre\\ACP\\ACPCompositeDefinitions.h5")
#str_cont.Add("ACP-Pre::D:\\ANSYSDev\\pyacp-private\\examples\\ACPCompositeDefinitions.h5")

null_cont = Ansys.Common.Interop.AnsCoreObjects.AnsVARIANTColl()
null_cont.Add(None)

em.Import(str_cont, null_cont)

em.Update()

