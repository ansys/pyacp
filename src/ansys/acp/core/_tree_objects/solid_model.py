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

from collections.abc import Iterable
import dataclasses
from typing import Any

from ansys.api.acp.v0 import (
    analysis_ply_pb2_grpc,
    cut_off_geometry_pb2_grpc,
    extrusion_guide_pb2_grpc,
    snap_to_geometry_pb2_grpc,
    solid_element_set_pb2_grpc,
    solid_model_pb2,
    solid_model_pb2_grpc,
)

from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from ._elemental_or_nodal_data import (
    ElementalData,
    NodalData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from ._grpc_helpers.linked_object_list import (
    define_linked_object_list,
    define_polymorphic_linked_object_list,
)
from ._grpc_helpers.mapping import (
    define_create_method,
    define_mutable_mapping,
    get_read_only_collection_property,
)
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from ._solid_model_export import SolidModelExportMixin
from .analysis_ply import AnalysisPly
from .base import (
    CreatableTreeObject,
    IdTreeObject,
    TreeObjectAttributeWithCache,
    nested_grpc_object_property,
)
from .cut_off_geometry import CutOffGeometry
from .edge_set import EdgeSet
from .element_set import ElementSet
from .enums import (
    DropOffType,
    ExtrusionMethod,
    SolidModelOffsetDirectionType,
    drop_off_type_from_pb,
    drop_off_type_to_pb,
    extrusion_method_type_from_pb,
    extrusion_method_type_to_pb,
    offset_direction_type_from_pb,
    offset_direction_type_to_pb,
    status_type_from_pb,
)
from .extrusion_guide import ExtrusionGuide
from .material import Material
from .modeling_ply import ModelingPly
from .object_registry import register
from .oriented_selection_set import OrientedSelectionSet
from .snap_to_geometry import SnapToGeometry
from .solid_element_set import SolidElementSet

__all__ = [
    "SolidModel",
    "DropOffSettings",
    "SolidModelExportSettings",
    "SolidModelElementalData",
    "SolidModelNodalData",
]


@dataclasses.dataclass
class SolidModelElementalData(ElementalData):
    """Represents elemental data for a Solid Model."""

    normal: VectorData | None = None


@dataclasses.dataclass
class SolidModelNodalData(NodalData):
    """Represents nodal data for a Solid Model."""


@mark_grpc_properties
class DropOffSettings(TreeObjectAttributeWithCache):
    """Defines the drop-off settings for a solid model.

    Parameters
    ----------
    drop_off_type :
        Determines whether the ply's drop-off is inside or outside the boundary
        of the ply.
    disable_drop_offs_on_bottom :
        Whether to remove drop-offs on the bottom surface of the laminate.
    drop_off_disabled_on_bottom_sets :
        Element sets or oriented selection sets on which drop-offs at the bottom
        surface are disabled.
    disable_drop_offs_on_top :
        Whether to remove drop-offs on the top surface of the laminate.
    drop_off_disabled_on_top_sets :
        Element sets or oriented selection sets on which drop-offs at the top
        surface are disabled.
    connect_butt_joined_plies :
        Prevent an element drop-off of two adjacent, sequential plies in the same
        modeling group.
    """

    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        drop_off_type: DropOffType = DropOffType.INSIDE_PLY,
        disable_drop_offs_on_bottom: bool = False,
        drop_off_disabled_on_bottom_sets: Iterable[ElementSet | OrientedSelectionSet] = (),
        disable_drop_offs_on_top: bool = False,
        drop_off_disabled_on_top_sets: Iterable[ElementSet | OrientedSelectionSet] = (),
        connect_butt_joined_plies: bool = True,
        _parent_object: SolidModel | None = None,
        _pb_object: Any | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(
            _parent_object=_parent_object,
            _pb_object=_pb_object,
            _attribute_path=_attribute_path,
        )
        # The '__init__' method can be called either with the explicit values
        # defined below, or from a parent object or protobuf object. In the case
        # where a parent object or protobuf object is provided, the explicit values
        # must not be set, otherwise the default values will override the existing
        # values.
        if _parent_object is None and _pb_object is None:
            self.drop_off_type = drop_off_type
            self.disable_drop_offs_on_bottom = disable_drop_offs_on_bottom
            self.drop_off_disabled_on_bottom_sets = drop_off_disabled_on_bottom_sets
            self.disable_drop_offs_on_top = disable_drop_offs_on_top
            self.drop_off_disabled_on_top_sets = drop_off_disabled_on_top_sets
            self.connect_butt_joined_plies = connect_butt_joined_plies

    @classmethod
    def _create_default_pb_object(self) -> solid_model_pb2.DropOffSettings:
        # There's no need to define the 'real' default values here, since
        # this method is only called when the object is created from scratch.
        # In that case, the '__init__' method will be called with the default
        # values defined there.
        # NOTE dgresch Oct'24: I'm not sure if '_create_default_pb_object' is
        # the right abstraction overall.
        # The concept _could_ be useful for avoiding the duplicate logic of
        # checking '_parent_object is None and _pb_object is None' (this class's
        # '__init__', and the 'TreeObjectAttribute.__init__').
        # But, it would need to be extended to allow also _overriding_ the defaults
        # on calling __init__.
        return solid_model_pb2.DropOffSettings()

    drop_off_type = grpc_data_property(
        "drop_off_type",
        from_protobuf=drop_off_type_from_pb,
        to_protobuf=drop_off_type_to_pb,
    )

    disable_drop_offs_on_bottom: ReadWriteProperty[bool, bool] = grpc_data_property(
        "disable_dropoffs_on_bottom"
    )
    drop_off_disabled_on_bottom_sets = define_polymorphic_linked_object_list(
        "dropoff_disabled_on_bottom_sets", allowed_types=(ElementSet, OrientedSelectionSet)
    )

    disable_drop_offs_on_top: ReadWriteProperty[bool, bool] = grpc_data_property(
        "disable_dropoffs_on_top"
    )
    drop_off_disabled_on_top_sets = define_polymorphic_linked_object_list(
        "dropoff_disabled_on_top_sets", allowed_types=(ElementSet, OrientedSelectionSet)
    )

    connect_butt_joined_plies: ReadWriteProperty[bool, bool] = grpc_data_property(
        "connect_butt_joined_plies"
    )


@mark_grpc_properties
class SolidModelExportSettings(TreeObjectAttributeWithCache):
    """Defines the settings for exporting a solid model.

    Parameters
    ----------
    use_default_section_index :
        Use the default start index for sections.
    section_index :
        Custom start index for sections.
        Only used if ``use_default_section_index`` is False.
    use_default_coordinate_system_index :
        Use the default start index for coordinate systems.
    coordinate_system_index :
        Custom start index for coordinate systems.
        Only used if ``use_default_coordinate_system_index`` is False.
    use_default_material_index :
        Use the default start index for materials.
    material_index :
        Custom start index for materials.
        Only used if ``use_default_material_index`` is False.
    use_default_node_index :
        Use the default start index for nodes.
    node_index :
        Custom start index for nodes.
        Only used if ``use_default_node_index`` is False.
    use_default_element_index :
        Use the default start index for elements.
    element_index :
        Custom start index for elements.
        Only used if ``use_default_element_index`` is False.
    use_solsh_elements :
        When True, export linear layered elements as Solsh (Solid190).
    write_degenerated_elements :
        Whether to export drop-off and cut-off elements.
    drop_hanging_nodes :
        When True, the hanging nodes of quadratic solid meshes are dropped.
    use_solid_model_prefix :
        Use the solid model name as a prefix for the exported file.
    transfer_all_sets :
        When True, all element sets and edge sets are exported.
    transferred_element_sets :
        Element sets to be exported.
        Only used if ``transfer_all_sets`` is False.
    transferred_edge_sets :
        Edge sets to be exported.
        Only used if ``transfer_all_sets`` is False.

    """

    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        use_default_section_index: bool = True,
        section_index: int = 0,
        use_default_coordinate_system_index: bool = True,
        coordinate_system_index: int = 0,
        use_default_material_index: bool = True,
        material_index: int = 0,
        use_default_node_index: bool = True,
        node_index: int = 0,
        use_default_element_index: bool = True,
        element_index: int = 0,
        use_solsh_elements: bool = False,
        write_degenerated_elements: bool = True,
        drop_hanging_nodes: bool = True,
        use_solid_model_prefix: bool = True,
        transfer_all_sets: bool = True,
        transferred_element_sets: Iterable[ElementSet] = (),
        transferred_edge_sets: Iterable[EdgeSet] = (),
        _parent_object: SolidModel | None = None,
        _pb_object: Any | None = None,
        _attribute_path: str | None = None,
    ):
        super().__init__(
            _parent_object=_parent_object,
            _pb_object=_pb_object,
            _attribute_path=_attribute_path,
        )
        # See comment on DropOffSettings.__init__ for the logic here.
        if _parent_object is None and _pb_object is None:
            self.use_default_section_index = use_default_section_index
            self.section_index = section_index
            self.use_default_coordinate_system_index = use_default_coordinate_system_index
            self.coordinate_system_index = coordinate_system_index
            self.use_default_material_index = use_default_material_index
            self.material_index = material_index
            self.use_default_node_index = use_default_node_index
            self.node_index = node_index
            self.use_default_element_index = use_default_element_index
            self.element_index = element_index
            self.use_solsh_elements = use_solsh_elements
            self.write_degenerated_elements = write_degenerated_elements
            self.drop_hanging_nodes = drop_hanging_nodes
            self.use_solid_model_prefix = use_solid_model_prefix
            self.transfer_all_sets = transfer_all_sets
            self.transferred_element_sets = transferred_element_sets
            self.transferred_edge_sets = transferred_edge_sets

    @classmethod
    def _create_default_pb_object(self) -> solid_model_pb2.ExportSettings:
        # See comment on DropOffSettings._create_default_pb_object
        return solid_model_pb2.ExportSettings()

    use_default_section_index: ReadWriteProperty[bool, bool] = grpc_data_property(
        "use_default_section_index"
    )
    section_index: ReadWriteProperty[int, int] = grpc_data_property("section_index")
    use_default_coordinate_system_index: ReadWriteProperty[bool, bool] = grpc_data_property(
        "use_default_coordinate_system_index"
    )
    coordinate_system_index: ReadWriteProperty[int, int] = grpc_data_property(
        "coordinate_system_index"
    )
    use_default_material_index: ReadWriteProperty[bool, bool] = grpc_data_property(
        "use_default_material_index"
    )
    material_index: ReadWriteProperty[int, int] = grpc_data_property("material_index")
    use_default_node_index: ReadWriteProperty[bool, bool] = grpc_data_property(
        "use_default_node_index"
    )
    node_index: ReadWriteProperty[int, int] = grpc_data_property("node_index")
    use_default_element_index: ReadWriteProperty[bool, bool] = grpc_data_property(
        "use_default_element_index"
    )
    element_index: ReadWriteProperty[int, int] = grpc_data_property("element_index")
    use_solsh_elements: ReadWriteProperty[bool, bool] = grpc_data_property("use_solsh_elements")
    write_degenerated_elements: ReadWriteProperty[bool, bool] = grpc_data_property(
        "write_degenerated_elements"
    )
    drop_hanging_nodes: ReadWriteProperty[bool, bool] = grpc_data_property("drop_hanging_nodes")
    use_solid_model_prefix: ReadWriteProperty[bool, bool] = grpc_data_property(
        "use_solid_model_prefix"
    )
    transfer_all_sets: ReadWriteProperty[bool, bool] = grpc_data_property("transfer_all_sets")
    transferred_element_sets = define_linked_object_list("transferred_element_sets", ElementSet)
    transferred_edge_sets = define_linked_object_list("transferred_edge_sets", EdgeSet)


@mark_grpc_properties
@register
class SolidModel(SolidModelExportMixin, CreatableTreeObject, IdTreeObject):
    """Instantiate a solid model.

    Parameters
    ----------
    name :
        Name of the solid model.
    active :
        Inactive solid models are not computed, and ignored in the analysis.
    element_sets :
        Element sets or oriented selection sets determining the extent of
        the solid model.
    extrusion_method :
        Determines how plies are bundled in the layered solid elements.
    max_element_thickness :
        Maximum thickness of the layered solid elements. A new element is
        introduced if the thickness exceeds this value.
        Only used if the ``extrusion_method`` is one of ``SPECIFY_THICKNESS``,
        ``MATERIAL_WISE``, or ``SANDWICH_WISE``.
    ply_group_pointers :
        Explicitly defines modeling plies where a new element is introduced.
        Only used if the ``extrusion_method`` is ``USER_DEFINED``.
    offset_direction_type :
        Determines how the extrusion direction is defined. With ``SHELL_NORMAL``,
        the normal direction of the shell is used during the entire extrusion.
        With ``SURFACE_NORMAL``, the offset direction is re-evaluated based
        on the surface of the solid model during the extrusion.
    skip_elements_without_plies :
        If True, elements without plies are automatically removed from the
        region of extrusion. This means that no drop-off elements are created
        for these elements.
    drop_off_material :
        This material is assigned to the layered solid drop-off elements if
        ``drop_off_material_handling`` is set to ``GLOBAL`` in the fabric
        definition.
    cut_off_material :
        This material is assigned to the degenerated solid cut-off elements if
        ``cut_off_material_handling`` is set to ``GLOBAL`` in the fabric
        definition.
    delete_bad_elements :
        If True, a final element check is performed to remove erroneous elements.
    warping_limit :
        Maximum allowable warping limit used in the element shape check. Elements
        with a warping limit exceeding this value are removed.
        Only used if ``delete_bad_elements`` is True.
    minimum_volume :
        Solid elements with a volume smaller or equal to this value are removed.
        With the default value of ``0``, only inverted or zero-volume elements
        are removed.
        Only used if ``delete_bad_elements`` is True.
    drop_off_settings :
        Determines how drop-off elements are handled in the solid model extrusion.
    export_settings :
        Defines the settings for exporting the solid model.

    """

    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "solid_models"
    _OBJECT_INFO_TYPE = solid_model_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = solid_model_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "SolidModel",
        active: bool = True,
        element_sets: Iterable[ElementSet | OrientedSelectionSet] = (),
        extrusion_method: ExtrusionMethod = ExtrusionMethod.ANALYSIS_PLY_WISE,
        max_element_thickness: float = 1.0,
        ply_group_pointers: Iterable[ModelingPly] = (),
        offset_direction_type: SolidModelOffsetDirectionType = SolidModelOffsetDirectionType.SHELL_NORMAL,
        skip_elements_without_plies: bool = False,
        drop_off_material: Material | None = None,
        cut_off_material: Material | None = None,
        delete_bad_elements: bool = True,
        warping_limit: float = 0.4,
        minimum_volume: float = 0.0,
        drop_off_settings: DropOffSettings = DropOffSettings(),
        export_settings: SolidModelExportSettings = SolidModelExportSettings(),
    ):
        super().__init__(
            name=name,
        )
        self.active = active
        self.element_sets = element_sets
        self.extrusion_method = extrusion_method
        self.max_element_thickness = max_element_thickness
        self.ply_group_pointers = ply_group_pointers
        self.offset_direction_type = offset_direction_type
        self.skip_elements_without_plies = skip_elements_without_plies
        self.drop_off_material = drop_off_material
        self.cut_off_material = cut_off_material
        self.delete_bad_elements = delete_bad_elements
        self.warping_limit = warping_limit
        self.minimum_volume = minimum_volume
        self.drop_off_settings = drop_off_settings
        self.export_settings = export_settings

    def _create_stub(self) -> solid_model_pb2_grpc.ObjectServiceStub:
        return solid_model_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")

    element_sets = define_polymorphic_linked_object_list(
        "properties.element_sets", allowed_types=(ElementSet, OrientedSelectionSet)
    )
    extrusion_method = grpc_data_property(
        "properties.extrusion_method",
        from_protobuf=extrusion_method_type_from_pb,
        to_protobuf=extrusion_method_type_to_pb,
    )
    max_element_thickness: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.max_element_thickness"
    )
    ply_group_pointers = define_linked_object_list("properties.ply_group_pointers", ModelingPly)
    offset_direction_type = grpc_data_property(
        "properties.offset_direction",
        from_protobuf=offset_direction_type_from_pb,
        to_protobuf=offset_direction_type_to_pb,
    )
    skip_elements_without_plies: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.skip_elements_without_plies"
    )
    drop_off_material = grpc_link_property("properties.drop_off_material", allowed_types=Material)
    cut_off_material = grpc_link_property("properties.cut_off_material", allowed_types=Material)
    delete_bad_elements: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.delete_bad_elements"
    )
    warping_limit: ReadWriteProperty[float, float] = grpc_data_property("properties.warping_limit")
    minimum_volume: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.minimum_volume"
    )

    drop_off_settings = nested_grpc_object_property("properties.drop_off_settings", DropOffSettings)
    export_settings = nested_grpc_object_property(
        "properties.export_settings", SolidModelExportSettings
    )

    create_extrusion_guide = define_create_method(
        ExtrusionGuide,
        func_name="create_extrusion_guide",
        parent_class_name="SolidModel",
        module_name=__module__,
    )
    extrusion_guides = define_mutable_mapping(
        ExtrusionGuide, extrusion_guide_pb2_grpc.ObjectServiceStub
    )

    create_snap_to_geometry = define_create_method(
        SnapToGeometry,
        func_name="create_snap_to_geometry",
        parent_class_name="SolidModel",
        module_name=__module__,
    )
    snap_to_geometries = define_mutable_mapping(
        SnapToGeometry, snap_to_geometry_pb2_grpc.ObjectServiceStub
    )

    solid_element_sets = get_read_only_collection_property(
        SolidElementSet, solid_element_set_pb2_grpc.ObjectServiceStub
    )

    create_cut_off_geometry = define_create_method(
        CutOffGeometry,
        func_name="create_cut_off_geometry",
        parent_class_name="SolidModel",
        module_name=__module__,
    )
    cut_off_geometries = define_mutable_mapping(
        CutOffGeometry, cut_off_geometry_pb2_grpc.ObjectServiceStub
    )

    analysis_plies = get_read_only_collection_property(
        AnalysisPly, analysis_ply_pb2_grpc.ObjectServiceStub
    )

    elemental_data = elemental_data_property(SolidModelElementalData)
    nodal_data = nodal_data_property(SolidModelNodalData)
