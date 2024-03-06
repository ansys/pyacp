Getting started
---------------

Testing session (to be removed)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The documentation below is still valid for the Ansys internal testing session except Installation.

Installation
~~~~~~~~~~~~

It is recommended to use a `virtual environment <https://docs.python.org/3/library/venv.html>`_,
because it keeps Python packages isolated from your system Python,
and activate it before installing PyACP:

.. code::
    python -m venv C:\pyacp_venv
    C:\pyacp_venv\Scripts\activate

Since the module is not yet public, please install from GitHub:

.. code::
    pip install git+https://github.com/ansys/pyacp.git

.. note::
    Ensure that a recent version of Ansys WB 2024 R2 is installed on your machine before you start using pyACP.

Reporting
~~~~~~~~~

Any kind of feedback (feature requests, API, documentation, bugs etc.) is welcome.
Please add issues on the `GitHub repository <https://github.com/ansys/pyacp/issues>`_.
Or write to us on the
`pyACP Testing channel <https://teams.microsoft.com/l/channel/19%3An30o8gW_b9zH7hJo4gOhTNPCzCPfCjtIy2iJiGH_m701%40thread.tacv2/?groupId=abd72c46-92b0-4bf7-9599-de8b4d52404b&tenantId=>`_.

Installation (not for testing session)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Get a model
~~~~~~~~~~~

A model can be resumed from an existing ACP DB (acph5) file or built from
scratch by importing an FE model (mesh).

To load an existing model with pyACP, use the :meth:`ACPWorkflow.from_acph5_file <.ACP.ACPWorkflow.from_acph5_file>` method:

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

    workflow = pyacp.ACPWorkflow.from_acph5_file(
        acp=acp,
        acph5_file_path="model.acph5",
    )
    model = workflow.model

To import an FE model, use the
:meth:`ACPWorkflow.from_cdb_or_dat_file <.ACP.ACPWorkflow.from_cdb_or_dat_file>` method.
The following example imports a CDB file.

.. testcode::
    :hide:

    with tempfile.TemporaryDirectory() as tempdir:
        tmp_file = os.path.join(tempdir, "model.cdb")
        shutil.copy("../tests/data/minimal_model_2.cdb", tmp_file)
        acp.upload_file(tmp_file)

.. testcode::

    workflow = pyacp.ACPWorkflow.from_cdb_or_dat_file(
        acp=acp,
        cdb_or_dat_file_path="model.cdb",
        unit_system=pyacp.UnitSystemType.MPA,
    )
    model = workflow.model

.. testcode::
    :hide:

    model.materials["2"].name = "Carbon Woven"

See :class:`.FeFormat` for a list of supported FE formats. Check out the
:ref:`input_file_for_pyacp` section to see how input files can be created.


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

- Check out the `examples <examples/index>`_ to see complete examples of how to use PyACP.
- The `how-to guides <howto/index>`_ provide instructions on how to perform specific tasks.
- The `API reference <api/index>`_ provides detailed information on all available classes and methods.
