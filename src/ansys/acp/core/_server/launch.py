from __future__ import annotations

from ansys.tools.local_product_launcher.config import get_launch_mode_for
from ansys.tools.local_product_launcher.launch import launch_product

from .acp_instance import (
    ACP,
    FiletransferStrategy,
    LocalFileTransferStrategy,
    RemoteFileTransferStrategy,
)
from .common import ControllableServerProtocol, LaunchMode, ServerKey
from .direct import DirectLaunchConfig
from .docker_compose import DockerComposeLaunchConfig

__all__ = ["launch_acp"]


def launch_acp(
    config: DirectLaunchConfig | DockerComposeLaunchConfig | None = None,
    launch_mode: LaunchMode | None = None,
    timeout: float | None = 30.0,
) -> ACP[ControllableServerProtocol]:
    """Launch an ACP instance.

    Launch the ACP gRPC server with the given configuration. If no
    configuration is provided, the configured default is used.

    Parameters
    ----------
    config :
        The configuration used for launching ACP. If unspecified, the
        default for the given launch mode is used.
    launch_mode :
        Specifies which ACP launcher is used. One of ``direct`` or
        ``docker_compose``. If unspecified, the configured default is
        used.
    timeout :
        Timeout to wait until ACP responds. If ``None`` is specified,
        the check that ACP has started is skipped.

    Returns
    -------
    :
        ACP instance which can be used to control the server, and
        instantiate objects on the server.
    """
    launch_mode_evaluated = get_launch_mode_for(product_name="ACP", launch_mode=launch_mode)
    server_instance: ControllableServerProtocol = launch_product(
        product_name="ACP", config=config, launch_mode=launch_mode_evaluated
    )
    if launch_mode_evaluated == LaunchMode.DIRECT:
        filetransfer_strategy: FiletransferStrategy = LocalFileTransferStrategy()
        is_remote = False
    elif launch_mode_evaluated == LaunchMode.DOCKER_COMPOSE:
        filetransfer_strategy = RemoteFileTransferStrategy(
            channel=server_instance.channels[ServerKey.FILE_TRANSFER]
        )
        is_remote = True

    else:
        raise ValueError("Invalid launch mode for ACP: " + str(launch_mode_evaluated))

    acp = ACP(
        server=server_instance,
        filetransfer_strategy=filetransfer_strategy,
        channel=server_instance.channels[ServerKey.MAIN],
        is_remote=is_remote,
    )
    if timeout is not None:
        acp._server.wait(timeout=timeout)
    return acp
