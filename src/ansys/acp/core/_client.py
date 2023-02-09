import os
import pathlib
import shutil
import tempfile
from typing import Any, Optional
import uuid

from ansys.api.acp.v0 import model_pb2_grpc
from ansys.api.acp.v0.base_pb2 import CollectionPath, DeleteRequest, ListRequest
from ansys.utilities.filetransfer import Client as FileTransferClient

from ._server import ServerKey, ServerProtocol
from ._tree_objects import Model
from ._typing_helper import PATH as _PATH

__all__ = ["Client"]


class Client:
    """Top-level controller for the models loaded in a server.

    Parameters
    ----------
    server :
        The ACP gRPC server to which the ``Client`` connects.
    """

    def __init__(self, server: ServerProtocol):
        self._channel = server.channels[ServerKey.MAIN]
        if ServerKey.FILE_TRANSFER in server.channels:
            self._ft_client: Optional[FileTransferClient] = FileTransferClient(
                server.channels[ServerKey.FILE_TRANSFER]
            )
            self._tmp_dir = None
        else:
            self._ft_client = None
            self._tmp_dir = tempfile.TemporaryDirectory()

    def upload_file(self, local_path: _PATH) -> pathlib.PurePath:
        if self._ft_client is None:
            assert self._tmp_dir is not None
            # TODO: The '_tmp_dir', and file tracking / up-/download in general
            # should probably be handled by the local server itself.
            # For now, we just do it client-side.
            dest_dir = pathlib.Path(self._tmp_dir.name) / uuid.uuid4().hex
            dest_dir.mkdir(parents=True)
            filename = os.path.basename(local_path)
            res_path = dest_dir / filename
            shutil.copyfile(local_path, res_path)
            return pathlib.Path(res_path)

        else:
            remote_filename = os.path.basename(local_path)
            self._ft_client.upload_file(
                local_filename=str(local_path), remote_filename=str(remote_filename)
            )
            # TODO: turn this into a 'file reference' object
            return pathlib.PurePosixPath(remote_filename)

    def download_file(self, remote_filename: _PATH, local_path: _PATH) -> None:
        if self._ft_client is None:
            shutil.copyfile(remote_filename, local_path)
        else:
            self._ft_client.download_file(
                remote_filename=str(remote_filename), local_filename=str(local_path)
            )

    def import_model(
        self,
        *,
        name: Optional[str] = None,
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
            ListRequest(collection_path=CollectionPath(value=Model.COLLECTION_LABEL))
        ).objects:
            model_stub.Delete(
                DeleteRequest(resource_path=model.info.resource_path, version=model.info.version)
            )
