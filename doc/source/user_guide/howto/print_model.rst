Printing the model tree
-----------------------

To get an overview of an ACP model, you can print its tree structure. Starting with a :class:`.Model` instance:

.. testsetup::

    import ansys.acp.core as pyacp

    acp = pyacp.launch_acp()
    path = acp.upload_file("../tests/data/minimal_complete_model.acph5")
    model = acp.import_model(path=path)


.. doctest::

    >>> model
    <Model with name 'ACP Model'>

You can print the tree structure using the :func:`.print_model` function:

.. doctest::

    >>> pyacp.print_model(model)
    Model
        Material Data
            Materials
                Structural Steel
            Fabrics
                Fabric.1
        Element Sets
            All_Elements
        Edge Sets
            ns_edge
        Geometry
        Rosettes
            Global Coordinate System
        Lookup Tables
        Selection Rules
        Oriented Selection Sets
            OrientedSelectionSet.1
        Modeling Groups
            ModelingGroup.1
                ModelingPly.1
                    ProductionPly
                        P1L1__ModelingPly.1
    <BLANKLINE>


Alternatively, you can use :func:`.get_model_tree` to get a tree representation. This allows manually iterating over the tree structure:

.. doctest::

    >>> tree_root = pyacp.get_model_tree(model)
    >>> tree_root.label
    'Model'
    >>> for child in tree_root.children:
    ...     print(child.label)
    ...
    Material Data
    Element Sets
    Edge Sets
    Geometry
    Rosettes
    Lookup Tables
    Selection Rules
    Oriented Selection Sets
    Modeling Groups
