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

from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import CutOffGeometry, CutOffGeometryOrientationType

from .common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(CutOffGeometry._SUPPORTED_SINCE):
        pytest.skip("CutOffGeometry is not supported on this version of the server.")


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture(params=["create_solid_model", "create_imported_solid_model"])
def parent_object(model, request):
    return getattr(model, request.param)()


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_cut_off_geometry()


class TestCutOffGeometry(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "cut_off_geometries"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "active": True,
            "cad_geometry": None,
            "orientation": CutOffGeometryOrientationType.UP,
            "relative_merge_tolerance": 0.1,
        }

    CREATE_METHOD_NAME = "create_cut_off_geometry"
    INITIAL_OBJECT_NAMES = tuple()

    @staticmethod
    @pytest.fixture
    def object_properties(model):
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_cut_off_geometry"),
                ("active", False),
                ("cad_geometry", model.create_virtual_geometry()),
                ("orientation", CutOffGeometryOrientationType.DOWN),
                ("relative_merge_tolerance", 0.1257),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )
