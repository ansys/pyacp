Managing input and output files
-------------------------------

When defining your workflow using PyACP and other tools, you may need control
over where input and output files are stored. This guide will show you different
ways to achieve this.

For now, let's assume the ACP instance is launched on a remote server. The
final section :ref:`local_vs_remote` will discuss the differences between local and
remote ACP instances in terms of file management.

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
manages the most common use case, using predetermined output file names.

Loading input files
~~~~~~~~~~~~~~~~~~~

To get started, you must define a workflow. This can be done using either an
FE model (``.cdb`` or ``.dat``) file, or an ACP model (``.acph5``) file.

Let us assume you have a directory ``DATA_DIRECTORY`` containing a file ``input_file.cdb``.

.. doctest::

    >>> DATA_DIRECTORY
    PosixPath('...')
    >>> list(DATA_DIRECTORY.iterdir())
    [PosixPath('.../input_file.cdb')]

To create an :class:`.ACPWorkflow` instance for working with this file, use the
:meth:`.ACPWorkflow.from_cdb_or_dat_file` method as follows:

.. doctest::

    >>> workflow = pyacp.ACPWorkflow.from_cdb_or_dat_file(
    ...     acp=acp,
    ...     cdb_or_dat_file_path=DATA_DIRECTORY / "input_file.cdb",
    ...     unit_system=pyacp.UnitSystemType.MPA,
    ... )

This uploads the file the ACP instance and creates a new model from it. The
newly created model is accessible as ``workflow.model``:

.. doctest::

    >>> workflow.model
    <Model with name 'ACP Lay-up Model'>

Getting output files
~~~~~~~~~~~~~~~~~~~~

The ``get_local_*`` methods of the workflow can be used to create and download
output files. For example, to get the ``.acph5`` file of the model, use the
:meth:`.get_local_acph5_file` method:

.. doctest::

    >>> model = workflow.model
    >>> model.name = "My model"
    >>> workflow.get_local_acph5_file()
    PosixPath('/tmp/.../My model.acph5')

Note that the file name is based on the model name.

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

Now the output files will be stored in the custom working directory. Input files
are also copied to this directory before being uploaded to the ACP instance.


Manual file management
''''''''''''''''''''''

To get more control over where files are stored, you can manually upload and
download files to the server, and specify the file names.

Loading input files
~~~~~~~~~~~~~~~~~~~

If you again want to load the file ``input_file.cdb`` into the ACP instance, you
can use the :meth:`.upload_file` method of the ACP instance:

.. doctest::

    >>> uploaded_path = acp.upload_file(DATA_DIRECTORY / "input_file.cdb")
    >>> uploaded_path
    PurePosixPath('input_file.cdb')

This method returns the path of the uploaded file on the server. This path can
be used to create a new model:

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

To get the ``.acph5`` file, we first need to store it on the server. This is done
using the :meth:`.save` method of the model:

.. doctest::

    >>> model.save("output_file.acph5")

This file can then be downloaded using the :meth:`.download_file` method of the ACP
instance:

.. doctest::

    >>> acp.download_file(
    ...     remote_filename="output_file.acph5", local_path="output_file_downloaded.acph5"
    ... )


.. _local_vs_remote:

Local vs remote ACP instance
''''''''''''''''''''''''''''

In the preceding examples, we have assumed that ACP runs on a remote server. However,
you can also launch ACP as a process on your local machine. Refer to the :ref:`launch_configuration` guide
for details on how to do this.

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