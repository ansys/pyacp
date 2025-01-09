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
import pathlib
import shutil
import typing
from typing import Any, Generic, Protocol, TypeVar, cast

import grpc

from ansys.api.acp.v0 import control_pb2_grpc, model_pb2_grpc
from ansys.api.acp.v0.base_pb2 import CollectionPath, DeleteRequest, Empty, ListRequest
from ansys.tools.filetransfer import Client as FileTransferClient

from .._tree_objects._grpc_helpers.exceptions import wrap_grpc_errors
from .._utils.typing_helper import PATH as _PATH
from .common import ServerProtocol

if typing.TYPE_CHECKING:  # pragma: no cover
    from .._tree_objects import Model


__all__ = ["ACPInstance"]


class FileTransferStrategy(Protocol):
    def upload_file(self, local_path: _PATH) -> pathlib.PurePath: ...

    def download_file(self, remote_path: _PATH, local_path: _PATH) -> None: ...

    def to_export_path(self, path: _PATH) -> _PATH: ...


class LocalFileTransferStrategy(FileTransferStrategy):
    def __init__(self, working_directory: _PATH) -> None:
        self._working_directory = pathlib.Path(working_directory)

    def upload_file(self, local_path: _PATH) -> pathlib.Path:
        if not pathlib.Path(local_path).exists():
            raise FileNotFoundError(f"No such file or directory: '{local_path}'")
        return self._get_remote_path(local_path)

    def download_file(self, remote_path: _PATH, local_path: _PATH) -> None:
        remote_path_aslocal = self._get_local_path(remote_path)
        local_filename = pathlib.Path(local_path)
        if local_filename.exists() and local_filename.samefile(remote_path_aslocal):
            return
        shutil.copyfile(remote_path_aslocal, local_path)

    def to_export_path(self, path: _PATH) -> _PATH:
        return self._get_remote_path(path)

    def _get_remote_path(self, path: _PATH) -> pathlib.Path:
        """Get the path in the format understood by the server.

        Convert the path from the format understood by the Python client to
        the format understood by the server.
        """
        return self._get_path_impl(path, pathlib.Path().cwd(), self._working_directory)

    def _get_local_path(self, path: _PATH) -> pathlib.Path:
        """Get the path in the format understood by the Python client.

        Convert the path from the format understood by the server to
        the format understood by the Python client.
        """
        return self._get_path_impl(path, self._working_directory, pathlib.Path().cwd())

    @staticmethod
    def _get_path_impl(
        path: _PATH,
        initial_working_directory: pathlib.Path,
        target_working_directory: pathlib.Path,
    ) -> pathlib.Path:
        path = pathlib.Path(path)
        if path.is_absolute() or initial_working_directory == target_working_directory:
            return path
        path = (initial_working_directory / path).resolve()
        try:
            return path.relative_to(target_working_directory)
        except ValueError:
            # If the path cannot be made relative (e.g. since it is on a different drive),
            # return the absolute path.
            return path


class RemoteFileTransferStrategy(FileTransferStrategy):
    _ft_client: FileTransferClient

    def __init__(self, channel: grpc.Channel) -> None:
        self._ft_client = FileTransferClient(channel)

    def upload_file(self, local_path: _PATH) -> pathlib.PurePath:
        remote_path = os.path.basename(local_path)
        self._ft_client.upload_file(local_filename=str(local_path), remote_filename=remote_path)
        return pathlib.PurePosixPath(remote_path)

    def download_file(self, remote_path: _PATH, local_path: _PATH) -> None:
        self._ft_client.download_file(
            remote_filename=str(remote_path), local_filename=str(local_path)
        )

    def to_export_path(self, path: _PATH) -> _PATH:
        # Export to the working directory of the server
        return pathlib.Path(path).name


class FileTransferHandler:
    def __init__(
        self, filetransfer_strategy: FileTransferStrategy, auto_transfer_files: bool
    ) -> None:
        self._filetransfer_strategy = filetransfer_strategy
        self._auto_transfer_files = auto_transfer_files

    def upload_file_if_autotransfer(self, local_path: _PATH) -> pathlib.PurePath:
        if self._auto_transfer_files:
            return self.upload_file(local_path)
        return pathlib.Path(local_path)

    def download_file_if_autotransfer(self, remote_path: _PATH, local_path: _PATH) -> None:
        if self._auto_transfer_files:
            self.download_file(remote_path, local_path)
        else:
            # If auto-transfer is disabled, the export path should be the
            # same as the local path. Otherwise, this is a bug in our code.
            assert remote_path == local_path

    def to_export_path(self, path: _PATH) -> _PATH:
        if self._auto_transfer_files:
            return self._filetransfer_strategy.to_export_path(path)
        return path

    def upload_file(self, local_path: _PATH) -> pathlib.PurePath:
        return self._filetransfer_strategy.upload_file(local_path)

    def download_file(self, remote_path: _PATH, local_path: _PATH) -> None:
        self._filetransfer_strategy.download_file(remote_path, local_path)


ServerT = TypeVar("ServerT", bound=ServerProtocol, covariant=True)


class ACPInstance(Generic[ServerT]):
    """Control an ACP instance.

    Supports the following operations to control an ACP instance:

    - Loading and unloading ACP models
    - Up- and download of files to the (possibly remote) ACP instance
    - Check if the ACP instance is running

    In addition, the ACP instance *may* support starting, stopping,
    and restarting.

    Note that this class is not meant for instantiating directly.
    The :func:`.launch_acp` function should be used instead.
    """

    _server: ServerT
    _filetransfer_handler: FileTransferHandler
    _channel: grpc.Channel
    _is_remote: bool

    def __init__(
        self,
        *,
        server: ServerT,
        channel: grpc.Channel,
        filetransfer_handler: FileTransferHandler,
        is_remote: bool,
    ) -> None:
        self._server = server
        self._channel = channel
        self._filetransfer_handler = filetransfer_handler
        self._is_remote = is_remote

    @property
    def is_remote(self) -> bool:
        """Whether the server is remote or local."""
        return self._is_remote

    @property
    def server_version(self) -> str:
        """Version of the connected server."""
        control_stub = control_pb2_grpc.ControlStub(self._channel)
        server_info = control_stub.GetServerInfo(Empty())
        version = server_info.version
        if not version:
            raise RuntimeError("Server version could not be determined.")
        return cast(str, version)

    def import_model(
        self,
        path: _PATH,
        *,
        name: str | None = None,
        format: str = "acp:h5",  # pylint: disable=redefined-builtin
        **kwargs: Any,
    ) -> Model:
        """Load an ACP model from a file.

        Parameters
        ----------
        name :
            Name of the newly loaded model.
        path :
            Path of the file to be loaded.
        format :
            Format of the file to be loaded. Can be one of ``"acp:h5"``,
            ``"ansys:h5"``, ``"ansys:cdb"``, ``"ansys:dat"``, ``"abaqus:inp"``,
            or ``"nastran:bdf"``.
        ignored_entities:
            Entities to ignore when loading the FE file. Can be a subset of
            the following values:
            ``"coordinate_systems"``, ``"element_sets"``, ``"materials"``,
            ``"mesh"``, or ``"shell_sections"``.
            Available only when the format is not ``"acp:h5"``.
        convert_section_data:
            Whether to import the section data of a shell model and convert it
            into ACP composite definitions.
            Available only when the format is not ``"acp:h5"``.
        unit_system:
            Defines the unit system of the imported file. Must be set if the
            input file does not have units. If the input file does have units,
            ``unit_system`` must be either ``"from_file"``, or match the input
            unit system.
            Available only when the format is not ``"acp:h5"``.

        Returns
        -------
        :
            The loaded ``Model`` instance.
        """
        from .._tree_objects import Model
        from .._tree_objects.base import ServerWrapper

        server_wrapper = ServerWrapper.from_acp_instance(self)
        if format == "acp:h5":
            if kwargs:
                raise ValueError(
                    f"Parameters '{kwargs.keys()}' cannot be passed when "
                    f"loading a model with format '{format}'."
                )
            model = Model._from_file(path=path, server_wrapper=server_wrapper)
        else:
            model = Model._from_fe_file(
                path=path,
                server_wrapper=server_wrapper,
                format=format,
                **kwargs,
            )
        if name is not None:
            model.name = name
        return model

    def clear(self) -> None:
        """Close all models.

        Closes the models which are currently open, without first
        saving them to a file.
        """
        from .._tree_objects import Model

        model_stub = model_pb2_grpc.ObjectServiceStub(self._channel)
        with wrap_grpc_errors():
            for model in model_stub.List(
                ListRequest(collection_path=CollectionPath(value=Model._COLLECTION_LABEL))
            ).objects:
                model_stub.Delete(
                    DeleteRequest(
                        resource_path=model.info.resource_path, version=model.info.version
                    )
                )

    @property
    def models(self) -> tuple[Model, ...]:
        """Models currently loaded on the server.

        Note that the models are listed in arbitrary order.
        """
        from .._tree_objects import Model

        model_stub = model_pb2_grpc.ObjectServiceStub(self._channel)
        return tuple(
            [
                Model._from_object_info(model_info, self._channel)
                for model_info in model_stub.List(
                    ListRequest(collection_path=CollectionPath(value=Model._COLLECTION_LABEL))
                ).objects
            ]
        )

    def upload_file(self, local_path: _PATH) -> pathlib.PurePath:
        """Upload a file to the server.

        .. warning::

            Do not execute this function with untrusted input parameters.
            See the :ref:`security guide<security_file_upload_download>`
            for details.

        Parameters
        ----------
        local_path :
            The path of the file to be uploaded.

        Returns
        -------
        :
            The path of the uploaded file on the server.
        """
        return self._filetransfer_handler.upload_file(local_path)

    def download_file(self, remote_path: _PATH, local_path: _PATH) -> None:
        """Download a file from the server.

        .. warning::

            Do not execute this function with untrusted input parameters.
            See the :ref:`security guide<security_file_upload_download>`
            for details.

        Parameters
        ----------
        remote_path :
            The path of the file on the server.
        local_path :
            The path of the file to be downloaded to.
        """
        self._filetransfer_handler.download_file(remote_path, local_path)

    def check(self, timeout: float | None = None) -> bool:
        """Check if the ACP instance is running.

        Parameters
        ----------
        timeout :
            Time to wait for the ACP instance to respond, in seconds. Note that
            there is no *guarantee* that ``check`` returns within this time.
            Instead, this parameter is used as a hint to the underlying
            implementation.
        """
        return self._server.check(timeout=timeout)

    def wait(self, timeout: float) -> None:
        """Wait for the ACP instance to respond.

        Repeatedly checks if the ACP instance is running, returning as
        soon as it is running.

        Parameters
        ----------
        timeout :
            Wait time before raising an exception.

        Raises
        ------
        RuntimeError
            In case the server still has not responded after ``timeout`` seconds.
        """
        self._server.wait(timeout=timeout)

    def start(self) -> None:
        """Start the product instance.

        Raises
        ------
        RuntimeError
            If the instance is already in the started state.
        RuntimeError
            If the instance does not allow manual starting.
        """
        if not hasattr(self._server, "start"):
            raise RuntimeError(
                "This ACP server does not expose a method to start it. "
                "Please use a different launch method."
            )
        self._server.start()

    def stop(self, *, timeout: float | None = None) -> None:
        """Stop the product instance.

        Parameters
        ----------
        timeout :
            Time in seconds after which the instance is forcefully stopped. Note
            that not all launch methods may implement this parameter. If they
            do not, the parameter is ignored.

        Raises
        ------
        RuntimeError
            If the instance is already in the stopped state.
        RuntimeError
            If the instance does not allow stopping.
        """
        if not hasattr(self._server, "stop"):
            raise RuntimeError(
                "This ACP server does not expose a method to stop it. "
                "Please use a different launch method."
            )
        self._server.stop(timeout=timeout)

    def restart(self, stop_timeout: float | None = None) -> None:
        """Stop, then start the product instance.

        Parameters
        ----------
        stop_timeout :
            Time in seconds after which the instance is forcefully stopped. Note
            that not all launch methods may implement this parameter. If they
            do not, the parameter is ignored.

        Raises
        ------
        RuntimeError
            If the instance is already in the stopped state.
        RuntimeError
            If the instance does not allow restarting.
        """
        if not hasattr(self._server, "restart"):
            raise RuntimeError(
                "This ACP server does not expose a method to restart it. "
                "Please use a different launch method."
            )
        self._server.restart(stop_timeout=stop_timeout)
