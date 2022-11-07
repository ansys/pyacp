import google.protobuf.message

from ansys.api.acp.v0.base_pb2 import CollectionPath, ResourcePath

__all__ = ("unlink_objects",)


def unlink_objects(pb_object: google.protobuf.message.Message) -> None:
    """Remove all ResourcePaths and CollectionPaths from a protobuf object."""
    for field_descriptor, field_value in pb_object.ListFields():
        if isinstance(field_value, (ResourcePath, CollectionPath)):
            pb_object.ClearField(field_descriptor.name)
        elif isinstance(field_value, google.protobuf.message.Message):
            unlink_objects(pb_object=field_value)
