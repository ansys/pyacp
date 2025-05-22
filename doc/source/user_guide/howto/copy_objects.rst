Copy tree objects
=================

The :func:`.recursive_copy` function is a powerful tool for copying ACP tree objects. It allows you to:

- copy objects within the same model or across models
- copy the entire layup, or just a specific branch of the model tree
- control how links between objects are handled

The following sections explain the parameters of the :func:`.recursive_copy` function by applying them to an example model.

Copy to the same model
----------------------

This section shows how to use :func:`.recursive_copy` to duplicate objects within the same ACP model.

Model setup
~~~~~~~~~~~

To get started, launch an ACP instance and load a model:

**Code:**

.. testcode::

    import pathlib
    import tempfile

    import ansys.acp.core as pyacp
    from ansys.acp.core.extras import ExampleKeys, get_example_file

    acp = pyacp.launch_acp()
    tempdir = tempfile.TemporaryDirectory()
    input_file = get_example_file(
        ExampleKeys.MINIMAL_PLATE_ACPH5, pathlib.Path(tempdir.name)
    )

    model = acp.import_model(input_file)

The model structure is as follows:

**Code:**

.. testcode::

    pyacp.print_model(model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

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
                        └── 'ProductionPly'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.1'


At the start of each example, the model is deleted and rel-loaded to get back to the initial state:

**Code:**

.. testcode::

    acp.clear()
    model = acp.import_model(input_file)

Copy one object
~~~~~~~~~~~~~~~

The objects to be copied are passed to :func:`.recursive_copy` in the ``source_objects`` parameter. For example, the following code copies the fabric ``Fabric.1``:

**Code:**

.. testcode::

    fabric = model.fabrics["Fabric.1"]

    res = pyacp.recursive_copy(
        source_objects=[fabric],
        parent_mapping={model: model},
        linked_object_handling="keep",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")

**Output:**

.. testoutput::

    Copied 'Fabric.1' to 'Fabric.2'

The return value of :func:`.recursive_copy` is a dictionary that maps the pre-existing objects to their newly created copies. In the code above, this is used to print what has been copied.

The model now has the following structure:

**Code:**

.. testcode::

    pyacp.print_model(model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

    'ACP Model'
    ├── Materials
    │   └── 'Structural Steel'
    ├── Fabrics
    │   ├── 'Fabric.1'
    │   └── 'Fabric.2'
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
                        └── 'ProductionPly'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.1'


The ``linked_object_handling="keep"`` parameter indicates that links from the fabric to other objects in the tree should be preserved. This means that the new fabric will still have the same material assigned:

**Code:**

.. testcode::

    print(model.fabrics["Fabric.2"].material.id)

**Output:**

.. testoutput::

    Structural Steel

Discard object links
~~~~~~~~~~~~~~~~~~~~

**Code:**

.. testcode::

    acp.clear()
    model = acp.import_model(input_file)

To instead discard links between the copied objects and other objects in the tree, set the ``linked_object_handling`` parameter to ``discard``. For example, the following code copies the fabric ``Fabric.1`` and discards its link to the material:

**Code:**

.. testcode::

    fabric = model.fabrics["Fabric.1"]

    res = pyacp.recursive_copy(
        source_objects=[fabric],
        parent_mapping={model: model},
        linked_object_handling="discard",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")

**Output:**

.. testoutput::

    Copied 'Fabric.1' to 'Fabric.2'

The fabric ``Fabric.2`` does not have a material assigned:

**Code:**

.. testcode::

    print(model.fabrics["Fabric.2"].material)

**Output:**

.. testoutput::

    None

Copy multiple objects
~~~~~~~~~~~~~~~~~~~~~

**Code:**

.. testcode::

    acp.clear()
    model = acp.import_model(input_file)

The ``source_objects`` parameter can include multiple objects. The following example copies the fabric ``Fabric.1`` and the element set ``All_Elements``:

**Code:**

.. testcode::

    fabric = model.fabrics["Fabric.1"]
    element_set = model.element_sets["All_Elements"]

    res = pyacp.recursive_copy(
        source_objects=[fabric, element_set],
        parent_mapping={model: model},
        linked_object_handling="keep",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")

**Output:**

.. testoutput::

    Copied 'All_Elements' to 'All_Elements.2'
    Copied 'Fabric.1' to 'Fabric.2'

This is the model tree after copying:

**Code:**

.. testcode::

    pyacp.print_model(model, show_lines=True, label_by_id=True)


**Output:**

.. testoutput::

    'ACP Model'
    ├── Materials
    │   └── 'Structural Steel'
    ├── Fabrics
    │   ├── 'Fabric.1'
    │   └── 'Fabric.2'
    ├── Element Sets
    │   ├── 'All_Elements'
    │   └── 'All_Elements.2'
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
                        └── 'ProductionPly'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.1'


Copy an object and its children
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Code:**

.. testcode::

    acp.clear()
    model = acp.import_model(input_file)

When an object has children in the ACP model tree, these are automatically included in the copy. The following example copies the modeling group ``ModelingGroup.1`` and its children:

**Code:**

.. testcode::

    modeling_group = model.modeling_groups["ModelingGroup.1"]
    res = pyacp.recursive_copy(
        source_objects=[modeling_group],
        parent_mapping={model: model},
        linked_object_handling="keep",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")

**Output:**

.. testoutput::

    Copied 'ModelingGroup.1' to 'ModelingGroup.2'
    Copied 'ModelingPly.1' to 'ModelingPly.2'

**Code:**

.. testcode::

    pyacp.print_model(model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

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
        ├── 'ModelingGroup.1'
        │   └── Modeling Plies
        │       └── 'ModelingPly.1'
        │           └── Production Plies
        │               └── 'ProductionPly'
        │                   └── Analysis Plies
        │                       └── 'P1L1__ModelingPly.1'
        └── 'ModelingGroup.2'
            └── Modeling Plies
                └── 'ModelingPly.2'

You may notice that the production and analysis plies have not been copied. This is because these are read-only objects which are generated on update. After a model update, they are present:

**Code:**

.. testcode::

    model.update()
    pyacp.print_model(model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

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
        ├── 'ModelingGroup.1'
        │   └── Modeling Plies
        │       └── 'ModelingPly.1'
        │           └── Production Plies
        │               └── 'ProductionPly'
        │                   └── Analysis Plies
        │                       └── 'P1L1__ModelingPly.1'
        └── 'ModelingGroup.2'
            └── Modeling Plies
                └── 'ModelingPly.2'
                    └── Production Plies
                        └── 'ProductionPly.2'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.2'

Copy to a different location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Code:**

.. testcode::

    acp.clear()
    model = acp.import_model(input_file)

The ``parent_mapping`` parameter controls where in the model tree the copied objects are placed. The keys of the dictionary are the original parent objects, and the values are the new parent objects. This means that children of the original parent will be copied to the new parent.

.. note::

    The key and value of the ``parent_mapping`` dictionary must generally (with some exceptions) be of the same type. For example, a :class:`.ModelingPly` object always has a :class:`.ModelingGroup` as its parent. For more details, consult the :ref:`feature_tree` section of the user guide.

The following example copies a the modeling ply ``ModelingPly.1`` into its own parent, ``ModelingGroup.1``.

**Code:**

.. testcode::

    modeling_group_1 = model.modeling_groups["ModelingGroup.1"]
    modeling_ply = modeling_group_1.modeling_plies["ModelingPly.1"]

    res = pyacp.recursive_copy(
        source_objects=[modeling_ply],
        parent_mapping={modeling_group_1: modeling_group_1},
        linked_object_handling="keep",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")

**Output:**

.. testoutput::

    Copied 'ModelingPly.1' to 'ModelingPly.2'

This results in the following model tree:

**Code:**

.. testcode::

    model.update()
    pyacp.print_model(model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

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
                ├── 'ModelingPly.1'
                │   └── Production Plies
                │       └── 'ProductionPly'
                │           └── Analysis Plies
                │               └── 'P1L1__ModelingPly.1'
                └── 'ModelingPly.2'
                    └── Production Plies
                        └── 'ProductionPly.2'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.2'


By changing the value in the ``parent_mapping`` dictionary, you can instead copy it to a new modeling group:

**Code:**

.. testcode::

    modeling_group_2 = model.create_modeling_group(name="New Modeling Group")

    res = pyacp.recursive_copy(
        source_objects=[modeling_ply],
        parent_mapping={modeling_group_1: modeling_group_2},
        linked_object_handling="keep",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")

**Output:**

.. testoutput::

    Copied 'ModelingPly.1' to 'ModelingPly.3'


**Code:**

.. testcode::

    model.update()
    pyacp.print_model(model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

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
        ├── 'ModelingGroup.1'
        │   └── Modeling Plies
        │       ├── 'ModelingPly.1'
        │       │   └── Production Plies
        │       │       └── 'ProductionPly'
        │       │           └── Analysis Plies
        │       │               └── 'P1L1__ModelingPly.1'
        │       └── 'ModelingPly.2'
        │           └── Production Plies
        │               └── 'ProductionPly.2'
        │                   └── Analysis Plies
        │                       └── 'P1L1__ModelingPly.2'
        └── 'New Modeling Group'
            └── Modeling Plies
                └── 'ModelingPly.3'
                    └── Production Plies
                        └── 'ProductionPly.3'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.3'

Copy linked objects
~~~~~~~~~~~~~~~~~~~

**Code:**

.. testcode::

    acp.clear()
    model = acp.import_model(input_file)

Instead of keeping or discarding links to other objects, you can also copy the linked objects. This is done by setting the ``linked_object_handling`` parameter to ``copy``. The following example copies the fabric ``Fabric.1`` and its linked material ``Structural Steel``:


**Code:**

.. testcode::

    fabric = model.fabrics["Fabric.1"]
    res = pyacp.recursive_copy(
        source_objects=[fabric],
        parent_mapping={model: model},
        linked_object_handling="copy",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")

**Output:**

.. testoutput::

    Copied 'Structural Steel' to 'Structural Steel.2'
    Copied 'Fabric.1' to 'Fabric.2'


**Code:**

.. testcode::

    pyacp.print_model(model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

    'ACP Model'
    ├── Materials
    │   ├── 'Structural Steel'
    │   └── 'Structural Steel.2'
    ├── Fabrics
    │   ├── 'Fabric.1'
    │   └── 'Fabric.2'
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
                        └── 'ProductionPly'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.1'


The copied fabric uses the copied material:

**Code:**

.. testcode::

    print(model.fabrics["Fabric.2"].material.id)

**Output:**

.. testoutput::

    Structural Steel.2


Copy linked objects recursively
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Code:**

.. testcode::

    acp.clear()
    model = acp.import_model(input_file)

The copy of linked objects is recursive. In the following example, the modeling group ``ModelingGroup.1`` is used as a source object. Since its child modeling ply ``ModelingPly.1`` has a linked fabric, this fabric and its linked material are also copied. Similarly, the oriented selection set and its linked element set and rosette are copied:

**Code:**

.. testcode::

    modeling_group = model.modeling_groups["ModelingGroup.1"]
    res = pyacp.recursive_copy(
        source_objects=[modeling_group],
        parent_mapping={model: model},
        linked_object_handling="copy",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")

**Output:**

.. testoutput::

    Copied 'Structural Steel' to 'Structural Steel.2'
    Copied 'Global Coordinate System' to 'Global Coordinate System.2'
    Copied 'All_Elements' to 'All_Elements.2'
    Copied 'Fabric.1' to 'Fabric.2'
    Copied 'OrientedSelectionSet.1' to 'OrientedSelectionSet.2'
    Copied 'ModelingGroup.1' to 'ModelingGroup.2'
    Copied 'ModelingPly.1' to 'ModelingPly.2'


**Code:**

.. testcode::

    model.update()
    pyacp.print_model(model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

    'ACP Model'
    ├── Materials
    │   ├── 'Structural Steel'
    │   └── 'Structural Steel.2'
    ├── Fabrics
    │   ├── 'Fabric.1'
    │   └── 'Fabric.2'
    ├── Element Sets
    │   ├── 'All_Elements'
    │   └── 'All_Elements.2'
    ├── Edge Sets
    │   └── 'ns_edge'
    ├── Rosettes
    │   ├── 'Global Coordinate System'
    │   └── 'Global Coordinate System.2'
    ├── Oriented Selection Sets
    │   ├── 'OrientedSelectionSet.1'
    │   └── 'OrientedSelectionSet.2'
    └── Modeling Groups
        ├── 'ModelingGroup.1'
        │   └── Modeling Plies
        │       └── 'ModelingPly.1'
        │           └── Production Plies
        │               └── 'ProductionPly'
        │                   └── Analysis Plies
        │                       └── 'P1L1__ModelingPly.1'
        └── 'ModelingGroup.2'
            └── Modeling Plies
                └── 'ModelingPly.2'
                    └── Production Plies
                        └── 'ProductionPly.2'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.2'

Control the copy of linked objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Code:**

.. testcode::

    acp.clear()
    model = acp.import_model(input_file)

To avoid copying a specific linked object, you can add it (as both key and value) to the ``parent_mapping`` dictionary. The following example copies the modeling group ``ModelingGroup.1`` and its children, but does not copy the material ``Structural Steel`` and rosette ``Global Coordinate System``:


**Code:**

.. testcode::

    material = model.materials["Structural Steel"]
    modeling_group = model.modeling_groups["ModelingGroup.1"]
    rosette = model.rosettes["Global Coordinate System"]

    res = pyacp.recursive_copy(
        source_objects=[modeling_group],
        parent_mapping={model: model, material: material, rosette: rosette},
        linked_object_handling="copy",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")


**Output:**

.. testoutput::

    Copied 'All_Elements' to 'All_Elements.2'
    Copied 'Fabric.1' to 'Fabric.2'
    Copied 'OrientedSelectionSet.1' to 'OrientedSelectionSet.2'
    Copied 'ModelingGroup.1' to 'ModelingGroup.2'
    Copied 'ModelingPly.1' to 'ModelingPly.2'

**Code:**

.. testcode::

    model.update()
    pyacp.print_model(model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

    'ACP Model'
    ├── Materials
    │   └── 'Structural Steel'
    ├── Fabrics
    │   ├── 'Fabric.1'
    │   └── 'Fabric.2'
    ├── Element Sets
    │   ├── 'All_Elements'
    │   └── 'All_Elements.2'
    ├── Edge Sets
    │   └── 'ns_edge'
    ├── Rosettes
    │   └── 'Global Coordinate System'
    ├── Oriented Selection Sets
    │   ├── 'OrientedSelectionSet.1'
    │   └── 'OrientedSelectionSet.2'
    └── Modeling Groups
        ├── 'ModelingGroup.1'
        │   └── Modeling Plies
        │       └── 'ModelingPly.1'
        │           └── Production Plies
        │               └── 'ProductionPly'
        │                   └── Analysis Plies
        │                       └── 'P1L1__ModelingPly.1'
        └── 'ModelingGroup.2'
            └── Modeling Plies
                └── 'ModelingPly.2'
                    └── Production Plies
                        └── 'ProductionPly.2'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.2'

Copy to a different model
-------------------------

Copying objects to a different model works exactly the same as within the same model, with one exception: Since the linked objects do not exist on the target model, ``linked_object_handling="keep"`` is not allowed. Only ``linked_object_handling="discard"`` and ``linked_object_handling="copy"`` are possible.

For the subsequent examples, a second model is created:

**Code:**

.. testcode::

    input_file_2 = get_example_file(
        ExampleKeys.MINIMAL_PLATE_CDB, pathlib.Path(tempdir.name)
    )

    acp.clear()
    source_model = acp.import_model(input_file)
    target_model = acp.import_model(
        input_file_2, name="New ACP Model", format="ansys:cdb", unit_system="SI"
    )

    pyacp.print_model(target_model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

    'New ACP Model'
    ├── Materials
    │   ├── '1'
    │   ├── '2'
    │   ├── '3'
    │   ├── '4'
    │   ├── '5'
    │   └── '6'
    ├── Element Sets
    │   ├── 'All_Elements'
    │   ├── 'BOTTOM_LEFT'
    │   ├── 'FRONT'
    │   ├── 'MIDDLE'
    │   ├── 'TAIL'
    │   ├── 'TOP_RIGHT'
    │   └── '_CM_EXT_SEC_0'
    ├── Edge Sets
    │   ├── 'ED_FRONT'
    │   └── 'ED_TAIL'
    └── Rosettes
        ├── '12'
        └── '13'

Copy the entire layup
~~~~~~~~~~~~~~~~~~~~~

The following example copies all tree objects from the source model to the target model. All children of the ``source_model`` are copied, but the model itself is not copied since it is present in the ``parent_mapping`` dictionary:

**Code:**

.. testcode::

    res = pyacp.recursive_copy(
        source_objects=[source_model],
        parent_mapping={source_model: target_model},
        linked_object_handling="copy",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")


**Output:**

.. testoutput::

    Copied 'Structural Steel' to 'Structural Steel'
    Copied 'Global Coordinate System' to 'Global Coordinate System'
    Copied 'All_Elements' to 'All_Elements.2'
    Copied 'Fabric.1' to 'Fabric.1'
    Copied 'OrientedSelectionSet.1' to 'OrientedSelectionSet.1'
    Copied 'ModelingGroup.1' to 'ModelingGroup.1'
    Copied 'ModelingPly.1' to 'ModelingPly.1'
    Copied 'ns_edge' to 'ns_edge'


**Code:**

.. testcode::

    target_model.update()
    pyacp.print_model(target_model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

    'New ACP Model'
    ├── Materials
    │   ├── '1'
    │   ├── '2'
    │   ├── '3'
    │   ├── '4'
    │   ├── '5'
    │   ├── '6'
    │   └── 'Structural Steel'
    ├── Fabrics
    │   └── 'Fabric.1'
    ├── Element Sets
    │   ├── 'All_Elements'
    │   ├── 'BOTTOM_LEFT'
    │   ├── 'FRONT'
    │   ├── 'MIDDLE'
    │   ├── 'TAIL'
    │   ├── 'TOP_RIGHT'
    │   ├── '_CM_EXT_SEC_0'
    │   └── 'All_Elements.2'
    ├── Edge Sets
    │   ├── 'ED_FRONT'
    │   ├── 'ED_TAIL'
    │   └── 'ns_edge'
    ├── Rosettes
    │   ├── '12'
    │   ├── '13'
    │   └── 'Global Coordinate System'
    ├── Oriented Selection Sets
    │   └── 'OrientedSelectionSet.1'
    └── Modeling Groups
        └── 'ModelingGroup.1'
            └── Modeling Plies
                └── 'ModelingPly.1'
                    └── Production Plies
                        └── 'ProductionPly'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.1'

Control the copy of linked objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Code:**

.. testcode::

    acp.clear()
    source_model = acp.import_model(input_file)
    target_model = acp.import_model(
        input_file_2, name="New ACP Model", format="ansys:cdb", unit_system="SI"
    )

As with the copy within the same model, the ``parent_mapping`` dictionary can be used to limit the copy of linked objects. The following example copies the entire layup, except for the material ``Structural Steel``, element set ``All_Elements``, edge set ``ns_edge``, and rosette ``Global Coordinate System``:

**Code:**

.. testcode::

    res = pyacp.recursive_copy(
        source_objects=[source_model],
        parent_mapping={
            source_model: target_model,
            source_model.materials["Structural Steel"]: target_model.materials["1"],
            source_model.element_sets["All_Elements"]: target_model.element_sets[
                "All_Elements"
            ],
            source_model.edge_sets["ns_edge"]: target_model.edge_sets["ED_TAIL"],
            source_model.rosettes["Global Coordinate System"]: target_model.rosettes["12"],
        },
        linked_object_handling="copy",
    )
    for source, target in res.items():
        print(f"Copied '{source.id}' to '{target.id}'")

**Output:**

.. testoutput::

    Copied 'Fabric.1' to 'Fabric.1'
    Copied 'OrientedSelectionSet.1' to 'OrientedSelectionSet.1'
    Copied 'ModelingGroup.1' to 'ModelingGroup.1'
    Copied 'ModelingPly.1' to 'ModelingPly.1'


**Code:**

.. testcode::

    target_model.update()
    pyacp.print_model(target_model, show_lines=True, label_by_id=True)

**Output:**

.. testoutput::

    'New ACP Model'
    ├── Materials
    │   ├── '1'
    │   ├── '2'
    │   ├── '3'
    │   ├── '4'
    │   ├── '5'
    │   └── '6'
    ├── Fabrics
    │   └── 'Fabric.1'
    ├── Element Sets
    │   ├── 'All_Elements'
    │   ├── 'BOTTOM_LEFT'
    │   ├── 'FRONT'
    │   ├── 'MIDDLE'
    │   ├── 'TAIL'
    │   ├── 'TOP_RIGHT'
    │   └── '_CM_EXT_SEC_0'
    ├── Edge Sets
    │   ├── 'ED_FRONT'
    │   └── 'ED_TAIL'
    ├── Rosettes
    │   ├── '12'
    │   └── '13'
    ├── Oriented Selection Sets
    │   └── 'OrientedSelectionSet.1'
    └── Modeling Groups
        └── 'ModelingGroup.1'
            └── Modeling Plies
                └── 'ModelingPly.1'
                    └── Production Plies
                        └── 'ProductionPly'
                            └── Analysis Plies
                                └── 'P1L1__ModelingPly.1'
