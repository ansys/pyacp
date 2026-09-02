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

from typing import Any, cast

import pytest

from ansys.acp.core import Rosette
from ansys.acp.core._tree_objects._grpc_helpers.linked_object_list import ReadOnlyLinkedObjectList


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def oriented_selection_set(model):
    return next(iter(model.oriented_selection_sets.values()))


@pytest.fixture
def read_only_rosettes(oriented_selection_set):
    return ReadOnlyLinkedObjectList._initialize_with_cache(
        parent_object=oriented_selection_set,
        attribute_name="properties.rosettes",
        object_constructor=Rosette._from_resource_path,
        allowed_types=(Rosette,),
    )


def test_read_only_linked_object_list_reads_existing_values(
    oriented_selection_set, read_only_rosettes
):
    """Test read access through a read-only linked-object list."""
    expected_rosettes = list(oriented_selection_set.rosettes)

    assert len(read_only_rosettes) == len(expected_rosettes)
    assert list(read_only_rosettes) == expected_rosettes
    assert read_only_rosettes[0] == expected_rosettes[0]
    assert read_only_rosettes[:] == expected_rosettes
    assert list(reversed(read_only_rosettes)) == list(reversed(expected_rosettes))
    assert expected_rosettes[0] in read_only_rosettes
    assert read_only_rosettes.count(expected_rosettes[0]) == 1
    assert read_only_rosettes.index(expected_rosettes[0]) == 0


@pytest.mark.parametrize(
    "method_name",
    ("append", "clear", "extend", "insert", "pop", "remove", "reverse", "sort"),
)
def test_read_only_linked_object_list_has_no_mutation_methods(read_only_rosettes, method_name):
    """Test mutation methods are unavailable on a read-only linked-object list."""
    with pytest.raises(AttributeError):
        getattr(read_only_rosettes, method_name)


def test_read_only_linked_object_list_rejects_item_assignment(read_only_rosettes):
    """Test item assignment raises instead of silently changing a read-only list."""
    with pytest.raises(TypeError):
        cast(Any, read_only_rosettes)[0] = None


def test_read_only_linked_object_list_rejects_item_deletion(read_only_rosettes):
    """Test item deletion raises instead of silently changing a read-only list."""
    with pytest.raises(TypeError):
        del cast(Any, read_only_rosettes)[0]
