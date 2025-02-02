.. _file_management:

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
over where the input and output files are stored. There are two main ways to
manage files: auto-transfer mode and manual file management.

.. note::

    When using a local ACP instance (``"direct"`` launch mode), the auto-transfer
    and manual modes are identical, as long as the current working directory is
    not changed after launching the ACP instance.

Auto-transfer mode
------------------

When passing the ``auto_transfer_files=True`` parameter to :func:`.launch_acp`
(the default behavior), PyACP automatically uploads files to the ACP instance
and downloads output files to the local machine.

Paths passed to the PyACP functions are all paths on the local machine. They
can be either absolute paths, or relative to the current working directory of
the Python instance.

The only exception is the ``external_path`` attribute of the :class:`.CADGeometry`
and :class:`.ImportedSolidModel` classes. This attribute refers to a path on the
server side. It can again be an absolute path, or relative to the ACP instance's
working directory.
You can instead use the :meth:`.CADGeometry.refresh` and
:meth:`.ImportedSolidModel.refresh` methods to define the input file, which also
handles the upload automatically.

.. note::

    On local ACP instances, the up- and download methods simply convert the
    paths to be relative to the ACP instance's working directory if needed.


Loading input files
~~~~~~~~~~~~~~~~~~~

To load an input file, pass its path on your local machine to the
:meth:`.import_model` method:

.. doctest::

    >>> import ansys.acp.core as pyacp
    >>> acp = pyacp.launch_acp()
    >>> # DATA_DIRECTORY is a directory containing the input file
    >>> model = acp.import_model(
    ...     DATA_DIRECTORY / "input_file.cdb",
    ...     format="ansys:cdb",
    ...     unit_system=pyacp.UnitSystemType.MPA,
    ... )
    >>> model
    <Model with name 'ACP Lay-up Model'>

Getting output files
~~~~~~~~~~~~~~~~~~~~

When getting output files, pass the desired path on your local machine to the
export / save method.

.. doctest::

    >>> import os
    >>> model.save("output_file.acph5")
    >>> "output_file.acph5" in os.listdir()
    True


Manual file management
----------------------

When passing ``auto_transfer_files=False`` to :func:`.launch_acp`, PyACP does not
automatically upload or download files.

In this case, you need to manually manage the up- and download of files, as
described in the following sections.

Loading input files
~~~~~~~~~~~~~~~~~~~

You can manually load the ``input_file.cdb`` file to the ACP instance by
using the :meth:`.upload_file` method:

.. doctest::

    >>> acp = pyacp.launch_acp(auto_transfer_files=False)
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
    :hide:

    >>> # need to delete the file since it was created in the previous example
    >>> pathlib.Path("output_file.acph5").unlink(missing_ok=True)

.. doctest::

    >>> model.save("output_file.acph5")
    >>> "output_file.acph5" in os.listdir()
    False

Then, you can download the file using the :meth:`.download_file` method of the ACP
instance:

.. doctest::

    >>> acp.download_file(
    ...     remote_path="output_file.acph5",
    ...     local_path="output_file_downloaded.acph5",
    ... )
    >>> "output_file_downloaded.acph5" in os.listdir()
    True

.. doctest::
    :hide:

    >>> os.chdir(old_cwd)
