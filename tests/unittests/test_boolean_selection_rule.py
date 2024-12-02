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

from ansys.acp.core import BooleanOperationType, LinkedSelectionRule
from ansys.acp.core.mesh_data import (
    BooleanSelectionRuleElementalData,
    BooleanSelectionRuleNodalData,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_boolean_selection_rule()


class TestBooleanSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "boolean_selection_rules"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "selection_rules": [],
            "include_rule": True,
        }

    CREATE_METHOD_NAME = "create_boolean_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        material = model.create_material()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Boolean Selection Rule name"),
                (
                    "selection_rules",
                    [
                        LinkedSelectionRule(
                            selection_rule=model.create_parallel_selection_rule(),
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=False,
                            parameter_1=1.0,
                            parameter_2=2.0,
                        ),
                        LinkedSelectionRule(
                            selection_rule=model.create_cylindrical_selection_rule(),
                            operation_type=BooleanOperationType.ADD,
                            template_rule=True,
                            parameter_1=1.1,
                            parameter_2=2.2,
                        ),
                        LinkedSelectionRule(
                            selection_rule=model.create_spherical_selection_rule(),
                            operation_type=BooleanOperationType.REMOVE,
                            template_rule=True,
                            parameter_1=2.3,
                            parameter_2=-1.3,
                        ),
                        LinkedSelectionRule(
                            selection_rule=model.create_tube_selection_rule(),
                            operation_type=BooleanOperationType.INTERSECT,
                            template_rule=False,
                            parameter_1=1.3,
                            parameter_2=2.9,
                        ),
                        LinkedSelectionRule(
                            selection_rule=model.create_geometrical_selection_rule(),
                            operation_type=BooleanOperationType.REMOVE,
                            template_rule=False,
                            parameter_1=1.5,
                            parameter_2=2.5,
                        ),
                        LinkedSelectionRule(
                            selection_rule=model.create_variable_offset_selection_rule(),
                            operation_type=BooleanOperationType.ADD,
                            template_rule=False,
                            parameter_1=0.0,
                            parameter_2=0.0,
                        ),
                    ],
                ),
                ("include_rule", False),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = parent_object.create_boolean_selection_rule()
    assert isinstance(rule.elemental_data, BooleanSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, BooleanSelectionRuleNodalData)


def test_add_method(parent_object):
    """Verify add method for selection rule."""
    boolean_rule = parent_object.create_boolean_selection_rule()
    parallel_rule = parent_object.create_parallel_selection_rule()
    linked_rule = boolean_rule.add_selection_rule(parallel_rule)
    assert linked_rule.selection_rule == parallel_rule

    tube_rule = parent_object.create_tube_selection_rule()
    linked_rule = boolean_rule.add_selection_rule(
        tube_rule,
        operation_type=BooleanOperationType.REMOVE,
        template_rule=True,
        parameter_1=3.2,
        parameter_2=5.4,
    )
    assert linked_rule.selection_rule == tube_rule
    assert linked_rule.operation_type == BooleanOperationType.REMOVE
    assert linked_rule.template_rule
    assert linked_rule.parameter_1 == 3.2
    assert linked_rule.parameter_2 == 5.4
