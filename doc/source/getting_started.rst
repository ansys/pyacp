.. _getting_started:

Getting started
---------------

Prerequisites
^^^^^^^^^^^^^

To use PyACP, you need the following prerequisites:

- Ansys Composite PrepPost (ACP), version 2024 R2 or later.
- Python, version 3.10, 3.11 or 3.12.

Installation
^^^^^^^^^^^^

To install PyACP, run the following command:

.. code-block:: bash

    pip install ansys-acp-core[all]

You should use a `virtual environment <https://docs.python.org/3/library/venv.html>`_,
because it keeps Python packages isolated from your system Python.

Usage
^^^^^

Tutorial setup
~~~~~~~~~~~~~~

Start a python interpreter and import the required PyACP packages:

.. testcode::

    import ansys.acp.core as pyacp
    from ansys.acp.core.extras import (
        ExampleKeys,
        get_example_file,
    )  # This is only required for the tutorial

To not pollute the filesystem, create a temporary directory for the example files:

.. testcode::

    import tempfile
    import pathlib

    tempdir = tempfile.TemporaryDirectory()
    WORKING_DIR = pathlib.Path(tempdir.name)

Download the example files by using the provided helper function as:

.. testcode::

    plate_acph5_path = get_example_file(ExampleKeys.MINIMAL_PLATE_ACPH5, WORKING_DIR)
    plate_cdb_path = get_example_file(ExampleKeys.MINIMAL_PLATE_CDB, WORKING_DIR)

Start ACP
~~~~~~~~~

Next, start an ACP instance:

.. testcode::

    acp = pyacp.launch_acp()

This launches ACP in the background and creates a connection to it. You can interact
with this ACP instance using the PyACP API.

.. note::

    It's not possible to connect to the ACP GUI with PyACP.

Load a model
~~~~~~~~~~~~

You can resume a model from an existing ACP DB (ACPH5) or built it from
scratch by importing an FE model (mesh). The example uses the path to the model
returned by the ``get_example_file`` function, but a raw path like
``r"path\to\your\model.acph5"`` can also be used.

To load an existing ACP layup model with PyACP, use the :meth:`.import_model` method:

.. testcode::

    plate_acph5_model = acp.import_model(plate_acph5_path)

To import an FE model, use the ``format="ansys:cdb"`` or ``format="ansys:dat"``
parameter, respectively.
The following example imports a CDB file.

.. testcode::

    plate_cdb_model = acp.import_model(
        plate_cdb_path,
        format="ansys:cdb",
        unit_system=pyacp.UnitSystemType.MPA,
    )

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

Once loaded, you can modify the object directly, for example you can assigning a name to a material with:

.. testcode::

    plate_cdb_model.materials["2"].name = "Carbon Woven"

Start defining new objects in the model. For example, to create a ply and all its dependencies:

.. testcode::

    fabric = plate_cdb_model.create_fabric(name="Carbon Woven 0.2mm", thickness=0.2)
    oss = plate_cdb_model.create_oriented_selection_set(
        name="OSS",
        orientation_direction=(-0.0, 1.0, 0.0),
        element_sets=[plate_cdb_model.element_sets["All_Elements"]],
        rosettes=[plate_cdb_model.rosettes["12"]],
    )
    modeling_group = plate_cdb_model.create_modeling_group(name="Modeling Group 1")
    modeling_ply = modeling_group.create_modeling_ply(name="Ply 1", ply_angle=10.0)

These ``create_*`` methods take additional parameters, which can be used to immediately set the properties of the new object.
For example, refer to the documentation of :meth:`create_modeling_ply <.ModelingGroup.create_modeling_ply>`.

Alternatively, you can always set the properties of an object after it has been created:

.. testcode::

    fabric.material = plate_cdb_model.materials["Carbon Woven"]
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

    plate_cdb_model.update()

Many PyACP objects provide data which can be plotted. For example, to show the mesh:

.. testcode::

    plate_cdb_model.mesh.to_pyvista().plot(show_edges=True)

Or to show the thickness of a modeling ply or fiber directions:

.. testcode::

    modeling_ply.elemental_data.thickness.get_pyvista_mesh(mesh=plate_cdb_model.mesh).plot()
    plotter = pyacp.get_directions_plotter(
        model=plate_cdb_model, components=[modeling_ply.elemental_data.fiber_direction]
    )
    plotter.show()

The model can also be opened in the ACP GUI. See :ref:`view_the_model_in_the_acp_gui`.


Continue exploring
~~~~~~~~~~~~~~~~~~

This is just a brief introduction to PyACP. To learn more:

- Check out the :ref:`examples <ref_examples>` to see complete examples of how to use PyACP.
- The :ref:`how-to guides <howto>` provide instructions on how to perform specific tasks.
- The :ref:`API reference <api_reference>` provides detailed information on all available classes and methods.
