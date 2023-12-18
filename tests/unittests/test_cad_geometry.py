import pytest

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_cad_geometry()


class TestCADGeometry(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "cad_geometries"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "external_path": "",
        "scale_factor": 1.0,
        "use_default_precision": True,
        "precision": 1e-3,
        "use_default_offset": True,
        "offset": 0.0,
    }

    CREATE_METHOD_NAME = "create_cad_geometry"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        element_set = model.create_element_set()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "CAD Geometry name"),
                ("external_path", "some/path/to/file"),
                ("scale_factor", 2.0),
                ("use_default_precision", False),
                ("precision", 1e-4),
                ("use_default_offset", False),
                ("offset", 1.3),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )
