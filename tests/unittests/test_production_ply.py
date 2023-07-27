import pytest

from ansys.acp.core import Model, ModelingPly

from .common.tree_object_tester import TreeObjectTesterReadOnly


@pytest.fixture
def parent_model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        # Todo: why is model up-to-date?
        yield model


@pytest.fixture
def parent_object(parent_model):
    return parent_model.modeling_groups["ModelingGroup.1"].modeling_plies["ModelingPly.1"]


class TestProductionPly(TreeObjectTesterReadOnly):
    COLLECTION_NAME = "production_plies"

    @pytest.fixture
    def properties(self, parent_model: Model):
        first_fabric = parent_model.fabrics["Fabric.1"]
        return {
            "ProductionPly": {
                "status": "UPTODATE",
                "material": first_fabric,
                "angle": 0.0,
            },
            "ProductionPly.2": {
                "status": "UPTODATE",
                "material": first_fabric,
                "angle": 0.0,
            },
            "ProductionPly.3": {
                "status": "UPTODATE",
                "material": first_fabric,
                "angle": 0.0,
            },
        }

    @pytest.fixture
    def collection_test_data(self, parent_object: ModelingPly, parent_model: Model):
        parent_object.number_of_layers = 3
        parent_model.update()
        object_collection = getattr(parent_object, self.COLLECTION_NAME)
        object_names = ["P1__ModelingPly.1", "P2__ModelingPly.1", "P3__ModelingPly.1"]
        object_ids = ["ProductionPly", "ProductionPly.2", "ProductionPly.3"]

        return object_collection, object_names, object_ids

    def test_properties(self, parent_object: ModelingPly, parent_model: Model, properties):
        parent_object.number_of_layers = 3
        parent_model.update()
        for ply_name, ply_properties in properties.items():
            ply_obj = parent_object.production_plies[ply_name]
            for prop, value in ply_properties.items():
                assert getattr(ply_obj, prop) == value

        for ply_name, ply_properties in properties.items():
            ply_obj = parent_object.production_plies[ply_name]
            for prop, value in ply_properties.items():
                with pytest.raises(AttributeError):
                    setattr(ply_obj, prop, value)
