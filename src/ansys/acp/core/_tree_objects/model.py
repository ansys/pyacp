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
import dataclasses
import typing
from typing import Any, cast

import numpy as np

from ansys.api.acp.v0 import (
    boolean_selection_rule_pb2_grpc,
    cad_geometry_pb2_grpc,
    cutoff_selection_rule_pb2_grpc,
    cylindrical_selection_rule_pb2_grpc,
    edge_set_pb2_grpc,
    element_set_pb2_grpc,
    enum_types_pb2,
    fabric_pb2_grpc,
    field_definition_pb2_grpc,
    geometrical_selection_rule_pb2_grpc,
    imported_modeling_group_pb2_grpc,
    imported_solid_model_pb2_grpc,
    lookup_table_1d_pb2_grpc,
    lookup_table_3d_pb2_grpc,
    material_pb2,
    material_pb2_grpc,
    model_pb2,
    model_pb2_grpc,
    modeling_group_pb2_grpc,
    modeling_ply_pb2_grpc,
    oriented_selection_set_pb2_grpc,
    parallel_selection_rule_pb2_grpc,
    ply_geometry_export_pb2,
    rosette_pb2_grpc,
    sampling_point_pb2_grpc,
    section_cut_pb2_grpc,
    sensor_pb2_grpc,
    solid_model_pb2_grpc,
    spherical_selection_rule_pb2_grpc,
    stackup_pb2_grpc,
    sublaminate_pb2_grpc,
    tube_selection_rule_pb2_grpc,
    variable_offset_selection_rule_pb2_grpc,
    virtual_geometry_pb2_grpc,
)
from ansys.api.acp.v0.base_pb2 import CollectionPath

from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from .._utils.resource_paths import join as rp_join
from .._utils.typing_helper import PATH as _PATH
from ._elemental_or_nodal_data import (
    ElementalData,
    NodalData,
    ScalarData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from ._grpc_helpers.enum_wrapper import wrap_to_string_enum
from ._grpc_helpers.exceptions import wrap_grpc_errors
from ._grpc_helpers.mapping import define_create_method, define_mutable_mapping
from ._grpc_helpers.property_helper import (
    _PROTOBUF_T,
    _set_data_attribute,
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._grpc_helpers.protocols import ObjectInfo
from ._grpc_helpers.supported_since import supported_since
from ._mesh_data import full_mesh_property, shell_mesh_property, solid_mesh_property
from .base import ServerWrapper, TreeObject
from .boolean_selection_rule import BooleanSelectionRule
from .cad_geometry import CADGeometry
from .cut_off_selection_rule import CutOffSelectionRule
from .cylindrical_selection_rule import CylindricalSelectionRule
from .edge_set import EdgeSet
from .element_set import ElementSet
from .enums import (
    ArrowType,
    OffsetType,
    PlyGeometryExportFormat,
    UnitSystemType,
    arrow_type_to_pb,
    offset_type_to_pb,
    ply_geometry_export_format_to_pb,
    unit_system_type_from_pb,
    unit_system_type_to_pb,
)
from .fabric import Fabric
from .field_definition import FieldDefinition
from .geometrical_selection_rule import GeometricalSelectionRule
from .imported_modeling_group import ImportedModelingGroup
from .imported_solid_model import ImportedSolidModel
from .lookup_table_1d import LookUpTable1D
from .lookup_table_3d import LookUpTable3D
from .material import Material
from .modeling_group import ModelingGroup
from .modeling_ply import ModelingPly
from .object_registry import register
from .oriented_selection_set import OrientedSelectionSet
from .parallel_selection_rule import ParallelSelectionRule
from .rosette import Rosette
from .sampling_point import SamplingPoint
from .section_cut import SectionCut
from .sensor import Sensor
from .solid_model import SolidModel
from .spherical_selection_rule import SphericalSelectionRule
from .stackup import Stackup
from .sublaminate import SubLaminate
from .tube_selection_rule import TubeSelectionRule
from .utils import CoordinateTransformation
from .variable_offset_selection_rule import VariableOffsetSelectionRule
from .virtual_geometry import VirtualGeometry

__all__ = [
    "FeFormat",
    "HDF5CompositeCAEImportMode",
    "HDF5CompositeCAEProjectionMode",
    "IgnorableEntity",
    "Model",
    "ModelElementalData",
    "ModelNodalData",
    "ShellMappingProperties",
    "SolidMappingProperties",
]

FeFormat, fe_format_to_pb, _ = wrap_to_string_enum(
    "FeFormat",
    enum_types_pb2.FileFormat,
    module=__name__,
    value_converter=lambda val: val.lower().replace("_", ":"),
    doc="Options for the format of the FE file.",
    explicit_value_list=(
        enum_types_pb2.FileFormat.ANSYS_H5,
        enum_types_pb2.FileFormat.ANSYS_CDB,
        enum_types_pb2.FileFormat.ANSYS_DAT,
    ),
)
IgnorableEntity, ignorable_entity_to_pb, _ = wrap_to_string_enum(
    "IgnorableEntity",
    model_pb2.LoadFromFEFileRequest.IgnorableEntity,
    module=__name__,
    doc="Options for the entities to ignore when loading an FE file.",
)
HDF5CompositeCAEImportMode, hdf5_composite_cae_import_mode_to_pb, _ = wrap_to_string_enum(
    "HDF5CompositeCAEImportMode",
    model_pb2.ImportMode,
    module=__name__,
    doc="Options for the import mode of the HDF5 Composite CAE file.",
)
HDF5CompositeCAEProjectionMode, hdf5_composite_cae_projection_mode_to_pb, _ = wrap_to_string_enum(
    "HDF5CompositeCAEProjectionMode",
    model_pb2.ProjectionMode,
    module=__name__,
    doc="Options for the projection mode of the HDF5 Composite CAE file.",
)


@dataclasses.dataclass
class ModelElementalData(ElementalData):
    """Represents elemental data for a Model."""

    normal: VectorData | None = None
    thickness: ScalarData[np.float64] | None = None
    relative_thickness_correction: ScalarData[np.float64] | None = None
    area: ScalarData[np.float64] | None = None
    # Retrieving the 'price' can crash the server if the model contains void
    # analysis plies (on an imported solid model).
    # This is fixed in the backend for 2025R2, but for now we simply comment
    # out the property. In this way, the other properties can still be accessed,
    # and we can avoid the crash.
    # See https://github.com/ansys/pyacp/issues/717
    # price: ScalarData[np.float64] | None = None
    volume: ScalarData[np.float64] | None = None
    mass: ScalarData[np.float64] | None = None
    offset: ScalarData[np.float64] | None = None
    cog: VectorData | None = None


@dataclasses.dataclass
class ModelNodalData(NodalData):
    """Represents nodal data for a Model."""


@dataclasses.dataclass
class ShellMappingProperties:
    """Properties for mapping to the shell on importing HDF5 Composite CAE files."""

    all_elements: bool = True
    element_sets: Sequence[ElementSet] = ()
    relative_thickness_tolerance: float = 0.5
    relative_in_plane_tolerance: float = 0.01
    angle_tolerance: float = 35.0
    small_hole_threshold: float = 0.0


@dataclasses.dataclass
class SolidMappingProperties:
    """Properties for importing HDF5 Composite CAE files as imported plies."""

    offset_type: OffsetType = OffsetType.BOTTOM_OFFSET


@mark_grpc_properties
@register
class Model(TreeObject):
    """Defines an ACP Model.

    Wrapper for accessing an ACP Model residing on a server.

    Parameters
    ----------
    name :
        The name of the model.
    use_nodal_thicknesses :
        Defines whether to use nodal thicknesses or element thicknesses.
    draping_offset_correction :
        Defines whether to consider lay-up thickness in draping analysis.
    angle_tolerance :
        Section computation angle tolerance (in degree).
    relative_thickness_tolerance :
        Section computation relative thickness tolerance.
    minimum_analysis_ply_thickness :
        Section computation minimum analysis ply thickness (in length
        unit of model).
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "models"
    _OBJECT_INFO_TYPE = model_pb2.ObjectInfo
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "ACP Model",
        use_nodal_thicknesses: bool = False,
        draping_offset_correction: bool = False,
        angle_tolerance: float = 1.0,
        relative_thickness_tolerance: float = 0.01,
        minimum_analysis_ply_thickness: float = 1e-6,
    ) -> None:
        super().__init__(name=name)

        self.use_nodal_thicknesses = use_nodal_thicknesses
        self.draping_offset_correction = draping_offset_correction
        self.angle_tolerance = angle_tolerance
        self.relative_thickness_tolerance = relative_thickness_tolerance
        self.minimum_analysis_ply_thickness = minimum_analysis_ply_thickness

    def _get_stub(self) -> model_pb2_grpc.ObjectServiceStub:
        return cast(model_pb2_grpc.ObjectServiceStub, super()._get_stub())

    def _create_stub(self) -> model_pb2_grpc.ObjectServiceStub:
        return model_pb2_grpc.ObjectServiceStub(self._channel)

    # # TODO: document further properties, or autogenerate docstring from .proto files.

    use_nodal_thicknesses: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_nodal_thicknesses"
    )
    draping_offset_correction: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.draping_offset_correction"
    )
    angle_tolerance: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.angle_tolerance"
    )
    relative_thickness_tolerance: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.relative_thickness_tolerance"
    )
    minimum_analysis_ply_thickness: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.minimum_analysis_ply_thickness"
    )

    @staticmethod
    def _set_unit_system_data_attribute(pb_obj: ObjectInfo, name: str, value: _PROTOBUF_T) -> None:
        # remove the 'minimum_analysis_ply_thickness' property from the pb object, to
        # allow the backend to convert it to the new unit system.
        pb_obj.properties.ClearField("minimum_analysis_ply_thickness")
        _set_data_attribute(pb_obj, name, value)

    unit_system = grpc_data_property(
        "properties.unit_system",
        from_protobuf=unit_system_type_from_pb,
        to_protobuf=unit_system_type_to_pb,
        setter_func=_set_unit_system_data_attribute,
        writable_since="25.1",
    )

    average_element_size: ReadOnlyProperty[float] = grpc_data_property_read_only(
        "properties.average_element_size"
    )

    @classmethod
    def _from_file(cls, *, path: _PATH, server_wrapper: ServerWrapper) -> Model:
        """Instantiate a Model from an ACPH5 file.

        Parameters
        ----------
        path:
            File path, on the server.
        server_wrapper:
            Representation of the ACP instance.
        """
        request = model_pb2.LoadFromFileRequest(path=server_wrapper.auto_upload(path))
        with wrap_grpc_errors():
            reply = model_pb2_grpc.ObjectServiceStub(server_wrapper.channel).LoadFromFile(request)
        return cls._from_object_info(object_info=reply, server_wrapper=server_wrapper)

    @classmethod
    def _from_fe_file(
        cls,
        *,
        path: _PATH,
        server_wrapper: ServerWrapper,
        format: FeFormat,  # type: ignore
        ignored_entities: Iterable[IgnorableEntity] = (),  # type: ignore
        convert_section_data: bool = False,
        unit_system: UnitSystemType = UnitSystemType.FROM_FILE,
    ) -> Model:
        """Load the model from an FE file.

        Parameters
        ----------
        path:
            File path, on the server.
        server_wrapper:
            Representation of the ACP instance.
        format:
            Format of the FE file. Can be one of ``"ansys:h5"``, ``"ansys:cdb"``,
            ``"ansys:dat"``, ``"abaqus:inp"``, or ``"nastran:bdf"``.
        ignored_entities:
            Entities to ignore when loading the FE file. Can be a subset of
            the following values:
            ``"coordinate_systems"``, ``"element_sets"``, ``"materials"``,
            ``"mesh"``, or ``"shell_sections"``.
        convert_section_data:
            Whether to import the section data of a shell model and convert it
            into ACP composite definitions.
        unit_system:
            Defines the unit system of the imported file. Must be set if the
            input file does not have units. If the input file does have units,
            ``unit_system`` must be either ``"from_file"``, or match the input
            unit system.
        """
        format_pb = fe_format_to_pb(format)
        ignored_entities_pb = [ignorable_entity_to_pb(val) for val in ignored_entities]

        request = model_pb2.LoadFromFEFileRequest(
            path=server_wrapper.auto_upload(path),
            format=cast(Any, format_pb),
            ignored_entities=cast(Any, ignored_entities_pb),
            convert_section_data=convert_section_data,
            unit_system=cast(Any, unit_system_type_to_pb(unit_system)),
        )
        with wrap_grpc_errors():
            reply = model_pb2_grpc.ObjectServiceStub(server_wrapper.channel).LoadFromFEFile(request)
        return cls._from_object_info(object_info=reply, server_wrapper=server_wrapper)

    def update(self, *, relations_only: bool = False) -> None:
        """Update the model.

        Parameters
        ----------
        relations_only :
            Whether to update and propagate only the status of all objects.
        """
        with wrap_grpc_errors():
            self._get_stub().Update(
                model_pb2.UpdateRequest(
                    resource_path=self._resource_path, relations_only=relations_only
                )
            )

    def save(self, path: _PATH, *, save_cache: bool = True) -> None:
        """
        Save ACP Model (.acph5).

        Parameters
        ----------
        path:
            File path.
        save_cache:
            Whether to store the update results such as Analysis Plies and solid models.
        """
        with self._server_wrapper.auto_download(path) as export_path:
            with wrap_grpc_errors():
                self._get_stub().SaveToFile(
                    model_pb2.SaveToFileRequest(
                        resource_path=self._resource_path,
                        path=export_path,
                        save_cache=save_cache,
                    )
                )

    def export_analysis_model(self, path: _PATH) -> None:
        """Save the analysis model to a CDB file.

        Parameters
        ----------
        path:
            Target file path. E.g. /tmp/ACPAnalysisModel.cdb
        """
        with self._server_wrapper.auto_download(path) as export_path:
            with wrap_grpc_errors():
                self._get_stub().SaveAnalysisModel(
                    model_pb2.SaveAnalysisModelRequest(
                        resource_path=self._resource_path,
                        path=export_path,
                    )
                )

    @supported_since("25.1")
    def export_hdf5_composite_cae(
        self,
        path: _PATH,
        *,
        remove_midside_nodes: bool = True,
        layup_representation_3d: bool = False,
        offset_type: OffsetType = OffsetType.BOTTOM_OFFSET,
        all_elements: bool = True,
        element_sets: Sequence[ElementSet | OrientedSelectionSet] = (),
        all_plies: bool = True,
        plies: Sequence[ModelingGroup | ModelingPly] = (),
        ascii_encoding: bool = False,
    ) -> None:
        """
        Export the lay-up to the HDF5 Composite CAE format.

        Parameters
        ----------
        path :
            File path.
        remove_midside_nodes :
            If True, remove mid-side nodes from the exported mesh. This increases the
            overall performance.
        layup_representation_3d :
            If True, the 3D representation of the lay-up is computed, and the offset ply
            surfaces are exported.
        offset_type :
            Defines if the bottom, mid, or top surface of the plies is exported.
            Only used if ``layup_representation_3d`` is True.
        all_elements :
            Whether to limit the export to some user-defined element sets or not.
        element_sets :
            Only plies defined on the selected element sets or oriented selection
            sets will be exported.
            Used only if ``all_elements`` is False.
        all_plies :
            Whether to export all plies or a user-defined set.
        plies :
            User-defined set of Modeling Plies and/or Modeling Groups.
            Used only if ``all_plies`` is False.
        ascii_encoding :
            If True, use ASCII encoding when writing text attributes to the HDF5 CAE
            file. This may be needed for compatibility with programs that don't fully
            support unicode when reading the file.
        """
        with self._server_wrapper.auto_download(path) as export_path:
            with wrap_grpc_errors():
                self._get_stub().ExportHDF5CompositeCAE(
                    model_pb2.ExportHDF5CompositeCAERequest(
                        resource_path=self._resource_path,
                        path=export_path,
                        remove_midside_nodes=remove_midside_nodes,
                        layup_representation_3d=layup_representation_3d,
                        offset_type=offset_type_to_pb(offset_type),  # type: ignore
                        ascii_encoding=ascii_encoding,
                        all_elements=all_elements,
                        element_sets=[element_set._resource_path for element_set in element_sets],
                        all_plies=all_plies,
                        plies=[ply._resource_path for ply in plies],
                    )
                )

    @supported_since("25.1")
    def import_hdf5_composite_cae(
        self,
        path: _PATH,
        import_mode: HDF5CompositeCAEImportMode = HDF5CompositeCAEImportMode.APPEND,  # type: ignore
        projection_mode: HDF5CompositeCAEProjectionMode = HDF5CompositeCAEProjectionMode.SHELL,  # type: ignore
        minimum_angle_tolerance: float = 0.001,
        recompute_reference_directions: bool = False,
        shell_mapping_properties: ShellMappingProperties = ShellMappingProperties(),
        solid_mapping_properties: SolidMappingProperties = SolidMappingProperties(),
        coordinate_transformation: CoordinateTransformation = CoordinateTransformation(),
    ) -> None:
        """Import the lay-up from an HDF5 Composite CAE file.

        Parameters
        ----------
        path :
            File path.
        import_mode :
            In :py:attr:`.HDF5CompositeCAEImportMode.APPEND` mode, the imported objects are
            appended to existing layup.
            In :py:attr:`.HDF5CompositeCAEImportMode.OVERWRITE` mode, existing objects in the model
            with the same name are replaced if possible (not locked).
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
        if projection_mode == HDF5CompositeCAEProjectionMode.SHELL:
            mapping_properties_kwargs: (
                dict[str, model_pb2.ShellMappingProperties]
                | dict[str, model_pb2.SolidMappingProperties]
            ) = {
                "shell_mapping_properties": model_pb2.ShellMappingProperties(
                    all_elements=shell_mapping_properties.all_elements,
                    element_sets=[
                        element_set._resource_path
                        for element_set in shell_mapping_properties.element_sets
                    ],
                    relative_thickness_tolerance=shell_mapping_properties.relative_thickness_tolerance,
                    relative_in_plane_tolerance=shell_mapping_properties.relative_in_plane_tolerance,
                    angle_tolerance=shell_mapping_properties.angle_tolerance,
                    small_hole_threshold=shell_mapping_properties.small_hole_threshold,
                ),
            }
        else:
            assert projection_mode == HDF5CompositeCAEProjectionMode.SOLID
            mapping_properties_kwargs = {
                "solid_mapping_properties": model_pb2.SolidMappingProperties(
                    offset_type=offset_type_to_pb(solid_mapping_properties.offset_type)  # type: ignore
                ),
            }

        with wrap_grpc_errors():
            self._get_stub().ImportHDF5CompositeCAE(
                model_pb2.ImportHDF5CompositeCAERequest(
                    resource_path=self._resource_path,
                    path=self._server_wrapper.auto_upload(path),
                    import_mode=hdf5_composite_cae_import_mode_to_pb(import_mode),  # type: ignore
                    projection_mode=hdf5_composite_cae_projection_mode_to_pb(projection_mode),  # type: ignore
                    minimum_angle_tolerance=minimum_angle_tolerance,
                    recompute_reference_directions=recompute_reference_directions,
                    coordinate_transformation=model_pb2.CoordinateTransformation(
                        **dataclasses.asdict(coordinate_transformation)
                    ),
                    **mapping_properties_kwargs,
                )
            )

    def export_shell_composite_definitions(self, path: _PATH) -> None:
        """
        Export the lay-up of the shell as HDF5 used by DPF Composites or Mechanical.

        Parameters
        ----------
        path:
            File path. Eg. /tmp/ACPCompositeDefinitions.h5
        """
        with self._server_wrapper.auto_download(path) as export_path:
            with wrap_grpc_errors():
                self._get_stub().SaveShellCompositeDefinitions(
                    model_pb2.SaveShellCompositeDefinitionsRequest(
                        resource_path=self._resource_path, path=export_path
                    )
                )

    @supported_since("25.1")
    def import_materials(
        self,
        matml_path: _PATH,
        *,
        material_apdl_path: _PATH | None = None,
    ) -> None:
        """
        Import materials from a MatML file.

        Import materials from a ``MatML.xml`` (Engineering Data) file.

        Optionally, a material APDL file can be defined. This is a pre-generated
        solver snippet, needed in case of variable materials or non-standard
        material models. The snippet is used when exporting solid models or
        surface section cuts in the CDB format.

        Parameters
        ----------
        matml_path:
            File path to the MatML file.
        material_apdl_path:
            File path to the material APDL file.
        """
        material_stub = material_pb2_grpc.ObjectServiceStub(self._channel)
        collection_path = CollectionPath(
            value=rp_join(self._resource_path.value, Material._COLLECTION_LABEL)
        )

        with wrap_grpc_errors():
            material_stub.ImportMaterialFiles(
                material_pb2.ImportMaterialFilesRequest(
                    collection_path=collection_path,
                    matml_path=self._server_wrapper.auto_upload(matml_path),
                    material_apdl_path=self._server_wrapper.auto_upload(
                        material_apdl_path, allow_none=True
                    ),
                )
            )

    def export_materials(self, path: _PATH) -> None:
        """
        Write materials to a XML (MatML) file.

        The XML file is required for the post-processing with DPF or can be loaded by
        Engineering Data under WB.

        Parameters
        ----------
        path:
            File path. E.g. /tmp/acp_materials.xml
        """
        material_stub = material_pb2_grpc.ObjectServiceStub(self._channel)
        collection_path = CollectionPath(
            value=rp_join(self._resource_path.value, Material._COLLECTION_LABEL)
        )
        with self._server_wrapper.auto_download(path) as export_path:
            with wrap_grpc_errors():
                material_stub.SaveToFile(
                    material_pb2.SaveToFileRequest(
                        collection_path=collection_path,
                        path=export_path,
                        format=material_pb2.SaveToFileRequest.ANSYS_XML,
                    )
                )

    @supported_since("25.1")
    def export_modeling_ply_geometries(
        self,
        path: _PATH,
        *,
        modeling_plies: Iterable[ModelingPly] | None = None,
        format: PlyGeometryExportFormat = PlyGeometryExportFormat.STEP,
        offset_type: OffsetType = OffsetType.MIDDLE_OFFSET,
        include_surface: bool = True,
        include_boundary: bool = True,
        include_first_material_direction: bool = True,
        include_second_material_direction: bool = True,
        arrow_length: float | None = None,
        arrow_type: ArrowType = ArrowType.NO_ARROW,
    ) -> None:
        """
        Write ply geometries to a STEP, IGES, or STL file.

        Parameters
        ----------
        path :
            File path to save the geometries to.
        modeling_plies :
            List of modeling plies whose geometries should be exported. If not
            provided, the geometries of all modeling plies in the model are exported.
        format :
            Format of the created file. Can be one of ``"STEP"``, ``"IGES"``,
            or ``"STL"``.
        offset_type :
            Determines how the ply offset is calculated. Can be one of
            ``"NO_OFFSET"``, ``"BOTTOM_OFFSET"``, ``"MIDDLE_OFFSET"``, or
            ``"TOP_OFFSET"``.
        include_surface :
            Whether to include the ply surface in the exported geometry.
        include_boundary :
            Whether to include the ply boundary in the exported geometry.
        include_first_material_direction :
            Whether to include the first material direction in the exported geometry.
        include_second_material_direction :
            Whether to include the second material direction in the exported geometry.
        arrow_length :
            Size of the arrow used to represent the material directions. By default, the
            square root of the average element area is used.
        arrow_type :
            Type of the arrow used to represent the material directions. Can be
            one of ``"NO_ARROW"``, ``"HALF_ARROW"``, or ``"STANDARD_ARROW"``.
        """
        if modeling_plies is None:
            modeling_plies = [
                ply
                for modeling_group in self.modeling_groups.values()
                for ply in modeling_group.modeling_plies.values()
            ]
        mp_resource_paths = [ply._resource_path for ply in modeling_plies]

        modeling_ply_stub = modeling_ply_pb2_grpc.ObjectServiceStub(self._channel)

        if arrow_length is None:
            arrow_length = np.sqrt(self.average_element_size)

        with self._server_wrapper.auto_download(path) as export_path:
            with wrap_grpc_errors():
                modeling_ply_stub.ExportGeometries(
                    ply_geometry_export_pb2.ExportGeometriesRequest(
                        path=export_path,
                        plies=mp_resource_paths,
                        options=ply_geometry_export_pb2.ExportOptions(
                            format=typing.cast(
                                typing.Any, ply_geometry_export_format_to_pb(format)
                            ),
                            offset_type=typing.cast(typing.Any, offset_type_to_pb(offset_type)),
                            include_surface=include_surface,
                            include_boundary=include_boundary,
                            include_first_material_direction=include_first_material_direction,
                            include_second_material_direction=include_second_material_direction,
                            arrow_length=arrow_length,
                            arrow_type=typing.cast(typing.Any, arrow_type_to_pb(arrow_type)),
                        ),
                    )
                )

    create_material = define_create_method(
        Material, func_name="create_material", parent_class_name="Model", module_name=__module__
    )
    materials = define_mutable_mapping(Material, material_pb2_grpc.ObjectServiceStub)

    create_fabric = define_create_method(
        Fabric, func_name="create_fabric", parent_class_name="Model", module_name=__module__
    )
    fabrics = define_mutable_mapping(Fabric, fabric_pb2_grpc.ObjectServiceStub)

    create_stackup = define_create_method(
        Stackup, func_name="create_stackup", parent_class_name="Model", module_name=__module__
    )
    stackups = define_mutable_mapping(Stackup, stackup_pb2_grpc.ObjectServiceStub)

    create_sublaminate = define_create_method(
        SubLaminate,
        func_name="create_sublaminate",
        parent_class_name="Model",
        module_name=__module__,
    )
    sublaminates = define_mutable_mapping(SubLaminate, sublaminate_pb2_grpc.ObjectServiceStub)

    create_element_set = define_create_method(
        ElementSet,
        func_name="create_element_set",
        parent_class_name="Model",
        module_name=__module__,
    )
    element_sets = define_mutable_mapping(ElementSet, element_set_pb2_grpc.ObjectServiceStub)

    create_edge_set = define_create_method(
        EdgeSet, func_name="create_edge_set", parent_class_name="Model", module_name=__module__
    )
    edge_sets = define_mutable_mapping(EdgeSet, edge_set_pb2_grpc.ObjectServiceStub)

    create_cad_geometry = define_create_method(
        CADGeometry,
        func_name="create_cad_geometry",
        parent_class_name="Model",
        module_name=__module__,
    )
    cad_geometries = define_mutable_mapping(CADGeometry, cad_geometry_pb2_grpc.ObjectServiceStub)

    create_virtual_geometry = define_create_method(
        VirtualGeometry,
        func_name="create_virtual_geometry",
        parent_class_name="Model",
        module_name=__module__,
    )
    virtual_geometries = define_mutable_mapping(
        VirtualGeometry, virtual_geometry_pb2_grpc.ObjectServiceStub
    )

    create_rosette = define_create_method(
        Rosette, func_name="create_rosette", parent_class_name="Model", module_name=__module__
    )
    rosettes = define_mutable_mapping(Rosette, rosette_pb2_grpc.ObjectServiceStub)

    create_lookup_table_1d = define_create_method(
        LookUpTable1D,
        func_name="create_lookup_table_1d",
        parent_class_name="Model",
        module_name=__module__,
    )
    lookup_tables_1d = define_mutable_mapping(
        LookUpTable1D, lookup_table_1d_pb2_grpc.ObjectServiceStub
    )

    create_lookup_table_3d = define_create_method(
        LookUpTable3D,
        func_name="create_lookup_table_3d",
        parent_class_name="Model",
        module_name=__module__,
    )
    lookup_tables_3d = define_mutable_mapping(
        LookUpTable3D, lookup_table_3d_pb2_grpc.ObjectServiceStub
    )

    create_parallel_selection_rule = define_create_method(
        ParallelSelectionRule,
        func_name="create_parallel_selection_rule",
        parent_class_name="Model",
        module_name=__module__,
    )
    parallel_selection_rules = define_mutable_mapping(
        ParallelSelectionRule, parallel_selection_rule_pb2_grpc.ObjectServiceStub
    )

    create_cylindrical_selection_rule = define_create_method(
        CylindricalSelectionRule,
        func_name="create_cylindrical_selection_rule",
        parent_class_name="Model",
        module_name=__module__,
    )
    cylindrical_selection_rules = define_mutable_mapping(
        CylindricalSelectionRule, cylindrical_selection_rule_pb2_grpc.ObjectServiceStub
    )

    create_spherical_selection_rule = define_create_method(
        SphericalSelectionRule,
        func_name="create_spherical_selection_rule",
        parent_class_name="Model",
        module_name=__module__,
    )
    spherical_selection_rules = define_mutable_mapping(
        SphericalSelectionRule, spherical_selection_rule_pb2_grpc.ObjectServiceStub
    )

    create_tube_selection_rule = define_create_method(
        TubeSelectionRule,
        func_name="create_tube_selection_rule",
        parent_class_name="Model",
        module_name=__module__,
    )
    tube_selection_rules = define_mutable_mapping(
        TubeSelectionRule, tube_selection_rule_pb2_grpc.ObjectServiceStub
    )

    create_cut_off_selection_rule = define_create_method(
        CutOffSelectionRule,
        func_name="create_cut_off_selection_rule",
        parent_class_name="Model",
        module_name=__module__,
    )
    cut_off_selection_rules = define_mutable_mapping(
        CutOffSelectionRule, cutoff_selection_rule_pb2_grpc.ObjectServiceStub
    )

    create_geometrical_selection_rule = define_create_method(
        GeometricalSelectionRule,
        func_name="create_geometrical_selection_rule",
        parent_class_name="Model",
        module_name=__module__,
    )
    geometrical_selection_rules = define_mutable_mapping(
        GeometricalSelectionRule, geometrical_selection_rule_pb2_grpc.ObjectServiceStub
    )

    create_variable_offset_selection_rule = define_create_method(
        VariableOffsetSelectionRule,
        func_name="create_variable_offset_selection_rule",
        parent_class_name="Model",
        module_name=__module__,
    )
    variable_offset_selection_rules = define_mutable_mapping(
        VariableOffsetSelectionRule, variable_offset_selection_rule_pb2_grpc.ObjectServiceStub
    )

    create_boolean_selection_rule = define_create_method(
        BooleanSelectionRule,
        func_name="create_boolean_selection_rule",
        parent_class_name="Model",
        module_name=__module__,
    )
    boolean_selection_rules = define_mutable_mapping(
        BooleanSelectionRule, boolean_selection_rule_pb2_grpc.ObjectServiceStub
    )

    create_oriented_selection_set = define_create_method(
        OrientedSelectionSet,
        func_name="create_oriented_selection_set",
        parent_class_name="Model",
        module_name=__module__,
    )
    oriented_selection_sets = define_mutable_mapping(
        OrientedSelectionSet, oriented_selection_set_pb2_grpc.ObjectServiceStub
    )

    create_modeling_group = define_create_method(
        ModelingGroup,
        func_name="create_modeling_group",
        parent_class_name="Model",
        module_name=__module__,
    )
    modeling_groups = define_mutable_mapping(
        ModelingGroup, modeling_group_pb2_grpc.ObjectServiceStub
    )

    create_imported_modeling_group = define_create_method(
        ImportedModelingGroup,
        func_name="create_imported_modeling_group",
        parent_class_name="Model",
        module_name=__module__,
    )
    imported_modeling_groups = define_mutable_mapping(
        ImportedModelingGroup, imported_modeling_group_pb2_grpc.ObjectServiceStub
    )

    create_sampling_point = define_create_method(
        SamplingPoint,
        func_name="create_sampling_point",
        parent_class_name="Model",
        module_name=__module__,
    )
    sampling_points = define_mutable_mapping(
        SamplingPoint, sampling_point_pb2_grpc.ObjectServiceStub
    )

    create_section_cut = define_create_method(
        SectionCut,
        func_name="create_section_cut",
        parent_class_name="Model",
        module_name=__module__,
    )
    section_cuts = define_mutable_mapping(SectionCut, section_cut_pb2_grpc.ObjectServiceStub)

    create_solid_model = define_create_method(
        SolidModel,
        func_name="create_solid_model",
        parent_class_name="Model",
        module_name=__module__,
    )
    solid_models = define_mutable_mapping(SolidModel, solid_model_pb2_grpc.ObjectServiceStub)

    create_imported_solid_model = define_create_method(
        ImportedSolidModel,
        func_name="create_imported_solid_model",
        parent_class_name="Model",
        module_name=__module__,
    )
    imported_solid_models = define_mutable_mapping(
        ImportedSolidModel, imported_solid_model_pb2_grpc.ObjectServiceStub
    )

    create_sensor = define_create_method(
        Sensor, func_name="create_sensor", parent_class_name="Model", module_name=__module__
    )
    sensors = define_mutable_mapping(Sensor, sensor_pb2_grpc.ObjectServiceStub)

    create_field_definition = define_create_method(
        FieldDefinition,
        func_name="create_field_definition",
        parent_class_name="Model",
        module_name=__module__,
    )
    field_definitions = define_mutable_mapping(
        FieldDefinition, field_definition_pb2_grpc.ObjectServiceStub
    )

    mesh = full_mesh_property
    shell_mesh = shell_mesh_property
    solid_mesh = solid_mesh_property
    elemental_data = elemental_data_property(ModelElementalData)
    nodal_data = nodal_data_property(ModelNodalData)
