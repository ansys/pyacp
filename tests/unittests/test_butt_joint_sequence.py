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

from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import ButtJointSequence, ButtJointSequenceDefinitionType, PrimaryPly
from ansys.acp.core._tree_objects._grpc_helpers.linked_object_list import ReadOnlyLinkedObjectList

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester
from .common.utils import AnyThing


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(
        ButtJointSequence._SUPPORTED_SINCE
    ):
        pytest.skip("ButtJointSequence is not supported on this version of the server.")


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
    def default_properties(acp_instance):
        properties: dict[str, Any] = {
            "status": "NOTUPTODATE",
            "active": True,
            "global_ply_nr": AnyThing(),
            "primary_plies": [],
            "secondary_plies": [],
        }
        if parse_version(acp_instance.server_version) >= parse_version("27.1"):
            properties.update(
                {
                    "definition_type": ButtJointSequenceDefinitionType.MANUAL,
                    "starting_modeling_plies": [],
                    "automatically_added_sequences": [],
                }
            )
        return properties

    CREATE_METHOD_NAME = "create_butt_joint_sequence"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_model, acp_instance):
        mg1 = parent_model.create_modeling_group()
        mg2 = parent_model.create_modeling_group()
        mp1 = mg1.create_modeling_ply()
        mp2 = mg1.create_modeling_ply()
        read_write: list[tuple[str, Any]] = [
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
        ]
        read_only: list[tuple[str, Any]] = [
            ("id", "some_id"),
            ("status", "UPTODATE"),
        ]
        if parse_version(acp_instance.server_version) >= parse_version("27.1"):
            read_write.extend(
                [
                    ("definition_type", ButtJointSequenceDefinitionType.AUTOMATIC_ALL_PLY_TYPES),
                    ("starting_modeling_plies", [mp2]),
                    # Set the 'primary_plies' and 'secondary_plies' to match the 'automatic' mode:
                    # The 'create_with_defined_properties' test picks the last entry for each attribute
                    # in the 'read_write' list, so they need to be consistent.
                    ("primary_plies", []),
                    ("secondary_plies", []),
                ]
            )
            read_only.append(("automatically_added_sequences", []))

        return ObjectPropertiesToTest(
            read_write=read_write,
            read_only=read_only,
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


def test_convert_to_manual_definition(load_model_from_tempfile, raises_before_version):
    """Verify conversion from automatic to manual definition."""
    with load_model_from_tempfile("minimal_complete_model.acph5") as model:
        modeling_group = model.modeling_groups["ModelingGroup.1"]
        modeling_ply = modeling_group.modeling_plies["ModelingPly.1"]
        butt_joint_sequence = modeling_group.create_butt_joint_sequence(
            definition_type=ButtJointSequenceDefinitionType.AUTOMATIC_ALL_PLY_TYPES,
            starting_modeling_plies=[modeling_ply],
        )
        assert (
            butt_joint_sequence.definition_type
            == ButtJointSequenceDefinitionType.AUTOMATIC_ALL_PLY_TYPES
        )
        model.update()
        with raises_before_version("27.1"):
            butt_joint_sequence.convert_to_manual_definition()
            assert butt_joint_sequence.definition_type == ButtJointSequenceDefinitionType.MANUAL


def test_automatically_added_sequences_is_read_only(parent_object, skip_before_version):
    """Verify automatically added sequences use a read-only linked-object list."""
    skip_before_version("27.1")  # automatically_added_sequences is only available since 27.1
    butt_joint_sequence = parent_object.create_butt_joint_sequence(
        definition_type=ButtJointSequenceDefinitionType.AUTOMATIC_ALL_PLY_TYPES
    )

    automatically_added_sequences = butt_joint_sequence.automatically_added_sequences

    assert isinstance(automatically_added_sequences, ReadOnlyLinkedObjectList)
    assert list(automatically_added_sequences) == []
    with pytest.raises(AttributeError):
        cast(Any, automatically_added_sequences).append(parent_object.create_modeling_ply())


def test_default_definition_type_warns(parent_object, skip_before_version):
    """Verify the backwards-compatible default definition type."""
    skip_before_version("27.1")  # definition_type is only available since 27.1
    with pytest.warns(DeprecationWarning, match="'definition_type'.*will change"):
        butt_joint_sequence = parent_object.create_butt_joint_sequence()
    assert butt_joint_sequence.definition_type == ButtJointSequenceDefinitionType.MANUAL
