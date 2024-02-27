# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
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
from typing import Any, cast

from grpc import Channel
import numpy as np
import numpy.typing as npt
from pyvista.core.pointset import UnstructuredGrid

from ansys.api.acp.v0 import (
    base_pb2,
    boolean_selection_rule_pb2_grpc,
    cad_geometry_pb2_grpc,
    cutoff_selection_rule_pb2_grpc,
    cylindrical_selection_rule_pb2_grpc,
    edge_set_pb2_grpc,
    element_set_pb2_grpc,
    fabric_pb2_grpc,
    geometrical_selection_rule_pb2_grpc,
    lookup_table_1d_pb2_grpc,
    lookup_table_3d_pb2_grpc,
    material_pb2,
    material_pb2_grpc,
    mesh_query_pb2_grpc,
    model_pb2,
    model_pb2_grpc,
    modeling_group_pb2_grpc,
    oriented_selection_set_pb2_grpc,
    parallel_selection_rule_pb2_grpc,
    rosette_pb2_grpc,
    sensor_pb2_grpc,
    spherical_selection_rule_pb2_grpc,
    stackup_pb2_grpc,
    sublaminate_pb2_grpc,
    tube_selection_rule_pb2_grpc,
    variable_offset_selection_rule_pb2_grpc,
    virtual_geometry_pb2_grpc,
)
from ansys.api.acp.v0.base_pb2 import CollectionPath

from .._typing_helper import PATH as _PATH
from .._utils.array_conversions import to_numpy
from .._utils.path_to_str import path_to_str_checked
from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from .._utils.resource_paths import join as rp_join
from .._utils.visualization import to_pyvista_faces, to_pyvista_types
from ._grpc_helpers.enum_wrapper import wrap_to_string_enum
from ._grpc_helpers.exceptions import wrap_grpc_errors
from ._grpc_helpers.mapping import define_create_method, define_mutable_mapping
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import (
    ElementalData,
    NodalData,
    ScalarData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from .base import TreeObject
from .boolean_selection_rule import BooleanSelectionRule
from .cad_geometry import CADGeometry
from .cutoff_selection_rule import CutoffSelectionRule
from .cylindrical_selection_rule import CylindricalSelectionRule
from .edge_set import EdgeSet
from .element_set import ElementSet
from .enums import UnitSystemType, unit_system_type_from_pb, unit_system_type_to_pb
from .fabric import Fabric
from .geometrical_selection_rule import GeometricalSelectionRule
from .lookup_table_1d import LookUpTable1D
from .lookup_table_3d import LookUpTable3D
from .material import Material
from .modeling_group import ModelingGroup
from .oriented_selection_set import OrientedSelectionSet
from .parallel_selection_rule import ParallelSelectionRule
from .rosette import Rosette
from .sensor import Sensor
from .spherical_selection_rule import SphericalSelectionRule
from .stackup import Stackup
from .sublaminate import SubLaminate
from .tube_selection_rule import TubeSelectionRule
from .variable_offset_selection_rule import VariableOffsetSelectionRule
from .virtual_geometry import VirtualGeometry

__all__ = [
    "MeshData",
    "Model",
    "ModelElementalData",
    "ModelNodalData",
    "FeFormat",
    "IgnorableEntity",
]

FeFormat, fe_format_to_pb, _ = wrap_to_string_enum(
    "FeFormat",
    model_pb2.Format,
    module=__name__,
    value_converter=lambda val: val.lower().replace("_", ":"),
    doc="Options for the format of the FE file.",
)
IgnorableEntity, ignorable_entity_to_pb, _ = wrap_to_string_enum(
    "IgnorableEntity",
    model_pb2.LoadFromFEFileRequest.IgnorableEntity,
    module=__name__,
    doc="Options for the entities to ignore when loading an FE file.",
)


@dataclasses.dataclass
class MeshData:
    """Container for the mesh data of an ACP Model."""

    node_labels: npt.NDArray[np.int32]
    node_coordinates: npt.NDArray[np.float64]
    element_labels: npt.NDArray[np.int32]
    element_types: npt.NDArray[np.int32]
    element_nodes: npt.NDArray[np.int32]
    element_nodes_offsets: npt.NDArray[np.int32]

    def to_pyvista(self) -> UnstructuredGrid:
        """Convert the mesh data to a PyVista mesh."""
        return UnstructuredGrid(
            to_pyvista_faces(
                element_types=self.element_types,
                element_nodes=self.element_nodes,
                element_nodes_offsets=self.element_nodes_offsets,
            ),
            to_pyvista_types(self.element_types),
            self.node_coordinates,
        )


@dataclasses.dataclass
class ModelElementalData(ElementalData):
    """Represents elemental data for a Model."""

    normal: VectorData | None = None
    thickness: ScalarData[np.float64] | None = None
    relative_thickness_correction: ScalarData[np.float64] | None = None
    area: ScalarData[np.float64] | None = None
    price: ScalarData[np.float64] | None = None
    volume: ScalarData[np.float64] | None = None
    mass: ScalarData[np.float64] | None = None
    offset: ScalarData[np.float64] | None = None
    cog: VectorData | None = None


@dataclasses.dataclass
class ModelNodalData(NodalData):
    """Represents nodal data for a Model."""


@mark_grpc_properties
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
    unit_system = grpc_data_property_read_only(
        "properties.unit_system", from_protobuf=unit_system_type_from_pb
    )

    average_element_size: ReadOnlyProperty[float] = grpc_data_property_read_only(
        "properties.average_element_size"
    )

    @classmethod
    def from_file(cls, *, path: _PATH, channel: Channel) -> Model:
        """Instantiate a Model from an ACPH5 file.

        Parameters
        ----------
        path:
            File path, on the server.
        channel:
            gRPC channel to the server.
        """
        # Send absolute paths to the server, since its CWD may not match
        # the Python CWD.
        request = model_pb2.LoadFromFileRequest(path=path_to_str_checked(path))
        with wrap_grpc_errors():
            reply = model_pb2_grpc.ObjectServiceStub(channel).LoadFromFile(request)
        return cls._from_object_info(object_info=reply, channel=channel)

    @classmethod
    def from_fe_file(
        cls,
        *,
        path: _PATH,
        channel: Channel,
        format: FeFormat,  # type: ignore
        ignored_entities: Iterable[IgnorableEntity] = (),  # type: ignore
        convert_section_data: bool = False,
        unit_system: UnitSystemType = UnitSystemType.UNDEFINED,
    ) -> Model:
        """Load the model from an FE file.

        Parameters
        ----------
        path:
            File path, on the server.
        channel:
            gRPC channel to the server.
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
            Set the unit system of the model to the given value. Ignored
            if the unit system is already set in the FE file.
        """
        format_pb = fe_format_to_pb(format)
        ignored_entities_pb = [ignorable_entity_to_pb(val) for val in ignored_entities]

        request = model_pb2.LoadFromFEFileRequest(
            path=path_to_str_checked(path),
            format=cast(Any, format_pb),
            ignored_entities=cast(Any, ignored_entities_pb),
            convert_section_data=convert_section_data,
            unit_system=cast(Any, unit_system_type_to_pb(unit_system)),
        )
        with wrap_grpc_errors():
            reply = model_pb2_grpc.ObjectServiceStub(channel).LoadFromFEFile(request)
        return cls._from_object_info(object_info=reply, channel=channel)

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
        with wrap_grpc_errors():
            self._get_stub().SaveToFile(
                model_pb2.SaveToFileRequest(
                    resource_path=self._resource_path,
                    path=path_to_str_checked(path),
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
        with wrap_grpc_errors():
            self._get_stub().SaveAnalysisModel(
                model_pb2.SaveAnalysisModelRequest(
                    resource_path=self._resource_path,
                    path=path_to_str_checked(path),
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
        with wrap_grpc_errors():
            self._get_stub().SaveShellCompositeDefinitions(
                model_pb2.SaveShellCompositeDefinitionsRequest(
                    resource_path=self._resource_path, path=path_to_str_checked(path)
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
        with wrap_grpc_errors():
            material_stub.SaveToFile(
                material_pb2.SaveToFileRequest(
                    collection_path=collection_path,
                    path=path_to_str_checked(path),
                    format=material_pb2.SaveToFileRequest.ANSYS_XML,
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

    create_cutoff_selection_rule = define_create_method(
        CutoffSelectionRule,
        func_name="create_cutoff_selection_rule",
        parent_class_name="Model",
        module_name=__module__,
    )
    cutoff_selection_rules = define_mutable_mapping(
        CutoffSelectionRule, cutoff_selection_rule_pb2_grpc.ObjectServiceStub
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

    create_sensor = define_create_method(
        Sensor, func_name="create_sensor", parent_class_name="Model", module_name=__module__
    )
    sensors = define_mutable_mapping(Sensor, sensor_pb2_grpc.ObjectServiceStub)

    @property
    def mesh(self) -> MeshData:
        """Mesh on which the model is defined."""
        mesh_query_stub = mesh_query_pb2_grpc.MeshQueryServiceStub(self._channel)
        reply = mesh_query_stub.GetMeshData(base_pb2.GetRequest(resource_path=self._resource_path))
        return MeshData(
            node_labels=to_numpy(reply.node_labels),
            node_coordinates=to_numpy(reply.node_coordinates),
            element_labels=to_numpy(reply.element_labels),
            element_types=to_numpy(reply.element_types),
            element_nodes=to_numpy(reply.element_nodes),
            element_nodes_offsets=to_numpy(reply.element_nodes_offsets),
        )

    elemental_data = elemental_data_property(ModelElementalData)
    nodal_data = nodal_data_property(ModelNodalData)
