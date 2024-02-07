from pathlib import PurePath

from .._typing_helper import PATH

__all__ = ["path_to_str_checked"]


def path_to_str_checked(path: PATH) -> str:
    """Convert a path to a string, with a type check."""
    if isinstance(path, str):
        return path
    elif isinstance(path, PurePath):
        return str(path)
    else:
        raise TypeError(f"Expected a Path or str, got {type(path)}")
