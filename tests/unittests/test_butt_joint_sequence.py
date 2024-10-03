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

from ansys.acp.core import PrimaryPly

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester
from .common.utils import AnyThing


@pytest.fixture
def parent_model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def parent_object(parent_model):
    return parent_model.modeling_groups["ModelingGroup.1"]


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_butt_joint_sequence()


class TestButtJointSequence(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "butt_joint_sequences"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "active": True,
            "global_ply_nr": AnyThing(),
            "primary_plies": [],
            "secondary_plies": [],
        }

    CREATE_METHOD_NAME = "create_butt_joint_sequence"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_model):
        mg1 = parent_model.create_modeling_group()
        mg2 = parent_model.create_modeling_group()
        mp1 = mg1.create_modeling_ply()
        mp2 = mg1.create_modeling_ply()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "ButtJointSequence name"),
                ("active", False),
                ("global_ply_nr", 3),
                (
                    "primary_plies",
                    [
                        PrimaryPly(sequence=mg1, level=1),
                        PrimaryPly(sequence=mp2, level=3),
                    ],
                ),
                ("secondary_plies", [mg2, mp1]),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
            ],
        )


def test_wrong_primary_ply_type_error_message(tree_object, parent_model):
    butt_joint_sequence = tree_object
    fabric = parent_model.create_fabric()
    with pytest.raises(TypeError) as exc:
        butt_joint_sequence.primary_plies = [fabric]
    assert "PrimaryPly" in str(exc.value)
    assert "Fabric" in str(exc.value)


def test_add_primary_ply(parent_object):
    """Verify add method for primary plies."""
    modeling_ply_1 = parent_object.create_modeling_ply()

    butt_joint_sequence = parent_object.create_butt_joint_sequence()
    butt_joint_sequence.add_primary_ply(modeling_ply_1)
    assert butt_joint_sequence.primary_plies[-1].sequence == modeling_ply_1
    assert butt_joint_sequence.primary_plies[-1].level == 1
    modeling_ply_2 = modeling_ply_1.clone()
    modeling_ply_2.store(parent=parent_object)
    butt_joint_sequence.add_primary_ply(modeling_ply_2, level=3)
    assert butt_joint_sequence.primary_plies[-1].sequence == modeling_ply_2
    assert butt_joint_sequence.primary_plies[-1].level == 3
