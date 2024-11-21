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


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_cad_geometry()


class TestCADGeometry(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "cad_geometries"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "external_path": "",
            "scale_factor": 1.0,
            "use_default_precision": True,
            "precision": 1e-3,
            "use_default_offset": True,
            "offset": 0.0,
        }

    CREATE_METHOD_NAME = "create_cad_geometry"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        element_set = model.create_element_set()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "CAD Geometry name"),
                ("external_path", "some/path/to/file"),
                ("scale_factor", 2.0),
                ("use_default_precision", False),
                ("precision", 1e-4),
                ("use_default_offset", False),
                ("offset", 1.3),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )

    @staticmethod
    def test_refresh(load_cad_geometry, load_model_from_tempfile):
        """Test refreshing the geometry.

        Only tests that the call does not raise an exception.
        """
        with (
            load_model_from_tempfile() as model,
            load_cad_geometry(model=model) as (cad_geometry, local_cad_path),
        ):
            cad_geometry.refresh(local_cad_path)

    @staticmethod
    def test_refresh_inexistent_raises(tree_object):
        """Test refreshing the geometry from an inexistent file."""
        with pytest.raises(FileNotFoundError):
            tree_object.refresh("inexistent_file")

    @staticmethod
    def test_accessing_root_shapes(load_cad_geometry, load_model_from_tempfile):
        """
        Ensure that the property root_shapes can only be accessed if
        the CADGeometry is up-to-date.
        """
        with (
            load_model_from_tempfile() as model,
            load_cad_geometry(model=model) as (cad_geometry, _),
        ):
            assert cad_geometry.status == "NOTUPTODATE"
            with pytest.raises(
                RuntimeError,
                match="The object CADGeometry must be up-to-date to access CADComponent.",
            ):
                _ = cad_geometry.root_shapes
            model.update()
            assert cad_geometry.status == "UPTODATE"
            assert len(cad_geometry.root_shapes) == 2
