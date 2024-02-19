from __future__ import annotations

from collections.abc import Iterable
import typing
from typing import Any, Callable

from ansys.api.acp.v0 import base_pb2, virtual_geometry_pb2, virtual_geometry_pb2_grpc

from ._grpc_helpers.edge_property_list import GenericEdgePropertyType, define_edge_property_list
from ._grpc_helpers.property_helper import grpc_data_property_read_only, mark_grpc_properties
from .base import CreatableTreeObject, IdTreeObject
from .cad_geometry import CADGeometry
from .enums import status_type_from_pb, virtual_geometry_dimension_from_pb
from .object_registry import register

if typing.TYPE_CHECKING:
    from .cad_component import CADComponent


class SubShape(GenericEdgePropertyType):
    """Represents a sub-shape of a virtual geometry."""

    def __init__(self, cad_geometry: CADGeometry, path: str):
        self._cad_geometry = cad_geometry
        self._path = path
        self._callback_apply_changes: Callable[[], None] | None = None

    @property
    def cad_geometry(self) -> CADGeometry:
        """Linked CAD geometry."""
        return self._cad_geometry

    @cad_geometry.setter
    def cad_geometry(self, value: CADGeometry) -> None:
        self._cad_geometry = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    @property
    def path(self) -> str:
        """Topological path of the sub-shape within the CAD geometry."""
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        self._path = value
        if self._callback_apply_changes:
            self._callback_apply_changes()

    def _set_callback_apply_changes(self, callback_apply_changes: Callable[[], None]) -> None:
        self._callback_apply_changes = callback_apply_changes

    @classmethod
    def _from_pb_object(
        cls,
        parent_object: CreatableTreeObject,
        message: virtual_geometry_pb2.SubShape,
        apply_changes: Callable[[], None],
    ) -> SubShape:
        new_obj = cls(
            cad_geometry=CADGeometry._from_resource_path(
                message.cad_geometry, channel=parent_object._channel
            ),
            path=message.path,
        )
        new_obj._set_callback_apply_changes(apply_changes)
        return new_obj

    def _to_pb_object(self) -> virtual_geometry_pb2.SubShape:
        return virtual_geometry_pb2.SubShape(
            cad_geometry=self._cad_geometry._resource_path, path=self._path
        )

    def _check(self) -> bool:
        # Check for empty resource paths
        return bool(self._cad_geometry._resource_path.value)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return (
                self._cad_geometry._resource_path == other._cad_geometry._resource_path
                and self._path == other._path
            )

        return False

    def __repr__(self) -> str:
        return f"SubShape(cad_geometry={self._cad_geometry.__repr__()}, path={self._path})"


@mark_grpc_properties
@register
class VirtualGeometry(CreatableTreeObject, IdTreeObject):
    """Instantiate a Virtual Geometry.

    The virtual geometry can be created from a set of CAD components or from a set of SubShapes.
    Combining CAD Components and SubShapes is not allowed.

    Parameters
    ----------
    name :
        Name of the Virtual Geometry.
    cad_components :
        CAD Components that make up the virtual geometry.
    sub_shapes :
        SubShapes that make up the virtual geometry.

    """

    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "virtual_geometries"
    OBJECT_INFO_TYPE = virtual_geometry_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = virtual_geometry_pb2.CreateRequest

    def __init__(
        self,
        *,
        name: str = "VirtualGeometry",
        cad_components: Iterable[CADComponent] | None = None,
        sub_shapes: Iterable[SubShape] | None = None,
    ):
        super().__init__(
            name=name,
        )

        if cad_components is not None and sub_shapes is not None:
            raise ValueError("cad_components and sub_shapes cannot be set at the same time")

        if cad_components is None and sub_shapes is None:
            self.sub_shapes = []

        if cad_components is not None:
            self.set_cad_components(cad_components=cad_components)

        if sub_shapes is not None:
            self.sub_shapes = sub_shapes

    def _create_stub(self) -> virtual_geometry_pb2_grpc.ObjectServiceStub:
        return virtual_geometry_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    dimension = grpc_data_property_read_only(
        "properties.dimension", from_protobuf=virtual_geometry_dimension_from_pb
    )

    sub_shapes = define_edge_property_list(
        "properties.sub_shapes",
        SubShape,
    )

    def set_cad_components(self, cad_components: Iterable[CADComponent]) -> None:
        """Set the sub-shapes to match the given CADComponents.

        Parameters
        ----------
        cad_components :
            The components which make up the virtual geometry.
        """

        # TODO: find a better / more generic way to do this
        def _get_parent(cad_component: CADComponent) -> CADGeometry:
            rp = "/".join(cad_component._resource_path.value.split("/")[:-2])
            return CADGeometry._from_resource_path(
                base_pb2.ResourcePath(value=rp), channel=cad_component._channel
            )

        sub_shapes = [
            SubShape(cad_geometry=_get_parent(component), path=component.path)
            for component in cad_components
        ]
        self.sub_shapes = sub_shapes
