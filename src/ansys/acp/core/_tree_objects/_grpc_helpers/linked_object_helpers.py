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

from collections.abc import Iterable

from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.message import Message

from ansys.api.acp.v0.base_pb2 import ResourcePath

__all__ = ("unlink_objects", "get_linked_paths")


def unlink_objects(pb_object: Message) -> None:
    """Remove all ResourcePaths and CollectionPaths from a protobuf object."""
    for parent_message, field_descriptor, _ in _linked_path_fields(pb_object):
        parent_message.ClearField(field_descriptor.name)


def get_linked_paths(pb_object: Message) -> Iterable[ResourcePath]:
    """Get all resource paths present in a protobuf object."""
    for _, field_descriptor, field_value in _linked_path_fields(pb_object):
        if field_descriptor.label == field_descriptor.LABEL_REPEATED:
            yield from field_value  # type: ignore
        else:
            yield field_value  # type: ignore


def _linked_path_fields(
    pb_object: Message,
) -> Iterable[tuple[Message, FieldDescriptor, Message]]:
    """Get the field field information for resource paths in the message.

    Get tuples (parent_message, field_descriptor, field_value) describing
    all resource paths present in the protobuf object. Note that the fields
    can also be repeated (containing multiple resource paths).
    """
    for field_descriptor, field_value in pb_object.ListFields():
        if getattr(field_descriptor.message_type, "name", None) == "ResourcePath":
            yield (pb_object, field_descriptor, field_value)
        elif field_descriptor.type == field_descriptor.TYPE_MESSAGE:
            if field_descriptor.label == field_descriptor.LABEL_REPEATED:
                for sub_obj in field_value:
                    yield from _linked_path_fields(sub_obj)
            else:
                yield from _linked_path_fields(field_value)
