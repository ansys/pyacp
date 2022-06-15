from dataclasses import dataclass
from typing import Tuple

from .resource import Resource


@dataclass
class Rosette(Resource):
    locked: bool  # read only
    status: str  # read only
    origin: Tuple[float, ...]
    dir1: Tuple[float, ...]
    dir2: Tuple[float, ...]
