.. _launch_configuration:

Change ACP startup

By default, the :func:`.launch_acp` function will start ACP from the unified installer, using the latest available version.

Change the default launch configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To change this behavior, you can use the ``ansys-launcher`` command line tool to configure how ACP is started.

.. note::

    The virtual environment in which PyACP is installed must be activated before running the ``ansys-launcher`` command.

    On Windows, the executable may be called ``ansys-launcher.exe``.

.. code-block:: bash

    $ ansys-launcher configure ACP
    Usage: ansys-launcher configure ACP [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      connect
      connect_local
      direct
      docker_compose

As indicated in the preceding output, three methods are available for starting ACP:

- ``direct`` (default): Start ACP directly by providing the path to the ``acp_grpcserver`` executable.
- ``docker_compose``: Start ACP using Docker Compose.
- ``connect``: Connect to an already running ACP server (with file transfer).
- ``connect_local``: Connect to an already running ACP server (without file transfer).

.. hint::

    Except for advanced use cases, the recommended launch mode is ``direct``.

You may configure any of the three methods with the ``ansys-launcher`` tool. For example, to use the
``direct`` method, run the following command:

.. code-block:: bash

    ansys-launcher configure ACP direct

The tool prompts you for the required information, providing the default value
in square brackets. You can accept the default value by pressing the **Enter** key or input a
new value by typing it and then pressing the **Enter** key.

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

    transport_mode:
        Specifies the gRPC transport mode to use. Possible values: 'uds' (default), 'mtls', 'insecure'.

    uds_dir:
        Directory path for UDS socket files (default: ~/.conn). Only used if transport_mode is 'uds'.
    [default]:

    certs_dir:
        Directory path for mTLS certificate files. Only used if transport_mode is 'mtls'.
    [default]:

    Overwrite default launch mode for ACP (currently set to 'docker_compose')? [y/N]: Y

    Updated ~/.config/ansys_tools_local_product_launcher/config.json

The new configuration is used by the :func:`.launch_acp` function. Note that you
may have to restart your Python session for the changes to take effect.

Choose the launch mode at runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To switch between the launch modes, you can specify the ``launch_mode`` argument
when calling the :func:`.launch_acp` function. Note that the selected launch mode must already
be configured with the ``ansys-launcher`` tool.

.. testcode::

    import ansys.acp.core as pyacp

    acp = pyacp.launch_acp(launch_mode="docker_compose")

You may use the ``config`` parameter to fully customize the launch of ACP at runtime.
This parameter expects a configuration object matching the selected ``launch_mode``:

- :class:`.DirectLaunchConfig` for the ``direct`` launch mode.
- :class:`.DockerComposeLaunchConfig` for the ``docker_compose`` launch mode.
- :class:`.ConnectLaunchConfig` for the ``connect`` launch mode.
- :class:`.ConnectLocalLaunchConfig` for the ``connect_local`` launch mode.

.. testcode::

    import os
    import ansys.acp.core as pyacp

    acp = pyacp.launch_acp(
        config=pyacp.DockerComposeLaunchConfig(
            image_name_acp="ghcr.io/ansys/acp:latest",
            image_name_filetransfer="ghcr.io/ansys/tools-filetransfer:latest",
            keep_volume=True,
            license_server=f"1055@{os.environ['LICENSE_SERVER']}",
        ),
        launch_mode="docker_compose",
    )

.. _launch_configuration_transport_mode:

Change the gRPC transport mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, PyACP chooses a secure gRPC transport mode to communicate with the ACP server, based
on the selected ``launch_mode`` and the operating system.
If needed, each ``launch_mode`` configuration provides additional parameters for controlling the
transport mode.

The following example shows how to use mutual TLS (mTLS) as the transport mode when using the
``direct`` launch mode:

.. code::

    import ansys.acp.core as pyacp

    acp = pyacp.launch_acp(
        config=pyacp.DirectLaunchConfig(
            binary_path="/usr/ansys_inc/v261/ACP/acp_grpcserver",
            transport_mode="mtls",
            certs_dir="/path/to/certificates",
        ),
        launch_mode="direct",
    )

In general, the following transport modes are available:

- **UDS (Unix Domain Sockets):**

  Recommended for local connections on Unix systems. A file-based socket is created for communication
  between the client and server. The socket file is created in the ``$HOME/.conn`` directory by default
  but can be customized using the ``uds_dir`` parameter.

  Access permissions to the socket file determine which users can connect to the server.

- **WNUA (Windows Named User Authentication):**

  Recommended for local connections on Windows systems. The gRPC server checks that the user making the
  connection is the same as the user who started the server. No additional configuration is required.

- **mTLS (Mutual TLS):**

  Recommended for secure remote connections.
  mTLS uses the TLS protocol to encrypt communication between client and server and requires that both
  the server and client have the appropriate certificates configured. By default, these certificates
  are searched in the ``certs`` directory within the working directory from which the ACP instance is
  launched. You can change this path by setting the environment variable ``ANSYS_GRPC_CERTIFICATES``, or
  passing the ``certs_dir`` option.

  The server expects the following files in the certificate directory:

  - ``server.key``: Contains the private key corresponding to the public key in ``server.crt``.
  - ``server.crt``: Contains the public certificate for your server.
  - ``ca.crt``: Contains the public certificate of the Certificate Authority (CA) that issued (signed) ``client.crt``.

  The client expects the following files in the certificate directory:

  - ``client.key``: Contains the private key corresponding to the public key in ``client.crt``.
  - ``client.crt``: Contains the public certificate for your client.
  - ``ca.crt``: Contains the public certificate of the Certificate Authority (CA) that issued (signed) ``server.crt``.

  Contact your IT department regarding certificate setup on your client and server.

- **INSECURE (not recommended):**

  Not recommended. Communication between client and server is not encrypted. Any user on the machine
  can potentially intercept and read the data being transmitted. If the ``allow_remote_host`` option
  is used, any user on the network may be able to connect to the server without authentication.

Refer to the API documentation for each launch mode configuration class for details on how to set the transport options:

- :class:`.DirectLaunchConfig` for the ``direct`` launch mode.
- :class:`.DockerComposeLaunchConfig` for the ``docker_compose`` launch mode.
- :class:`.ConnectLaunchConfig` for the ``connect`` launch mode.
- :class:`.ConnectLocalLaunchConfig` for the ``connect_local`` launch mode.

The following table shows which ``transport_mode`` options are compatible with each ``launch_mode``.

Legend: ✔️ = Supported, ❌ = Not supported

.. list-table::
    :header-rows: 1

    * - ``launch_mode``
      - UDS (Unix only)
      - WNUA (Windows only)
      - mTLS
      - INSECURE (not recommended)
    * - ``direct``
      - ✔️ (Unix default)
      - ✔️ (Windows default)
      - ✔️
      - ✔️
    * - ``docker_compose``
      - ❌
      - ❌
      - ✔️ (default)
      - ✔️
    * - ``connect``
      - ✔️
      - ✔️
      - ✔️ (default)
      - ✔️
    * - ``connect_local``
      - ✔️
      - ✔️
      - ✔️ (default)
      - ✔️
