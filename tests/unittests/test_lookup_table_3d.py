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

from ansys.acp.core import LookUpTable3DInterpolationAlgorithm

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_lookup_table_3d()


class TestLookUpTable3D(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "lookup_tables_3d"

    @staticmethod
    @pytest.fixture
    def default_properties(acp_instance):
        if parse_version(acp_instance.server_version) < parse_version("25.2"):
            return {
                "status": "NOTUPTODATE",
                "interpolation_algorithm": LookUpTable3DInterpolationAlgorithm.WEIGHTED_NEAREST_NEIGHBOR,
                "use_default_search_radius": True,
                "search_radius": 0.0,
                "num_min_neighbors": 1,
            }
        else:
            return {
                "status": "NOTUPTODATE",
                "use_global_coordinate_system": True,
                "rosette": None,
                "interpolation_algorithm": LookUpTable3DInterpolationAlgorithm.WEIGHTED_NEAREST_NEIGHBOR,
                "use_default_search_radius": True,
                "search_radius": 0.0,
                "num_min_neighbors": 1,
            }

    CREATE_METHOD_NAME = "create_lookup_table_3d"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object, acp_instance):
        model = parent_object
        rosette = model.create_rosette(name="Rosette")
        if parse_version(acp_instance.server_version) < parse_version("25.2"):
            return ObjectPropertiesToTest(
                read_write=[
                    ("name", "3D Look-Up Table name"),
                    (
                        "interpolation_algorithm",
                        LookUpTable3DInterpolationAlgorithm.NEAREST_NEIGHBOR,
                    ),
                    (
                        "interpolation_algorithm",
                        LookUpTable3DInterpolationAlgorithm.LINEAR_TRIANGULATION,
                    ),
                    ("use_default_search_radius", False),
                    ("search_radius", 3.5),
                    ("num_min_neighbors", 7),
                ],
                read_only=[
                    ("id", "some id"),
                    ("status", "UPTODATE"),
                ],
            )
        else:
            return ObjectPropertiesToTest(
                read_write=[
                    ("name", "3D Look-Up Table name"),
                    ("use_global_coordinate_system", False),
                    ("rosette", rosette),
                    (
                        "interpolation_algorithm",
                        LookUpTable3DInterpolationAlgorithm.NEAREST_NEIGHBOR,
                    ),
                    (
                        "interpolation_algorithm",
                        LookUpTable3DInterpolationAlgorithm.LINEAR_TRIANGULATION,
                    ),
                    ("use_default_search_radius", False),
                    ("search_radius", 3.5),
                    ("num_min_neighbors", 7),
                ],
                read_only=[
                    ("id", "some id"),
                    ("status", "UPTODATE"),
                ],
            )
