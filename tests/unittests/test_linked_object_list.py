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

import pytest


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def oriented_selection_set(model):
    return list(model.oriented_selection_sets.values())[0]


def test_error_on_wrong_type(model, oriented_selection_set):
    """Test that the correct error is raised when assigning the wrong type.

    This test replaces the entire contents of a LinkedObjectList.
    """
    with pytest.raises(TypeError) as excinfo:
        oriented_selection_set.rosettes = [model.create_element_set()]
    assert "Rosette" in str(excinfo.value)


def test_error_on_wrong_type_polymorphic(model, oriented_selection_set):
    """Test that the correct error is raised when assigning the wrong type.

    This test replaces the entire contents of a polymorphic LinkedObjectList.
    """
    with pytest.raises(TypeError) as excinfo:
        oriented_selection_set.selection_rules = [model.create_element_set()]
    assert "SelectionRule" in str(excinfo.value)


def test_error_on_wrong_single_assignment(model, oriented_selection_set):
    """Test that the correct error is raised when assigning the wrong type.

    This test assigns to a single item in a LinkedObjectList.
    """
    with pytest.raises(TypeError) as excinfo:
        oriented_selection_set.rosettes[0] = model.create_element_set()
    assert "Rosette" in str(excinfo.value)


def test_error_on_wrong_single_assignment_polymorphic(model, oriented_selection_set):
    """Test that the correct error is raised when assigning the wrong type.

    This test assigns to a single item in a polymorphic LinkedObjectList.
    """
    with pytest.raises(TypeError) as excinfo:
        oriented_selection_set.selection_rules[0] = model.create_element_set()
    assert "SelectionRule" in str(excinfo.value)


def test_error_on_wrong_append(model, oriented_selection_set):
    """Test that the correct error is raised when assigning the wrong type.

    This test appends to a LinkedObjectList.
    """
    with pytest.raises(TypeError) as excinfo:
        oriented_selection_set.rosettes.append(model.create_element_set())
    assert "Rosette" in str(excinfo.value)


def test_error_on_wrong_append_polymorphic(model, oriented_selection_set):
    """Test that the correct error is raised when assigning the wrong type.

    This test appends to a polymorphic LinkedObjectList.
    """
    with pytest.raises(TypeError) as excinfo:
        oriented_selection_set.selection_rules.append(model.create_element_set())
    assert "SelectionRule" in str(excinfo.value)


def test_error_on_wrong_insert(model, oriented_selection_set):
    """Test that the correct error is raised when assigning the wrong type.

    This test inserts into a LinkedObjectList.
    """
    with pytest.raises(TypeError) as excinfo:
        oriented_selection_set.rosettes.insert(0, model.create_element_set())
    assert "Rosette" in str(excinfo.value)


def test_error_on_wrong_insert_polymorphic(model, oriented_selection_set):
    """Test that the correct error is raised when assigning the wrong type.

    This test inserts into a polymorphic LinkedObjectList.
    """
    with pytest.raises(TypeError) as excinfo:
        oriented_selection_set.selection_rules.insert(0, model.create_element_set())
    assert "SelectionRule" in str(excinfo.value)


def test_error_on_wrong_extend(model, oriented_selection_set):
    """Test that the correct error is raised when assigning the wrong type.

    This test extends a LinkedObjectList.
    """
    with pytest.raises(TypeError) as excinfo:
        oriented_selection_set.rosettes.extend([model.create_element_set()])
    assert "Rosette" in str(excinfo.value)


def test_error_on_wrong_extend_polymorphic(model, oriented_selection_set):
    """Test that the correct error is raised when assigning the wrong type.

    This test extends a polymorphic LinkedObjectList.
    """
    with pytest.raises(TypeError) as excinfo:
        oriented_selection_set.selection_rules.extend([model.create_element_set()])
    assert "SelectionRule" in str(excinfo.value)
