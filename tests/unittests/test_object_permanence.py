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

import gc

import pytest

import ansys.acp.core as pyacp
from ansys.acp.core._tree_objects._grpc_helpers.edge_property_list import EdgePropertyList
from ansys.acp.core._tree_objects._grpc_helpers.linked_object_list import LinkedObjectList
from ansys.acp.core._tree_objects._grpc_helpers.mapping import Mapping, MutableMapping


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


def test_object_identity(model):
    mg_0 = model.create_modeling_group()
    mg_1 = model.modeling_groups[mg_0.id]
    mg_2 = model.modeling_groups[mg_0.id]
    assert mg_0 is mg_1 is mg_2


def test_object_identity_after_deletion(model):
    """Check that objects are deleted when no longer referenced."""
    key = list(model.modeling_groups.keys())[0]

    # Immediately consume the objects via 'id' to ensure no references
    # are kept by the test infrastructure.
    id1 = id(model.modeling_groups[key])
    gc.collect()
    id2 = id(model.modeling_groups[key])
    assert id1 != id2

    # test the inverse: keep a reference alive explicitly
    _ = model.modeling_groups[key]
    id1 = id(model.modeling_groups[key])
    gc.collect()
    id2 = id(model.modeling_groups[key])
    assert id1 == id2


def test_unstored():
    """Check that unstored objects have unique identities."""
    assert pyacp.ModelingPly() is not pyacp.ModelingPly()


def test_mapping_identity(model):
    """Check that Mapping objects have the same ID when accessed twice."""
    modeling_ply = list(list(model.modeling_groups.values())[0].modeling_plies.values())[0]
    production_ply_mapping_1 = modeling_ply.production_plies
    production_ply_mapping_2 = modeling_ply.production_plies
    assert isinstance(production_ply_mapping_1, Mapping)
    assert not isinstance(production_ply_mapping_1, MutableMapping)
    assert production_ply_mapping_1 is production_ply_mapping_2


def test_mutable_mapping_identity(model):
    """Check that MutableMapping objects have the same ID when accessed twice."""
    mg_mapping_1 = model.modeling_groups
    mg_mapping_2 = model.modeling_groups
    assert isinstance(mg_mapping_1, MutableMapping)
    assert mg_mapping_1 is mg_mapping_2


def test_linked_object_list_identity(model):
    """Check that LinkedObjectList objects have the same ID when accessed twice."""
    oss = list(model.oriented_selection_sets.values())[0]
    element_sets_list_1 = oss.element_sets
    element_sets_list_2 = oss.element_sets
    assert isinstance(element_sets_list_1, LinkedObjectList)
    assert element_sets_list_1 is element_sets_list_2


def test_edge_property_list_identity(model):
    """Check that EdgePropertyList objects have the same ID when accessed twice."""
    modeling_ply = list(list(model.modeling_groups.values())[0].modeling_plies.values())[0]
    selection_rules_1 = modeling_ply.selection_rules
    selection_rules_2 = modeling_ply.selection_rules
    assert isinstance(selection_rules_1, EdgePropertyList)
    assert selection_rules_1 is selection_rules_2


def test_linked_object_list_parent_deleted(model):
    """Check that the linked object list identity is unique even if its parent is no
    longer explicitly referenced."""
    oss = list(model.oriented_selection_sets.values())[0]
    element_sets = oss.element_sets

    del oss
    gc.collect()

    oss = list(model.oriented_selection_sets.values())[0]
    assert oss.element_sets is element_sets


def test_linked_object_list_parent_store(model):
    """Check that the linked object list identity is unique even after its parent is stored."""
    oss = pyacp.OrientedSelectionSet()
    element_sets = oss.element_sets
    oss.store(parent=model)
    oss_id = oss.id

    del oss
    gc.collect()

    oss = model.oriented_selection_sets[oss_id]
    assert oss.element_sets is element_sets


def test_edge_property_list_parent_deleted(model):
    """Check that the edge_property list identity is unique even if its parent is no
    longer explicitly referenced."""
    stackup = model.create_stackup()
    fabrics = stackup.fabrics

    del stackup
    gc.collect()

    stackup = list(model.stackups.values())[-1]
    assert stackup.fabrics is fabrics


def test_edge_property_list_parent_store(model):
    """Check that the edge property list identity is unique even after its parent is stored."""
    pytest.xfail(
        "We no longer allow accessing the edge property list while the parent is unstored."
    )
    stackup = pyacp.Stackup()
    fabrics = stackup.fabrics
    stackup.store(parent=model)
    stackup_id = stackup.id

    del stackup
    gc.collect()

    stackup = model.stackups[stackup_id]
    assert stackup.fabrics is fabrics
