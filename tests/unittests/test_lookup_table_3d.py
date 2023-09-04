import pytest

from ansys.acp.core._tree_objects.enums import LookUpTable3DInterpolationAlgorithm

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_lookup_table_3d()


class TestLookUpTable1D(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "lookup_tables_3d"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "interpolation_algorithm": LookUpTable3DInterpolationAlgorithm.WEIGHTED_NEAREST_NEIGHBOR,
        "use_default_search_radius": True,
        "search_radius": 0.0,
        "num_min_neighbors": 1,
    }

    CREATE_METHOD_NAME = "create_lookup_table_3d"

    @staticmethod
    @pytest.fixture
    def object_properties():
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "1D Look-Up Table name"),
                ("interpolation_algorithm", LookUpTable3DInterpolationAlgorithm.NEAREST_NEIGHBOR),
                (
                    "interpolation_algorithm",
                    LookUpTable3DInterpolationAlgorithm.LINEAR_TRIANGULATION,
                ),
                ("use_default_search_radius", False),
                ("search_radius", 3.5),
                ("num_min_neighbors", 7),
            ],
            read_only=[
                ("id", "some id"),
                ("status", "UPTODATE"),
            ],
        )
