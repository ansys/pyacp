from dataclasses import dataclass

__all__ = ["Resource"]


@dataclass
class Resource:
    name: str
    id: str
    version: int
