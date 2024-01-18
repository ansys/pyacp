import pytest

from ansys.acp.core import CADGeometry, VirtualGeometry
from ansys.acp.core._tree_objects.enums import VirtualGeometryDimension
from ansys.acp.core._tree_objects.virtual_geometry import SubShape

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    virtual_geometry = VirtualGeometry()
    parent_object.add_virtual_geometry(virtual_geometry)
    return virtual_geometry


class TestVirtualGeometry(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "virtual_geometries"
    DEFAULT_PROPERTIES = {
        "status": "NOTUPTODATE",
        "dimension": VirtualGeometryDimension.UNKNOWN,
        "sub_shapes": [],
    }
    OBJECT_CLS = VirtualGeometry
    ADD_METHOD_NAME = "add_virtual_geometry"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        cad_geometry = CADGeometry()
        model.add_cad_geometry(cad_geometry)
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
