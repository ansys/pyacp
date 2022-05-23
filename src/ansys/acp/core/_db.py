from typing import Any
from typing import Optional

from ansys.api.acp.v0.base_pb2 import CollectionPath
from ansys.api.acp.v0.model_pb2 import ListModelsRequest
from ansys.api.acp.v0.model_pb2 import ModelRequest
from ansys.api.acp.v0.model_pb2_grpc import ModelStub

from ._launcher import ServerProtocol
from ._model import Model
from ._typing_helper import PATH as _PATH


class DB:
    def __init__(self, server: ServerProtocol):
        self._server = server
        self._active_model: Optional[Model] = None

    @property
    def active_model(self) -> Optional[Model]:
        return self._active_model

    def import_model(
        self, *, name: Optional[str] = None, path: _PATH, format: str = "acp:h5", **kwargs: Any
    ) -> None:
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
        self._active_model = model

    def clear(self) -> None:
        model_stub = ModelStub(self._server.channel)
        for model in model_stub.List(
            ListModelsRequest(collection_path=CollectionPath(value=Model.COLLECTION_LABEL))
        ).models:
            model_stub.Delete(ModelRequest(resource_path=model.info.resource_path))
