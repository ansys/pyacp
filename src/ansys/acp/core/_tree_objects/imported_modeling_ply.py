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

from __future__ import annotations

from collections.abc import Iterable, Sequence

from ansys.api.acp.v0 import (
    imported_modeling_ply_pb2,
    imported_modeling_ply_pb2_grpc,
    imported_production_ply_pb2_grpc,
)

from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.linked_object_list import define_linked_object_list
from ._grpc_helpers.mapping import get_read_only_collection_property
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import (
    ImportedPlyDrapingType,
    ImportedPlyOffsetType,
    ImportedPlyThicknessType,
    MeshImportType,
    RosetteSelectionMethod,
    ThicknessFieldType,
    imported_ply_draping_type_from_pb,
    imported_ply_draping_type_to_pb,
    imported_ply_offset_type_from_pb,
    imported_ply_offset_type_to_pb,
    imported_ply_thickness_type_from_pb,
    imported_ply_thickness_type_to_pb,
    mesh_import_type_from_pb,
    mesh_import_type_to_pb,
    rosette_selection_method_from_pb,
    rosette_selection_method_to_pb,
    status_type_from_pb,
    thickness_field_type_from_pb,
    thickness_field_type_to_pb,
)
from .fabric import Fabric
from .imported_production_ply import ImportedProductionPly
from .lookup_table_1d_column import LookUpTable1DColumn
from .lookup_table_3d_column import LookUpTable3DColumn
from .object_registry import register
from .rosette import Rosette
from .virtual_geometry import VirtualGeometry

__all__ = [
    "ImportedModelingPly",
]


@mark_grpc_properties
@register
class ImportedModelingPly(CreatableTreeObject, IdTreeObject):
    """Instantiate an Imported Modeling Ply.

    Parameters
    ----------
    name :
        The name of the Modeling Ply
    active :
        Inactive plies are ignored in ACP and the downstream analysis.
    offset_type :
        Defines the location of the mesh (plane) with respect to the laminate.
        One of ``BOTTOM_OFFSET``, ``MIDDLE_OFFSET``, and ``TOP_OFFSET``.
    mesh_import_type :
        Source of the imported mesh. Either from geometry or from hdf5.
    mesh_geometry:
        Link to the geometry with represents the ply surface. Only used if ``mesh_import_type``
        is ``FROM_GEOMETRY``.
    rosette_selection_method :
        Selection Method for Rosettes of the Oriented Selection Set.
    rosettes :
        Rosettes of the Oriented Selection Set.
    reference_direction_field :
        A 3D lookup table column that defines the reference directions.
    rotation_angle :
        Angle in degrees by which the initial reference directions are rotated around the orientations.
    ply_material :
        The material (only fabric is supported) of the ply.
    ply_angle :
        Design angle between the reference direction and the ply fiber direction.
    draping_type :
        Chooses between different draping formulations. ``NO_DRAPING`` by default.
    draping_angle_1_field :
        Correction angle between the fiber and draped fiber directions, in degree.
    draping_angle_2_field :
        Correction angle between the transverse and draped transverse directions,
        in degree. Optional, uses the same values as ``draping_angle_1_field``
        (no shear) by default.
    thickness_type :
        Choose :attr:`ThicknessType.FROM_TABLE` to define a ply with variable thickness.
        The default value is :attr:`ThicknessType.NOMINAL`, which means the ply
        thickness is constant and determined by the thickness of the ply material.
    thickness_field :
        Defines the look-up table column used to determine the ply thickness.
        Only applies if ``thickness_type`` is :attr:`ThicknessType.FROM_TABLE`.
    thickness_field_type :
        If ``thickness_type`` is :attr:`ThicknessType.FROM_TABLE`, this parameter
        determines how the thickness values are interpreted. They can be either
        absolute values (:attr:`ThicknessFieldType.ABSOLUTE_VALUES`) or relative
        values (:attr:`ThicknessFieldType.RELATIVE_SCALING_FACTOR`).
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "imported_modeling_plies"
    _OBJECT_INFO_TYPE = imported_modeling_ply_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = imported_modeling_ply_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "ModelingPly",
        active: bool = True,
        offset_type: ImportedPlyOffsetType = ImportedPlyOffsetType.MIDDLE_OFFSET,
        mesh_import_type: MeshImportType = MeshImportType.FROM_GEOMETRY,
        mesh_geometry: VirtualGeometry | None = None,
        rosette_selection_method: RosetteSelectionMethod = "minimum_angle",
        rosettes: Sequence[Rosette] = tuple(),
        reference_direction_field: LookUpTable3DColumn | LookUpTable1DColumn | None = None,
        rotation_angle: float = 0.0,
        ply_material: Fabric | None = None,
        ply_angle: float = 0.0,
        draping_type: ImportedPlyDrapingType = ImportedPlyDrapingType.NO_DRAPING,
        draping_angle_1_field: LookUpTable1DColumn | LookUpTable3DColumn | None = None,
        draping_angle_2_field: LookUpTable1DColumn | LookUpTable3DColumn | None = None,
        thickness_type: ImportedPlyThicknessType = ImportedPlyThicknessType.NOMINAL,
        thickness_field: LookUpTable1DColumn | LookUpTable3DColumn | None = None,
        thickness_field_type: ThicknessFieldType = ThicknessFieldType.ABSOLUTE_VALUES,
    ):
        super().__init__(name=name)

        self.active = active
        self.offset_type = ImportedPlyOffsetType(offset_type)
        self.mesh_import_type = MeshImportType(mesh_import_type)
        self.mesh_geometry = mesh_geometry
        self.rosette_selection_method = rosette_selection_method
        self.rosettes = rosettes
        self.reference_direction_field = reference_direction_field
        self.rotation_angle = rotation_angle

        self.ply_material = ply_material
        self.ply_angle = ply_angle

        self.draping_type = ImportedPlyDrapingType(draping_type)
        self.draping_angle_1_field = draping_angle_1_field
        self.draping_angle_2_field = draping_angle_2_field

        self.thickness_type = ImportedPlyThicknessType(thickness_type)
        self.thickness_field = thickness_field
        self.thickness_field_type = thickness_field_type

    def _create_stub(self) -> imported_modeling_ply_pb2_grpc.ObjectServiceStub:
        return imported_modeling_ply_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")
    offset_type = grpc_data_property(
        "properties.offset_type",
        from_protobuf=imported_ply_offset_type_from_pb,
        to_protobuf=imported_ply_offset_type_to_pb,
    )
    mesh_import_type = grpc_data_property(
        "properties.mesh_import_type",
        from_protobuf=mesh_import_type_from_pb,
        to_protobuf=mesh_import_type_to_pb,
    )
    mesh_geometry = grpc_link_property("properties.mesh_geometry", allowed_types=VirtualGeometry)
    rosette_selection_method = grpc_data_property(
        "properties.rosette_selection_method",
        from_protobuf=rosette_selection_method_from_pb,
        to_protobuf=rosette_selection_method_to_pb,
    )
    rosettes = define_linked_object_list("properties.rosettes", Rosette)
    reference_direction_field = grpc_link_property(
        "properties.reference_direction_field",
        allowed_types=(LookUpTable1DColumn, LookUpTable3DColumn),
    )
    rotation_angle: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.rotation_angle"
    )

    ply_material = grpc_link_property("properties.ply_material", allowed_types=(Fabric,))
    ply_angle: ReadWriteProperty[float, float] = grpc_data_property("properties.ply_angle")

    draping_type = grpc_data_property(
        "properties.draping",
        from_protobuf=imported_ply_draping_type_from_pb,
        to_protobuf=imported_ply_draping_type_to_pb,
    )
    draping_angle_1_field = grpc_link_property(
        "properties.draping_angle_1_field", allowed_types=(LookUpTable1DColumn, LookUpTable3DColumn)
    )
    draping_angle_2_field = grpc_link_property(
        "properties.draping_angle_2_field", allowed_types=(LookUpTable1DColumn, LookUpTable3DColumn)
    )

    thickness_type = grpc_data_property(
        "properties.thickness_type",
        from_protobuf=imported_ply_thickness_type_from_pb,
        to_protobuf=imported_ply_thickness_type_to_pb,
    )
    thickness_field = grpc_link_property(
        "properties.thickness_field", allowed_types=(LookUpTable1DColumn, LookUpTable3DColumn)
    )
    thickness_field_type = grpc_data_property(
        "properties.thickness_field_type",
        from_protobuf=thickness_field_type_from_pb,
        to_protobuf=thickness_field_type_to_pb,
    )

    imported_production_plies = get_read_only_collection_property(
        ImportedProductionPly, imported_production_ply_pb2_grpc.ObjectServiceStub
    )
