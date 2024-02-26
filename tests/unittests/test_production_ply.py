import pytest

from ansys.acp.core import Model, ModelingPly, ProductionPlyElementalData, ProductionPlyNodalData

from .common.tree_object_tester import TreeObjectTesterReadOnly


@pytest.fixture
def parent_model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def parent_object(parent_model):
    return parent_model.modeling_groups["ModelingGroup.1"].modeling_plies["ModelingPly.1"]


class TestProductionPly(TreeObjectTesterReadOnly):
    COLLECTION_NAME = "production_plies"

    @pytest.fixture
    def properties_3_layers(self, parent_model: Model):
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

    def test_properties(self, parent_object: ModelingPly, parent_model: Model, properties_3_layers):
        parent_object.number_of_layers = 3
        parent_model.update()
        for ply_name, ply_properties in properties_3_layers.items():
            ply_obj = parent_object.production_plies[ply_name]
            for prop, value in ply_properties.items():
                assert getattr(ply_obj, prop) == value

        for ply_name, ply_properties in properties_3_layers.items():
            ply_obj = parent_object.production_plies[ply_name]
            for prop, value in ply_properties.items():
                with pytest.raises(AttributeError):
                    setattr(ply_obj, prop, value)

    def test_after_update(
        self, parent_object: ModelingPly, parent_model: Model, properties_3_layers
    ):
        # Test that list of production plies stays up-to-date
        # after update that removes production plies.
        # Check that requesting properties on a removed production
        # ply throws the expected error
        parent_object.number_of_layers = 3
        parent_model.update()
        for ply_name, ply_properties in properties_3_layers.items():
            ply_obj = parent_object.production_plies[ply_name]
            for prop, value in ply_properties.items():
                assert getattr(ply_obj, prop) == value

        production_ply_that_gets_removed_on_update = parent_object.production_plies["ProductionPly"]
        parent_object.number_of_layers = 1
        parent_model.update()
        assert len(parent_object.production_plies) == 1

        with pytest.raises(LookupError, match="Entity not found") as ex:
            _ = production_ply_that_gets_removed_on_update.status


def test_mesh_data_existence(parent_object):
    """
    Test that the elemental and nodal data can be retrieved. Does not
    test the correctness of the data.
    """
    production_ply = list(parent_object.production_plies.values())[0]
    elemental_data = production_ply.elemental_data
    assert isinstance(elemental_data, ProductionPlyElementalData)
    nodal_data = production_ply.nodal_data
    assert isinstance(nodal_data, ProductionPlyNodalData)
