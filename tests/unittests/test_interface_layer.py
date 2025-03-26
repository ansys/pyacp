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

from ansys.acp.core import InterfaceLayer

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(InterfaceLayer._SUPPORTED_SINCE):
        pytest.skip("InterfaceLayer is not supported on this version of the server.")


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def parent_object(model):
    return list(model.modeling_groups.values())[0]


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_interface_layer()


class TestInterfaceLayer(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "interface_layers"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "active": True,
            "oriented_selection_sets": [],
            "open_area_sets": [],
        }

    CREATE_METHOD_NAME = "create_interface_layer"

    @staticmethod
    @pytest.fixture
    def object_properties(model):
        oriented_selection_sets = [model.create_oriented_selection_set() for _ in range(3)]
        open_area_sets = [model.create_oriented_selection_set(), model.create_element_set()]
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Interface layer name"),
                ("oriented_selection_sets", oriented_selection_sets),
                ("open_area_sets", open_area_sets),
                ("active", False),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_interface_layer_on_solid_model(load_model_from_tempfile, raises_before_version):
    with load_model_from_tempfile("minimal_complete_model.acph5") as model:
        modeling_group = next(iter(model.modeling_groups.values()))
        interface_layer = modeling_group.create_interface_layer()
        interface_layer.oriented_selection_sets = [
            next(iter(model.oriented_selection_sets.values()))
        ]
        # The interface layer needs to be surrounded by modeling plies to be present
        # in the solid model.
        new_ply = modeling_group.modeling_plies["ModelingPly.1"].clone()
        new_ply.global_ply_nr = 0  # at the end
        new_ply.store(parent=modeling_group)
        model.update()

        with raises_before_version("25.2"):
            solid_model = next(iter(model.solid_models.values()))
            assert interface_layer in list(solid_model.interface_layers.values())
