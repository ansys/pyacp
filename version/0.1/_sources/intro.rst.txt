.. _getting_started:

Getting started
---------------

Installation
^^^^^^^^^^^^

PyACP supports Ansys 2024 R2 and later. To install PyACP, run the following command:

.. code-block:: bash

    pip install ansys-acp-core[all]

You should use a `virtual environment <https://docs.python.org/3/library/venv.html>`_,
because it keeps Python packages isolated from your system Python.

Usage
^^^^^

Start ACP
~~~~~~~~~

Start a Python interpreter and import the PyACP package:

.. testcode::
    :hide:

    import tempfile
    import shutil
    import pathlib
    import os

    workdir_doctest = tempfile.TemporaryDirectory()
    DATA_DIRECTORY = pathlib.Path(workdir_doctest.name)
    _ = shutil.copyfile(
        "../tests/data/minimal_complete_model_no_matml_link.acph5",
        DATA_DIRECTORY / "model.acph5",
    )
    _ = shutil.copyfile("../tests/data/minimal_model_2.cdb", DATA_DIRECTORY / "model.cdb")
    old_cwd = os.getcwd()
    os.chdir(DATA_DIRECTORY)

.. testcode::

    import ansys.acp.core as pyacp

Next, start an ACP instance:

.. testcode::

    acp = pyacp.launch_acp()

Get a model
~~~~~~~~~~~

You can resume a model from an existing ACP DB (ACPH5) or built it from
scratch by importing an FE model (mesh).

To load an existing model with PyACP, use the :meth:`.import_model` method:

.. testcode::

    model = acp.import_model("model.acph5")

To import an FE model, use the ``format="ansys:cdb"`` or ``format="ansys:dat"``
parameter, respectively.
The following example imports a CDB file.

.. testcode::

    model = acp.import_model(
        "model.cdb",
        format="ansys:cdb",
        unit_system=pyacp.UnitSystemType.MPA,
    )

.. testcode::
    :hide:

    model.materials["2"].name = "Carbon Woven"

See :class:`.FeFormat` for a list of supported FE formats. Check out the
:ref:`input_file_for_pyacp` section to see how input files can be created.

.. danger::
    When working on Windows, be careful of backslashes in paths: These may correspond to
    `escape sequences <https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences>`_, resulting in errors.
    To avoid issues, make sure to quote the backslashes (by using ``\\``) or use a 
    `raw string literal <https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals>`_ by prefixing your string with **r**,
    like ``model = acp.import_model(r"path\to\your\model.acph5")``.


Start modelling
~~~~~~~~~~~~~~~

Start defining new objects in the model. For example, to create a ply and all its dependencies:

.. testcode::

    fabric = model.create_fabric(name="Carbon Woven 0.2mm", thickness=0.2)
    oss = model.create_oriented_selection_set(
        name="OSS",
        orientation_direction=(-0.0, 1.0, 0.0),
        element_sets=[model.element_sets["All_Elements"]],
        rosettes=[model.rosettes["12"]],
    )
    modeling_group = model.create_modeling_group(name="Modeling Group 1")
    modeling_ply = modeling_group.create_modeling_ply(name="Ply 1", ply_angle=10.0)

These ``create_*`` methods take additional parameters, which can be used to immediately set the properties of the new object.
For example, refer to the documentation of :meth:`create_modeling_ply <.ModelingGroup.create_modeling_ply>`.

Alternatively, you can always set the properties of an object after it has been created:

.. testcode::

    fabric.material = model.materials["Carbon Woven"]
    modeling_ply.ply_material = fabric
    modeling_ply.oriented_selection_sets = [oss]

.. hint::

    When using PyACP from an IDE, you can use autocompletion to explore the available methods and properties. PyACP provides type hints to make the autocompletion as helpful as possible.

Update and plot the model
~~~~~~~~~~~~~~~~~~~~~~~~~

The lay-up is not automatically updated. So data such as ply thicknesses
and fiber directions are only available after updating the model.
To perform the update, use the :meth:`update <.Model.update>` method:

.. testcode::

    model.update()

Many PyACP objects provide data which can be plotted. For example, to show the mesh:

.. testcode::

    model.mesh.to_pyvista().plot()

Or to show the thickness of a modeling ply or fiber directions:

.. testcode::

    modeling_ply.elemental_data.thickness.get_pyvista_mesh(mesh=model.mesh).plot()
    plotter = pyacp.get_directions_plotter(
        model=model, components=[modeling_ply.elemental_data.reference_direction]
    )
    plotter.show()

The model can also be opened in the ACP GUI. See :ref:`view_the_model_in_the_acp_gui`.


Continue exploring
~~~~~~~~~~~~~~~~~~

This is just a brief introduction to PyACP. To learn more:

- Check out the :ref:`examples <ref_examples>` to see complete examples of how to use PyACP.
- The :ref:`how-to guides <howto>` provide instructions on how to perform specific tasks.
- The :ref:`API reference <api_reference>` provides detailed information on all available classes and methods.

.. testcode::
    :hide:

    os.chdir(old_cwd)
