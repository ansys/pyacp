Stored versus unstored objects
------------------------------

General concept
~~~~~~~~~~~~~~~

PyACP objects can exist in two states: stored and unstored.

A stored object has been sent to the ACP server. When any of its properties change, the change is automatically propagated to the server. Similarly, when an attribute is accessed, the value is retrieved from the server.

An unstored object is a local representation of an ACP object. It can be used to specify the defining properties of the object, but any computed properties are not available. When an unstored object is stored, it is sent to the server and becomes a stored object.

Creating stored and unstored objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider the following example. First, launch an ACP instance and import a model. This creates a *stored* model object.

.. doctest::

    >>> import ansys.acp.core as pyacp
    >>> acp = pyacp.launch_acp()

.. testcode::
    :hide:

    path = acp.upload_file("../tests/data/minimal_complete_model.acph5")


.. doctest::

    >>> # path = ... # path to the model file
    >>> model = acp.import_model(path=path)
    >>> model
    <Model with name 'ACP Model'>

To create a new *stored* material object, call the :meth:`.create_material` method of the model object.

.. doctest::

    >>> model.create_material(name="New Material")
    <Material with id 'New Material'>

To instead create an *unstored* material object, directly call the :class:`.Material` constructor:

.. doctest::

    >>> material = pyacp.Material(name="Another Material")
    >>> material
    <Material with id ''>

Notice that the *unstored* material object has an empty ID. This is because the ID is assigned by the server when the object is stored.

Storing objects
~~~~~~~~~~~~~~~

You can make changes to the unstored material, but these are lost when the Python session ends.

.. doctest::

    >>> material.density.rho = 8000

To store the material on an ACP model, call the material's :meth:`store <.Material.store>` method. The ``parent`` parameter determines where in the ACP model the material is stored. In this case, the root of the model is the parent.

.. doctest::

    >>> material.store(parent=model)
    >>> material
    <Material with id 'Another Material'>

Cloning objects
~~~~~~~~~~~~~~~

You can create an *unstored* copy of an existing object by calling the :meth:`clone <.Material.clone>` method. The source object can be either stored or unstored.

.. doctest::

    >>> material_copy = material.clone()
    >>> material_copy
    <Material with id ''>
    >>> material_copy.density.rho
    8000.0

This can also be used to copy an object between models, even if the models are on different ACP servers.

.. doctest::

    >>> acp2 = pyacp.launch_acp()

.. testcode::
    :hide:

    path = acp2.upload_file("../tests/data/minimal_complete_model.acph5")

.. doctest::

    >>> # path = ... # path to another model file
    >>> model2 = acp2.import_model(path=path)
    >>> material_copy.store(parent=model2)
    >>> material_copy
    <Material with id 'Another Material'>

Performance considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~

When building up ACP models, performance can vary depending on whether objects are stored or unstored. In general, it is best to first build up an unstored object, and then store its finished form. This is because otherwise each change to the object is sent to the server, which can be slow depending on the network connection.

However, this doesn't mean that you necessarily need to use the ``store`` method. It is just as efficient to use the ``create_*`` methods, and simply pass all the defining properties at once.
