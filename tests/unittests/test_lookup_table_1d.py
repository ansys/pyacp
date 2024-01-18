import pytest

from ansys.acp.core import LookUpTable1D

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    lookup_table_1d = LookUpTable1D()
    parent_object.add_lookup_table_1d(lookup_table_1d)
    return lookup_table_1d


class TestLookUpTable1D(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "lookup_tables_1d"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "origin": (0.0, 0.0, 0.0),
        "direction": (0.0, 0.0, 0.0),
    }
    OBJECT_CLS = LookUpTable1D
    ADD_METHOD_NAME = "add_lookup_table_1d"

    @staticmethod
    @pytest.fixture
    def object_properties():
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "1D Look-Up Table name"),
                ("origin", (-3.4, 2.9, 7.6)),
                ("direction", (0.0, -1.0, 0.0)),
            ],
            read_only=[
                ("id", "some id"),
                ("status", "UPTODATE"),
            ],
        )
