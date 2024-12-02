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
import numpy.testing
from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import ExtrusionGuide, ExtrusionGuideType

from .common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(ExtrusionGuide._SUPPORTED_SINCE):
        pytest.skip("ExtrusionGuide is not supported on this version of the server.")


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def parent_object(model):
    return model.create_solid_model()


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_extrusion_guide()


class TestExtrusionGuide(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "extrusion_guides"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "active": True,
            "edge_set": None,
            "cad_geometry": None,
            "direction": (0.0, 0.0, 1.0),
            "radius": 0.0,
            "depth": 0.0,
            "use_curvature_correction": False,
            "extrusion_guide_type": "by_direction",
        }

    CREATE_METHOD_NAME = "create_extrusion_guide"
    INITIAL_OBJECT_NAMES = tuple()

    @staticmethod
    @pytest.fixture
    def object_properties(model):
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_extrusion_guide"),
                ("active", False),
                ("edge_set", model.create_edge_set()),
                ("extrusion_guide_type", ExtrusionGuideType.BY_DIRECTION),
                ("cad_geometry", None),
                ("direction", (2.0, 3.0, 4.0)),
                ("radius", 1.5),
                ("depth", 2.0),
                ("use_curvature_correction", True),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_handling_of_extrusion_guide_type(model, parent_object, skip_before_version):
    """Verify the handling of extrusion_guide_type.

    The backend determines the extrusion guide type based on the direction.
    extrusion_guide_type = BY_DIRECTION if direction != 0., else
    extrusion_guide_type = BY_GEOMETRY.

    In addition, the virtual geometry is None if
    extrusion_guide_type = BY_DIRECTION.
    """
    skip_before_version("25.1")

    virtual_cad = model.create_virtual_geometry(name="dummy")

    """ Case extrusion guide type = BY_DIRECTION """
    ex_by_direction = parent_object.create_extrusion_guide(
        name="ExtrusionGuide",
        direction=(0.0, 1.0, 1.0),
        extrusion_guide_type=ExtrusionGuideType.BY_DIRECTION,
    )
    assert ex_by_direction.extrusion_guide_type == ExtrusionGuideType.BY_DIRECTION
    assert ex_by_direction.cad_geometry is None
    numpy.testing.assert_allclose(ex_by_direction.direction, (0.0, 1.0, 1.0))
    # check that the user can modify the direction as long as the extrusion guide type is BY_DIRECTION
    ex_by_direction.direction = (2.3, 2.0, 1.0)
    # check that the user can change the extrusion guide type to BY_GEOMETRY
    ex_by_direction.extrusion_guide_type = ExtrusionGuideType.BY_GEOMETRY
    ex_by_direction.cad_geometry = virtual_cad

    """ Case extrusion guide type = BY_GEOMETRY """
    ex_by_geometry = parent_object.create_extrusion_guide(
        name="ExtrusionGuide",
        direction=(0.0, 0.0, 0.0),
        extrusion_guide_type=ExtrusionGuideType.BY_GEOMETRY,
        cad_geometry=virtual_cad,
    )
    assert ex_by_geometry.extrusion_guide_type == ExtrusionGuideType.BY_GEOMETRY
    assert ex_by_geometry.cad_geometry is not None and ex_by_geometry.cad_geometry.name == "dummy"
    with pytest.raises(RuntimeError) as exc:
        direction = ex_by_geometry.direction
    assert "Cannot access direction if the extrusion guide type is not 'by_direction'!" in str(
        exc.value
    )

    with pytest.raises(RuntimeError) as exc:
        ex_by_geometry.direction = (0.0, 1.0, 1.0)
    assert "Cannot set direction if extrusion guide type is not 'by_direction'!" in str(exc.value)
    """ Case invalid initialization """
    with pytest.raises(RuntimeError) as exc:
        ex_by_geometry = parent_object.create_extrusion_guide(
            name="ExtrusionGuide",
            direction=(0.0, 2.0, 1.0),
            extrusion_guide_type=ExtrusionGuideType.BY_GEOMETRY,
            cad_geometry=virtual_cad,
        )
    assert "Cannot set direction if extrusion guide type is not 'by_direction'!" in str(exc.value)
