analysis = Model.AddStaticStructuralAnalysis()

# Geometry has 4 named selctions the
# NS2 is xmin and NS2 is xmax
NS2 = Model.NamedSelections.Children[1]
NS3 = Model.NamedSelections.Children[2]

fixed_support_48 =analysis.AddFixedSupport()
fixed_support_48.Location = NS2

force_37 = analysis.AddForce()
force_37.DefineBy = LoadDefineBy.Components
force_37.XComponent.Output.SetDiscreteValue(0, Quantity(1000, "N"))
force_37.Location = NS3

