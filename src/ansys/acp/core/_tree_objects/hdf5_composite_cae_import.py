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

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Any

from ansys.api.acp.v0 import hdf5_composite_cae_import_pb2, hdf5_composite_cae_import_pb2_grpc

from .._utils.property_protocols import ReadWriteProperty
from .._utils.typing_helper import PATH as _PATH
from ._grpc_helpers.linked_object_list import define_linked_object_list
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    mark_grpc_properties,
)
from ._import_object import ImportObjectMixin
from .base import (
    CreatableTreeObject,
    IdTreeObject,
    TreeObjectAttributeWithCache,
    nested_grpc_object_property,
)
from .element_set import ElementSet
from .enums import (
    HDF5CompositeCAEProjectionMode,
    OffsetType,
    hdf5_composite_cae_projection_mode_from_pb,
    hdf5_composite_cae_projection_mode_to_pb,
    offset_type_from_pb,
    offset_type_to_pb,
)
from .object_registry import register


@mark_grpc_properties
class ShellMappingProperties(TreeObjectAttributeWithCache):
    """Properties for mapping to the shell on importing HDF5 Composite CAE files.

    Parameters
    ----------
    all_elements :
        If True, all element sets are used for shell projection. If False, only the selected element sets are used.
    element_sets :
        Element sets used to restrict the shell projection area.
        This parameter only applies when ``all_elements`` is False.
    relative_thickness_tolerance :
        Thickness tolerance for shell projection.
    relative_in_plane_tolerance :
        In-plane tolerance for shell projection.
    angle_tolerance :
        Angle tolerance (in degrees) for shell projection.
    small_hole_tolerance :
        Holes in the mesh smaller than this threshold are filled during shell projection.

    """

    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        all_elements: bool = True,
        element_sets: Sequence[ElementSet] = (),
        relative_thickness_tolerance: float = 0.5,
        relative_in_plane_tolerance: float = 0.01,
        angle_tolerance: float = 35.0,
        small_hole_threshold: float = 0.0,
        _parent_object: HDF5CompositeCAEImport | None = None,
        _pb_object: Any | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(
            _parent_object=_parent_object,
            _pb_object=_pb_object,
            _attribute_path=_attribute_path,
        )
        if _parent_object is None and _pb_object is None:
            self.all_elements = all_elements
            self.element_sets = element_sets
            self.relative_thickness_tolerance = relative_thickness_tolerance
            self.relative_in_plane_tolerance = relative_in_plane_tolerance
            self.angle_tolerance = angle_tolerance
            self.small_hole_threshold = small_hole_threshold

    @classmethod
    def _create_default_pb_object(cls) -> hdf5_composite_cae_import_pb2.ShellMappingProperties:
        """Create a default protobuf object for the ShellMappingProperties."""
        return hdf5_composite_cae_import_pb2.ShellMappingProperties()

    all_elements: ReadWriteProperty[bool, bool] = grpc_data_property("all_elements")
    element_sets = define_linked_object_list("element_sets", ElementSet)
    relative_thickness_tolerance: ReadWriteProperty[float, float] = grpc_data_property(
        "relative_thickness_tolerance"
    )
    relative_in_plane_tolerance: ReadWriteProperty[float, float] = grpc_data_property(
        "relative_in_plane_tolerance"
    )
    angle_tolerance: ReadWriteProperty[float, float] = grpc_data_property("angle_tolerance")
    small_hole_threshold: ReadWriteProperty[float, float] = grpc_data_property(
        "small_hole_threshold"
    )


@mark_grpc_properties
class SolidMappingProperties(TreeObjectAttributeWithCache):
    """Properties for importing HDF5 Composite CAE files as imported plies."""

    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        offset_type: OffsetType = OffsetType.BOTTOM_OFFSET,
        _parent_object: HDF5CompositeCAEImport | None = None,
        _pb_object: Any | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(
            _parent_object=_parent_object, _pb_object=_pb_object, _attribute_path=_attribute_path
        )
        if _parent_object is None and _pb_object is None:
            self.offset_type = offset_type

    @classmethod
    def _create_default_pb_object(cls) -> hdf5_composite_cae_import_pb2.SolidMappingProperties:
        """Create a default protobuf object for the SolidMappingProperties."""
        return hdf5_composite_cae_import_pb2.SolidMappingProperties()

    offset_type = grpc_data_property(
        "offset_type",
        to_protobuf=offset_type_to_pb,
        from_protobuf=offset_type_from_pb,
    )


@mark_grpc_properties
class CoordinateTransformation(TreeObjectAttributeWithCache):
    """Defines a coordinate transformation via rotation angles and translations.

    All angles are in degrees. The operations are performed in the following order:

    1. Rotation about the x-axis
    2. Rotation about the y-axis
    3. Rotation about the z-axis
    4. Translation

    """

    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        rotation_angle_x: float = 0.0,
        rotation_angle_y: float = 0.0,
        rotation_angle_z: float = 0.0,
        translation_x: float = 0.0,
        translation_y: float = 0.0,
        translation_z: float = 0.0,
        _parent_object: HDF5CompositeCAEImport | None = None,
        _pb_object: Any | None = None,
        _attribute_path: str | None = None,
    ) -> None:
        super().__init__(
            _parent_object=_parent_object, _pb_object=_pb_object, _attribute_path=_attribute_path
        )
        # The '__init__' method can be called either with the explicit values
        # defined below, or from a parent object or protobuf object. In the case
        # where a parent object or protobuf object is provided, the explicit values
        # must not be set, otherwise the default values will override the existing
        # values.
        if _parent_object is None and _pb_object is None:
            self.rotation_angle_x = rotation_angle_x
            self.rotation_angle_y = rotation_angle_y
            self.rotation_angle_z = rotation_angle_z
            self.translation_x = translation_x
            self.translation_y = translation_y
            self.translation_z = translation_z

    @classmethod
    def _create_default_pb_object(cls) -> hdf5_composite_cae_import_pb2.CoordinateTransformation:
        """Create a default protobuf object for the CoordinateTransformation."""
        return hdf5_composite_cae_import_pb2.CoordinateTransformation()

    rotation_angle_x: ReadWriteProperty[float, float] = grpc_data_property("rotation_angle_x")
    rotation_angle_y: ReadWriteProperty[float, float] = grpc_data_property("rotation_angle_y")
    rotation_angle_z: ReadWriteProperty[float, float] = grpc_data_property("rotation_angle_z")
    translation_x: ReadWriteProperty[float, float] = grpc_data_property("translation_x")
    translation_y: ReadWriteProperty[float, float] = grpc_data_property("translation_y")
    translation_z: ReadWriteProperty[float, float] = grpc_data_property("translation_z")


@mark_grpc_properties
@register
class HDF5CompositeCAEImport(ImportObjectMixin, CreatableTreeObject, IdTreeObject):
    """Initialize a HDF5CompositeCAEImport object.

    Parameters
    ----------
    name :
        Name of the HDF5 composite CAE import object.
    path :
        File path.
    projection_mode :
        Determines whether loaded plies are mapped onto the reference surface
        (:py:attr:`.HDF5CompositeCAEProjectionMode.SHELL` mode) or exposed as
        3D plies (:py:attr:`.HDF5CompositeCAEProjectionMode.SOLID` mode).
    minimum_angle_tolerance :
        Minimum angle tolerance for which tabular correction angles for plies are computed.
    recompute_reference_directions :
        Whether reference directions should be recomputed from tabular angle data or not.
    shell_mapping_properties :
        Properties for mapping to the shell on importing HDF5 Composite CAE files.
        Used only if ``projection_mode`` is set to ``"shell"``.
    solid_mapping_properties :
        Properties for importing HDF5 Composite CAE files as imported plies.
        Used only if ``projection_mode`` is set to ``"solid"``.
    coordinate_transformation :
        Coordinate transformation applied to the imported lay-up.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "hdf5_composite_cae_imports"
    _OBJECT_INFO_TYPE = hdf5_composite_cae_import_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = hdf5_composite_cae_import_pb2.CreateRequest
    _SUPPORTED_SINCE = "27.1"

    def __init__(
        self,
        *,
        name: str = "HDF5CompositeCAEImport",
        path: _PATH = "",
        projection_mode: HDF5CompositeCAEProjectionMode = HDF5CompositeCAEProjectionMode.SHELL,
        minimum_angle_tolerance: float = 0.001,
        recompute_reference_directions: bool = False,
        shell_mapping_properties: ShellMappingProperties | None = None,
        solid_mapping_properties: SolidMappingProperties | None = None,
        coordinate_transformation: CoordinateTransformation | None = None,
    ) -> None:
        super().__init__(name=name)
        self.path = path
        self.projection_mode = projection_mode
        self.minimum_angle_tolerance = minimum_angle_tolerance
        self.recompute_reference_directions = recompute_reference_directions
        if shell_mapping_properties is None:
            shell_mapping_properties = ShellMappingProperties()
        self.shell_mapping_properties = shell_mapping_properties
        if solid_mapping_properties is None:
            solid_mapping_properties = SolidMappingProperties()
        self.solid_mapping_properties = solid_mapping_properties
        if coordinate_transformation is None:
            coordinate_transformation = CoordinateTransformation()
        self.coordinate_transformation = coordinate_transformation

    def _create_stub(self) -> hdf5_composite_cae_import_pb2_grpc.ObjectServiceStub:
        """Create a gRPC stub for the HDF5CompositeCAEImport object."""
        return hdf5_composite_cae_import_pb2_grpc.ObjectServiceStub(self._channel)

    path: ReadWriteProperty[str, _PATH] = grpc_data_property("properties.path", to_protobuf=str)
    projection_mode = grpc_data_property(
        "properties.projection_mode",
        to_protobuf=hdf5_composite_cae_projection_mode_to_pb,
        from_protobuf=hdf5_composite_cae_projection_mode_from_pb,
    )
    minimum_angle_tolerance: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.minimum_angle_tolerance"
    )
    recompute_reference_directions: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.recompute_reference_directions"
    )
    shell_mapping_properties = nested_grpc_object_property(
        "properties.shell_mapping_properties",
        object_type=ShellMappingProperties,
    )
    solid_mapping_properties = nested_grpc_object_property(
        "properties.solid_mapping_properties",
        object_type=SolidMappingProperties,
    )
    coordinate_transformation = nested_grpc_object_property(
        "properties.coordinate_transformation",
        object_type=CoordinateTransformation,
    )

    def run(self) -> None:
        """Run the HDF5 composite CAE import using the stored settings.

        If the server is configured to automatically upload files, the ``path``
        parameter is treated as a local file path and the file is uploaded
        to the server.
        """
        upload_path = self._server_wrapper.auto_upload(self.path)
        orig_path = self.path
        has_uploaded = upload_path != orig_path
        try:
            if has_uploaded:
                # temporarily set the path to the uploaded file path for the
                # duration of the run
                self.path = upload_path
            super().run()
        finally:
            if has_uploaded:
                self.path = orig_path
