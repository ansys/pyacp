Getting started
---------------

Installation
^^^^^^^^^^^^

PyACP supports Ansys version 2024R2 and later. To install PyACP, run the following command:

.. code-block:: bash

    pip install ansys-acp-core

You should use a `virtual environment <https://docs.python.org/3/library/venv.html>`_,
because it keeps Python packages isolated from your system Python.

Usage
^^^^^

Start ACP
~~~~~~~~~

Start a Python interpreter and import the PyACP package:

.. testcode::

    import ansys.acp.core as pyacp


Next, start an ACP instance:

.. testcode::

    acp = pyacp.launch_acp()

Load a model
~~~~~~~~~~~~

To load a model in ACP, use the :meth:`import_model <.ACP.import_model>` method:

.. testcode::
    :hide:

    import os
    import shutil
    import tempfile

    with tempfile.TemporaryDirectory() as tempdir:
        tmp_file = os.path.join(tempdir, "model.acph5")
        shutil.copy("../tests/data/minimal_complete_model.acph5", tmp_file)
        acp.upload_file(tmp_file)

.. testcode::

    model = acp.import_model(path="model.acph5")

This can be either an existing ACP model (``.acph5`` format) or an FE model.
When an FE model is loaded, the format needs to be specified:

.. testcode::
    :hide:

    with tempfile.TemporaryDirectory() as tempdir:
        tmp_file = os.path.join(tempdir, "model.cdb")
        shutil.copy("../tests/data/minimal_model_2.cdb", tmp_file)
        acp.upload_file(tmp_file)

.. testcode::

    model = acp.import_model(path="model.cdb", format="ansys:cdb")

See :class:`.FeFormat` for a list of supported FE formats. Check out the
`Create Input File  <user_guide/howto/create_input_file>`_ section to see how input files can be created.


Start modelling
~~~~~~~~~~~~~~~

Start defining new objects in the model. For example, to create a new modeling group and modeling ply:

.. testcode::

    modeling_group = model.create_modeling_group(name="Modeling Group 1")
    modeling_ply = modeling_group.create_modeling_ply(name="Ply 1", ply_angle=10.0)

These ``create_*`` methods take additional parameters, which can be used to immediately set the properties of the new object.
For example, refer to the documentation of :meth:`create_modeling_ply <.ModelingGroup.create_modeling_ply>`.

Alternatively, you can always set the properties of an object after it has been created:

.. testcode::

    fabric = model.create_fabric(name="Fabric 1")
    modeling_ply.ply_material = fabric

.. hint::

    When using PyACP from an IDE, you can use autocompletion to explore the available methods and properties. PyACP provides type hints to make the autocompletion as helpful as possible.


Save the model
~~~~~~~~~~~~~~

To save the model, use the :meth:`save <.Model.save>` method:

.. testcode::

    model.save("saved_model.acph5")


Update and plot the model
~~~~~~~~~~~~~~~~~~~~~~~~~

To update the model, use the :meth:`update <.Model.update>` method:

.. doctest::

    >>> model.update()  # Note: our model is still incomplete, so this will raise an error
    Traceback (most recent call last):
    ...
    RuntimeError: Unknown error: No orthotropic material assigned to fabric Fabric 1!


Many PyACP objects provide data which can be plotted. For example, to show the mesh:

.. testcode::

    model.mesh.to_pyvista().plot()


Or to show the thickness of a modeling ply:

.. testcode::

    modeling_ply.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot()


Continue exploring
~~~~~~~~~~~~~~~~~~

This is just a brief introduction to PyACP. To learn more:

- Check out the `examples <examples/index>`_ to see complete examples of how to use PyACP.
- The `how-to guides <howto/index>`_ provide instructions on how to perform specific tasks.
- The `API reference <api/index>`_ provides detailed information on all available classes and methods.
