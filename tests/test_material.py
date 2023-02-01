import pytest

from ansys.acp.core._tree_objects.enums import PlyType
from common.tree_object_tester import ObjectProperties, TreeObjectTester, WithLockedMixin


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_material()


@pytest.fixture
def object_properties():
    return ObjectProperties(
        read_write={
            "name": "Material Name",
            "ply_type": PlyType.WOVEN,
        },
        read_only={
            "locked": True,
            "id": "some_id",
        },
    )


class TestMaterial(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "materials"
    DEFAULT_PROPERTIES = {
        "ply_type": PlyType.UNDEFINED,
    }
    CREATE_METHOD_NAME = "create_material"
    INITIAL_OBJECT_NAMES = ("Structural Steel",)
