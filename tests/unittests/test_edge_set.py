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

from ansys.acp.core import EdgeSetType

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_edge_set()


class TestEdgeSet(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "edge_sets"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "edge_set_type": EdgeSetType.BY_REFERENCE,
            "element_set": None,
            "defining_node_labels": tuple(),
            "limit_angle": -1.0,
            "origin": (0.0, 0.0, 0.0),
        }

    CREATE_METHOD_NAME = "create_edge_set"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        element_set = model.create_element_set()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Edge set name"),
                ("edge_set_type", EdgeSetType.BY_NODES),
                ("element_set", element_set),
                ("limit_angle", 3.21),
                ("origin", (2.0, 3.0, 1.0)),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )
