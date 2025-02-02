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
from pytest_cases import fixture, parametrize_with_cases

from ansys.acp.core import LookUpTableColumnValueType, RosetteSelectionMethod

from .common.linked_object_list_tester import LinkedObjectListTestCase, LinkedObjectListTester
from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_oriented_selection_set()


class TestOrientedSelectionSet(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "oriented_selection_sets"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "element_sets": [],
            "rosettes": [],
            "orientation_point": (0.0, 0.0, 0.0),
            "orientation_direction": (0.0, 0.0, 0.0),
            "rosette_selection_method": "minimum_angle",
            "draping": False,
            "draping_seed_point": (0.0, 0.0, 0.0),
            "auto_draping_direction": True,
            "draping_direction": (0.0, 0.0, 1.0),
            "use_default_draping_mesh_size": True,
            "draping_mesh_size": 0.0,
            "draping_material_model": "woven",
            "draping_ud_coefficient": 0.0,
            "rotation_angle": 0.0,
        }

    CREATE_METHOD_NAME = "create_oriented_selection_set"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        element_sets = [model.create_element_set() for _ in range(3)]
        rosettes = [model.create_rosette() for _ in range(4)]
        lookup_table_3d = model.create_lookup_table_3d()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
                ("element_sets", element_sets),
                ("orientation_point", (1.2, 6.3, -2.4)),
                ("orientation_direction", (1.0, -0.4, 0.9)),
                ("rosettes", rosettes),
                ("rosette_selection_method", RosetteSelectionMethod.MINIMUM_DISTANCE_SUPERPOSED),
                (
                    "selection_rules",
                    [
                        model.create_tube_selection_rule(),
                        model.create_parallel_selection_rule(),
                        model.create_spherical_selection_rule(),
                        model.create_cylindrical_selection_rule(),
                        model.create_variable_offset_selection_rule(),
                        model.create_boolean_selection_rule(),
                    ],
                ),
                ("draping", True),
                ("draping_seed_point", (0.0, 0.1, 0.0)),
                ("auto_draping_direction", False),
                ("draping_direction", (1.0, 0.0, 0.0)),
                ("use_default_draping_mesh_size", False),
                ("draping_mesh_size", 0.1),
                ("draping_material_model", "ud"),
                ("draping_ud_coefficient", 0.5),
                ("rotation_angle", 22.35),
                (
                    "reference_direction_field",
                    lookup_table_3d.create_column(value_type=LookUpTableColumnValueType.DIRECTION),
                ),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def case_link_to_elset_one_existing(parent_object):
    oss = parent_object.oriented_selection_sets["OrientedSelectionSet.1"]
    yield LinkedObjectListTestCase(
        parent_object=oss,
        linked_attribute_name="element_sets",
        existing_linked_object_names=tuple(["All_Elements"]),
        linked_object_constructor=parent_object.create_element_set,
    )


def case_link_to_elset_empty(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = model.create_oriented_selection_set()
        yield LinkedObjectListTestCase(
            parent_object=oss,
            linked_attribute_name="element_sets",
            existing_linked_object_names=tuple(),
            linked_object_constructor=model.create_element_set,
        )


def case_link_to_rosette_empty(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = model.create_oriented_selection_set()
        yield LinkedObjectListTestCase(
            parent_object=oss,
            linked_attribute_name="rosettes",
            existing_linked_object_names=tuple(),
            linked_object_constructor=model.create_rosette,
        )


def case_link_to_rosette_one_existing(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = model.oriented_selection_sets["OrientedSelectionSet.1"]
        yield LinkedObjectListTestCase(
            parent_object=oss,
            linked_attribute_name="rosettes",
            existing_linked_object_names=tuple(["Global Coordinate System"]),
            linked_object_constructor=model.create_rosette,
        )


@fixture
@parametrize_with_cases("linked_case", cases=".", glob="link_*")
def linked_object_case(linked_case):
    return linked_case


@fixture
@parametrize_with_cases("linked_case", cases=".", glob="link_*_existing")
def linked_object_case_nonempty(linked_case):
    return linked_case


@fixture
@parametrize_with_cases("linked_case", cases=".", glob="link_*_empty")
def linked_object_case_empty(linked_case):
    return linked_case


class TestLinkedObjectLists(LinkedObjectListTester):
    pass
