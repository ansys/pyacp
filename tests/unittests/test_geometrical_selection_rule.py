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

from ansys.acp.core import (
    GeometricalRuleType,
    GeometricalSelectionRuleElementalData,
    GeometricalSelectionRuleNodalData,
)

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_geometrical_selection_rule()


class TestGeometricalSelectionRule(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "geometrical_selection_rules"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "geometrical_rule_type": GeometricalRuleType.GEOMETRY,
            "geometry": None,
            "element_sets": [],
            "include_rule": True,
            "use_default_tolerances": True,
            "in_plane_capture_tolerance": 0.0,
            "negative_capture_tolerance": 0.0,
            "positive_capture_tolerance": 0.0,
        }

    CREATE_METHOD_NAME = "create_geometrical_selection_rule"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        geometry = model.create_virtual_geometry()
        element_sets = [model.create_element_set() for _ in range(3)]
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Geometrical Selection Rule name"),
                ("geometrical_rule_type", GeometricalRuleType.ELEMENT_SETS),
                ("geometry", geometry),
                ("element_sets", element_sets),
                ("include_rule", False),
                ("use_default_tolerances", False),
                ("in_plane_capture_tolerance", 1.2),
                ("negative_capture_tolerance", 2.3),
                ("positive_capture_tolerance", 3.4),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_mesh_data(parent_object):
    rule = parent_object.create_geometrical_selection_rule()
    assert isinstance(rule.elemental_data, GeometricalSelectionRuleElementalData)
    assert isinstance(rule.nodal_data, GeometricalSelectionRuleNodalData)


def test_error_message_when_cad_geometry_passed(parent_object):
    """Test that passing a CAD Geometry instead of a Virtual Geometry produces a nice error message."""

    rule = parent_object.create_geometrical_selection_rule()
    cad_geometry = parent_object.create_cad_geometry()
    with pytest.raises(TypeError) as exc_info:
        rule.geometry = cad_geometry
    assert "VirtualGeometry" in str(exc_info.value)
    assert "CADGeometry" in str(exc_info.value)
