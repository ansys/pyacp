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

import pytest

from .common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_element_set()


@pytest.fixture
def object_properties():
    return ObjectPropertiesToTest(
        read_write=[
            ("name", "new_name"),
            ("middle_offset", True),
            ("element_labels", (1, 2, 3, 4)),
        ],
        read_only=[
            ("id", "some_id"),
            ("status", "UPTODATE"),
        ],
    )


class TestElementSet(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "element_sets"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "locked": False,
            "middle_offset": False,
            "element_labels": tuple(),
        }

    CREATE_METHOD_NAME = "create_element_set"
    INITIAL_OBJECT_NAMES = ("All_Elements",)


def test_clone_locked(parent_object, skip_before_version):
    """Test that a locked element set can be correctly cloned.

    Regression test for #565: cloning and storing a locked element
    set produces an empty element set.
    The root cause for this issue was that the locked element set
    did not expose their 'element_labels' in the API.ga
    """
    skip_before_version("25.1")

    element_set = parent_object.element_sets["All_Elements"]
    assert len(element_set.element_labels) > 0
    cloned_element_set = element_set.clone()
    cloned_element_set.store(parent=parent_object)
    assert not cloned_element_set.locked
    assert len(cloned_element_set.element_labels) > 0
