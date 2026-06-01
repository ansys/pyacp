# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Test cloning with the 'unlink' option."""

import pytest


def test_store_after_unlink(load_model_from_tempfile):
    """
    Check that a model cloned with 'unlink=True' can be stored on another model.
    """
    with load_model_from_tempfile() as model1, load_model_from_tempfile() as model2:
        material = list(model1.materials.values())[0]
        fabric = model1.create_fabric(thickness=0.001, material=material)
        cloned_fabric = fabric.clone(unlink=True)
        cloned_fabric.store(parent=model2)


def test_error_on_store_with_linked(load_model_from_tempfile):
    """
    Check the error which is raised when trying to store with links to another model
    """
    with load_model_from_tempfile() as model1, load_model_from_tempfile() as model2:
        material = list(model1.materials.values())[0]
        fabric = model1.create_fabric(thickness=0.001, material=material)
        with pytest.raises(ValueError) as excinfo:
            cloned_fabric = fabric.clone()
            cloned_fabric.store(parent=model2)
        assert "contains links" in str(excinfo.value)
