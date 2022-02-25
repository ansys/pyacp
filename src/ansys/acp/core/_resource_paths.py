__all__ = ["join"]


def join(*parts: str) -> str:
    return "/".join(parts).replace("//", "/").strip("/")
