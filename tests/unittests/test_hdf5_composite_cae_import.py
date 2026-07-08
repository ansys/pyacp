# Copyright (C) 2022 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

from collections import Counter
import pathlib
import tempfile

from packaging.version import parse as parse_version
import pytest

import ansys.acp.core as pyacp

from .common.tree_object_tester import (
    NoLockedMixin,
    ObjectPropertiesToTest,
    PropertyWithCustomComparison,
    TreeObjectTester,
)


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version("27.1"):
        pytest.skip("HDF5CompositeCAEImport is not supported on this version of the server.")


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
    return parent_object.create_hdf5_composite_cae_import()


class TestHDF5CompositeCAEImport(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "hdf5_composite_cae_imports"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "path": "",
            "projection_mode": pyacp.HDF5CompositeCAEProjectionMode.SHELL,
            "minimum_angle_tolerance": 0.001,
            "recompute_reference_directions": False,
            "shell_mapping_properties": PropertyWithCustomComparison(
                pyacp.ShellMappingProperties(
                    all_elements=True,
                    element_sets=[],
                    relative_thickness_tolerance=0.5,
                    relative_in_plane_tolerance=0.01,
                    angle_tolerance=35.0,
                    small_hole_threshold=0.0,
                ),
                comparison_function=compare_pb_object,
            ),
            "solid_mapping_properties": PropertyWithCustomComparison(
                pyacp.SolidMappingProperties(
                    offset_type=pyacp.OffsetType.BOTTOM_OFFSET,
                ),
                comparison_function=compare_pb_object,
            ),
            "coordinate_transformation": PropertyWithCustomComparison(
                pyacp.CoordinateTransformation(
                    rotation_angle_x=0.0,
                    rotation_angle_y=0.0,
                    rotation_angle_z=0.0,
                    translation_x=0.0,
                    translation_y=0.0,
                    translation_z=0.0,
                ),
                comparison_function=compare_pb_object,
            ),
        }

    CREATE_METHOD_NAME = "create_hdf5_composite_cae_import"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
                ("path", "path/to/model_export.h5"),
                ("projection_mode", pyacp.HDF5CompositeCAEProjectionMode.SOLID),
                ("minimum_angle_tolerance", 1.23),
                ("recompute_reference_directions", True),
                (
                    "shell_mapping_properties",
                    PropertyWithCustomComparison(
                        initial_value=pyacp.ShellMappingProperties(
                            all_elements=False,
                            element_sets=[model.create_element_set(), model.create_element_set()],
                            relative_thickness_tolerance=0.4,
                            relative_in_plane_tolerance=0.02,
                            angle_tolerance=25.0,
                            small_hole_threshold=1.5,
                        ),
                        comparison_function=compare_pb_object,
                    ),
                ),
                (
                    "solid_mapping_properties",
                    PropertyWithCustomComparison(
                        initial_value=pyacp.SolidMappingProperties(
                            offset_type=pyacp.OffsetType.TOP_OFFSET,
                        ),
                        comparison_function=compare_pb_object,
                    ),
                ),
                (
                    "coordinate_transformation",
                    PropertyWithCustomComparison(
                        initial_value=pyacp.CoordinateTransformation(
                            rotation_angle_x=10.1,
                            rotation_angle_y=20.2,
                            rotation_angle_z=30.3,
                            translation_x=1.1,
                            translation_y=2.2,
                            translation_z=3.3,
                        ),
                        comparison_function=compare_pb_object,
                    ),
                ),
            ],
            read_only=[
                ("id", "some_id"),
            ],
        )


@pytest.fixture
def model_with_h5_export(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        with tempfile.TemporaryDirectory() as tmp_dir:
            export_file = pathlib.Path(tmp_dir) / "model_export.h5"
            model.export_hdf5_composite_cae(export_file)
            yield model, export_file


def test_run_method(model_with_h5_export):
    """
    Test the run method of HDF5CompositeCAEImport.
    """
    model, export_file = model_with_h5_export
    hdf5_import = model.create_hdf5_composite_cae_import(
        path=export_file,
    )
    hdf5_import.run()


def test_list_delete_generated_objects(model_with_h5_export):
    """
    Test the list_generated_objects and delete_generated_objects method of HDF5CompositeCAEImport.
    """
    # GIVEN: A model with an exported HDF5 Composite CAE file
    model, export_file = model_with_h5_export
    hdf5_import = model.create_hdf5_composite_cae_import(
        path=export_file,
    )

    # WHEN: The run method has not been called yet
    # THEN:
    # - list_generated_objects should return an empty list
    # - delete_generated_objects should not raise an error
    generated_objects = hdf5_import.list_generated_objects()
    assert generated_objects == []
    hdf5_import.delete_generated_objects()

    # WHEN: The run method is called
    hdf5_import.run()

    # THEN: list_generated_objects should return a non-empty list of generated objects
    generated_objects = hdf5_import.list_generated_objects()
    assert len(generated_objects) > 0
    # Check expected object types and counts
    assert Counter(type(obj) for obj in generated_objects) == {
        pyacp.ElementSet: 2,
        pyacp.Material: 1,
        pyacp.Fabric: 1,
        pyacp.LookUpTable3D: 1,
        pyacp.OrientedSelectionSet: 1,
        pyacp.Rosette: 1,
        pyacp.ModelingPly: 1,
        pyacp.ModelingGroup: 1,
    }

    # WHEN: The delete_generated_objects method is called
    hdf5_import.delete_generated_objects()

    # THEN: list_generated_objects should return an empty list again
    generated_objects = hdf5_import.list_generated_objects()
    assert generated_objects == []
