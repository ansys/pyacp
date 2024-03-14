Manage input and output files
-------------------------------

When defining your workflow using PyACP and other tools, you may need control
over where the input and output files are stored. This guide shows you two
ways to manage them.

In the following examples, the ACP instance is launched on a remote server. The
differences between local and remote ACP instances, in terms of file management,
are explained afterwards in the :ref:`local_vs_remote` section.

.. doctest::
    :hide:

    >>> import os
    >>> import pathlib
    >>> import shutil
    >>> import tempfile
    >>> workdir_doctest = tempfile.TemporaryDirectory()
    >>> DATA_DIRECTORY = pathlib.Path(workdir_doctest.name)
    >>> _ = shutil.copyfile(
    ...     "../tests/data/minimal_model_2.cdb", DATA_DIRECTORY / "input_file.cdb"
    ... )
    >>> old_cwd = os.getcwd()
    >>> doctest_tempdir = tempfile.TemporaryDirectory()
    >>> os.chdir(doctest_tempdir.name)


.. doctest::

    >>> import ansys.acp.core as pyacp
    >>> acp = pyacp.launch_acp()


Using a predefined workflow
'''''''''''''''''''''''''''

The simplest way to manage files is by using the :class:`.ACPWorkflow` class. This class
manages the use of predetermined output filenames, which is the most common use case.

Loading input files
~~~~~~~~~~~~~~~~~~~

To get started with loading input files, you must define a workflow using either an
FE model (``.cdb`` or ``.dat``) file or an ACP model (``.acph5``) file.

In the following example, assume you have a directory ``DATA_DIRECTORY`` containing a ``input_file.cdb`` file.

.. doctest::

    >>> DATA_DIRECTORY
    PosixPath('...')
    >>> list(DATA_DIRECTORY.iterdir())
    [PosixPath('.../input_file.cdb')]

Create an :class:`.ACPWorkflow` instance that works with this file using 
the :meth:`.ACPWorkflow.from_cdb_or_dat_file` method:

.. doctest::

    >>> workflow = pyacp.ACPWorkflow.from_cdb_or_dat_file(
    ...     acp=acp,
    ...     cdb_or_dat_file_path=DATA_DIRECTORY / "input_file.cdb",
    ...     unit_system=pyacp.UnitSystemType.MPA,
    ... )

That uploads the file to the ACP instance and creates a new model from it. You
can access the newly created model using ``workflow.model``:

.. doctest::

    >>> workflow.model
    <Model with name 'ACP Lay-up Model'>

Getting output files
~~~~~~~~~~~~~~~~~~~~

Use the workflow's ``get_local_*`` methods to create and download
output files. For example, to get the ``.acph5`` file of the model, use the
:meth:`.get_local_acph5_file` method:

.. doctest::

    >>> model = workflow.model
    >>> model.name = "My model"
    >>> workflow.get_local_acph5_file()
    PosixPath('/tmp/.../My model.acph5')

Note that the filename is based on the model name.

Using a custom working directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the output files are stored in a temporary directory. You can
specify a custom working directory using the ``local_working_directory`` argument of
the :class:`.ACPWorkflow` constructor:

.. doctest::

    >>> workflow = pyacp.ACPWorkflow.from_cdb_or_dat_file(
    ...     acp=acp,
    ...     cdb_or_dat_file_path=DATA_DIRECTORY / "input_file.cdb",
    ...     unit_system=pyacp.UnitSystemType.MPA,
    ...     local_working_directory=pathlib.Path("."),
    ... )

Any produced output files are now stored in the custom working directory. Input files
are also copied to this directory before being uploaded to the ACP instance.


Manual file management
''''''''''''''''''''''

To get more control over where files are stored, you can manually upload and
download them to the server, and specify their names.

Loading input files
~~~~~~~~~~~~~~~~~~~

You can manually load the file ``input_file.cdb`` to the ACP instance by
using the :meth:`.upload_file` method:

.. doctest::

    >>> uploaded_path = acp.upload_file(DATA_DIRECTORY / "input_file.cdb")
    >>> uploaded_path
    PurePosixPath('input_file.cdb')

This method returns the path of the uploaded file on the server. You can
use the path to create a new model:

.. doctest::

    >>> model = acp.import_model(
    ...     path=uploaded_path,
    ...     format="ansys:cdb",
    ...     unit_system=pyacp.UnitSystemType.MPA,
    ... )
    >>> model
    <Model with name 'ACP Lay-up Model'>

Getting output files
~~~~~~~~~~~~~~~~~~~~

To get the ``.acph5`` file, it needs to be stored on the server. You can
manually do that using the model's :meth:`.save` method:

.. doctest::

    >>> model.save("output_file.acph5")

Then, you can download the file using the :meth:`.download_file` method of the ACP
instance:

.. doctest::

    >>> acp.download_file(
    ...     remote_filename="output_file.acph5", local_path="output_file_downloaded.acph5"
    ... )


.. _local_vs_remote:

Local versus remote ACP instance
''''''''''''''''''''''''''''

In the preceding examples, ACP ran on a remote server. However,
you can also launch ACP as a process on your local machine. For information on launching
ACP locally, see the :ref:`launch_configuration` guide.

When the ACP instance is local, you can use the same code described previously. However,
the effects are slightly different:

When using the workflow
~~~~~~~~~~~~~~~~~~~~~~~

- The input file is still copied to the ``local_working_directory``, but then loaded directly
  into the ACP instance. There is no separate upload step.
- The output files are directly stored in the ``local_working_directory``.


When using manual upload and download
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The :meth:`.upload_file` method has no effect, and simply returns the input file path.
- The :meth:`.download_file` method copies the file to the specified ``local_path``, unless
  ``remote_filename`` and ``local_path`` are the same. In that case, nothing is done.

.. hint::

    Even when they have no effect, it is good practice to include the upload and download
    steps in your code. In this way, the same code can be used for both local and remote ACP
    instances.


.. doctest::
    :hide:

    >>> os.chdir(old_cwd)
