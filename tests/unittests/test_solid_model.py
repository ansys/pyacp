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

import pathlib
import tempfile

from hypothesis import HealthCheck, assume, given, settings
import hypothesis.strategies as st
from packaging.version import parse as parse_version
import pytest

import ansys.acp.core as pyacp

from .common.tree_object_tester import (
    ObjectPropertiesToTest,
    PropertyWithCustomComparison,
    TreeObjectTester,
    WithLockedMixin,
)


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(
        pyacp.SolidModel._SUPPORTED_SINCE
    ):
        pytest.skip("SolidModel is not supported on this version of the server.")


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
                        initial_value=pyacp.SolidModelExportSettings(
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
    assert (
        solid_model.drop_off_settings.dropoff_disabled_on_bottom_sets
        == dropoff_disabled_on_bottom_sets
    )
    assert (
        solid_model.drop_off_settings.dropoff_disabled_on_top_sets == dropoff_disabled_on_top_sets
    )


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
    assert (
        solid_model.drop_off_settings.dropoff_disabled_on_bottom_sets
        == dropoff_disabled_on_bottom_sets
    )
    assert (
        solid_model.drop_off_settings.dropoff_disabled_on_top_sets == dropoff_disabled_on_top_sets
    )


def test_drop_off_settings_assign_wrong_type(parent_object):
    """Check that assigning the wrong type to the drop-off settings raises an exception."""

    solid_model = parent_object.create_solid_model()
    with pytest.raises(TypeError):
        solid_model.drop_off_settings = "wrong_type"


def test_drop_off_settings_string_representation(parent_object):
    """Check that the string representation of the drop-off settings is correct."""
    solid_model = parent_object.create_solid_model()
    dropoff_disabled_on_bottom_sets = [
        parent_object.create_element_set(),
        parent_object.create_oriented_selection_set(),
    ]
    dropoff_disabled_on_top_sets = [
        parent_object.create_oriented_selection_set(),
        parent_object.create_element_set(),
    ]

    drop_off_settings = pyacp.DropOffSettings(
        drop_off_type=pyacp.DropOffType.OUTSIDE_PLY,
        disable_dropoffs_on_bottom=True,
        dropoff_disabled_on_bottom_sets=dropoff_disabled_on_bottom_sets,
        disable_dropoffs_on_top=True,
        dropoff_disabled_on_top_sets=dropoff_disabled_on_top_sets,
        connect_butt_joined_plies=False,
    )
    # When the drop-off settings are not yet linked to the server, the linked
    # object lists cannot instantiate the objects. Therefore, the string representation
    # will contain '<unavailable>' for the linked objects.
    assert "<unavailable>" in str(drop_off_settings)
    # Assign the drop-off settings to the solid model, to establish the
    # link to the server
    solid_model.drop_off_settings = drop_off_settings
    str_repr = str(solid_model.drop_off_settings)
    assert "DropOffSettings" in str_repr
    for val in dropoff_disabled_on_bottom_sets + dropoff_disabled_on_top_sets:
        assert repr(val) in str_repr


@pytest.mark.parametrize(
    "format",
    [
        "ansys:h5",
        "ansys:cdb",
        pyacp.SolidModelExportFormat.ANSYS_H5,
        pyacp.SolidModelExportFormat.ANSYS_CDB,
    ],
)
def test_solid_model_export(acp_instance, parent_object, format):
    """Check that the export to a file works."""
    model = parent_object
    solid_model = model.create_solid_model()
    solid_model.element_sets = [model.element_sets["All_Elements"]]
    model.update()

    with tempfile.TemporaryDirectory() as tmp_dir:
        if format == "ansys:h5":
            ext = ".h5"
        else:
            ext = ".cdb"

        out_file_name = f"out_file{ext}"
        out_path = pathlib.Path(tmp_dir) / out_file_name

        if not acp_instance.is_remote:
            # save directly to the local file, to avoid a copy in the working directory
            out_file_name = out_path  # type: ignore

        solid_model.export(path=out_file_name, format=format)
        acp_instance.download_file(out_file_name, out_path)

        assert out_path.exists()
        assert out_path.stat().st_size > 0


@given(invalid_format=st.text())
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture], deadline=None)
def test_export_with_invalid_format_raises(parent_object, invalid_format):
    """Check that the export to a file with an invalid format raises an exception."""
    assume(invalid_format not in ["ansys:h5", "ansys:cdb"])

    model = parent_object
    solid_model = model.create_solid_model()
    solid_model.element_sets = [model.element_sets["All_Elements"]]
    model.update()

    with tempfile.TemporaryDirectory() as tmp_dir:
        out_file_name = f"out_file.h5"
        out_path = pathlib.Path(tmp_dir) / out_file_name

        with pytest.raises(ValueError):
            solid_model.export(path=out_path, format=invalid_format)


@pytest.mark.parametrize("format", ["ansys:cdb", "step", "iges", "stl"])
def test_solid_model_skin_export(acp_instance, parent_object, format):
    """Check that the skin export to a file works."""
    model = parent_object
    solid_model = model.create_solid_model()
    solid_model.element_sets = [model.element_sets["All_Elements"]]
    model.update()

    with tempfile.TemporaryDirectory() as tmp_dir:
        ext = {"ansys:cdb": ".cdb", "step": ".stp", "iges": ".igs", "stl": ".stl"}[format]
        out_file_name = f"out_file{ext}"
        out_path = pathlib.Path(tmp_dir) / out_file_name

        if not acp_instance.is_remote:
            # save directly to the local file, to avoid a copy in the working directory
            out_file_name = out_path  # type: ignore

        solid_model.export_skin(path=out_file_name, format=format)
        acp_instance.download_file(out_file_name, out_path)

        assert out_path.exists()
        assert out_path.stat().st_size > 0


@given(invalid_format=st.text())
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture], deadline=None)
def test_skin_export_with_invalid_format_raises(parent_object, invalid_format):
    """Check that the export to a file with an invalid format raises an exception."""
    assume(invalid_format not in ["ansys:cdb", "step", "iges", "stl"])

    model = parent_object
    solid_model = model.create_solid_model()
    solid_model.element_sets = [model.element_sets["All_Elements"]]
    model.update()

    with tempfile.TemporaryDirectory() as tmp_dir:
        out_file_name = f"out_file.stp"
        out_path = pathlib.Path(tmp_dir) / out_file_name

        with pytest.raises(ValueError):
            solid_model.export_skin(path=out_path, format=invalid_format)


def test_elemental_data(parent_object):
    """Check that the elemental data can be accessed."""
    model = parent_object
    model.fabrics["Fabric.1"].thickness = 0.1

    solid_model = model.create_solid_model()
    solid_model.element_sets = [model.element_sets["All_Elements"]]
    model.update()

    elemental_data = solid_model.elemental_data
    empty_keys = [key for key, value in vars(elemental_data).items() if value is None]
    assert not empty_keys, f"Keys with None values: {empty_keys}"


def test_nodal_data(parent_object):
    """Check that the nodal data can be accessed."""
    model = parent_object
    model.fabrics["Fabric.1"].thickness = 0.1

    solid_model = model.create_solid_model()
    solid_model.element_sets = [model.element_sets["All_Elements"]]
    model.update()

    nodal_data = solid_model.nodal_data
    empty_keys = [key for key, value in vars(nodal_data).items() if value is None]
    assert not empty_keys, f"Keys with None values: {empty_keys}"
