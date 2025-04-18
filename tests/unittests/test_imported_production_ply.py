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

from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import ImportedProductionPly, Model

from .common.tree_object_tester import TreeObjectTesterReadOnly


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(
        ImportedProductionPly._SUPPORTED_SINCE
    ):
        pytest.skip("ImportedProductionPly is not supported on this version of the server.")


@pytest.fixture
def model(load_model_imported_plies_from_tempfile):
    with load_model_imported_plies_from_tempfile() as model:
        yield model


def get_hdf5_imported_modeling_group(parent_model: Model):
    return parent_model.imported_modeling_groups["by hdf5"]


def all_imported_production_plies(model: Model):
    modeling_group = get_hdf5_imported_modeling_group(model)
    imported_production_plies = []
    for imp in modeling_group.imported_modeling_plies.values():
        for ipp in imp.imported_production_plies.values():
            imported_production_plies.append(ipp)

    return imported_production_plies


class TestImportedProductionPly(TreeObjectTesterReadOnly):
    COLLECTION_NAME = "imported_production_plies"

    @staticmethod
    @pytest.fixture
    def parent_object(model: Model):
        img = get_hdf5_imported_modeling_group(model)
        return img.imported_modeling_plies["ud"]

    @pytest.fixture
    def collection_test_data(self, parent_object):
        imported_modeling_ply = parent_object
        object_collection = getattr(imported_modeling_ply, self.COLLECTION_NAME)
        object_collection.values()
        object_names = ["P1__ud"]
        object_ids = ["ImportedProductionPly"]

        return object_collection, object_names, object_ids

    @pytest.fixture
    def properties(self, model):
        fabric_ud = model.fabrics["ud_1.5mm"]
        fabric_woven = model.fabrics["woven_1mm"]
        return {
            "ImportedProductionPly": {
                "name": "P1__ud",
                "status": "UPTODATE",
                "material": fabric_ud,
                "angle": 45.0,
                "thickness": 0.0015,
            },
            "ImportedProductionPly.2": {
                "name": "P1__woven",
                "status": "UPTODATE",
                "material": fabric_woven,
                "angle": 30.0,
                "thickness": 0.001,
            },
            "ImportedProductionPly.3": {
                "name": "P1__ud 2",
                "status": "UPTODATE",
                "material": fabric_ud,
                "angle": 45.0,
                "thickness": 0.0015,
            },
        }

    def test_properties(self, model: Model, properties):
        for ply in all_imported_production_plies(model):
            ref_values = properties[ply.id]
            for prop, value in ref_values.items():
                assert getattr(ply, prop) == value

    def test_after_update(self, model):
        # Test that list of analysis plies stays up-to-date
        # after update that removes analysis plies.
        # Check that requesting properties on a removed analysis
        # ply throws the expected error

        initial_imported_production_plies = all_imported_production_plies(model)

        modeling_group = get_hdf5_imported_modeling_group(model)
        for imp in modeling_group.imported_modeling_plies.values():
            imp.active = False
        model.update()
        assert len(all_imported_production_plies(model)) == 0

        for iap in initial_imported_production_plies:
            with pytest.raises(LookupError, match="Entity not found") as ex:
                _ = iap.status

        for imp in modeling_group.imported_modeling_plies.values():
            imp.active = True

        model.update()
        imported_production_plies = all_imported_production_plies(model)
        assert len(imported_production_plies) == 3

        for ipp in imported_production_plies:
            assert len(ipp.imported_analysis_plies) == 1
