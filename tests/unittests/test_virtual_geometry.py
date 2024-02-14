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


def test_virtual_geometry_creation_from_cad_components(parent_object, load_cad_geometry):
    model = parent_object
    with load_cad_geometry(model) as cad_geometry:
        model.update()
        virtual_geometry = model.create_virtual_geometry(
            cad_components=cad_geometry.root_shapes.values()
        )

        assert len(virtual_geometry.sub_shapes) == 2
        assert virtual_geometry.sub_shapes[0].cad_geometry == cad_geometry
        assert virtual_geometry.sub_shapes[0].path == "SOLID"
        assert virtual_geometry.sub_shapes[1].cad_geometry == cad_geometry
        assert virtual_geometry.sub_shapes[1].path == "SHELL"


def test_virtual_geometry_no_or_invalid_links(parent_object, load_cad_geometry):
    model = parent_object
    with load_cad_geometry(model) as cad_geometry:
        model.update()

        # No sub_shapes or cad_components is ok
        virtual_geometry_no_shapes = model.create_virtual_geometry()
        assert len(virtual_geometry_no_shapes.sub_shapes) == 0

        # Cannot specify both sub_shapes and cad_components
        with pytest.raises(ValueError):
            model.create_virtual_geometry(
                cad_components=cad_geometry.root_shapes.values(),
                sub_shapes=[SubShape(cad_geometry=cad_geometry, path="some/path/to/shape")],
            )
