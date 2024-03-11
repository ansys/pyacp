.. _launch_configuration:

Change ACP startup
---------------------------

By default, the :func:`.launch_acp` function will start ACP from the unified installer, using the latest available version.

Change the default launch configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To change this behavior, you can use the ``ansys-launcher`` command line tool to configure how ACP is started.

.. note::

    On Windows, the executable may be called ``ansys-launcher.exe``.

.. code-block:: bash

    $ ansys-launcher configure ACP
    Usage: ansys-launcher configure ACP [OPTIONS] COMMAND [ARGS]...

    Options:
    --help  Show this message and exit.

    Commands:
    direct
    docker_compose
    connect

In the preceding output, the three available methods for starting ACP are listed:

- ``direct``: start ACP directly by providing the path to the ``acp_grpcserver`` executable.
- ``docker_compose``: start ACP using Docker Compose.
- ``connect``: connect to an already running ACP server.

Either method can be configured with ``ansys-launcher``. For example, to use the
``direct`` method, you can run ``ansys-launcher configure ACP direct``.
The tool will prompt you for the required information, providing a default value
in square brackets. You can press Enter to accept the default value, or type a
new value and press Enter.

.. code-block:: bash

    $ ansys-launcher configure ACP direct

    binary_path:
        Path to the ACP gRPC server executable.
    [/usr/ansys_inc/v242/ACP/acp_grpcserver]:

    stdout_file:
        File in which the server stdout is stored.
    [/dev/null]:

    stderr_file:
        File in which the server stderr is stored.
    [/dev/null]:

    Overwrite default launch mode for ACP (currently set to 'docker_compose')? [y/N]: Y

    Updated ~/.config/ansys_tools_local_product_launcher/config.json

The new configuration is used by the :func:`.launch_acp` function. Note that you
may have to restart your Python session for the changes to take effect.

Choosing the launch mode at runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To switch between the launch modes, you can specify the ``launch_mode`` argument
when calling :func:`.launch_acp`. Note that the selected launch mode must be
already configured with ``ansys-launcher``.

.. testcode::

    import ansys.acp.core as pyacp

    acp = pyacp.launch_acp(launch_mode="docker_compose")

The ``config`` parameter can be used to fully customize the launch of ACP at runtime.
This parameter expects a configuration object matching the selected ``launch_mode``:

- :class:`.DirectLaunchConfig` for the ``direct`` launch mode.
- :class:`.DockerComposeLaunchConfig` for the ``docker_compose`` launch mode.
- :class:`.ConnectLaunchConfig` for the ``connect`` launch mode.

.. testcode::

    import os
    import ansys.acp.core as pyacp

    acp = pyacp.launch_acp(
        config=pyacp.DockerComposeLaunchConfig(
            image_name_pyacp="ghcr.io/ansys/acp:latest",
            image_name_filetransfer="ghcr.io/ansys/tools-filetransfer:latest",
            keep_volume=True,
            license_server=f"1055@{os.environ['LICENSE_SERVER']}",
        ),
        launch_mode="docker_compose",
    )
