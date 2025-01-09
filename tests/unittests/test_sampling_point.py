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

from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import SamplingPoint

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(SamplingPoint._SUPPORTED_SINCE):
        pytest.skip("InterfaceLayer is not supported on this version of the server.")


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_sampling_point()


class TestSamplingPoint(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "sampling_points"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "point": (0.0, 0.0, 0.0),
            "direction": (0.0, 0.0, 0.0),
            "use_default_reference_direction": True,
            "rosette": None,
            "offset_is_middle": True,
            "consider_coupling_effect": True,
        }

    CREATE_METHOD_NAME = "create_sampling_point"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
                ("point", (0.1, 0.2, 0.3)),
                ("direction", (0.4, 0.5, 0.6)),
                ("use_default_reference_direction", False),
                ("rosette", parent_object.create_rosette()),
                ("offset_is_middle", False),
                ("consider_coupling_effect", False),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("reference_direction", (0.1, 0.2, 0.3)),
            ],
        )
