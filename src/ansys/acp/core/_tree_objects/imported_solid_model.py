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
    cut_off_geometry_pb2_grpc,
    enum_types_pb2,
    imported_solid_model_pb2,
    imported_solid_model_pb2_grpc,
    layup_mapping_object_pb2_grpc,
    solid_element_set_pb2_grpc,
    solid_model_pb2,
)

from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from .._utils.typing_helper import PATH as _PATH
from ._elemental_or_nodal_data import (
    ElementalData,
    NodalData,
    elemental_data_property,
    nodal_data_property,
)
from ._grpc_helpers.enum_wrapper import wrap_to_string_enum
from ._grpc_helpers.exceptions import wrap_grpc_errors
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
from ._mesh_data import solid_mesh_property
from ._solid_model_export import SolidModelExportMixin
from .base import (
    CreatableTreeObject,
    IdTreeObject,
    TreeObjectAttributeWithCache,
    nested_grpc_object_property,
)
from .cut_off_geometry import CutOffGeometry
from .enums import (
    UnitSystemType,
    status_type_from_pb,
    unit_system_type_from_pb,
    unit_system_type_to_pb,
)
from .layup_mapping_object import LayupMappingObject
from .material import Material
from .object_registry import register
from .solid_element_set import SolidElementSet

__all__ = [
    "ImportedSolidModel",
    "SolidModelImportFormat",
    "ImportedSolidModelExportSettings",
    "ImportedSolidModelElementalData",
    "ImportedSolidModelNodalData",
]


SolidModelImportFormat, solid_model_import_format_to_pb, solid_model_import_format_from_pb = (
    wrap_to_string_enum(
        "SolidModelImportFormat",
        enum_types_pb2.FileFormat,
        module=__name__,
        value_converter=lambda val: val.lower().replace("_", ":"),
        doc="Options for the file format when importing a solid model.",
        explicit_value_list=(
            enum_types_pb2.FileFormat.ANSYS_H5,
            enum_types_pb2.FileFormat.ANSYS_CDB,
            enum_types_pb2.FileFormat.ANSYS_DAT,
        ),
    )
)


@dataclasses.dataclass
class ImportedSolidModelElementalData(ElementalData):
    """Represents elemental data for an imported solid model."""


@dataclasses.dataclass
class ImportedSolidModelNodalData(NodalData):
    """Represents nodal data for an imported solid model."""


@mark_grpc_properties
class ImportedSolidModelExportSettings(TreeObjectAttributeWithCache):
    """Defines the settings for exporting an imported solid model.

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
    drop_hanging_nodes :
        When True, the hanging nodes of quadratic solid meshes are dropped.
    use_solid_model_prefix :
        Use the imported solid model name as a prefix for the exported file.

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
        drop_hanging_nodes: bool = True,
        use_solid_model_prefix: bool = True,
        _parent_object: ImportedSolidModel | None = None,
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
            self.drop_hanging_nodes = drop_hanging_nodes
            self.use_solid_model_prefix = use_solid_model_prefix

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
    drop_hanging_nodes: ReadWriteProperty[bool, bool] = grpc_data_property("drop_hanging_nodes")
    use_solid_model_prefix: ReadWriteProperty[bool, bool] = grpc_data_property(
        "use_solid_model_prefix"
    )


@mark_grpc_properties
@register
class ImportedSolidModel(SolidModelExportMixin, CreatableTreeObject, IdTreeObject):
    """Instantiate an imported solid model.

    Parameters
    ----------
    name :
        Name of the imported solid model.
    active :
        Inactive imported solid models are ignored in the analysis.
    format :
        Specifies the format of the file to be imported.
    unit_system :
        Specifies the unit system of the external solid mesh.
    external_path :
        Path of the file to be imported.
    delete_bad_elements :
        If True, run an element check and delete erroneous elements. Bad elements
        can falsify the mapping.
    warping_limit :
        Maximum allowable warping. Elements with a warping above this limit are
        deleted.
        Only used if ``delete_bad_elements`` is True.
    minimum_volume :
        Solid elements with a volume smaller or equal to this value are deleted.
        Only used if ``delete_bad_elements`` is True.
    cut_off_material :
        This material is assigned to the degenerated solid cut-off elements if
        ``cut_off_material_handling`` is set to ``GLOBAL`` in the fabric
        definition.
    export_settings :
        Defines the settings for exporting the imported solid model.

    """

    __slots__: Iterable[str] = tuple()
    _COLLECTION_LABEL = "imported_solid_models"
    _OBJECT_INFO_TYPE = imported_solid_model_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = imported_solid_model_pb2.CreateRequest
    _SUPPORTED_SINCE = "25.1"

    def __init__(
        self,
        *,
        name: str = "ImportedSolidModel",
        active: bool = True,
        format: SolidModelImportFormat = "ansys:cdb",  # type: ignore
        unit_system: UnitSystemType = "from_file",
        external_path: _PATH = "",
        delete_bad_elements: bool = True,
        warping_limit: float = 0.4,
        minimum_volume: float = 0.0,
        cut_off_material: Material | None = None,
        export_settings: ImportedSolidModelExportSettings = ImportedSolidModelExportSettings(),
    ):
        super().__init__(name=name)
        self.active = active
        self.format = format
        self.unit_system = unit_system
        self.external_path = external_path
        self.delete_bad_elements = delete_bad_elements
        self.warping_limit = warping_limit
        self.minimum_volume = minimum_volume
        self.cut_off_material = cut_off_material
        self.export_settings = export_settings

    def _create_stub(self) -> imported_solid_model_pb2_grpc.ObjectServiceStub:
        return imported_solid_model_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")
    format = grpc_data_property(
        "properties.format",
        from_protobuf=solid_model_import_format_from_pb,
        to_protobuf=solid_model_import_format_to_pb,
    )
    unit_system = grpc_data_property(
        "properties.unit_system",
        from_protobuf=unit_system_type_from_pb,
        to_protobuf=unit_system_type_to_pb,
    )
    external_path: ReadWriteProperty[str, _PATH] = grpc_data_property(
        "properties.external_path", to_protobuf=str
    )
    delete_bad_elements: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.delete_bad_elements"
    )
    warping_limit: ReadWriteProperty[float, float] = grpc_data_property("properties.warping_limit")
    minimum_volume: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.minimum_volume"
    )
    cut_off_material = grpc_link_property("properties.cut_off_material", allowed_types=(Material,))
    export_settings = nested_grpc_object_property(
        "properties.export_settings", ImportedSolidModelExportSettings
    )

    solid_element_sets = get_read_only_collection_property(
        SolidElementSet, solid_element_set_pb2_grpc.ObjectServiceStub
    )

    elemental_data = elemental_data_property(ImportedSolidModelElementalData)
    nodal_data = nodal_data_property(ImportedSolidModelNodalData)

    create_cut_off_geometry = define_create_method(
        CutOffGeometry,
        func_name="create_cut_off_geometry",
        parent_class_name="ImportedSolidModel",
        module_name=__module__,
    )
    cut_off_geometries = define_mutable_mapping(
        CutOffGeometry, cut_off_geometry_pb2_grpc.ObjectServiceStub
    )

    create_layup_mapping_object = define_create_method(
        LayupMappingObject,
        func_name="create_layup_mapping_object",
        parent_class_name="ImportedSolidModel",
        module_name=__name__,
    )
    layup_mapping_objects = define_mutable_mapping(
        LayupMappingObject,
        layup_mapping_object_pb2_grpc.ObjectServiceStub,
    )

    def refresh(self, path: _PATH, format: SolidModelImportFormat | None = None) -> None:  # type: ignore
        """
        Re-import the solid model from the external file.

        Parameters
        ----------
        path :
            Path of the new input file.
        format :
            Switch format of the input file. Optional, uses the current format of the
            imported solid model if not specified.
        """
        if format is not None:
            self.format = format
        self.external_path = self._server_wrapper.auto_upload(path)
        with wrap_grpc_errors():
            self._get_stub().Refresh(  # type: ignore
                imported_solid_model_pb2.RefreshRequest(resource_path=self._resource_path)
            )

    def import_initial_mesh(self) -> None:
        """Import the solid mesh and its element sets."""
        with wrap_grpc_errors():
            self._get_stub().ImportInitialMesh(  # type: ignore
                imported_solid_model_pb2.ImportInitialMeshRequest(resource_path=self._resource_path)
            )

    solid_mesh = solid_mesh_property
