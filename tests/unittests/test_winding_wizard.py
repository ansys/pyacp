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

from ansys.acp.core._tree_objects.winding_wizard import Layer, WindingWizard

from .common.tree_object_tester import (
    NoLockedMixin,
    ObjectPropertiesToTest,
    TreeObjectTester,
)


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(WindingWizard._SUPPORTED_SINCE):
        pytest.skip("WindingWizard is not supported on this version of the server.")


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_winding_wizard()


class TestWindingWizard(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "winding_wizards"
    CREATE_METHOD_NAME = "create_winding_wizard"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "origin": (0.0, 0.0, 0.0),
            "axial_direction": (0.0, 0.0, 1.0),
            "reference_radius": 0.0,
            "max_angle_with_thickness_correction": 90.0,
            "layers": [],
        }

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        fabric1 = parent_object.create_fabric()
        fabric2 = parent_object.create_fabric()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Winding wizard name"),
                ("origin", (1.0, 2.0, 3.0)),
                ("axial_direction", (0.0, 1.0, 0.0)),
                ("reference_radius", 12.5),
                ("max_angle_with_thickness_correction", 65.0),
                (
                    "layers",
                    [
                        Layer(fabric=fabric1, nominal_angle=35.0, add_mirrored_ply=True),
                        Layer(
                            fabric=fabric2,
                            nominal_angle=-20.0,
                            has_limits=True,
                            lower_limit=-1.0,
                            upper_limit=2.0,
                        ),
                    ],
                ),
            ],
            read_only=[
                ("id", "some_id"),
                ("has_run", False),
            ],
        )


def test_wrong_layer_error_message(parent_object):
    winding_wizard = parent_object.create_winding_wizard()

    with pytest.raises(TypeError) as exc:
        winding_wizard.layers = [parent_object.create_fabric()]

    assert "Layer" in str(exc.value)
    assert "Fabric" in str(exc.value)


def test_add_layer(parent_object):
    """Verify the add method for layers."""
    fabric1 = parent_object.create_fabric()
    fabric2 = parent_object.create_fabric()
    winding_wizard = parent_object.create_winding_wizard()

    layer1 = winding_wizard.add_layer(fabric=fabric1, nominal_angle=30.0)
    assert layer1.fabric == fabric1
    assert layer1.nominal_angle == 30.0
    assert layer1.has_limits is False
    assert layer1.lower_limit == 0.0
    assert layer1.upper_limit == 0.0
    assert layer1.add_mirrored_ply is False

    layer2 = winding_wizard.add_layer(
        fabric=fabric2,
        nominal_angle=-15.0,
        has_limits=True,
        lower_limit=-5.0,
        upper_limit=5.0,
        add_mirrored_ply=True,
    )
    assert layer2.fabric == fabric2
    assert layer2.nominal_angle == -15.0
    assert layer2.has_limits is True
    assert layer2.lower_limit == -5.0
    assert layer2.upper_limit == 5.0
    assert layer2.add_mirrored_ply is True


def test_layer_equality_check(parent_object):
    fabric = parent_object.create_fabric()
    layer = Layer(
        fabric=fabric,
        nominal_angle=45.0,
        has_limits=True,
        lower_limit=-1.0,
        upper_limit=2.0,
        add_mirrored_ply=True,
    )
    assert layer != Layer(
        fabric=parent_object.create_fabric(),
        nominal_angle=45.0,
        has_limits=True,
        lower_limit=-1.0,
        upper_limit=2.0,
        add_mirrored_ply=True,
    )
    assert layer == Layer(
        fabric=fabric,
        nominal_angle=45.0,
        has_limits=True,
        lower_limit=-1.0,
        upper_limit=2.0,
        add_mirrored_ply=True,
    )
