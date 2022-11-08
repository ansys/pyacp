"""Helper functions for dealing with Resource Paths."""

from typing import Tuple

__all__ = ["join"]


def join(*parts: str) -> str:
    """Joins parts of a Resource Path into a single string.

    Join parts of a Resource Path by slashes, ensuring that there are no
    double slashes in the result. Leading and trailing slashes are removed.
    """
    return "/".join(parts).replace("//", "/").strip("/")


def to_parts(path: str) -> Tuple[str, ...]:
    """Returns a tuple representation of the given path."""
    return tuple(path.split("/"))


def common_path(*paths: str) -> str:
    """Returns the partial path that all input paths have in common."""
    common_parts = []
    for path_parts in zip(*[to_parts(p) for p in paths]):
        first_path_part = path_parts[0]
        if all(part == first_path_part for part in path_parts):
            common_parts.append(first_path_part)
        else:
            break
    return "/".join(common_parts)
