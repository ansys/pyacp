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

import pytest

from ansys.acp.core import CutOffRuleType, PlyCutOffType
from ansys.acp.core.mesh_data import CutOffSelectionRuleElementalData, CutOffSelectionRuleNodalData

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_cut_off_selection_rule()


class TestCutOffSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "cut_off_selection_rules"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "cut_off_rule_type": CutOffRuleType.GEOMETRY,
            "cut_off_geometry": None,
            "taper_edge_set": None,
            "offset": 0.0,
            "angle": 0.0,
            "ply_cut_off_type": PlyCutOffType.PRODUCTION_PLY_CUTOFF,
            "ply_tapering": False,
        }

    CREATE_METHOD_NAME = "create_cut_off_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        geometry = model.create_virtual_geometry()
        edge_set = model.create_edge_set()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "CutOff Selection Rule name"),
                ("cut_off_rule_type", CutOffRuleType.TAPER),
                ("cut_off_geometry", geometry),
                ("taper_edge_set", edge_set),
                ("offset", 1.2),
                ("angle", 2.3),
                ("ply_cut_off_type", PlyCutOffType.ANALYSIS_PLY_CUTOFF),
                ("ply_tapering", True),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = parent_object.create_cut_off_selection_rule()
    assert isinstance(rule.elemental_data, CutOffSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, CutOffSelectionRuleNodalData)
