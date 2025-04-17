.. _feature_tree:

Feature tree
------------

.. testsetup::

    import ansys.acp.core as pyacp

    acp = pyacp.launch_acp()
    model = acp.import_model("../tests/data/minimal_complete_model_no_matml_link.acph5")

The following tree shows the hierarchy of PyACP objects:

.. doctest::

    >>> pyacp.extras.feature_tree.print_feature_tree()
    Model
    ├── Material
    ├── Fabric
    ├── Stackup
    ├── SubLaminate
    ├── ElementSet
    ├── EdgeSet
    ├── CADGeometry
    │   └── CADComponent (read-only)
    ├── VirtualGeometry
    ├── Rosette
    ├── LookUpTable1D
    │   └── LookUpTable1DColumn
    ├── LookUpTable3D
    │   └── LookUpTable3DColumn
    ├── ParallelSelectionRule
    ├── CylindricalSelectionRule
    ├── SphericalSelectionRule
    ├── TubeSelectionRule
    ├── CutOffSelectionRule
    ├── GeometricalSelectionRule
    ├── VariableOffsetSelectionRule
    ├── BooleanSelectionRule
    ├── OrientedSelectionSet
    ├── ModelingGroup
    │   ├── ModelingPly
    │   │   └── ProductionPly (read-only)
    │   │       └── AnalysisPly (read-only)
    │   ├── InterfaceLayer
    │   └── ButtJointSequence
    ├── ImportedModelingGroup
    │   └── ImportedModelingPly
    │       └── ImportedProductionPly (read-only)
    │           └── ImportedAnalysisPly (read-only)
    ├── SamplingPoint
    ├── SectionCut
    ├── SolidModel
    │   ├── ExtrusionGuide
    │   ├── SnapToGeometry
    │   ├── SolidElementSet (read-only)
    │   ├── CutOffGeometry
    │   ├── AnalysisPly (read-only)
    │   └── InterfaceLayer (read-only)
    ├── ImportedSolidModel
    │   ├── SolidElementSet (read-only)
    │   ├── CutOffGeometry
    │   ├── LayupMappingObject
    │   │   ├── AnalysisPly (read-only)
    │   │   └── ImportedAnalysisPly (read-only)
    │   ├── AnalysisPly (read-only)
    │   └── ImportedAnalysisPly (read-only)
    ├── Sensor
    └── FieldDefinition
    <BLANKLINE>


This structure determines how objects can be created, accessed, and stored in the model.


For example, :class:`.ModelingPly` is a child of :class:`.ModelingGroup`, which is a child of :class:`.Model`. To access a specific modeling ply, you can traverse this tree hierarchy:

.. doctest::

    >>> model
    <Model with name 'ACP Model'>
    >>> model.modeling_groups
    <MutableMapping[ModelingGroup] with keys ['ModelingGroup.1']>
    >>> modeling_group = model.modeling_groups["ModelingGroup.1"]
    >>> modeling_group.modeling_plies
    <MutableMapping[ModelingPly] with keys ['ModelingPly.1']>
    >>> modeling_ply = modeling_group.modeling_plies["ModelingPly.1"]
    >>> modeling_ply
    <ModelingPly with id 'ModelingPly.1'>

To create a new modeling ply, you can use the :meth:`.ModelingGroup.create_modeling_ply` method:

.. doctest::

    >>> new_ply = modeling_group.create_modeling_ply(name="New Ply")
    >>> new_ply
    <ModelingPly with id 'New Ply'>

When cloning and storing a modeling ply, the ``parent`` argument must be a :class:`.ModelingGroup` object:

.. doctest::

    >>> other_modeling_group = model.create_modeling_group()
    >>> cloned_ply = modeling_ply.clone()
    >>> cloned_ply
    <ModelingPly with id ''>
    >>> cloned_ply.store(parent=other_modeling_group)
    >>> cloned_ply
    <ModelingPly with id 'ModelingPly.2'>
