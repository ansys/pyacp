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
