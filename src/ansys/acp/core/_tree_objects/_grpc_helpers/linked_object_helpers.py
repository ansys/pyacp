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

from collections.abc import Iterable
from typing import Union

from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.message import Message

from ansys.api.acp.v0.base_pb2 import CollectionPath, ResourcePath

__all__ = ("unlink_objects", "linked_path_fields")


def unlink_objects(pb_object: Message) -> None:
    """Remove all ResourcePaths and CollectionPaths from a protobuf object."""
    for parent_message, field_descriptor, _ in linked_path_fields(pb_object):
        parent_message.ClearField(field_descriptor.name)


def linked_path_fields(
    pb_object: Message,
) -> Iterable[tuple[Message, FieldDescriptor, Union[ResourcePath, CollectionPath]]]:
    """Get all linked paths from a protobuf object.

    Get tuples (parent_message, field_descriptor, {resource_path or collection_path})
    describing all resource or collection paths present in the protobuf
    object.
    """
    for field_descriptor, field_value in pb_object.ListFields():
        if isinstance(field_value, (ResourcePath, CollectionPath)):
            yield (pb_object, field_descriptor, field_value)
        elif isinstance(field_value, Message):
            yield from linked_path_fields(field_value)
