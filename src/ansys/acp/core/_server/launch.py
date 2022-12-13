from typing import Optional

from ansys.tools.local_product_launcher.interface import LAUNCHER_CONFIG_T
from ansys.tools.local_product_launcher.launch import launch_product

from .common import LaunchMode, ServerProtocol

__all__ = ["launch_acp"]


def launch_acp(
    # binary_path: _PATH,
    # port: Optional[int] = None,
    # stdout_file: _PATH = os.devnull,
    # stderr_file: _PATH = os.devnull,
    config: Optional[LAUNCHER_CONFIG_T] = None,
    launch_mode: Optional[LaunchMode] = None,
) -> ServerProtocol:
    """Launch a local ACP server.

    Launch the ``acp_grpcserver`` executable on the local machine.

    Parameters
    ----------
    binary_path :
        Path to the ``acp_grpcserver`` executable.
    port :
        Port on which the server should listen to gRPC calls. If no port
        is given, a free port will be chosen automatically.
    stdout_file :
        Path of the file to which the server output is written.
    stderr_file :
        Path of the file to which the server error log is written.

    Returns
    -------
    :
        Server object which can be used to control the server, and
        instantiate objects on the server.
    """
    # TODO: implement remote (PIM) launch if it is configured
    return launch_product(product_name="ACP", config=config, launch_mode=launch_mode)
