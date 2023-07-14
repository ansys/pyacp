analysis = Model.AddStaticStructuralAnalysis()

NS1 = Model.NamedSelections.Children[0]
NS2 = Model.NamedSelections.Children[1]
NS3 = Model.NamedSelections.Children[2]

fixed_support_48 =analysis.AddFixedSupport()
fixed_support_48.Location = NS2

force_37 = analysis.AddForce()
force_37.DefineBy = LoadDefineBy.Components
force_37.XComponent.Output.SetDiscreteValue(0, Quantity(100, "N"))
force_37.Location = NS3

