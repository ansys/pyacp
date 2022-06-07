from typing import Any, Optional

from ansys.api.acp.v0.base_pb2 import CollectionPath
from ansys.api.acp.v0.model_pb2 import DeleteModelRequest, ListModelsRequest
from ansys.api.acp.v0.model_pb2_grpc import ModelStub

from ._model import Model
from ._server import ServerProtocol
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
        self._server = server

    def import_model(
        self, *, name: Optional[str] = None, path: _PATH, format: str = "acp:h5", **kwargs: Any
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
            model = Model.from_file(path=path, server=self._server)
        else:
            model = Model.from_fe_file(path=path, server=self._server, format=format, **kwargs)
        if name is not None:
            model.name = name
        return model

    def clear(self) -> None:
        """Close all models currently loaded on the server.

        Closes the models which are open on the server, without first
        saving them to a file.
        """
        model_stub = ModelStub(self._server.channel)
        for model in model_stub.List(
            ListModelsRequest(collection_path=CollectionPath(value=Model.COLLECTION_LABEL))
        ).models:
            model_stub.Delete(DeleteModelRequest(info=model.info))
