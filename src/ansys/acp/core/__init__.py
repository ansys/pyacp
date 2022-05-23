try:
    import importlib.metadata as importlib_metadata  # type: ignore
except ModuleNotFoundError:
    import importlib_metadata  # type: ignore

from ._launcher import launch_acp
from ._model import Model
from ._modeling_group import ModelingGroup
from ._db import DB

__version__ = importlib_metadata.version(__name__.replace(".", "-"))


__all__ = ["__version__", "launch_acp", "Model", "ModelingGroup", "DB"]
