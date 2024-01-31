import dataclasses
from enum import Enum, auto
import pathlib
import urllib.request

__all__ = ["ExampleKeys", "get_example_file"]

_EXAMPLE_REPO = "https://github.com/ansys/example-data/raw/master/pyacp/"


@dataclasses.dataclass
class _ExampleLocation:
    directory: str
    filename: str


class ExampleKeys(Enum):
    """
    Keys for the example files.
    """

    BASIC_FLAT_PLATE_CDB = auto()
    BASIC_FLAT_PLATE_ACPH5 = auto()


EXAMPLE_FILES: dict[ExampleKeys, _ExampleLocation] = {
    ExampleKeys.BASIC_FLAT_PLATE_CDB: _ExampleLocation(
        directory="basic_flat_plate_example", filename="flat_plate_input.dat"
    ),
    ExampleKeys.BASIC_FLAT_PLATE_ACPH5: _ExampleLocation(
        directory="basic_flat_plate_example", filename="flat_plate.acph5"
    ),
}


def get_example_file(example_key: ExampleKeys, working_directory: pathlib.Path) -> pathlib.Path:
    """Downloads an example file from the example-data repo to the working directory.

    Parameters
    ----------
    example_key
        Key for the example file.
    working_directory
        Working directory to download the example file to.
    """
    example_location = EXAMPLE_FILES[example_key]
    _download_file(example_location, working_directory / example_location.filename)
    return working_directory / example_location.filename


def _get_file_url(example_location: _ExampleLocation) -> str:
    return _EXAMPLE_REPO + "/".join([example_location.directory, example_location.filename])


def _download_file(example_location: _ExampleLocation, local_path: pathlib.Path) -> None:
    file_url = _get_file_url(example_location)
    urllib.request.urlretrieve(file_url, local_path)
