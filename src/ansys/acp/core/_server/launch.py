# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

import os

from packaging import version

from ansys.tools.local_product_launcher.config import get_launch_mode_for
from ansys.tools.local_product_launcher.interface import FALLBACK_LAUNCH_MODE_NAME
from ansys.tools.local_product_launcher.launch import launch_product

from .acp_instance import (
    ACPInstance,
    FileTransferHandler,
    FileTransferStrategy,
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
    auto_transfer_files: bool = True,
) -> ACPInstance[ControllableServerProtocol]:
    """Launch an ACP instance.

    Launch the ACP gRPC server with the given configuration. If no
    configuration is provided, the configured default is used.

    .. warning::

        Do not execute this function with untrusted input parameters.
        See the :ref:`security guide<security_launch_acp>` for details.

    Parameters
    ----------
    config :
        The configuration used for launching ACP. If unspecified, the
        default for the given launch mode is used.
    launch_mode :
        Specifies which ACP launcher is used. One of ``direct``,
        ``docker_compose``, or ``connect``. If unspecified, the
        configured default is used. If no default is configured,
        ``direct`` is used.
    timeout :
        Timeout to wait until ACP responds. If ``None`` is specified,
        the check that ACP has started is skipped.
    auto_transfer_files :
        Determines whether input and output files are automatically
        transferred (up- or downloaded) to the server. If ``True``,
        files are automatically transferred, and all paths in the
        import or export methods are *local* paths. If ``False``,
        file transfer needs to be handled manually, and the paths
        are relative to the server working directory.
        If the ``launch_mode`` is ``"direct"``, this only has an
        effect if the current working directory is changed after
        launching the server.

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
    # The fallback launch mode for ACP is the direct launch mode.
    if launch_mode_evaluated in (LaunchMode.DIRECT, FALLBACK_LAUNCH_MODE_NAME):
        filetransfer_strategy: FileTransferStrategy = LocalFileTransferStrategy(os.getcwd())
        is_remote = False
    elif launch_mode_evaluated in (LaunchMode.DOCKER_COMPOSE, LaunchMode.CONNECT):
        filetransfer_strategy = RemoteFileTransferStrategy(
            channel=server_instance.channels[ServerKey.FILE_TRANSFER],
        )
        is_remote = True
    else:
        raise ValueError("Invalid launch mode for ACP: " + str(launch_mode_evaluated))

    acp = ACPInstance(
        server=server_instance,
        filetransfer_handler=FileTransferHandler(
            filetransfer_strategy, auto_transfer_files=auto_transfer_files
        ),
        channel=server_instance.channels[ServerKey.MAIN],
        is_remote=is_remote,
    )
    if timeout is not None:
        acp._server.wait(timeout=timeout)
        # We can only check the server version after the server has started;
        # if the timeout is set to 'None', we skip this check.
        MIN_VERSION = "24.2"
        if version.parse(acp.server_version) < version.parse(MIN_VERSION):
            raise RuntimeError(
                f"ACP version {acp.server_version} is not supported. "
                f"Please use ACP version {MIN_VERSION} or later."
            )
    return acp
