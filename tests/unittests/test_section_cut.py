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

import math
import os
import pathlib
import tempfile

from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import ExtrusionType, IntersectionType, SectionCut, SectionCutType

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(SectionCut._SUPPORTED_SINCE):
        pytest.skip("InterfaceLayer is not supported on this version of the server.")


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_section_cut()


class TestSectionCut(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "section_cuts"
    CREATE_METHOD_NAME = "create_section_cut"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "locked": False,
            "active": True,
            "origin": (0, 0, 0),
            "normal": (0, 0, 1),
            "in_plane_reference_direction1": (1, 0, 0),
            "scope_entire_model": True,
            "scope_element_sets": [],
            "extrusion_type": ExtrusionType.WIRE_FRAME,
            "scale_factor": 1.0,
            "core_scale_factor": 1.0,
            "section_cut_type": SectionCutType.MODELING_PLY_WISE,
            "intersection_type": IntersectionType.NORMAL_TO_SURFACE,
            "use_default_tolerance": True,
            "tolerance": 0.0,
            "use_default_interpolation_settings": True,
            "search_radius": 0.0,
            "number_of_interpolation_points": 1,
        }

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
                ("active", False),
                ("origin", (0.1, 0.2, 0.3)),
                ("normal", (0, 1.0 / math.sqrt(2), 1.0 / math.sqrt(2))),
                ("in_plane_reference_direction1", (math.sqrt(1 / 3), math.sqrt(2 / 3), 0)),
                ("scope_entire_model", False),
                (
                    "scope_element_sets",
                    [parent_object.create_element_set(), parent_object.create_element_set()],
                ),
                ("extrusion_type", ExtrusionType.SURFACE_NORMAL),
                ("extrusion_type", ExtrusionType.SURFACE_SWEEP_BASED),
                ("scale_factor", 1.5),
                ("core_scale_factor", 12.3),
                ("section_cut_type", SectionCutType.PRODUCTION_PLY_WISE),
                ("section_cut_type", SectionCutType.ANALYSIS_PLY_WISE),
                ("intersection_type", IntersectionType.IN_PLANE),
                ("use_default_tolerance", False),
                ("tolerance", 0.6),
                ("use_default_interpolation_settings", False),
                ("search_radius", 12.3),
                ("number_of_interpolation_points", 5),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("locked", True),
            ],
        )


@pytest.mark.parametrize("export_type", ["mesh_only", "solid_model"])
def test_section_cut_export(parent_object, export_type):
    """Test the export to CDB. Only the presence of the file is checked."""

    model = parent_object
    section_cut = model.create_section_cut()
    section_cut.normal = (1, 0, 0)
    section_cut.extrusion_type = ExtrusionType.SURFACE_NORMAL
    section_cut.section_cut_type = SectionCutType.ANALYSIS_PLY_WISE
    model.update()

    with tempfile.TemporaryDirectory() as tempdir:
        path = pathlib.Path(tempdir) / "section_cut.cdb"
        section_cut.export(path=path, export_type=export_type)
        assert path.exists()
        assert path.is_file()
        assert os.stat(path).st_size > 0


@pytest.fixture(params=[True, False])
def use_pathlib_path(request):
    return request.param


@pytest.fixture(params=[True, False])
def export_strength_limits(request):
    return request.param


def test_section_cut_becas_export(parent_object, export_strength_limits, use_pathlib_path):
    """Test the export to CDB. Only the presence of the file is checked."""

    model = parent_object
    section_cut = model.create_section_cut()
    section_cut.normal = (1, 0, 0)
    section_cut.extrusion_type = ExtrusionType.SURFACE_NORMAL
    section_cut.section_cut_type = SectionCutType.ANALYSIS_PLY_WISE
    model.update()

    expected_filename = ["E2D.in", "EMAT.in", "MATPROPS.in", "N2D.in"]
    if export_strength_limits:
        expected_filename.append("FAILMAT.in")

    with tempfile.TemporaryDirectory() as tempdir:
        tempdir_path = pathlib.Path(tempdir)
        if use_pathlib_path:
            section_cut.export_becas_input(
                path=tempdir_path, export_strength_limits=export_strength_limits
            )
        else:
            section_cut.export_becas_input(
                path=tempdir, export_strength_limits=export_strength_limits
            )

        assert sorted(tempdir_path.iterdir()) == sorted(
            [tempdir_path / filename for filename in expected_filename]
        )
