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

from ansys.acp.core.mesh_data import (
    VariableOffsetSelectionRuleElementalData,
    VariableOffsetSelectionRuleNodalData,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_variable_offset_selection_rule()


class TestVariableOffsetSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "variable_offset_selection_rules"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "edge_set": None,
            "offsets": None,
            "angles": None,
            "include_rule": True,
            "use_offset_correction": False,
            "element_set": None,
            "inherit_from_lookup_table": True,
            "radius_origin": (0.0, 0.0, 0.0),
            "radius_direction": (1.0, 0.0, 0.0),
            "distance_along_edge": False,
        }

    CREATE_METHOD_NAME = "create_variable_offset_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        edge_set = model.create_edge_set()
        lookup_table = model.create_lookup_table_1d()
        column_1 = lookup_table.create_column()
        column_2 = lookup_table.create_column()
        element_set = model.create_element_set()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Variable Offset Selection Rule name"),
                ("edge_set", edge_set),
                ("offsets", column_1),
                ("angles", column_2),
                ("include_rule", False),
                ("use_offset_correction", True),
                ("element_set", element_set),
                ("inherit_from_lookup_table", False),
                ("radius_origin", (0.1, 0.2, 0.3)),
                ("radius_direction", (0.4, 0.5, 0.6)),
                ("distance_along_edge", True),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = parent_object.create_variable_offset_selection_rule()
    assert isinstance(rule.elemental_data, VariableOffsetSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, VariableOffsetSelectionRuleNodalData)
