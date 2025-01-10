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

import pytest

from ansys.acp.core.mesh_data import TubeSelectionRuleElementalData, TubeSelectionRuleNodalData

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_tube_selection_rule()


class TestTubeSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "tube_selection_rules"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "edge_set": None,
            "outer_radius": 1.0,
            "inner_radius": 0.0,
            "include_rule": True,
            "extend_endings": False,
            "symmetrical_extension": True,
            "head": (0.0, 0.0, 0.0),
            "head_extension": 0.0,
            "tail_extension": 0.0,
        }

    CREATE_METHOD_NAME = "create_tube_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        edge_set = model.create_edge_set()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Tube Selection Rule name"),
                ("edge_set", edge_set),
                ("outer_radius", 1.3),
                ("inner_radius", 0.3),
                ("include_rule", False),
                ("extend_endings", True),
                ("symmetrical_extension", False),
                ("head", (1.0, 2.0, 3.0)),
                ("head_extension", 4.0),
                ("tail_extension", 5.0),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = parent_object.create_tube_selection_rule()
    assert isinstance(rule.elemental_data, TubeSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, TubeSelectionRuleNodalData)
