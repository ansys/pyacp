import dataclasses
from enum import Enum, auto
import pathlib
import urllib.request

EXAMPLE_REPO = "https://github.com/ansys/example-data/raw/master/pyacp/"


@dataclasses.dataclass
class ExampleLocation:
    directory: str
    filename: str


class ExampleKeys(Enum):
    BASIC_FLAT_PLATE = auto()


EXAMPLE_FILES: dict[ExampleKeys, ExampleLocation] = {
    ExampleKeys.BASIC_FLAT_PLATE: ExampleLocation(
        directory="basic_flat_plate_example", filename="flat_plate_input.dat"
    ),
}


def get_example_file(example_key: ExampleKeys, working_directory: pathlib.Path) -> pathlib.Path:
    example_location = EXAMPLE_FILES[example_key]
    _download_file(example_location, working_directory)
    return working_directory / example_location.filename


def _get_file_url(example_location: ExampleLocation) -> str:
    return EXAMPLE_REPO + "/".join([example_location.directory, example_location.filename])


def _download_file(example_location: ExampleLocation, local_path: pathlib.Path) -> None:
    file_url = _get_file_url(example_location)
    urllib.request.urlretrieve(file_url, local_path)
