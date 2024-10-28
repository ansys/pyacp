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

from hypothesis import HealthCheck, given, settings
import hypothesis.strategies as st
import pytest

import ansys.acp.core as pyacp

from .common.tree_object_tester import (
    ObjectPropertiesToTest,
    PropertyWithCustomComparison,
    TreeObjectTester,
    WithLockedMixin,
)


def compare_pb_object(given, expected):
    if not isinstance(given, type(expected)):
        return False
    return given._pb_object == expected._pb_object


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_solid_model()


class TestSolidModel(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "solid_models"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
        }

    CREATE_METHOD_NAME = "create_solid_model"
    INITIAL_OBJECT_NAMES = tuple()

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        modeling_group = model.create_modeling_group()

        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
                ("active", False),
                (
                    "element_sets",
                    [model.create_element_set(), model.create_oriented_selection_set()],
                ),
                ("extrusion_method", pyacp.ExtrusionMethodType.MONOLITHIC),
                ("max_element_thickness", 12.3),
                ("ply_group_pointers", [modeling_group.create_modeling_ply() for _ in range(3)]),
                ("offset_direction", pyacp.OffsetDirectionType.SURFACE_NORMAL),
                ("skip_elements_without_plies", True),
                ("drop_off_material", model.create_material()),
                ("cut_off_material", model.create_material()),
                ("delete_bad_elements", False),
                ("warping_limit", 0.6),
                ("minimum_volume", 1.2),
                (
                    "drop_off_settings",
                    PropertyWithCustomComparison(
                        initial_value=pyacp.DropOffSettings(
                            drop_off_type=pyacp.DropOffType.OUTSIDE_PLY,
                            disable_dropoffs_on_bottom=True,
                            dropoff_disabled_on_bottom_sets=[
                                model.create_element_set(),
                                model.create_oriented_selection_set(),
                            ],
                            disable_dropoffs_on_top=True,
                            dropoff_disabled_on_top_sets=[
                                model.create_oriented_selection_set(),
                                model.create_element_set(),
                            ],
                            connect_butt_joined_plies=False,
                        ),
                        comparison_function=compare_pb_object,
                    ),
                ),
                (
                    "export_settings",
                    PropertyWithCustomComparison(
                        initial_value=pyacp.ExportSettings(
                            use_default_section_index=False,
                            section_index=2,
                            use_default_coordinate_system_index=False,
                            coordinate_system_index=3,
                            use_default_material_index=False,
                            material_index=4,
                            use_default_node_index=False,
                            node_index=5,
                            use_default_element_index=False,
                            element_index=6,
                            use_solsh_elements=True,
                            write_degenerated_elements=False,
                            drop_hanging_nodes=False,
                            use_solid_model_prefix=False,
                            transfer_all_sets=False,
                            transferred_element_sets=[model.create_element_set() for _ in range(2)],
                            transferred_edge_sets=[model.create_edge_set() for _ in range(3)],
                        ),
                        comparison_function=compare_pb_object,
                    ),
                ),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("locked", True),
            ],
        )


@given(
    disable_dropoffs_on_bottom=st.booleans(),
    disable_dropoffs_on_top=st.booleans(),
    connect_butt_joined_plies=st.booleans(),
)
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture], deadline=None)
def test_drop_off_settings_on_init(
    parent_object, disable_dropoffs_on_bottom, disable_dropoffs_on_top, connect_butt_joined_plies
):
    """Check that the drop-off settings are correctly set when passed to the SolidModel constructor."""
    dropoff_disabled_on_bottom_sets = [
        parent_object.create_element_set(),
        parent_object.create_oriented_selection_set(),
    ]
    dropoff_disabled_on_top_sets = [
        parent_object.create_oriented_selection_set(),
        parent_object.create_element_set(),
    ]

    drop_off_settings = pyacp.DropOffSettings(
        disable_dropoffs_on_bottom=disable_dropoffs_on_bottom,
        dropoff_disabled_on_bottom_sets=dropoff_disabled_on_bottom_sets,
        disable_dropoffs_on_top=disable_dropoffs_on_top,
        dropoff_disabled_on_top_sets=dropoff_disabled_on_top_sets,
        connect_butt_joined_plies=connect_butt_joined_plies,
    )

    solid_model = parent_object.create_solid_model(drop_off_settings=drop_off_settings)
    assert solid_model.drop_off_settings.disable_dropoffs_on_bottom == disable_dropoffs_on_bottom
    assert solid_model.drop_off_settings.disable_dropoffs_on_top == disable_dropoffs_on_top
    assert solid_model.drop_off_settings.connect_butt_joined_plies == connect_butt_joined_plies
    assert solid_model.drop_off_settings.disable_dropoffs_on_bottom == disable_dropoffs_on_bottom
    assert solid_model.drop_off_settings.disable_dropoffs_on_top == disable_dropoffs_on_top


@given(
    disable_dropoffs_on_bottom=st.booleans(),
    disable_dropoffs_on_top=st.booleans(),
    connect_butt_joined_plies=st.booleans(),
)
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture], deadline=None)
def test_drop_off_settings_assign(
    parent_object, disable_dropoffs_on_bottom, disable_dropoffs_on_top, connect_butt_joined_plies
):
    """Check that the drop-off settings are correctly set when assigned to the SolidModel."""
    dropoff_disabled_on_bottom_sets = [
        parent_object.create_element_set(),
        parent_object.create_oriented_selection_set(),
    ]
    dropoff_disabled_on_top_sets = [
        parent_object.create_oriented_selection_set(),
        parent_object.create_element_set(),
    ]

    drop_off_settings = pyacp.DropOffSettings(
        disable_dropoffs_on_bottom=disable_dropoffs_on_bottom,
        dropoff_disabled_on_bottom_sets=dropoff_disabled_on_bottom_sets,
        disable_dropoffs_on_top=disable_dropoffs_on_top,
        dropoff_disabled_on_top_sets=dropoff_disabled_on_top_sets,
        connect_butt_joined_plies=connect_butt_joined_plies,
    )

    solid_model = parent_object.create_solid_model()
    solid_model.drop_off_settings = drop_off_settings
    assert solid_model.drop_off_settings.disable_dropoffs_on_bottom == disable_dropoffs_on_bottom
    assert solid_model.drop_off_settings.disable_dropoffs_on_top == disable_dropoffs_on_top
    assert solid_model.drop_off_settings.connect_butt_joined_plies == connect_butt_joined_plies
    assert solid_model.drop_off_settings.disable_dropoffs_on_bottom == disable_dropoffs_on_bottom
    assert solid_model.drop_off_settings.disable_dropoffs_on_top == disable_dropoffs_on_top
    assert solid_model.drop_off_settings.connect_butt_joined_plies == connect_butt_joined_plies
    assert solid_model.drop_off_settings.disable_dropoffs_on_bottom == disable_dropoffs_on_bottom
    assert solid_model.drop_off_settings.disable_dropoffs_on_top == disable_dropoffs_on_top
