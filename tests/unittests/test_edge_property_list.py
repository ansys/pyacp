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

"""Tests for the EdgePropertyList container."""

import pathlib
import tempfile

import pytest

from ansys.acp.core import Fabric, Lamina, SubLaminate
from ansys.acp.core._typing_helper import PATH


@pytest.fixture
def simple_model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def simple_sublaminate(simple_model, check_simple_sublaminate):
    """Simple sublaminate whose materials are stored in an edge property list."""
    sublaminate = simple_model.create_sublaminate(name="simple_sublaminate")
    sublaminate.add_material(
        simple_model.create_fabric(name="fabric1", material=simple_model.create_material()),
        angle=0.0,
    )
    sublaminate.add_material(
        simple_model.create_fabric(name="fabric2", material=simple_model.create_material()),
        angle=10.0,
    )
    check_simple_sublaminate(sublaminate)
    return sublaminate


@pytest.fixture
def check_simple_sublaminate():
    """Provides a function to check the simple sublaminate."""

    def check(sublaminate):
        assert sublaminate.name == "simple_sublaminate"
        assert len(sublaminate.materials) == 2
        assert [m.angle for m in sublaminate.materials] == [0.0, 10.0]
        assert [m.material.name for m in sublaminate.materials] == ["fabric1", "fabric2"]

    return check


def test_save_load_with_existing_entries(
    acp_instance, simple_model, simple_sublaminate, check_simple_sublaminate
):
    """Regression test for bug #561.

    Checks that sublaminates are correctly loaded from a saved model.
    """
    model = simple_model
    # GIVEN: a model with a sublaminate which has two materials
    sublaminate = simple_sublaminate

    # WHEN: the model is saved and loaded
    with tempfile.TemporaryDirectory() as tmp_dir:
        if not acp_instance.is_remote:
            file_path: PATH = pathlib.Path(tmp_dir) / "model.acph5"
        else:
            file_path = "model.acph5"
        model.save(file_path)
        acp_instance.clear()
        model = acp_instance.import_model(path=file_path)

    # THEN: the sublaminate is still present and has the same materials
    sublaminate = model.sublaminates["simple_sublaminate"]
    check_simple_sublaminate(sublaminate)


def test_clone_store(simple_model, simple_sublaminate, check_simple_sublaminate):
    """Check that the edge property list is preserved when cloning and storing an object."""
    model = simple_model
    # GIVEN: a model with a sublaminate which has two materials
    sublaminate = simple_sublaminate

    # WHEN: cloning the sublaminate, then storing the clone
    sublaminate_clone = sublaminate.clone()
    sublaminate_clone.store(parent=model)

    # THEN: the clone is stored and has the same materials
    check_simple_sublaminate(sublaminate_clone)


def test_clone_access_raises(simple_model, simple_sublaminate, check_simple_sublaminate):
    """Check that the EdgePropertyList cannot be accessed on an unstored object."""
    model = simple_model
    # GIVEN: a model with a sublaminate which has two materials
    sublaminate = simple_sublaminate

    # WHEN: cloning the sublaminate
    sublaminate_clone = sublaminate.clone()

    # THEN: accessing the materials raises an error
    with pytest.raises(RuntimeError):
        sublaminate_clone.materials


def test_clone_clear_store(simple_model, simple_sublaminate):
    """Check that the edge property list can be cleared on a cloned object."""
    model = simple_model
    # GIVEN: a model with a sublaminate which has two materials
    sublaminate = simple_sublaminate

    # WHEN: cloning the sublaminate, removing the materials, then storing the clone
    sublaminate_clone = sublaminate.clone()
    sublaminate_clone.materials = []
    sublaminate_clone.store(parent=model)

    # THEN: the clone is stored and has no materials
    assert len(sublaminate_clone.materials) == 0


def test_clone_assign_store(simple_model, simple_sublaminate):
    """Check that the edge property list can be changed on a cloned object."""
    model = simple_model
    # GIVEN: a model with a sublaminate which has two materials
    sublaminate = simple_sublaminate

    # WHEN: cloning the sublaminate, setting new materials, then storing the clone
    sublaminate_clone = sublaminate.clone()
    import gc

    gc.collect()
    fabric = simple_model.create_fabric(name="new_fabric", material=simple_model.create_material())
    new_materials = [Lamina(material=fabric, angle=3.0)]
    sublaminate_clone.materials = new_materials
    sublaminate_clone.store(parent=model)

    # THEN: the clone is stored and has no materials
    assert len(sublaminate_clone.materials) == 1
    assert sublaminate_clone.materials[0].material.name == "new_fabric"
    assert sublaminate_clone.materials[0].angle == 3.0


def test_store_with_entries(simple_model, check_simple_sublaminate):
    """Check that a sublaminate can be created with materials, and then stored."""
    fabric1 = simple_model.create_fabric(name="fabric1", material=simple_model.create_material())
    fabric2 = simple_model.create_fabric(name="fabric2", material=simple_model.create_material())

    sublaminate = SubLaminate(
        name="simple_sublaminate",
        materials=[Lamina(material=fabric1, angle=0.0), Lamina(material=fabric2, angle=10.0)],
    )
    sublaminate.store(parent=simple_model)
    check_simple_sublaminate(sublaminate)


def test_wrong_type_raises(simple_model):
    """Check that assigning a wrong type to the materials raises an error."""
    sublaminate = simple_model.create_sublaminate(name="simple_sublaminate")
    with pytest.raises(TypeError):
        sublaminate.materials = [1]


def test_incomplete_object_check(simple_model):
    """Check that unstored objects cannot be added to the edge property list."""
    sublaminate = simple_model.create_sublaminate(name="simple_sublaminate")
    with pytest.raises(RuntimeError) as e:
        sublaminate.materials.append(
            Lamina(material=Fabric(material=simple_model.create_material()), angle=0.0)
        )
    assert "incomplete object" in str(e.value)
