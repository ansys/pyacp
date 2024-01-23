from __future__ import annotations

import dataclasses
import os
import pathlib
import shutil
import tempfile
from typing import Any, cast
import uuid

from ansys.api.acp.v0 import control_pb2_grpc, model_pb2_grpc
from ansys.api.acp.v0.base_pb2 import CollectionPath, DeleteRequest, Empty, ListRequest
from ansys.tools.filetransfer import Client as FileTransferClient

from ._server import ServerKey, ServerProtocol
from ._tree_objects import Model
from ._typing_helper import PATH as _PATH

__all__ = ["Client"]

class LocalWorkingDir:
    def __init__(self, path: pathlib.Path =None):
        self._user_defined_working_dir = None
        self._temp_working_dir = None
        if path is None:
            self._temp_working_dir = tempfile.TemporaryDirectory()
        else:
            self._user_defined_working_dir = path

    @property
    def path(self) -> pathlib.Path:
        if self._user_defined_working_dir is not None:
            return self._user_defined_working_dir
        else:
            return pathlib.Path(self._temp_working_dir.name)

    @property
    def is_temp_dir(self) -> bool:
        return self._temp_working_dir is not None

class Client:
    """Top-level controller for the models loaded in a server.

    Parameters
    ----------
    server :
        The ACP gRPC server to which the ``Client`` connects.
    """

    def __init__(self, server: ServerProtocol, local_working_dir: _PATH | None = None) -> None:
        self._channel = server.channels[ServerKey.MAIN]
        if ServerKey.FILE_TRANSFER in server.channels:
            self._ft_client: FileTransferClient | None = FileTransferClient(
                server.channels[ServerKey.FILE_TRANSFER]
            )
        else:
            self._ft_client = None
        self._local_working_dir = LocalWorkingDir(local_working_dir)

    @property
    def local_working_dir(self) -> LocalWorkingDir:
        return self._local_working_dir

    @property
    def is_remote(self) -> bool:
        return self._ft_client is not None

    def upload_file(self, local_path: _PATH) -> pathlib.PurePath:
        """Upload local file.

        If the server is remote, uploads the file to the server and returns the path
        on the server.
        If the server is local and the working directory is a temp dir, copies the file to
        the working directory.
        If the server is local and the working directory is a user defined dir, does nothing
        and returns the input path.
        """
        if self._ft_client is None:
            assert self._local_working_dir is not None
            if self._local_working_dir.is_temp_dir:
                # Copy file to working dir if it is a temp dir
                # TODO: The '_tmp_dir', and file tracking / up-/download in general
                # should probably be handled by the local server itself.
                # For now, we just do it client-side.
                dest_dir = self._local_working_dir.path / uuid.uuid4().hex
                dest_dir.mkdir(parents=True, exist_ok=True)
                filename = os.path.basename(local_path)
                res_path = dest_dir / filename
                shutil.copyfile(local_path, res_path)
                return pathlib.Path(res_path)
            # Just return the local path if this is a user defined
            # working directory
            return pathlib.Path(local_path)

        else:
            remote_filename = os.path.basename(local_path)
            self._ft_client.upload_file(
                local_filename=str(local_path), remote_filename=str(remote_filename)
            )
            # TODO: turn this into a 'file reference' object
            return pathlib.PurePosixPath(remote_filename)

    def download_file(self, remote_filename: _PATH, local_path: _PATH) -> None:
        """
        Download a file from the server.

        If the server is remote, download the file to the local path.
        If the server is local and the working directory is a temp dir, copy the file to the
        temp dir.
        If the server is local and the working directory is a user defined dir, do nothing.
        """
        if self._ft_client is None:
            if self._local_working_dir.is_temp_dir:
                shutil.copyfile(remote_filename, local_path)
        else:
            self._ft_client.download_file(
                remote_filename=str(remote_filename), local_filename=str(local_path)
            )

    def import_model(
        self,
        *,
        name: str | None = None,
        path: _PATH,
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
            Format of the file to be loaded. Can be one of (TODO: list options).

        Returns
        -------
        :
            The loaded ``Model`` instance.
        """
        if format == "acp:h5":
            if kwargs:
                raise ValueError(
                    f"Parameters '{kwargs.keys()}' cannot be passed when "
                    f"loading a model with format '{format}'."
                )
            model = Model.from_file(path=path, channel=self._channel)
        else:
            model = Model.from_fe_file(path=path, channel=self._channel, format=format, **kwargs)
        if name is not None:
            model.name = name
        return model

    def clear(self) -> None:
        """Close all models currently loaded on the server.

        Closes the models which are open on the server, without first
        saving them to a file.
        """
        model_stub = model_pb2_grpc.ObjectServiceStub(self._channel)
        for model in model_stub.List(
            ListRequest(collection_path=CollectionPath(value=Model._COLLECTION_LABEL))
        ).objects:
            model_stub.Delete(
                DeleteRequest(resource_path=model.info.resource_path, version=model.info.version)
            )

    @property
    def server_version(self) -> str:
        """The version of the connected server."""
        control_stub = control_pb2_grpc.ControlStub(self._channel)
        server_info = control_stub.GetServerInfo(Empty())
        version = server_info.version
        if not version:
            raise RuntimeError("Server version could not be determined.")
        return cast(str, version)
