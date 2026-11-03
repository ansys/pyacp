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

from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import SamplingPoint
from ansys.acp.core._server import acp_instance

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


def test_get_layup(parent_object, acp_instance):

    if parse_version(acp_instance.server_version) < parse_version("27.2"):
        pytest.skip(
            "Get_layup is not supported on this version of the server. Requires 27.2 or later."
        )

    sampling_point = parent_object.create_sampling_point(
        name="SP", point=(0.0, 0.0, 0.0), direction=(0.0, 0.0, 1.0)
    )
    parent_object.update()
    layup = sampling_point.get_layup()
    assert layup is not None
    assert layup.offset == 0.0
    assert layup.aligned is True
    assert layup.element_label == 1

    assert len(layup.analysis_plies) == 1
    assert len(layup.production_plies) == 1
    assert len(layup.modeling_plies) == 1

    analysis_entry = layup.analysis_plies[0]
    assert analysis_entry.order == 0
    assert analysis_entry.ply is not None
    assert analysis_entry.ply.id == "P1L1__ModelingPly.1"
    assert analysis_entry.angle == 90.0
    assert analysis_entry.thickness == 0.0001
    assert analysis_entry.design_thickness == 0.0001
    assert analysis_entry.offset == 0.0

    production_entry = layup.production_plies[0]
    assert production_entry.order == 0
    assert production_entry.ply is not None
    assert production_entry.ply.id == "ProductionPly"
    assert production_entry.angle == 0.0
    assert production_entry.thickness == 0.0001
    assert production_entry.design_thickness == 0.0001
    assert production_entry.offset == 0.0

    modeling_entry = layup.modeling_plies[0]
    assert modeling_entry.order == 0
    assert modeling_entry.ply is not None
    assert modeling_entry.ply.id == "ModelingPly.1"
    assert modeling_entry.angle == 0.0
    assert modeling_entry.thickness == 0.0001
    assert modeling_entry.design_thickness == 0.0001
    assert modeling_entry.offset == 0.0
