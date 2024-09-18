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

import numpy as np
import pytest

from ansys.acp.core import FabricWithAngle, recursive_copy


@pytest.fixture
def minimal_complete_model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


def test_basic_recursive_copy(minimal_complete_model):
    """Test copying a Modeling Ply and its linked objects."""
    # GIVEN: A Modeling Ply with linked objects
    mg = minimal_complete_model.modeling_groups["ModelingGroup.1"]
    mp = mg.modeling_plies["ModelingPly.1"]

    # WHEN: Recursively copying the Modeling Ply onto the same Modeling Group
    new_objects = recursive_copy(
        source_objects=[mp],
        parent_mapping={mg: mg, minimal_complete_model: minimal_complete_model},
        linked_object_handling="copy",
    )

    # THEN: The expected new objects are created
    assert len(new_objects) == 6
    assert {obj.id for obj in new_objects.values()} == {  # type: ignore
        "Global Coordinate System.2",
        "All_Elements.2",
        "Structural Steel.2",
        "Fabric.2",
        "OrientedSelectionSet.2",
        "ModelingPly.2",
    }


def test_basic_recursive_copy_keep_links(minimal_complete_model):
    """Test copying a Modeling Ply without linked objects."""
    # GIVEN: A Modeling Ply with linked objects
    mg = minimal_complete_model.modeling_groups["ModelingGroup.1"]
    mp = mg.modeling_plies["ModelingPly.1"]

    # WHEN: Recursively copying the Modeling Ply onto the same Modeling Group, without linked objects
    new_objects = recursive_copy(
        source_objects=[mp], parent_mapping={mg: mg}, linked_object_handling="keep"
    )

    # THEN: The expected new objects are created, with the links kept
    assert len(new_objects) == 1
    assert {obj.id for obj in new_objects.values()} == {  # type: ignore
        "ModelingPly.2",
    }
    assert list(new_objects.values())[0].ply_material.id == "Fabric.1"  # type: ignore


def test_basic_recursive_copy_no_links(minimal_complete_model):
    """Test copying a Modeling Ply without linked objects."""
    # GIVEN: A Modeling Ply with linked objects
    mg = minimal_complete_model.modeling_groups["ModelingGroup.1"]
    mp = mg.modeling_plies["ModelingPly.1"]

    # WHEN: Recursively copying the Modeling Ply onto the same Modeling Group, without linked objects
    new_objects = recursive_copy(
        source_objects=[mp], parent_mapping={mg: mg}, linked_object_handling="discard"
    )

    # THEN: The expected new objects are created, without links
    assert len(new_objects) == 1
    assert {obj.id for obj in new_objects.values()} == {  # type: ignore
        "ModelingPly.2",
    }
    assert list(new_objects.values())[0].ply_material is None  # type: ignore


def test_copy_all_objects(minimal_complete_model):
    """Test copying all objects on a model onto itself."""
    # GIVEN: A simple model
    model = minimal_complete_model

    # WHEN: Recursively copying, starting from the root of the model
    new_objects = recursive_copy(source_objects=[model], parent_mapping={model: model})

    # THEN: The expected new objects are created
    # NOTE: This list may need to be updated when the model reference file
    # is changed.
    assert len(new_objects) == 8
    assert {obj.id for obj in new_objects.values()} == {  # type: ignore
        "Global Coordinate System.2",
        "All_Elements.2",
        "ns_edge.2",
        "Structural Steel.2",
        "Fabric.2",
        "OrientedSelectionSet.2",
        "ModelingGroup.2",
        "ModelingPly.2",
    }


def test_copy_to_different_model(minimal_complete_model, load_model_from_tempfile):
    """Test copying all objects on a model onto a different model."""
    # GIVEN: Two models
    model1 = minimal_complete_model
    with load_model_from_tempfile() as model2:

        # WHEN: Recursively copying all objects from model1 to model2
        new_objects = recursive_copy(
            source_objects=[model1], parent_mapping={model1: model2}, linked_object_handling="copy"
        )

        # THEN: The expected new objects are created
        # NOTE: This list may need to be updated when the model reference file
        # is changed.
        assert len(new_objects) == 8
        assert {obj.id for obj in new_objects.values()} == {  # type: ignore
            "Global Coordinate System.2",
            "All_Elements.2",
            "ns_edge.2",
            "Structural Steel.2",
            "Fabric.2",
            "OrientedSelectionSet.2",
            "ModelingGroup.2",
            "ModelingPly.2",
        }


def test_copy_edge_property_list(minimal_complete_model):
    """Test copying an object which has an Edge Property List."""
    # GIVEN: A simple model with a Stackup
    model = minimal_complete_model
    fabric1 = model.fabrics["Fabric.1"]
    fabric2 = model.create_fabric(name="other_fabric", material=model.materials["Structural Steel"])
    stackup = model.create_stackup(
        name="Stackup.1",
        fabrics=[
            FabricWithAngle(fabric=fabric1, angle=0),
            FabricWithAngle(fabric=fabric2, angle=90),
        ],
    )

    # WHEN: Recursively copying the Stackup
    new_objects = recursive_copy(
        source_objects=[stackup], parent_mapping={model: model}, linked_object_handling="copy"
    )

    # THEN:
    # - The stackup, fabrics, and materials are copied
    # - The copied stackup links the new fabrics with the correct order and angles
    assert len(new_objects) == 4
    assert {obj.id for obj in new_objects.values()} == {  # type: ignore
        "Stackup.2",
        "Fabric.2",
        "other_fabric.2",
        "Structural Steel.2",
    }
    new_stackup = model.stackups["Stackup.2"]
    linked_fabrics = new_stackup.fabrics
    assert [fabric_with_angle.fabric.id for fabric_with_angle in linked_fabrics] == [
        "Fabric.2",
        "other_fabric.2",
    ]
    assert [fabric_with_angle.angle for fabric_with_angle in linked_fabrics] == [0, 90]


def test_missing_parent_object_raises(minimal_complete_model):
    """Test that an exception is raised if the parent_mapping is incomplete"""

    # GIVEN: A simple model
    mg = minimal_complete_model.modeling_groups["ModelingGroup.1"]
    mp = mg.modeling_plies["ModelingPly.1"]

    # WHEN: Recursively copying a Modeling Ply without providing the Model in
    # the parent_mapping (needed due to links to e.g. the Global Coordinate System)
    # THEN: An exception is raised
    with pytest.raises(KeyError) as exc_info:
        recursive_copy(
            source_objects=[mp],
            parent_mapping={mg: mg},
            linked_object_handling="copy",
        )

    msg = str(exc_info.value)
    assert "Parent object" in msg
    assert "parent_mapping" in msg


def test_copy_lookup_table_with_columns(minimal_complete_model):
    """Test copying lookup tables with columns and their data.

    This case is special because LUT implement a check for the shape
    of the data in their columns, which is determined by the "Location"
    column.
    """
    # GIVEN: a model which has objects with sub-attributes
    # (here: a lookup table with columns)
    model = minimal_complete_model
    lut = model.create_lookup_table_1d()
    lut.columns["Location"].data = [1.0, 2.0, 3.0]
    lut.create_column(name="column1", data=[4.0, 5.0, 6.0])

    # WHEN: recursively copying the lookup table
    new_objects = recursive_copy(source_objects=[lut], parent_mapping={model: model})

    # THEN: the expected new objects are created, but the sub-attributes are
    # not explicitly copied
    assert len(new_objects) == 2
    assert {obj.id for obj in new_objects.values()} == {  # type: ignore
        "LookUpTable1D.2",
        "column1",
    }
    new_lut = model.lookup_tables_1d["LookUpTable1D.2"]
    assert np.allclose(new_lut.columns["Location"].data, [1.0, 2.0, 3.0])
    assert np.allclose(new_lut.columns["column1"].data, [4.0, 5.0, 6.0])
