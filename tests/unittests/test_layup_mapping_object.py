# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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

from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import (
    BaseElementMaterialHandling,
    ElementTechnology,
    LayupMappingObject,
    LayupMappingRosetteSelectionMethod,
    ReinforcingBehavior,
    StressStateType,
)

from .common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(
        LayupMappingObject._SUPPORTED_SINCE
    ):
        pytest.skip("LayupMappingObject is not supported on this version of the server.")


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def parent_object(model):
    return model.create_imported_solid_model()


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_layup_mapping_object()


class TestLayupMappingObject(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "layup_mapping_objects"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "active": True,
            "element_technology": ElementTechnology.LAYERED_ELEMENT,
            "shell_element_sets": tuple(),
            "use_imported_plies": False,
            "select_all_plies": True,
            "sequences": tuple(),
            "entire_solid_mesh": True,
            "solid_element_sets": tuple(),
            "scale_ply_thicknesses": True,
            "void_material": None,
            "minimum_void_material_thickness": 1e-6,
            "delete_lost_elements": True,
            "filler_material": None,
            "rosettes": tuple(),
            "rosette_selection_method": LayupMappingRosetteSelectionMethod.MINIMUM_DISTANCE,
            "reinforcing_behavior": ReinforcingBehavior.TENSION_AND_COMPRESSION,
            "base_element_material_handling": BaseElementMaterialHandling.REMOVE,
            "stress_state": StressStateType.PLANE_STRESS_STATE_WITH_TRANSVERSE_SHEAR_AND_BENDING_STIFFNESS,
            "base_material": None,
            "base_element_rosettes": tuple(),
            "base_element_rosette_selection_method": LayupMappingRosetteSelectionMethod.MINIMUM_DISTANCE,
        }

    CREATE_METHOD_NAME = "create_layup_mapping_object"
    INITIAL_OBJECT_NAMES = tuple()

    @staticmethod
    @pytest.fixture
    def object_properties(model):
        modeling_group = model.create_modeling_group()
        imported_modeling_group = model.create_imported_modeling_group()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_layup_mapping_object"),
                ("active", False),
                ("element_technology", ElementTechnology.REINFORCING),
                ("shell_element_sets", [model.create_element_set() for _ in range(3)]),
                ("select_all_plies", False),
                (
                    "sequences",
                    [modeling_group.create_modeling_ply(), model.create_modeling_group()],
                ),
                ("use_imported_plies", True),
                (
                    "sequences",
                    [
                        imported_modeling_group.create_imported_modeling_ply(),
                        model.create_imported_modeling_group(),
                    ],
                ),
                ("entire_solid_mesh", False),
                # Note: solid_element_sets is not tested because we would need to
                # create a fully-defined solid model
                ("scale_ply_thicknesses", False),
                ("void_material", model.create_material()),
                ("minimum_void_material_thickness", 1e-3),
                ("delete_lost_elements", False),
                ("filler_material", model.create_material()),
                ("rosettes", [model.create_rosette() for _ in range(3)]),
                (
                    "rosette_selection_method",
                    LayupMappingRosetteSelectionMethod.MINIMUM_DISTANCE_SUPERPOSED,
                ),
                ("reinforcing_behavior", ReinforcingBehavior.TENSION_ONLY),
                ("base_element_material_handling", BaseElementMaterialHandling.RETAIN),
                ("stress_state", StressStateType.PLANE_STRESS_STATE),
                ("base_material", model.create_material()),
                ("base_element_rosettes", [model.create_rosette() for _ in range(3)]),
                (
                    "base_element_rosette_selection_method",
                    LayupMappingRosetteSelectionMethod.MINIMUM_DISTANCE_SUPERPOSED,
                ),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )
