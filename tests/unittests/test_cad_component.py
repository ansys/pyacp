import pytest

from .common.tree_object_tester import TreeObjectTesterReadOnly


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


class TestCADComponent(TreeObjectTesterReadOnly):
    COLLECTION_NAME = "cad_components"

    @pytest.fixture
    def collection_test_data(self, model):
        model.update()
        cad_geometry = model.cad_geometries["CADGeometry.1"]
        return cad_geometry.root_shapes, ["SOLID", "SHELL"], ["SOLID", "SHELL"]
