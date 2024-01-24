"""
Defines helpers for synchronizing object properties with the backend
via gRPC Put / Get calls.
"""
from __future__ import annotations

from functools import reduce
from typing import Any, Callable, TypeVar

from ansys.api.acp.v0.base_pb2 import ResourcePath

from .polymorphic_from_pb import CreatableFromResourcePath, tree_object_from_resource_path
from .protocols import Editable, GrpcObjectBase, ObjectInfo, Readable

_TO_PROTOBUF_T = Callable[[Any], Any]
_FROM_PROTOBUF_T = Callable[[Any], Any]


class _exposed_grpc_property(property):
    """
    Wrapper around 'property', used to signal that the object should
    be collected into the '_GRPC_PROPERTIES' class attribute.
    """

    pass


T = TypeVar("T", bound=type[GrpcObjectBase])


def mark_grpc_properties(cls: T) -> T:
    props: list[str] = []
    # Loop is needed because we otherwise get only the _GRPC_PROPERTIES of one of the base classes.
    for base_cls in reversed(cls.__bases__):
        if hasattr(base_cls, "_GRPC_PROPERTIES"):
            props.extend(base_cls._GRPC_PROPERTIES)
    for key, value in vars(cls).items():
        if isinstance(value, _exposed_grpc_property):
            props.append(key)
    props_unique = []
    for name in props:
        if name not in props_unique:
            props_unique.append(name)
    cls._GRPC_PROPERTIES = tuple(props_unique)
    return cls


def grpc_linked_object_getter(name: str) -> Callable[[Readable], Any]:
    """
    Creates a getter method which obtains the linked server object
    """

    def inner(self: Readable) -> CreatableFromResourcePath | None:
        #  Import here to avoid circular references. Cannot use the registry before
        #  all the object have been imported.
        if not self._is_stored:
            raise Exception("Cannot get linked object from unstored object")
        self._get()
        object_resource_path = _get_data_attribute(self._pb_object, name)

        return tree_object_from_resource_path(object_resource_path, self._channel)

    return inner


def grpc_data_getter(
    name: str, from_protobuf: _FROM_PROTOBUF_T, check_optional: bool = False
) -> Callable[[Readable], Any]:
    """
    Creates a getter method which obtains the server object via the gRPC
    Get endpoint.

    Parameters
    ----------
    from_protobuf :
        Function to convert the protobuf object to the type exposed by the
        property.
    check_optional :
        If ``True``, the getter will return ``None`` if the property is not
        set on the protobuf object. Otherwise, the default protobuf value
        will be used.
    """

    def inner(self: Readable) -> Any:
        self._get_if_stored()
        pb_attribute = _get_data_attribute(self._pb_object, name, check_optional=check_optional)
        if check_optional and pb_attribute is None:
            return None
        return from_protobuf(pb_attribute)

    return inner


def grpc_data_setter(name: str, to_protobuf: _TO_PROTOBUF_T) -> Callable[[Editable, Any], None]:
    """
    Creates a setter method which updates the server object via the gRPC
    Put endpoint.
    """

    def inner(self: Editable, value: Any) -> None:
        self._get_if_stored()
        current_value = _get_data_attribute(self._pb_object, name)
        value_pb = to_protobuf(value)
        try:
            needs_updating = current_value != value_pb
        except TypeError:
            needs_updating = True
        if needs_updating:
            _set_data_attribute(self._pb_object, name, value_pb)
            self._put_if_stored()

    return inner


def _get_data_attribute(pb_obj: ObjectInfo, name: str, check_optional: bool = False) -> Any:
    name_parts = name.split(".")
    if check_optional:
        parent_obj = reduce(getattr, name_parts[:-1], pb_obj)
        if hasattr(parent_obj, "HasField") and not parent_obj.HasField(name_parts[-1]):
            return None
    return reduce(getattr, name_parts, pb_obj)


def _set_data_attribute(pb_obj: ObjectInfo, name: str, value: Any) -> None:
    name_parts = name.split(".")

    try:
        parent = reduce(getattr, name_parts[:-1], pb_obj)
        setattr(parent, name_parts[-1], value)
    except AttributeError:
        target_object: Any = reduce(getattr, name_parts, pb_obj)
        if hasattr(target_object, "CopyFrom"):
            target_object.CopyFrom(value)
        else:
            try:
                target_object[:] = value
            except TypeError:
                del target_object[:]
                for item in value:
                    target_object.add().CopyFrom(item)


def _wrap_doc(obj: Any, doc: str | None) -> Any:
    if doc is not None:
        obj.__doc__ = doc
    return obj


def grpc_data_property(
    name: str,
    to_protobuf: _TO_PROTOBUF_T = lambda x: x,
    from_protobuf: _FROM_PROTOBUF_T = lambda x: x,
    check_optional: bool = False,
    doc: str | None = None,
) -> Any:
    """
    Helper for defining properties accessed via gRPC. The property getter
    and setter make calls to the gRPC Get and Put endpoints to synchronize
    the local object with the remote backend.

    Parameters
    ----------
    name :
        Name of the property.
    to_protobuf :
        Function to convert the property value to the protobuf type.
    from_protobuf :
        Function to convert the protobuf object to the type exposed by the
        property.
    check_optional :
        If ``True``, the getter will return ``None`` if the property is not
        set on the protobuf object. Otherwise, the default protobuf value
        will be used.
    doc :
        Docstring for the property.
    """
    # Note jvonrick August 2023: We don't ensure with typechecks that the property returned here is
    # compatible with the class on which this property is created. For example:
    # grpc_data_setter returns a callable that expects an editable object as the first argument.
    # But this property can also be added to a class that does not satisfy the Editable
    # Protocol
    # See the discussion here on why it is hard to have typed properties:
    # https://github.com/python/typing/issues/985
    return _wrap_doc(
        _exposed_grpc_property(
            grpc_data_getter(name, from_protobuf=from_protobuf, check_optional=check_optional)
        ).setter(grpc_data_setter(name, to_protobuf=to_protobuf)),
        doc=doc,
    )


def grpc_data_property_read_only(
    name: str,
    from_protobuf: _FROM_PROTOBUF_T = lambda x: x,
    check_optional: bool = False,
    doc: str | None = None,
) -> Any:
    """
    Helper for defining properties accessed via gRPC. The property getter
    makes call to the gRPC Get endpoints to synchronize
    the local object with the remote backend.

    Parameters
    ----------
    name :
        Name of the property.
    from_protobuf :
        Function to convert the protobuf object to the type exposed by the
        property.
    check_optional :
        If ``True``, the getter will return ``None`` if the property is not
        set on the protobuf object. Otherwise, the default protobuf value
        will be used.
    doc :
        Docstring for the property.
    """
    return _wrap_doc(
        _exposed_grpc_property(
            grpc_data_getter(name, from_protobuf=from_protobuf, check_optional=check_optional)
        ),
        doc=doc,
    )


def grpc_link_property(name: str) -> Any:
    """
    Helper for defining linked properties accessed via gRPC. The property getter
    makes call to the gRPC Get endpoints to get the linked object
    """
    return _exposed_grpc_property(grpc_linked_object_getter(name)).setter(
        # Resource path represents an object that is not set as an empty string
        grpc_data_setter(
            name=name,
            to_protobuf=lambda obj: ResourcePath(value="") if obj is None else obj._resource_path,
        )
    )


def grpc_link_property_read_only(name: str) -> Any:
    """
    Helper for defining linked properties accessed via gRPC. The property getter
    makes call to the gRPC Get endpoints to get the linked object
    """
    return _exposed_grpc_property(grpc_linked_object_getter(name))
