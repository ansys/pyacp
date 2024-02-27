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

from .common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_rosette()


class TestRosette(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "rosettes"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "locked": False,
            "origin": (0.0, 0.0, 0.0),
            "dir1": (1.0, 0.0, 0.0),
            "dir2": (0.0, 1.0, 0.0),
        }

    CREATE_METHOD_NAME = "create_rosette"
    INITIAL_OBJECT_NAMES = ("Global Coordinate System",)

    @staticmethod
    @pytest.fixture
    def object_properties():
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
                ("origin", (2.0, 3.0, 1.0)),
                ("dir1", (0.0, 0.0, 1.0)),
                ("dir2", (1.0, 0.0, 0.0)),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("locked", True),
            ],
        )
