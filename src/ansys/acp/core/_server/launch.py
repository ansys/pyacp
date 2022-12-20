from typing import Optional

from ansys.tools.local_product_launcher.interface import LAUNCHER_CONFIG_T
from ansys.tools.local_product_launcher.launch import launch_product

from .common import LaunchMode, ServerProtocol

__all__ = ["launch_acp"]


def launch_acp(
    config: Optional[LAUNCHER_CONFIG_T] = None,
    launch_mode: Optional[LaunchMode] = None,
) -> ServerProtocol:
    """Launch a local ACP server.

    Launch the ``acp_grpcserver`` executable on the local machine.

    Parameters
    ----------
    config :
        The configuration used for launching ACP. If unspecified, the
        default for the given launch mode is used.
    launch_mode :
        Specifies which ACP launcher is used. One of ``direct``, ``docker``,
        or ``docker_compose``. If unspecified, the configured default is
        used.

    Returns
    -------
    :
        Server object which can be used to control the server, and
        instantiate objects on the server.
    """
    # TODO: implement remote (PIM) launch if it is configured
    return launch_product(product_name="ACP", config=config, launch_mode=launch_mode)
