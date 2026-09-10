Print model tree
----------------

A tree structure gives an overview of an ACP model. To print a model's tree structure, start with a :class:`.Model` instance:

.. testsetup::

    import ansys.acp.core as pyacp

    acp = pyacp.launch_acp()
    model = acp.import_model("../tests/data/minimal_complete_model_no_matml_link.acph5")


.. doctest::

    >>> model
    <Model with name 'ACP Model'>

You can print the tree structure using the :func:`.print_model` function:

.. doctest::

    >>> pyacp.print_model(model, show_lines=True)
    'ACP Model'
    ├── Materials
    │   └── 'Structural Steel'
    ├── Fabrics
    │   └── 'Fabric.1'
    ├── Element Sets
    │   └── 'All_Elements'
    ├── Edge Sets
    │   └── 'ns_edge'
    ├── Rosettes
    │   └── 'Global Coordinate System'
    ├── Oriented Selection Sets
    │   └── 'OrientedSelectionSet.1'
    └── Modeling Groups
        └── 'ModelingGroup.1'
            └── Modeling Plies
                └── 'ModelingPly.1'
                    └── Production Plies
                        └── 'P1__ModelingPly.1'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.1'
    <BLANKLINE>


Alternatively, you can use :func:`.get_model_tree` to get a tree representation. This allows manually iterating over the tree structure:

.. doctest::

    >>> tree_root = pyacp.get_model_tree(model)
    >>> tree_root.label
    "'ACP Model'"
    >>> for child in tree_root.children:
    ...     print(child.label)
    ...
    Materials
    Fabrics
    Element Sets
    Edge Sets
    Rosettes
    Oriented Selection Sets
    Modeling Groups


The ``hide_empty`` label can be set to ``False`` to also show empty groups:

.. doctest::

    >>> pyacp.print_model(model, hide_empty=False, show_lines=True)
    'ACP Model'
    ├── Materials
    │   └── 'Structural Steel'
    ├── Fabrics
    │   └── 'Fabric.1'
    ├── Stackups
    ├── Sublaminates
    ├── Element Sets
    │   └── 'All_Elements'
    ├── Edge Sets
    │   └── 'ns_edge'
    ├── Cad Geometries
    ├── Virtual Geometries
    ├── Rosettes
    │   └── 'Global Coordinate System'
    ├── Lookup Tables 1d
    ├── Lookup Tables 3d
    ├── Parallel Selection Rules
    ├── Cylindrical Selection Rules
    ├── Spherical Selection Rules
    ├── Tube Selection Rules
    ├── Cut Off Selection Rules
    ├── Geometrical Selection Rules
    ├── Variable Offset Selection Rules
    ├── Boolean Selection Rules
    ├── Oriented Selection Sets
    │   └── 'OrientedSelectionSet.1'
    ├── Modeling Groups
    │   └── 'ModelingGroup.1'
    │       ├── Modeling Plies
    │       │   └── 'ModelingPly.1'
    │       │       └── Production Plies
    │       │           └── 'P1__ModelingPly.1'
    │       │               └── Analysis Plies
    │       │                   └── 'P1L1__ModelingPly.1'
    │       ├── Interface Layers
    │       └── Butt Joint Sequences
    ├── Imported Modeling Groups
    ├── Sampling Points
    ├── Section Cuts
    ├── Solid Models
    ├── Imported Solid Models
    ├── Sensors
    └── Field Definitions
    <BLANKLINE>
