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
    SphericalSelectionRuleElementalData,
    SphericalSelectionRuleNodalData,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_spherical_selection_rule()


class TestSphericalSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "spherical_selection_rules"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "use_global_coordinate_system": True,
            "rosette": None,
            "origin": (0.0, 0.0, 0.0),
            "radius": 0.0,
            "relative_rule": False,
            "include_rule": True,
        }

    CREATE_METHOD_NAME = "create_spherical_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        rosette = model.create_rosette()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Spherical Selection Rule name"),
                ("use_global_coordinate_system", False),
                ("rosette", rosette),
                ("origin", (1.0, 2.0, 3.0)),
                ("radius", 4.0),
                ("relative_rule", True),
                ("include_rule", False),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = parent_object.create_spherical_selection_rule()
    assert isinstance(rule.elemental_data, SphericalSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, SphericalSelectionRuleNodalData)
