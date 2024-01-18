import pytest

from ansys.acp.core import Rosette

from .common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    rosette = Rosette()
    parent_object.add_rosette(rosette)
    return rosette


class TestRosette(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "rosettes"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "locked": False,
        "origin": (0.0, 0.0, 0.0),
        "dir1": (1.0, 0.0, 0.0),
        "dir2": (0.0, 1.0, 0.0),
    }
    ADD_METHOD_NAME = "add_rosette"
    OBJECT_CLS = Rosette
    INITIAL_OBJECT_NAMES = ("Global Coordinate System",)

    @staticmethod
    @pytest.fixture
    def object_properties():
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
                ("origin", (2.0, 3.0, 1.0)),
                ("dir1", (0.0, 0.0, 1.0)),
                ("dir2", (1.0, 0.0, 0.0)),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("locked", True),
            ],
        )
