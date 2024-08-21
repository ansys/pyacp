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

import pathlib
import tempfile

import pytest

from ansys.acp.core import Fabric, FabricWithAngle, Lamina, Stackup, SymmetryType
from ansys.acp.core._typing_helper import PATH

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_sublaminate()


class TestSubLaminate(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "sublaminates"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "topdown": True,
            "materials": [],
            "symmetry": SymmetryType.NO_SYMMETRY,
        }

    CREATE_METHOD_NAME = "create_sublaminate"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        material = model.create_material()
        fabric = model.create_fabric(
            name="fabric 1", thickness=0.1, material=material, area_price=15.0
        )
        fabric_stack = [
            FabricWithAngle(fabric=fabric, angle=30.0),
            FabricWithAngle(fabric=fabric, angle=-30.0),
        ]
        stackup = model.create_stackup(name="stackup 1", fabrics=fabric_stack, area_price=32.5)
        sublaminat_stack = [
            Lamina(material=fabric, angle=45.0),
            Lamina(material=stackup, angle=-60.0),
        ]
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Sub-laminate name"),
                ("topdown", False),
                ("materials", sublaminat_stack),
                ("symmetry", SymmetryType.EVEN_SYMMETRY),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("thickness", 0.3),
                ("area_weight", 0.0),
                ("area_price", 47.5),
            ],
        )


def test_add_lamina(parent_object):
    """Verify add method for lamina."""
    fabric1 = parent_object.create_fabric()
    fabric1.material = parent_object.create_material()
    stackup = parent_object.create_stackup()
    stackup.add_fabric(fabric1, angle=30.0)
    stackup.add_fabric(fabric1, angle=-30.0)

    sublaminate = parent_object.create_sublaminate()
    sublaminate.add_material(fabric1, angle=45.0)
    sublaminate.add_material(stackup, angle=0.0)
    sublaminate.add_material(fabric1, angle=-45.0)
    assert len(sublaminate.materials) == 3
    assert sublaminate.materials[1].material == stackup
    assert sublaminate.materials[1].angle == 0.0
    assert sublaminate.materials[2].material == fabric1
    assert sublaminate.materials[2].angle == -45.0


def test_load_with_existing_sublaminate(acp_instance, parent_object):
    """Regression test for bug #561.

    Checks that sublaminates are correctly loaded from a saved model.
    """
    model = parent_object
    # GIVEN: a model with a sublaminate which has three materials
    fabric1 = model.create_fabric()
    fabric1.material = model.create_material()
    stackup = model.create_stackup()
    stackup.add_fabric(fabric1, angle=30.0)
    stackup.add_fabric(fabric1, angle=-30.0)

    sublaminate = model.create_sublaminate(name="test_sublaminate")
    sublaminate.add_material(fabric1, angle=45.0)
    sublaminate.add_material(stackup, angle=0.0)
    sublaminate.add_material(fabric1, angle=-45.0)
    assert len(sublaminate.materials) == 3
    assert sublaminate.materials[0].angle == 45.0
    assert sublaminate.materials[1].angle == 0.0
    assert sublaminate.materials[2].angle == -45.0
    assert isinstance(sublaminate.materials[0].material, Fabric)
    assert isinstance(sublaminate.materials[1].material, Stackup)
    assert isinstance(sublaminate.materials[2].material, Fabric)

    # WHEN: the model is saved and loaded
    with tempfile.TemporaryDirectory() as tmp_dir:
        if acp_instance.is_remote:
            file_path: PATH = pathlib.Path(tmp_dir) / "model.acph5"
        else:
            file_path = "model.acph5"
        model.save(file_path)
        acp_instance.clear()
        model = acp_instance.import_model(path=file_path)

    # THEN: the sublaminate is still present and has the same materials
    sublaminate = model.sublaminates["test_sublaminate"]
    assert len(sublaminate.materials) == 3
    assert sublaminate.materials[0].angle == 45.0
    assert sublaminate.materials[1].angle == 0.0
    assert sublaminate.materials[2].angle == -45.0
    assert isinstance(sublaminate.materials[0].material, Fabric)
    assert isinstance(sublaminate.materials[1].material, Stackup)
    assert isinstance(sublaminate.materials[2].material, Fabric)
