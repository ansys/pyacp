Security considerations
=======================

This section provides information on security considerations for the use
of PyACP. It is important to understand the capabilities which PyACP
provides, especially when using it to build apps or scripts that accept
untrusted input.

.. _security_launch_acp:

Launching ACP
-------------

The :py:func:`.launch_acp` function has different security implications depending
on the launch mode used:

Direct launch
^^^^^^^^^^^^^

When using the ``"direct"`` launch mode:

- The executable which is launched is configurable either in the function
  parameters, or in the ``ansys-tools-local-product-launcher`` configuration
  file. This may allow an attacker to launch arbitrary executables on the system.
- The standard output and standard error file paths are configurable. This may
  be used to overwrite arbitrary files on the system.

When exposing the ``"direct"`` launch mode to untrusted users, it is important
to validate that the executable path and file paths are safe, or hard-code
them in the app.

Docker compose launch
^^^^^^^^^^^^^^^^^^^^^

The ``"docker_compose"`` launch mode executes the ``docker`` or ``docker-compose``
commands on the system.

This may pose the following risks:

- If the user can override which container is launched, they may be able to
  launch arbitrary containers on the system. This is especially problematic
  if ``docker`` is configured to run with elevated privileges.
- If the user can override the ``docker`` or ``docker-compose`` executable
  in the environment, they may be able to execute arbitrary commands on the
  system.

When exposing the ``"docker_compose"`` launch mode to untrusted users, it is important
to validate that the container being launched, and control the environment the
command is executed in.

Connect launch
^^^^^^^^^^^^^^

The ``"connect"`` launch mode connects to an existing ACP server. This mode does
not pose any particular security risks, besides allowing access to a port on the
system.

.. _security_file_upload_download:

File up- and downloads
----------------------

The :py:meth:`.ACPInstance.upload_file` and :py:meth:`.ACPInstance.download_file` methods create files
on the local or remote machine, without any validation of the file content or path.

When exposing these methods to untrusted users, it is important to validate that
only files that are safe to be uploaded or downloaded are processed.
