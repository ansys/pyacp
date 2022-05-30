"""Helper functions for dealing with Resource Paths."""

__all__ = ["join"]


def join(*parts: str) -> str:
    """Joins parts of a Resource Path into a single string.

    Join parts of a Resource Path by slashes, ensuring that there are no
    double slashes in the result. Leading and trailing slashes are removed.
    """
    return "/".join(parts).replace("//", "/").strip("/")
