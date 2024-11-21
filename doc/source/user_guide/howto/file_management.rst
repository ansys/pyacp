Manage input and output files
=============================

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

When defining your workflow using PyACP and other tools, you may need control
over where the input and output files are stored.

Local ACP instance
------------------

When running PyACP with a local instance (``"direct"`` launch mode, see
:ref:`launch_configuration`), file paths are relative to the current working
directory.
If you need to keep all files in a specific directory, you can use the
Python facilities for managing file paths. For example, you can use
the :class:`tempfile.TemporaryDirectory` class to create a temporary directory,
and :class:`pathlib.Path` to manage file paths.

The following example:
- creates a temporary directory
- copies an input file to it
- creates an ACP model from the input file
- saves the model to an output file

Note that the temporary directory and its contents are deleted when the
Python session ends. You can also specify a custom directory to store the
files permanently.

.. doctest::

    >>> import pathlib
    >>> import shutil
    >>> import tempfile
    >>> import ansys.acp.core as pyacp
    >>> workdir = tempfile.TemporaryDirectory()
    >>> workdir_path = pathlib.Path(workdir.name)
    >>> # DATA_DIRECTORY is a directory containing the input file
    >>> shutil.copyfile(DATA_DIRECTORY / "input_file.cdb", workdir_path / "input_file.cdb")
    >>> acp = pyacp.launch_acp()
    >>> model = acp.import_model(
    ...     workdir_path / "input_file.cdb",
    ...     "ansys:cdb",
    ...     format="ansys:cdb",
    ...     unit_system=pyacp.UnitSystemType.MPA,
    ... )
    >>> model
    <Model with name 'ACP Lay-up Model'>
    >>> # edit the model
    >>> model.save(workdir_path / "output_file.acph5")


Remote ACP instance
-------------------

When running PyACP with a remote instance (``"docker_compose"`` or ``"connect"``
launch mode), there are two ways to manage files: auto-upload mode and manual
file management.

Auto-upload mode
'''''''''''''''''

When passing the ``auto_upload_files=True`` parameter to :func:`.launch_acp`
(the default behavior), PyACP automatically uploads files to the ACP instance
and downloads output files to the local machine.
Paths passed to the PyACP functions are again relative to the current working
directory on the local machine.

Using auto-upload mode, you can use the same code as for local ACP instances,
with one exception:

The ``external_path`` attribute of the :class:`.CADGeometry` and
:class:`.ImportedSolidModel` classes is always relative to the ACP instance's
working directory.
When setting the ``external_path`` attribute, you must manually call the :meth:`.upload_file`
method to upload the file to the ACP instance.

Manual file management
''''''''''''''''''''''

When passing ``auto_upload_files=False`` to :func:`.launch_acp`, PyACP does not
automatically upload or download files.

In this case, you need to manually manage the up- and download of files, as
described in the following sections.

Loading input files
~~~~~~~~~~~~~~~~~~~

You can manually load the ``input_file.cdb`` file to the ACP instance by
using the :meth:`.upload_file` method:

.. doctest::

    >>> acp = pyacp.launch_acp(auto_upload_files=False)
    >>> uploaded_path = acp.upload_file(DATA_DIRECTORY / "input_file.cdb")
    >>> uploaded_path
    PurePosixPath('input_file.cdb')

This method returns the path of the uploaded file on the server. You can
use the path to create a model:

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

To get the ACPH5 file, it must be stored on the server. You can
manually do that using the model's :meth:`.save` method:

.. doctest::

    >>> model.save("output_file.acph5")

Then, you can download the file using the :meth:`.download_file` method of the ACP
instance:

.. doctest::

    >>> acp.download_file(
    ...     remote_filename="output_file.acph5",
    ...     local_path=workdir_path / "output_file_downloaded.acph5",
    ... )

.. doctest::
    :hide:

    >>> os.chdir(old_cwd)
