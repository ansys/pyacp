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

from ansys.api.acp.v0 import enum_types_pb2, layup_mapping_object_pb2, layup_mapping_object_pb2_grpc

from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.enum_wrapper import wrap_to_string_enum
from ._grpc_helpers.linked_object_list import (
    define_linked_object_list,
    define_polymorphic_linked_object_list,
)
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .element_set import ElementSet
from .enums import (
    BaseElementMaterialHandling,
    ElementTechnology,
    ReinforcingBehavior,
    StressStateType,
    base_element_material_handling_from_pb,
    base_element_material_handling_to_pb,
    element_technology_from_pb,
    element_technology_to_pb,
    reinforcing_behavior_from_pb,
    reinforcing_behavior_to_pb,
    status_type_from_pb,
    stress_state_type_from_pb,
    stress_state_type_to_pb,
)
from .imported_modeling_group import ImportedModelingGroup
from .imported_modeling_ply import ImportedModelingPly
from .material import Material
from .modeling_group import ModelingGroup
from .modeling_ply import ModelingPly
from .object_registry import register
from .rosette import Rosette
from .solid_element_set import SolidElementSet

__all__ = ["LayupMappingObject", "LayupMappingRosetteSelectionMethod"]


(
    LayupMappingRosetteSelectionMethod,
    layup_mapping_rosette_selection_method_to_pb,
    layup_mapping_rosette_selection_method_from_pb,
) = wrap_to_string_enum(
    "LayupMappingRosetteSelectionMethod",
    enum_types_pb2.RosetteSelectionMethod,
    module=__name__,
    doc="Options for how the rosette is selected in the layup mapping.",
    explicit_value_list=(
        enum_types_pb2.RosetteSelectionMethod.MINIMUM_DISTANCE,
        enum_types_pb2.RosetteSelectionMethod.MINIMUM_DISTANCE_SUPERPOSED,
    ),
)


@mark_grpc_properties
@register
class LayupMappingObject(CreatableTreeObject, IdTreeObject):
    """Instantiate a layup mapping object.

    Parameters
    ----------
    name :
        Name of the layup mapping object.
    active :
        Inactive layup mapping objects are not used.
    element_technology :
        Determines the element technology used for the layup mapping.
        Can be either ``"layered_element"`` or ``"reinforcing"``.
        Note that only brick and prism elements support the layered option,
        while reinforcing technology can be combined with all types of
        solid elements.
    shell_element_sets :
        Defines the shell area whose modeling plies are mapped onto the
        solid mesh.
        Used only if ``use_imported_plies`` is False.
    use_imported_plies :
        If True, imported modeling plies are mapped onto the solid mesh.
    select_all_plies :
        Determines whether all plies are selected for mapping, or only
        the ones specified in the ``sequences`` parameter.

        * If ``use_imported_plies`` is False and ``select_all_plies`` is True,
          all plies in the selected shell area are selected.
        * If ``use_imported_plies`` is True and ``select_all_plies`` is True,
          all imported modeling plies are selected.

    sequences :
        Determines which plies are considered for mapping. The intersection
        of shell elements and plies are then mapped onto the solid mesh.

        * If ``use_imported_plies`` is False, modeling groups and modeling
          plies are allowed
        * If ``use_imported_plies`` is True, imported modeling groups and
          imported modeling plies are allowed

    entire_solid_mesh :
        If True, the selected layup is mapped onto the entire solid mesh.
        Otherwise, the ``solid_element_sets`` parameter is used to refine
        the scope.
    solid_element_sets :
        List of solid element sets to which the mapping is applied.
    scale_ply_thicknesses :
        If True, scale the layer thickness to fill the gaps within an element,
        instead of filling them with the void material.
        Used only if ``element_technology`` is ``"layered_element"``.
    void_material :
        Material used to fill the gaps with.
        Only used if ``scale_ply_thicknesses`` is False, and
        the ``element_technology`` is ``"layered_element"``.
    minimum_void_material_thickness :
        Only gaps with a thickness greater than this value are filled with
        the void material.
        Only used if ``scale_ply_thicknesses`` is False, and
        the ``element_technology`` is ``"layered_element"``.
    delete_lost_elements :
        If True, elements without layup and degenerated elements are deleted.
        Otherwise, they are filled with the filler material.
        Used only if ``element_technology`` is ``"layered_element"``.
    filler_material :
        Material used to fill the degenerated elements.
        Only used if ``delete_lost_elements`` is False, and
        the ``element_technology`` is ``"layered_element"``.
    rosettes :
        List of rosettes to set the coordinate system of the filler elements.
        Used only if ``element_technology`` is ``"layered_element"``.
    rosette_selection_method :
        Defines how the coordinate systems are applied for the filler elements.
        Used only if ``element_technology`` is ``"layered_element"``.
    reinforcing_behavior :
        Determines whether the reinforcing elements carry tension and / or
        compression loads.
        Used only if ``element_technology`` is ``"reinforcing"``.
    base_element_material_handling :
        Determines how the base material is handled in the area with reinforcing
        elements. Can be either ``"remove"`` or ``"retain"``.
        Used only if ``element_technology`` is ``"reinforcing"``.
    stress_state :
        Specifies the stress state of the reinforcing elements.
        Used only if ``element_technology`` is ``"reinforcing"``.
    base_material :
        Define the initial material of the solid elements which will be reinforced
        by the selected plies.
        Used only if ``element_technology`` is ``"reinforcing"``.
    base_element_rosettes :
        List of rosettes to set the coordinate system of the base elements.
        This is important if the base material has an orthotropic characteristic.
        Used only if ``element_technology`` is ``"reinforcing"``.
    base_element_rosette_selection_method :
        Defines how the coordinate systems are applied for the base elements.
        Used only if ``element_technology`` is ``"reinforcing"``.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "layup_mapping_objects"
    _OBJECT_INFO_TYPE = layup_mapping_object_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = layup_mapping_object_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "LayupMappingObject",
        active: bool = True,
        element_technology: ElementTechnology = ElementTechnology.LAYERED_ELEMENT,
        shell_element_sets: Sequence[ElementSet] = (),
        use_imported_plies: bool = False,
        select_all_plies: bool = True,
        sequences: Sequence[
            ModelingGroup | ModelingPly | ImportedModelingGroup | ImportedModelingPly
        ] = (),
        entire_solid_mesh: bool = True,
        solid_element_sets: Sequence[SolidElementSet] = (),
        scale_ply_thicknesses: bool = True,
        void_material: Material | None = None,
        minimum_void_material_thickness: float = 1e-6,
        delete_lost_elements: bool = True,
        filler_material: Material | None = None,
        rosettes: Sequence[Rosette] = (),
        rosette_selection_method: LayupMappingRosetteSelectionMethod = LayupMappingRosetteSelectionMethod.MINIMUM_DISTANCE,  # type: ignore # noqa: E501
        reinforcing_behavior: ReinforcingBehavior = ReinforcingBehavior.TENSION_AND_COMPRESSION,
        base_element_material_handling: BaseElementMaterialHandling = BaseElementMaterialHandling.REMOVE,  # noqa: E501
        stress_state: StressStateType = StressStateType.PLANE_STRESS_STATE_WITH_TRANSVERSE_SHEAR_AND_BENDING_STIFFNESS,  # noqa: E501
        base_material: Material | None = None,
        base_element_rosettes: Sequence[Rosette] = (),
        base_element_rosette_selection_method: LayupMappingRosetteSelectionMethod = LayupMappingRosetteSelectionMethod.MINIMUM_DISTANCE,  # type: ignore # noqa: E501
    ):
        super().__init__(name=name)
        self.active = active
        self.element_technology = element_technology
        self.shell_element_sets = shell_element_sets
        self.use_imported_plies = use_imported_plies
        self.select_all_plies = select_all_plies
        self.sequences = sequences
        self.entire_solid_mesh = entire_solid_mesh
        self.solid_element_sets = solid_element_sets
        self.scale_ply_thicknesses = scale_ply_thicknesses
        self.void_material = void_material
        self.minimum_void_material_thickness = minimum_void_material_thickness
        self.delete_lost_elements = delete_lost_elements
        self.filler_material = filler_material
        self.rosettes = rosettes
        self.rosette_selection_method = rosette_selection_method
        self.reinforcing_behavior = reinforcing_behavior
        self.base_element_material_handling = base_element_material_handling
        self.stress_state = stress_state
        self.base_material = base_material
        self.base_element_rosettes = base_element_rosettes
        self.base_element_rosette_selection_method = base_element_rosette_selection_method

    def _create_stub(self) -> layup_mapping_object_pb2_grpc.ObjectServiceStub:
        return layup_mapping_object_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")
    element_technology = grpc_data_property(
        "properties.element_technology",
        from_protobuf=element_technology_from_pb,
        to_protobuf=element_technology_to_pb,
    )
    shell_element_sets = define_linked_object_list(
        "properties.shell_element_sets", object_class=ElementSet
    )
    use_imported_plies: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_imported_plies"
    )
    select_all_plies: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.select_all_plies"
    )
    sequences = define_polymorphic_linked_object_list(
        "properties.sequences",
        allowed_types=(ModelingGroup, ModelingPly, ImportedModelingGroup, ImportedModelingPly),
    )
    entire_solid_mesh: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.entire_solid_mesh"
    )
    solid_element_sets = define_linked_object_list(
        "properties.solid_element_sets", object_class=SolidElementSet
    )
    scale_ply_thicknesses: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.scale_ply_thicknesses"
    )
    void_material = grpc_link_property("properties.void_material", allowed_types=(Material,))
    minimum_void_material_thickness: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.minimum_void_material_thickness"
    )
    delete_lost_elements: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.delete_lost_elements"
    )
    filler_material = grpc_link_property("properties.filler_material", allowed_types=(Material,))
    rosettes = define_linked_object_list("properties.rosettes", object_class=Rosette)
    rosette_selection_method = grpc_data_property(
        "properties.rosette_selection_method",
        from_protobuf=layup_mapping_rosette_selection_method_from_pb,
        to_protobuf=layup_mapping_rosette_selection_method_to_pb,
    )
    reinforcing_behavior = grpc_data_property(
        "properties.reinforcing_behavior",
        from_protobuf=reinforcing_behavior_from_pb,
        to_protobuf=reinforcing_behavior_to_pb,
    )
    base_element_material_handling = grpc_data_property(
        "properties.base_element_material_handling",
        from_protobuf=base_element_material_handling_from_pb,
        to_protobuf=base_element_material_handling_to_pb,
    )
    stress_state = grpc_data_property(
        "properties.stress_state",
        from_protobuf=stress_state_type_from_pb,
        to_protobuf=stress_state_type_to_pb,
    )
    base_material = grpc_link_property("properties.base_material", allowed_types=(Material,))
    base_element_rosettes = define_linked_object_list(
        "properties.base_element_rosettes", object_class=Rosette
    )
    base_element_rosette_selection_method = grpc_data_property(
        "properties.base_element_rosette_selection_method",
        from_protobuf=layup_mapping_rosette_selection_method_from_pb,
        to_protobuf=layup_mapping_rosette_selection_method_to_pb,
    )
