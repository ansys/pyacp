import pytest

from ansys.acp.core import SubShape, VirtualGeometryDimension

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_virtual_geometry()


class TestVirtualGeometry(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "virtual_geometries"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "dimension": VirtualGeometryDimension.UNKNOWN,
            "sub_shapes": [],
        }

    CREATE_METHOD_NAME = "create_virtual_geometry"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        cad_geometry = model.create_cad_geometry()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Virtual Geometry name"),
                ("sub_shapes", [SubShape(cad_geometry=cad_geometry, path="some/path/to/shape")]),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("dimension", VirtualGeometryDimension.SOLID),
            ],
        )
