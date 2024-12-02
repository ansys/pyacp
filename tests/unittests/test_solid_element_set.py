# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
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

from ansys.acp.core import Model, SolidElementSet

from .common.tree_object_tester import TreeObjectTesterReadOnly

DUMMY_SM_NAME = "dummy"
ESET_ALL_ELEMENTS = "All_Elements"


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(SolidElementSet._SUPPORTED_SINCE):
        pytest.skip("SolidElementSet is not supported on this version of the server.")


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


def add_solid_model_to_model(model: Model):
    solid_model = model.create_solid_model(
        name=DUMMY_SM_NAME,
        element_sets=[model.element_sets[ESET_ALL_ELEMENTS]],
    )
    return solid_model


class TestSolidElementSet(TreeObjectTesterReadOnly):
    COLLECTION_NAME = "solid_element_sets"

    @staticmethod
    @pytest.fixture
    def parent_object(model: Model):
        solid_model = add_solid_model_to_model(model)
        #  Solid model must be up-to-date to access the solid element sets
        model.update()
        return solid_model

    @pytest.fixture
    def collection_test_data(self, parent_object):
        solid_model = parent_object
        object_collection = getattr(solid_model, self.COLLECTION_NAME)
        object_collection.values()
        object_names = [ESET_ALL_ELEMENTS]
        object_ids = [ESET_ALL_ELEMENTS]

        return object_collection, object_names, object_ids

    @staticmethod
    @pytest.fixture
    def properties():
        return {
            ESET_ALL_ELEMENTS: {
                "status": "UPTODATE",
                "locked": True,
                "element_labels": (2,),
            },
        }

    def test_properties(self, parent_object, properties):

        for solid_element_set in parent_object.solid_element_sets.values():
            ref_values = properties[solid_element_set.id]
            for prop, value in ref_values.items():
                assert getattr(solid_element_set, prop) == value

            assert solid_element_set.solid_mesh is not None
            assert solid_element_set.solid_mesh.element_labels == (2,)
