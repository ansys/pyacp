import pytest

from .common.tree_object_tester import TreeObjectTesterReadOnly


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def cad_geometry(model, load_cad_geometry):
    with load_cad_geometry(model) as cad_geometry:
        yield cad_geometry


class TestCADComponent(TreeObjectTesterReadOnly):
    COLLECTION_NAME = "cad_components"

    @pytest.fixture
    def collection_test_data(self, model, cad_geometry):
        model.update()
        return cad_geometry.root_shapes, ["SOLID", "SHELL"], ["SOLID", "SHELL"]
