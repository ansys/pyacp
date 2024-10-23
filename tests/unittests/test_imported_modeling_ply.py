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
from packaging.version import parse as parse_version


from ansys.acp.core import (
    ImportedPlyDrapingType,
    ImportedPlyOffsetType,
    ImportedPlyThicknessType,
    ImportedModelingPly,
    MeshImportType,
    RosetteSelectionMethod,
    ThicknessFieldType,
)

from .common.linked_object_list_tester import LinkedObjectListTestCase, LinkedObjectListTester
from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(
        ImportedModelingPly._SUPPORTED_SINCE
    ):
        pytest.skip("ImportedModelingPly is not supported on this version of the server.")


@pytest.fixture
def minimal_complete_model(load_model_imported_plies_from_tempfile):
    with load_model_imported_plies_from_tempfile() as model:
        yield model


@pytest.fixture
def parent_object(minimal_complete_model):
    return minimal_complete_model.imported_modeling_groups["by hdf5"]


@pytest.fixture
def existing_imported_modeling_ply(minimal_complete_model):
    return minimal_complete_model.imported_modeling_groups["by hdf5"].imported_modeling_plies["ud"]


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_imported_modeling_ply()


class TestImportedModelingPly(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "imported_modeling_plies"
    CREATE_METHOD_NAME = "create_imported_modeling_ply"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "active": True,
            "offset_type": ImportedPlyOffsetType.MIDDLE_OFFSET,
            "mesh_import_type": MeshImportType.FROM_GEOMETRY,
            "rosette_selection_method": "minimum_angle",
            "rosettes": [],
            "reference_direction_field": None,
            "rotation_angle": 0.0,
            "ply_material": None,
            "ply_angle": 0.0,
            "draping": ImportedPlyDrapingType.NO_DRAPING,
            "draping_angle_1_field": None,
            "draping_angle_2_field": None,
            "thickness_type": ImportedPlyThicknessType.NOMINAL,
            "thickness_field": None,
            "thickness_field_type": ThicknessFieldType.ABSOLUTE_VALUES,
        }

    @staticmethod
    @pytest.fixture(params=[v.value for v in ImportedPlyOffsetType])
    def object_properties(request, minimal_complete_model):
        ply_material = minimal_complete_model.create_fabric()
        create_lut_method = getattr(minimal_complete_model, "create_lookup_table_1d")
        lookup_table = create_lut_method()
        column_1 = lookup_table.create_column()
        column_2 = lookup_table.create_column()
        rosette = minimal_complete_model.create_rosette()
        virtual_geometry = minimal_complete_model.create_virtual_geometry()

        return ObjectPropertiesToTest(
            read_write=[
                ("active", False),
                ("offset_type", request.param),
                ("mesh_import_type", MeshImportType.FROM_GEOMETRY),
                ("mesh_geometry", virtual_geometry),
                ("rosette_selection_method", RosetteSelectionMethod.MINIMUM_DISTANCE),
                ("rosettes", [rosette]),
                ("reference_direction_field", column_1),
                ("rotation_angle", 67.2),
                ("ply_material", ply_material),
                ("ply_angle", 34.5),
                ("draping", ImportedPlyDrapingType.TABULAR_VALUES),
                ("draping_angle_1_field", column_1),
                ("draping_angle_2_field", column_2),
                ("thickness_type", ImportedPlyThicknessType.FROM_TABLE),
                ("thickness_field", column_1),
                ("thickness_field_type", ThicknessFieldType.RELATIVE_SCALING_FACTOR),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


@pytest.fixture
def linked_object_case(tree_object, minimal_complete_model):
    return LinkedObjectListTestCase(
        parent_object=tree_object,
        linked_attribute_name="rosettes",
        existing_linked_object_names=(),
        linked_object_constructor=minimal_complete_model.create_rosette,
    )


linked_object_case_empty = linked_object_case


@pytest.fixture
def linked_object_case_nonempty(tree_object, minimal_complete_model):
    tree_object.rosettes = [minimal_complete_model.create_rosette(name="rosette 32")]
    return LinkedObjectListTestCase(
        parent_object=tree_object,
        linked_attribute_name="rosettes",
        existing_linked_object_names=("rosette 32",),
        linked_object_constructor=minimal_complete_model.create_rosette,
    )


class TestLinkedObjectLists(LinkedObjectListTester):
    pass
