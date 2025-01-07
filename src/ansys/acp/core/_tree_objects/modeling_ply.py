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

from collections.abc import Callable, Container, Iterable
import dataclasses
from typing import Any

import numpy as np
from typing_extensions import Self

from ansys.api.acp.v0 import modeling_ply_pb2, modeling_ply_pb2_grpc, production_ply_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadWriteProperty
from ._elemental_or_nodal_data import (
    ElementalData,
    NodalData,
    ScalarData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from ._grpc_helpers.edge_property_list import (
    GenericEdgePropertyType,
    define_add_method,
    define_edge_property_list,
)
from ._grpc_helpers.linked_object_list import define_linked_object_list
from ._grpc_helpers.mapping import get_read_only_collection_property
from ._grpc_helpers.property_helper import (
    _exposed_grpc_property,
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from ._mesh_data import full_mesh_property, shell_mesh_property
from .base import CreatableTreeObject, IdTreeObject
from .edge_set import EdgeSet
from .enums import (
    DrapingType,
    ThicknessFieldType,
    ThicknessType,
    draping_type_from_pb,
    draping_type_to_pb,
    status_type_from_pb,
    thickness_field_type_from_pb,
    thickness_field_type_to_pb,
    thickness_type_from_pb,
    thickness_type_to_pb,
)
from .fabric import Fabric
from .linked_selection_rule import LinkedSelectionRule
from .lookup_table_1d_column import LookUpTable1DColumn
from .lookup_table_3d_column import LookUpTable3DColumn
from .object_registry import register
from .oriented_selection_set import OrientedSelectionSet
from .production_ply import ProductionPly
from .stackup import Stackup
from .sublaminate import SubLaminate
from .virtual_geometry import VirtualGeometry

__all__ = ["ModelingPly", "ModelingPlyElementalData", "ModelingPlyNodalData", "TaperEdge"]


@dataclasses.dataclass
class ModelingPlyElementalData(ElementalData):
    """Represents elemental data for a Modeling Ply."""

    normal: VectorData | None = None
    orientation: VectorData | None = None
    reference_direction: VectorData | None = None
    fiber_direction: VectorData | None = None
    draped_fiber_direction: VectorData | None = None
    transverse_direction: VectorData | None = None
    draped_transverse_direction: VectorData | None = None
    thickness: ScalarData[np.float64] | None = None
    relative_thickness_correction: ScalarData[np.float64] | None = None
    design_angle: ScalarData[np.float64] | None = None
    shear_angle: ScalarData[np.float64] | None = None
    draped_fiber_angle: ScalarData[np.float64] | None = None
    draped_transverse_angle: ScalarData[np.float64] | None = None
    area: ScalarData[np.float64] | None = None
    price: ScalarData[np.float64] | None = None
    volume: ScalarData[np.float64] | None = None
    mass: ScalarData[np.float64] | None = None
    offset: ScalarData[np.float64] | None = None
    cog: VectorData | None = None


@dataclasses.dataclass
class ModelingPlyNodalData(NodalData):
    """Represents nodal data for a Modeling Ply."""

    ply_offset: VectorData | None = None


@mark_grpc_properties
class TaperEdge(GenericEdgePropertyType):
    """Defines a taper edge.

    Parameters
    ----------
    edge_set :
        Defines the edge along which the ply tapering is applied.
    angle :
        Defines the angle between the cutting plane and  the reference surface.
    offset :
        Moves the cutting plane along the out-of-plane direction.
        A negative value cuts the elements at the edge where the in-plane
        offset is ``-offset/tan(angle)``.
    """

    _SUPPORTED_SINCE = "24.2"

    def __init__(self, edge_set: EdgeSet, *, angle: float, offset: float):
        self._callback_apply_changes: Callable[[], None] | None = None
        self.edge_set = edge_set
        self.angle = angle
        self.offset = offset

    @_exposed_grpc_property
    def edge_set(self) -> EdgeSet:
        """Edge along which the ply tapering is applied."""
        return self._edge_set

    @edge_set.setter
    def edge_set(self, edge_set: EdgeSet) -> None:
        if not isinstance(edge_set, EdgeSet):
            raise TypeError(f"Expected an EdgeSet, got {type(edge_set)}.")
        self._edge_set = edge_set
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def angle(self) -> float:
        """Angle between the cutting plane and  the reference surface."""
        return self._angle

    @angle.setter
    def angle(self, angle: float) -> None:
        self._angle = angle
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    @_exposed_grpc_property
    def offset(self) -> float:
        """Move the cutting plane along the out-of-plane direction.

        A negative value cuts the elements at the edge where the in-plane
        offset is ``-offset/tan(angle)``.
        """
        return self._offset

    @offset.setter
    def offset(self, offset: float) -> None:
        self._offset = offset
        if self._callback_apply_changes is not None:
            self._callback_apply_changes()

    def _set_callback_apply_changes(self, callback_apply_changes: Callable[[], None]) -> None:
        self._callback_apply_changes = callback_apply_changes

    @classmethod
    def _from_pb_object(
        cls,
        parent_object: CreatableTreeObject,
        message: modeling_ply_pb2.TaperEdge,
        apply_changes: Callable[[], None],
    ) -> Self:
        edge_set = EdgeSet._from_resource_path(
            resource_path=message.edge_set, server_wrapper=parent_object._server_wrapper
        )

        new_obj = cls(
            edge_set=edge_set,
            angle=message.angle,
            offset=message.offset,
        )
        new_obj._set_callback_apply_changes(apply_changes)
        return new_obj

    def _to_pb_object(self) -> modeling_ply_pb2.TaperEdge:
        return modeling_ply_pb2.TaperEdge(
            edge_set=self.edge_set._resource_path,
            angle=self.angle,
            offset=self.offset,
        )

    def _check(self) -> bool:
        return bool(self.edge_set._resource_path.value)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, TaperEdge):
            return (
                self.edge_set == other.edge_set
                and self.angle == other.angle
                and self.offset == other.offset
            )
        return False

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(edge_set={self.edge_set!r}, "
            f"angle={self.angle!r}, offset={self.offset!r})"
        )

    def clone(self) -> Self:
        """Create a new unstored TaperEdge with the same properties."""
        return type(self)(
            edge_set=self.edge_set,
            angle=self.angle,
            offset=self.offset,
        )


@mark_grpc_properties
@register
class ModelingPly(CreatableTreeObject, IdTreeObject):
    """Instantiate a Modeling Ply.

    Parameters
    ----------
    name :
        The name of the Modeling Ply
    ply_material :
        The material (fabric, stackup or sub-laminate) of the ply.
    ply_angle :
        Design angle between the reference direction and the ply fiber direction.
    number_of_layers :
        Number of times the plies are generated.
    active :
        Inactive plies are ignored in ACP and the downstream analysis.
    global_ply_nr :
        Defines the global ply order.
    selection_rules :
        Selection Rules which may limit the extent of the ply.
    draping_type :
        Chooses between different draping formulations.
    draping_seed_point :
        Starting point of the draping algorithm.
    auto_draping_direction :
        If ``True``, the fiber direction of the production ply at the draping
         seed point is used as draping direction.
    draping_direction :
        Set the primary draping direction for the draping algorithm. Only used if
        ``auto_draping_direction`` is ``False``.
    use_default_draping_mesh_size :
        Whether to use the average element size of the shell mesh for the draping.
    draping_mesh_size :
        Defines the mesh size for the draping algorithm.  If set to ``-1.``, the
        mesh size is automatically determined based on the average element size.
    draping_thickness_correction :
        Enables the thickness correction of draped plies based on the draping
        shear angle.
    draping_angle_1_field :
        Correction angle between the fiber and draped fiber directions, in degree.
    draping_angle_2_field :
        Correction angle between the transverse and draped transverse directions,
        in degree. Optional, uses the same values as ``draping_angle_1_field``
        (no shear) by default.
    thickness_type :
        Choose between :attr:`ThicknessType.FROM_GEOMETRY` or
        :attr:`ThicknessType.FROM_TABLE` to define a ply with variable thickness.
        The default value is :attr:`ThicknessType.NOMINAL`, which means the ply
        thickness is constant and determined by the thickness of the ply material.
    thickness_geometry :
        Defines the geometry used to determine the ply thickness. Only applies if
        ``thickness_type`` is :attr:`ThicknessType.FROM_GEOMETRY`.
    thickness_field :
        Defines the look-up table column used to determine the ply thickness.
        Only applies if ``thickness_type`` is :attr:`ThicknessType.FROM_TABLE`.
    thickness_field_type :
        If ``thickness_type`` is :attr:`ThicknessType.FROM_TABLE`, this parameter
        determines how the thickness values are interpreted. They can be either
        absolute values (:attr:`ThicknessFieldType.ABSOLUTE_VALUES`) or relative
        values (:attr:`ThicknessFieldType.RELATIVE_SCALING_FACTOR`).
    taper_edges :
        Defines the taper edges of the ply.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "modeling_plies"
    _OBJECT_INFO_TYPE = modeling_ply_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = modeling_ply_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "ModelingPly",
        ply_material: Fabric | Stackup | SubLaminate | None = None,
        oriented_selection_sets: Container[OrientedSelectionSet] = (),
        ply_angle: float = 0.0,
        number_of_layers: int = 1,
        active: bool = True,
        # Backend will automatically assign a consistent global_ply_nr
        # if global_ply_nr == 0
        global_ply_nr: int = 0,
        selection_rules: Iterable[LinkedSelectionRule] = (),
        draping_type: DrapingType = DrapingType.NO_DRAPING,
        draping_seed_point: tuple[float, float, float] = (0.0, 0.0, 0.0),
        auto_draping_direction: bool = True,
        draping_direction: tuple[float, float, float] = (1.0, 0.0, 0.0),
        use_default_draping_mesh_size: bool = True,
        draping_mesh_size: float = 0.0,
        draping_thickness_correction: bool = True,
        draping_angle_1_field: LookUpTable1DColumn | LookUpTable3DColumn | None = None,
        draping_angle_2_field: LookUpTable1DColumn | LookUpTable3DColumn | None = None,
        thickness_type: ThicknessType = ThicknessType.NOMINAL,
        thickness_geometry: VirtualGeometry | None = None,
        thickness_field: LookUpTable1DColumn | LookUpTable3DColumn | None = None,
        thickness_field_type: ThicknessFieldType = ThicknessFieldType.ABSOLUTE_VALUES,
        taper_edges: Iterable[TaperEdge] = (),
    ):
        super().__init__(name=name)

        self.oriented_selection_sets = oriented_selection_sets
        self.ply_material = ply_material
        self.ply_angle = ply_angle
        self.number_of_layers = number_of_layers
        self.active = active
        self.global_ply_nr = global_ply_nr
        self.selection_rules = selection_rules
        self.draping_type = draping_type
        self.draping_seed_point = draping_seed_point
        self.auto_draping_direction = auto_draping_direction
        self.draping_direction = draping_direction
        self.use_default_draping_mesh_size = use_default_draping_mesh_size
        self.draping_mesh_size = draping_mesh_size
        self.draping_thickness_correction = draping_thickness_correction
        self.draping_angle_1_field = draping_angle_1_field
        self.draping_angle_2_field = draping_angle_2_field
        self.thickness_type = thickness_type
        self.thickness_geometry = thickness_geometry
        self.thickness_field = thickness_field
        self.thickness_field_type = thickness_field_type
        self.taper_edges = taper_edges

    def _create_stub(self) -> modeling_ply_pb2_grpc.ObjectServiceStub:
        return modeling_ply_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    ply_material = grpc_link_property(
        "properties.ply_material", allowed_types=(Fabric, Stackup, SubLaminate)
    )

    oriented_selection_sets = define_linked_object_list(
        "properties.oriented_selection_sets", OrientedSelectionSet
    )

    ply_angle: ReadWriteProperty[float, float] = grpc_data_property("properties.ply_angle")
    number_of_layers: ReadWriteProperty[int, int] = grpc_data_property(
        "properties.number_of_layers"
    )
    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")
    global_ply_nr: ReadWriteProperty[int, int] = grpc_data_property("properties.global_ply_nr")

    draping_type = grpc_data_property(
        "properties.draping", from_protobuf=draping_type_from_pb, to_protobuf=draping_type_to_pb
    )
    draping_seed_point = grpc_data_property(
        "properties.draping_seed_point",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    auto_draping_direction: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.auto_draping_direction"
    )
    draping_direction = grpc_data_property(
        "properties.draping_direction",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    use_default_draping_mesh_size: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_default_draping_mesh_size"
    )
    draping_mesh_size: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.draping_mesh_size"
    )
    draping_thickness_correction: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.draping_thickness_correction"
    )
    draping_angle_1_field = grpc_link_property(
        "properties.draping_angle_1_field", allowed_types=(LookUpTable1DColumn, LookUpTable3DColumn)
    )
    draping_angle_2_field = grpc_link_property(
        "properties.draping_angle_2_field", allowed_types=(LookUpTable1DColumn, LookUpTable3DColumn)
    )

    selection_rules = define_edge_property_list("properties.selection_rules", LinkedSelectionRule)
    add_selection_rule = define_add_method(
        LinkedSelectionRule,
        attribute_name="selection_rules",
        func_name="add_selection_rule",
        parent_class_name="ModelingPly",
        module_name=__module__,
    )

    thickness_type = grpc_data_property(
        "properties.thickness_type",
        from_protobuf=thickness_type_from_pb,
        to_protobuf=thickness_type_to_pb,
    )
    thickness_geometry = grpc_link_property(
        "properties.thickness_geometry", allowed_types=VirtualGeometry
    )
    thickness_field = grpc_link_property(
        "properties.thickness_field", allowed_types=(LookUpTable1DColumn, LookUpTable3DColumn)
    )
    thickness_field_type = grpc_data_property(
        "properties.thickness_field_type",
        from_protobuf=thickness_field_type_from_pb,
        to_protobuf=thickness_field_type_to_pb,
    )

    taper_edges = define_edge_property_list("properties.taper_edges", TaperEdge)
    add_taper_edge = define_add_method(
        TaperEdge,
        attribute_name="taper_edges",
        func_name="add_taper_edge",
        parent_class_name="ModelingPly",
        module_name=__module__,
    )

    production_plies = get_read_only_collection_property(
        ProductionPly, production_ply_pb2_grpc.ObjectServiceStub
    )

    mesh = full_mesh_property
    shell_mesh = shell_mesh_property

    elemental_data = elemental_data_property(ModelingPlyElementalData)
    nodal_data = nodal_data_property(ModelingPlyNodalData)
