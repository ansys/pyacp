# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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

from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import ImportedAnalysisPly, Model

from .common.tree_object_tester import TreeObjectTesterReadOnly


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(
        ImportedAnalysisPly._SUPPORTED_SINCE
    ):
        pytest.skip("ImportedAnalysisPly is not supported on this version of the server.")


@pytest.fixture
def model(load_model_imported_plies_from_tempfile):
    with load_model_imported_plies_from_tempfile() as model:
        yield model


def get_hdf5_imported_modeling_group(parent_model: Model):
    return parent_model.imported_modeling_groups["by hdf5"]


def all_imported_analysis_plies(model: Model):
    modeling_group = get_hdf5_imported_modeling_group(model)
    imported_analysis_plies = []
    for imp in modeling_group.imported_modeling_plies.values():
        for ipp in imp.imported_production_plies.values():
            for iap in ipp.imported_analysis_plies.values():
                imported_analysis_plies.append(iap)

    return imported_analysis_plies


class TestImportedAnalysisPly(TreeObjectTesterReadOnly):
    COLLECTION_NAME = "imported_analysis_plies"

    @staticmethod
    @pytest.fixture(
        params=["imported_production_ply", "imported_solid_model", "layup_mapping_object"]
    )
    def parent_kind(request, acp_instance):
        # We are skipping the test entirely instead of using 'raises_before_version'
        # because it is generally the test _setup_ which fails, not the test itself.
        if request.param != "imported_production_ply" and parse_version(
            acp_instance.server_version
        ) < parse_version("25.2"):
            pytest.skip(
                "Accessing imported analysis plies from other parents is not supported in this version."
            )
        return request.param

    @staticmethod
    @pytest.fixture
    def parent_object(model: Model, parent_kind):
        if parent_kind == "imported_production_ply":
            img = get_hdf5_imported_modeling_group(model)
            return img.imported_modeling_plies["ud"].imported_production_plies[
                "ImportedProductionPly"
            ]
        else:
            ism = next(iter(model.imported_solid_models.values()))
            if parent_kind == "imported_solid_model":
                return ism
            else:
                assert parent_kind == "layup_mapping_object"
                return next(iter(ism.layup_mapping_objects.values()))

    @pytest.fixture
    def collection_test_data(self, parent_object, parent_kind):
        imported_production_ply = parent_object
        object_collection = getattr(imported_production_ply, self.COLLECTION_NAME)
        object_collection.values()
        if parent_kind == "imported_production_ply":
            object_names = ["P1L1__ud"]
            object_ids = ["P1L1__ud"]
        else:
            # solid model and layup mapping object contain all imported analysis plies
            object_names = ["P1L1__ud", "P1L1__woven", "P1L1__ud 2"]
            object_ids = ["P1L1__ud", "P1L1__woven", "P1L1__ud 2"]

        return object_collection, object_names, object_ids

    @pytest.fixture
    def properties(self, model):
        carbon_ud = model.materials["Epoxy Carbon UD (230 GPa) Prepreg"]
        woven = model.materials["Epoxy Carbon Woven (230 GPa) Prepreg"]
        return {
            "P1L1__ud": {
                "status": "UPTODATE",
                "material": carbon_ud,
                "angle": 45.0,
                "thickness": 0.0015,
            },
            "P1L1__woven": {
                "status": "UPTODATE",
                "material": woven,
                "angle": 30.0,
                "thickness": 0.001,
            },
            "P1L1__ud 2": {
                "status": "UPTODATE",
                "material": carbon_ud,
                "angle": 45.0,
                "thickness": 0.0015,
            },
        }

    def test_properties(self, model: Model, properties):
        for ply in all_imported_analysis_plies(model):
            ref_values = properties[ply.id]
            for prop, value in ref_values.items():
                assert getattr(ply, prop) == value

    def test_after_update(self, model):
        # Test that list of analysis plies stays up-to-date
        # after update that removes analysis plies.
        # Check that requesting properties on a removed analysis
        # ply throws the expected error

        initial_imported_analysis_plies = all_imported_analysis_plies(model)

        modeling_group = get_hdf5_imported_modeling_group(model)
        for imp in modeling_group.imported_modeling_plies.values():
            imp.active = False
        model.update()
        assert len(all_imported_analysis_plies(model)) == 0

        for iap in initial_imported_analysis_plies:
            with pytest.raises(LookupError, match="Entity not found") as ex:
                _ = iap.status

        for imp in modeling_group.imported_modeling_plies.values():
            imp.active = True

        model.update()
        assert len(all_imported_analysis_plies(model)) == 3

    def test_parent_access(self, collection_test_data, parent_object, parent_kind):  # type: ignore
        if parent_kind != "imported_production_ply":
            pytest.skip(
                "This test only applies to the canonical resource path parent (imported production ply)."
            )
        super().test_parent_access(collection_test_data, parent_object)
