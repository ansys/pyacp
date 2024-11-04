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

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester
from .common.linked_object_list_tester import LinkedObjectListTestCase, LinkedObjectListTester

@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_field_definition()


class TestFieldDefinition(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "field_definitions"

    @staticmethod
    @pytest.fixture
    def default_properties(acp_instance):
        return {
            "status": "NOTUPTODATE",
            "active": True,
            "scalar_field": None,
            "scope_entities": tuple(),
            "full_mapping": False,
        }
    CREATE_METHOD_NAME = "create_field_definition"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object, acp_instance):
        model = parent_object
        lut_3D = model.create_lookup_table_3d(name="LUT 3D")
        lut_col = lut_3D.create_column(name="Column 1")
        el_set = model.create_element_set(name="my element set")
        mg = model.create_modeling_group(name="my modeling group")
        modeling_ply = mg.create_modeling_ply(name="my Modeling Ply")
        oss = model.create_oriented_selection_set(name="my OSS")

        return ObjectPropertiesToTest(
            read_write=[
                ("name", "FD name"),
                ("active", False),
                ("scalar_field", lut_col),
                ("scope_entities", [el_set, modeling_ply, oss]),
                ("full_mapping", True),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


@pytest.fixture
def linked_object_case(tree_object, parent_object):
    return LinkedObjectListTestCase(
        parent_object=tree_object,
        linked_attribute_name="scope_entities",
        existing_linked_object_names=(),
        linked_object_constructor=parent_object.create_element_set,
    )


linked_object_case_empty = linked_object_case


@pytest.fixture
def linked_object_case_nonempty(tree_object, parent_object):
    tree_object.scope_entities = [parent_object.create_oriented_selection_set(name="OSS.1")]
    return LinkedObjectListTestCase(
        parent_object=tree_object,
        linked_attribute_name="scope_entities",
        existing_linked_object_names=("OSS.1",),
        linked_object_constructor=parent_object.create_oriented_selection_set,
    )


class TestLinkedObjectLists(LinkedObjectListTester):
    pass
