from __future__ import annotations

import dataclasses
from typing import Iterable, cast

from grpc import Channel
import numpy as np
import numpy.typing as npt
from pyvista.core.pointset import UnstructuredGrid

from ansys.api.acp.v0 import (
    base_pb2,
    edge_set_pb2_grpc,
    element_set_pb2_grpc,
    fabric_pb2_grpc,
    material_pb2,
    material_pb2_grpc,
    mesh_query_pb2_grpc,
    model_pb2,
    model_pb2_grpc,
    modeling_group_pb2_grpc,
    oriented_selection_set_pb2_grpc,
    rosette_pb2_grpc,
    stackup_pb2_grpc,
)
from ansys.api.acp.v0.base_pb2 import CollectionPath

from .._typing_helper import PATH as _PATH
from .._utils.array_conversions import to_numpy
from .._utils.resource_paths import join as rp_join
from .._utils.visualization import to_pyvista_faces, to_pyvista_types
from ._grpc_helpers.enum_wrapper import wrap_to_string_enum
from ._grpc_helpers.mapping import define_mapping
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ._mesh_data import ElementalData, NodalData, elemental_data_property, nodal_data_property
from .base import TreeObject
from .edge_set import EdgeSet
from .element_set import ElementSet
from .enums import UnitSystemType, unit_system_type_from_pb, unit_system_type_to_pb
from .fabric import Fabric
from .material import Material
from .modeling_group import ModelingGroup
from .oriented_selection_set import OrientedSelectionSet
from .rosette import Rosette
from .stackup import Stackup

__all__ = ["MeshData", "Model", "ModelElementalData", "ModelNodalData"]

_FeFormat, _fe_format_to_pb, _ = wrap_to_string_enum(
    "_FeFormat",
    model_pb2.Format,
    module=__name__,
    value_converter=lambda val: val.lower().replace("_", ":"),
)
_IgnorableEntity, _ignorable_entity_to_pb, _ = wrap_to_string_enum(
    "_IgnorableEntity", model_pb2.LoadFromFEFileRequest.IgnorableEntity, module=__name__
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

    normal: npt.NDArray[np.float64]
    thickness: npt.NDArray[np.float64]
    relative_thickness_correction: npt.NDArray[np.float64]
    area: npt.NDArray[np.float64]
    price: npt.NDArray[np.float64]
    volume: npt.NDArray[np.float64]
    mass: npt.NDArray[np.float64]
    offset: npt.NDArray[np.float64]
    cog: npt.NDArray[np.float64]


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
    OBJECT_INFO_TYPE = model_pb2.ObjectInfo

    def __init__(
        self,
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

    use_nodal_thicknesses = grpc_data_property("properties.use_nodal_thicknesses")
    draping_offset_correction = grpc_data_property("properties.draping_offset_correction")
    angle_tolerance = grpc_data_property("properties.angle_tolerance")
    relative_thickness_tolerance = grpc_data_property("properties.relative_thickness_tolerance")
    minimum_analysis_ply_thickness = grpc_data_property("properties.minimum_analysis_ply_thickness")
    unit_system = grpc_data_property_read_only(
        "properties.unit_system", from_protobuf=unit_system_type_from_pb
    )

    @classmethod
    def from_file(cls, *, path: _PATH, channel: Channel) -> Model:
        # Send absolute paths to the server, since its CWD may not match
        # the Python CWD.
        request = model_pb2.LoadFromFileRequest(path=str(path))
        reply = model_pb2_grpc.ObjectServiceStub(channel).LoadFromFile(request)
        return cls._from_object_info(object_info=reply, channel=channel)

    @classmethod
    def from_fe_file(
        cls,
        *,
        path: _PATH,
        channel: Channel,
        format: _FeFormat,  # type: ignore
        ignored_entities: Iterable[_IgnorableEntity] = (),  # type: ignore
        convert_section_data: bool = False,
        unit_system: UnitSystemType = UnitSystemType.UNDEFINED,
    ) -> Model:
        format_pb = _fe_format_to_pb(format)
        ignored_entities_pb = [_ignorable_entity_to_pb(val) for val in ignored_entities]

        request = model_pb2.LoadFromFEFileRequest(
            path=str(path),
            format=format_pb,
            ignored_entities=ignored_entities_pb,
            convert_section_data=convert_section_data,
            unit_system=unit_system_type_to_pb(unit_system),
        )
        reply = model_pb2_grpc.ObjectServiceStub(channel).LoadFromFEFile(request)
        return cls._from_object_info(object_info=reply, channel=channel)

    def update(self, *, relations_only: bool = False) -> None:
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
        self._get_stub().SaveToFile(
            model_pb2.SaveToFileRequest(
                resource_path=self._resource_path,
                path=str(path),
                save_cache=save_cache,
            )
        )

    def save_analysis_model(self, path: _PATH) -> None:
        self._get_stub().SaveAnalysisModel(
            model_pb2.SaveAnalysisModelRequest(
                resource_path=self._resource_path,
                path=str(path),
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
        self._get_stub().SaveShellCompositeDefinitions(
            model_pb2.SaveShellCompositeDefinitionsRequest(
                resource_path=self._resource_path, path=str(path)
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
        material_stub.SaveToFile(
            material_pb2.SaveToFileRequest(
                collection_path=collection_path,
                path=str(path),
                format=material_pb2.SaveToFileRequest.ANSYS_XML,
            )
        )

    create_material, materials = define_mapping(Material, material_pb2_grpc.ObjectServiceStub)
    create_fabric, fabrics = define_mapping(Fabric, fabric_pb2_grpc.ObjectServiceStub)
    create_stackup, stackups = define_mapping(Stackup, stackup_pb2_grpc.ObjectServiceStub)
    create_element_set, element_sets = define_mapping(
        ElementSet, element_set_pb2_grpc.ObjectServiceStub
    )
    create_edge_set, edge_sets = define_mapping(EdgeSet, edge_set_pb2_grpc.ObjectServiceStub)
    create_rosette, rosettes = define_mapping(Rosette, rosette_pb2_grpc.ObjectServiceStub)
    create_oriented_selection_set, oriented_selection_sets = define_mapping(
        OrientedSelectionSet, oriented_selection_set_pb2_grpc.ObjectServiceStub
    )
    create_modeling_group, modeling_groups = define_mapping(
        ModelingGroup, modeling_group_pb2_grpc.ObjectServiceStub
    )

    @property
    def mesh(self) -> MeshData:
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
