# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from numpy.testing import assert_equal
from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import FabricWithAngle, Model
from ansys.acp.core.mesh_data import AnalysisPlyElementalData, AnalysisPlyNodalData

from .common.tree_object_tester import TreeObjectTesterReadOnly


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile(relative_file_path="minimal_complete_model.acph5") as model:
        yield model


def get_first_modeling_ply(parent_model: Model):
    return parent_model.modeling_groups["ModelingGroup.1"].modeling_plies["ModelingPly.1"]


def get_first_production_ply(parent_model: Model):
    return get_first_modeling_ply(parent_model).production_plies["ProductionPly"]


def add_stackup_with_3_layers_to_modeling_ply(model: Model):
    fabric = model.fabrics["Fabric.1"]
    stackup = model.create_stackup(
        fabrics=[
            FabricWithAngle(fabric=fabric, angle=0.0),
            FabricWithAngle(fabric=fabric, angle=10.0),
            FabricWithAngle(fabric=fabric, angle=20.0),
        ]
    )
    get_first_modeling_ply(model).ply_material = stackup
    model.update()


class TestAnalysisPly(TreeObjectTesterReadOnly):
    COLLECTION_NAME = "analysis_plies"

    @pytest.fixture
    def properties_3_layers(self, model):
        first_material = model.materials["Structural Steel"]
        return {
            "P1L1__ModelingPly.1": {
                "status": "UPTODATE",
                "material": first_material,
                "angle": 0.0,
                "thickness": 0.0001,
            },
            "P1L2__ModelingPly.1": {
                "status": "UPTODATE",
                "material": first_material,
                "angle": 10.0,
                "thickness": 0.0001,
            },
            "P1L3__ModelingPly.1": {
                "status": "UPTODATE",
                "material": first_material,
                "angle": 20.0,
                "thickness": 0.0001,
            },
        }

    @staticmethod
    @pytest.fixture
    def parent_object(model: Model):
        add_stackup_with_3_layers_to_modeling_ply(model)

        production_ply = get_first_modeling_ply(model).production_plies["ProductionPly"]
        return production_ply

    @pytest.fixture
    def collection_test_data(self, parent_object):
        production_ply = parent_object
        object_collection = getattr(production_ply, self.COLLECTION_NAME)
        object_collection.values()
        object_names = ["P1L1__ModelingPly.1", "P1L2__ModelingPly.1", "P1L3__ModelingPly.1"]
        object_ids = ["P1L1__ModelingPly.1", "P1L2__ModelingPly.1", "P1L3__ModelingPly.1"]

        return object_collection, object_names, object_ids

    def test_properties(self, model: Model, properties_3_layers):
        add_stackup_with_3_layers_to_modeling_ply(model)
        for ply_name, ply_properties in properties_3_layers.items():
            ply_obj = get_first_production_ply(model).analysis_plies[ply_name]
            for prop, value in ply_properties.items():
                assert getattr(ply_obj, prop) == value

        for ply_name, ply_properties in properties_3_layers.items():
            ply_obj = get_first_production_ply(model).analysis_plies[ply_name]
            for prop, value in ply_properties.items():
                with pytest.raises(AttributeError):
                    setattr(ply_obj, prop, value)

    def test_after_update(self, model, properties_3_layers):
        # Test that list of analysis plies stays up-to-date
        # after update that removes analysis plies.
        # Check that requesting properties on a removed analysis
        # ply throws the expected error

        add_stackup_with_3_layers_to_modeling_ply(model)

        for ply_name, ply_properties in properties_3_layers.items():
            ply_obj = get_first_production_ply(model).analysis_plies[ply_name]
            for prop, value in ply_properties.items():
                assert getattr(ply_obj, prop) == value

        analysis_ply_that_gets_removed_on_update = get_first_production_ply(model).analysis_plies[
            "P1L1__ModelingPly.1"
        ]
        get_first_modeling_ply(model).ply_material = model.fabrics["Fabric.1"]
        model.update()
        assert len(get_first_modeling_ply(model).production_plies) == 1
        assert (
            len(get_first_modeling_ply(model).production_plies["ProductionPly"].analysis_plies) == 1
        )

        with pytest.raises(LookupError, match="Entity not found") as ex:
            _ = analysis_ply_that_gets_removed_on_update.status


class TestAnalysisPlyAlternateParents(TreeObjectTesterReadOnly):
    COLLECTION_NAME = "analysis_plies"

    @pytest.fixture(params=["solid_model", "imported_solid_model", "layup_mapping_object"])
    def parent_object(self, request, model, acp_instance):
        server_version_parsed = parse_version(acp_instance.server_version)
        if server_version_parsed < parse_version("25.1"):
            pytest.skip("Supported only from version 25.1")

        if request.param == "solid_model":
            return next(iter(model.solid_models.values()))

        if server_version_parsed < parse_version("25.2"):
            pytest.skip("Supported only from version 25.2")

        ism = next(iter(model.imported_solid_models.values()))
        if request.param == "imported_solid_model":
            return ism
        else:
            return next(iter(ism.layup_mapping_objects.values()))

    @pytest.fixture
    def collection_test_data(self, parent_object):
        object_collection = getattr(parent_object, self.COLLECTION_NAME)
        object_collection.values()
        object_names = ["P1L1__ModelingPly.1"]
        object_ids = ["P1L1__ModelingPly.1"]
        return object_collection, object_names, object_ids

    @staticmethod
    def test_parent_access():  # type: ignore[override]
        pytest.skip("Not applicable, since the parent object is the production ply.")


def test_mesh_data_existence(model: Model):
    """
    Test that the elemental and nodal data can be retrieved. Does not
    test the correctness of the data.
    """
    analysis_ply = list(get_first_production_ply(model).analysis_plies.values())[0]
    elemental_data = analysis_ply.elemental_data
    assert isinstance(elemental_data, AnalysisPlyElementalData)
    nodal_data = analysis_ply.nodal_data
    assert isinstance(nodal_data, AnalysisPlyNodalData)


def test_meshes(model: Model, raises_before_version):
    """
    Test that the mesh properties can be retrieved.
    """
    analysis_ply = list(get_first_production_ply(model).analysis_plies.values())[0]
    with raises_before_version("25.1"):
        assert_equal(analysis_ply.mesh.element_labels, [1, 2, 3])
    with raises_before_version("25.1"):
        assert_equal(analysis_ply.shell_mesh.element_labels, [1])
    with raises_before_version("25.1"):
        assert_equal(analysis_ply.solid_mesh.element_labels, [2, 3])
    with raises_before_version("25.1"):
        model.create_solid_model(
            element_sets=[model.element_sets["All_Elements"]],
        )
    model.update()
    with raises_before_version("25.1"):
        assert_equal(analysis_ply.mesh.element_labels, [1, 2, 3, 4])
    with raises_before_version("25.1"):
        assert_equal(analysis_ply.shell_mesh.element_labels, [1])
    with raises_before_version("25.1"):
        assert_equal(analysis_ply.solid_mesh.element_labels, [2, 3, 4])
