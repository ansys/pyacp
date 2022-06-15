from enum import Enum
from typing import Any, Iterable, Optional, Union

from ansys.api.acp.v0.base_pb2 import BasicInfo, CollectionPath, ResourcePath
from ansys.api.acp.v0.element_set_pb2 import (
    CreateElementSetRequest,
    DeleteElementSetRequest,
    ListElementSetsRequest,
)
from ansys.api.acp.v0.element_set_pb2_grpc import ElementSetStub
from ansys.api.acp.v0.model_pb2 import (
    LoadFEModelRequest,
    LoadModelRequest,
    ModelInfo,
    ModelRequest,
    SaveModelRequest,
    UpdateModelRequest,
)

# ModelingGroup
from ansys.api.acp.v0.model_pb2 import Format as _pb_Format
from ansys.api.acp.v0.model_pb2_grpc import ModelStub
from ansys.api.acp.v0.modeling_group_pb2 import (
    CreateModelingGroupRequest,
    DeleteModelingGroupRequest,
    ListModelingGroupsRequest,
)
from ansys.api.acp.v0.modeling_group_pb2_grpc import ModelingGroupStub

# Rosette
from ansys.api.acp.v0.rosette_pb2 import (
    CreateRosetteRequest,
    DeleteRosetteRequest,
    ListRosettesRequest,
)
from ansys.api.acp.v0.rosette_pb2_grpc import RosetteStub

from ._data_objects.model import Model as _ModelData
from ._element_set import ElementSet
from ._grpc_helpers.collection import Collection as _Collection
from ._log import LOGGER
from ._modeling_group import ModelingGroup
from ._property_helper import (
    ResourceProtocol,
    grpc_data_getter,
    grpc_data_property,
    grpc_data_setter,
)
from ._resource_paths import join as _rp_join
from ._rosette import Rosette
from ._server import ServerProtocol
from ._typing_helper import PATH as _PATH

__all__ = ["Model"]


class _FeFormat(str, Enum):
    ANSYS_H5 = "ansys:h5"
    ANSYS_CDB = "ansys:cdb"
    ANSYS_DAT = "ansys:dat"
    ABAQUS_INP = "abaqus:inp"
    NASTRAN_BDF = "nastran:bdf"


class _IgnorableEntity(str, Enum):
    MESH = "mesh"
    ELEMENT_SETS = "element_sets"
    MATERIALS = "materials"
    COORDINATE_SYSTEMS = "coordinate_systems"
    SHELL_SECTIONS = "shell_sections"


class Model(ResourceProtocol):
    """Defines an ACP Model.

    Wrapper for accessing an ACP Model residing on a server.

    Parameters
    ----------
    resource_path :
        The Resource Path identifying the Model.
    server :
        The ACP server on which the model resides.
    """

    COLLECTION_LABEL = "models"

    # TODO: make resource_path have a non-str type?
    def __init__(self, *, resource_path: str, server: ServerProtocol):
        self._resource_path = resource_path
        self._server = server
        self._stub = ModelStub(self._server.channel)
        self._data_object: Optional[_ModelData] = None

    def _get_pb_resource_path(self) -> ResourcePath:
        return ResourcePath(value=self._resource_path)

    def _get(self) -> None:
        request = ModelRequest(resource_path=self._get_pb_resource_path())
        LOGGER.debug("Model Get request.")
        reply = self._stub.Get(request)
        self._data_object = _ModelData(
            name=reply.info.name,
            id="",
            version=reply.info.version,
            use_nodal_thicknesses=reply.modeling_properties.use_nodal_thicknesses,
            draping_offset_correction=reply.modeling_properties.draping_offset_correction,
            use_default_section_tolerances=reply.modeling_properties.use_default_section_tolerances,
            angle_tolerance=reply.modeling_properties.angle_tolerance,
            relative_thickness_tolerance=reply.modeling_properties.relative_thickness_tolerance,
            minimum_analysis_ply_thickness=reply.modeling_properties.minimum_analysis_ply_thickness,
        )

    def _put(self) -> None:
        # TODO: add all other properties
        if self._data_object is None:
            raise RuntimeError("Cannot create PUT request, the data_object is uninitialized.")
        request = ModelInfo(
            info=BasicInfo(
                resource_path=self._get_pb_resource_path(),
                name=self._data_object.name,
                version=self._data_object.version,
            ),
            modeling_properties=ModelInfo.ModelingProperties(
                use_nodal_thicknesses=self._data_object.use_nodal_thicknesses,
                draping_offset_correction=self._data_object.draping_offset_correction,
                use_default_section_tolerances=self._data_object.use_default_section_tolerances,
                angle_tolerance=self._data_object.angle_tolerance,
                relative_thickness_tolerance=self._data_object.relative_thickness_tolerance,
                minimum_analysis_ply_thickness=self._data_object.minimum_analysis_ply_thickness,
            ),
        )
        LOGGER.debug("Model Put request.")
        self._stub.Put(request)
        # TODO: update local cache with Put response

    def _get_data_attribute(self, name: str) -> Any:
        return getattr(self._data_object, name)

    def _set_data_attribute(self, name: str, value: Any) -> None:
        setattr(self._data_object, name, value)

    name = grpc_data_property("name")
    """The name of the model"""

    # TODO: document further properties, or autogenerate docstring from .proto files.

    use_nodal_thicknesses = grpc_data_property("use_nodal_thicknesses")
    draping_offset_correction = grpc_data_property("draping_offset_correction")
    angle_tolerance = grpc_data_property("angle_tolerance")
    relative_thickness_tolerance = grpc_data_property("relative_thickness_tolerance")
    minimum_analysis_ply_thickness = grpc_data_property("minimum_analysis_ply_thickness")
    use_default_section_tolerances = property(grpc_data_getter("use_default_section_tolerances"))

    @use_default_section_tolerances.setter  # type: ignore
    def use_default_section_tolerances(self, value: bool) -> None:
        if self._data_object is None:
            raise RuntimeError("Cannot create PUT request, the data_object is uninitialized.")
        if value and not self._data_object.use_default_section_tolerances:
            raise NotImplementedError(
                "Cannot turn on default section tolerances from PyACP, since the preference manager"
                " is not implemented."
            )
        grpc_data_setter("use_default_section_tolerances")(self, value)

    @classmethod
    def from_file(cls, *, path: _PATH, server: ServerProtocol) -> "Model":
        # Send absolute paths to the server, since its CWD may not match
        # the Python CWD.
        request = LoadModelRequest(path=str(path))
        reply = ModelStub(server.channel).LoadFromFile(request)
        return cls(resource_path=reply.info.resource_path.value, server=server)

    @classmethod
    def from_fe_file(
        cls,
        *,
        path: _PATH,
        server: ServerProtocol,
        format: Union[str, _FeFormat],
        ignored_entities: Iterable[Union[str, _IgnorableEntity]] = (),
        convert_section_data: bool = False,
    ) -> "Model":
        format_pb = {
            _FeFormat.ANSYS_H5: _pb_Format.ANSYS_H5,
            _FeFormat.ANSYS_CDB: _pb_Format.ANSYS_CDB,
            _FeFormat.ANSYS_DAT: _pb_Format.ANSYS_DAT,
            _FeFormat.ABAQUS_INP: _pb_Format.ABAQUS_INP,
            _FeFormat.NASTRAN_BDF: _pb_Format.NASTRAN_BDF,
        }[_FeFormat(format)]

        ignored_mapping = {
            _IgnorableEntity.MESH: LoadFEModelRequest.IgnorableEntity.MESH,
            _IgnorableEntity.ELEMENT_SETS: LoadFEModelRequest.IgnorableEntity.ELEMENT_SETS,
            _IgnorableEntity.MATERIALS: LoadFEModelRequest.IgnorableEntity.MATERIALS,
            _IgnorableEntity.COORDINATE_SYSTEMS: LoadFEModelRequest.IgnorableEntity.COORDINATE_SYSTEMS,
            _IgnorableEntity.SHELL_SECTIONS: LoadFEModelRequest.IgnorableEntity.SHELL_SECTIONS,
        }
        ignored_entities_pb = [ignored_mapping[_IgnorableEntity(val)] for val in ignored_entities]

        request = LoadFEModelRequest(
            path=str(path),
            format=format_pb,
            ignored_entities=ignored_entities_pb,
            convert_section_data=convert_section_data,
        )
        reply = ModelStub(server.channel).LoadFromFEFile(request)
        return cls(resource_path=reply.info.resource_path.value, server=server)

    def update(self, *, relations_only: bool = False) -> None:
        self._stub.Update(
            UpdateModelRequest(
                resource_path=self._get_pb_resource_path(), relations_only=relations_only
            )
        )

    def save(self, path: _PATH, *, save_cache: bool = False) -> None:
        self._stub.SaveToFile(
            SaveModelRequest(
                resource_path=self._get_pb_resource_path(),
                path=str(path),
                save_cache=save_cache,
            )
        )

    def create_modeling_group(self, name: str) -> ModelingGroup:
        collection_path = CollectionPath(
            value=_rp_join(self._resource_path, ModelingGroup.COLLECTION_LABEL)
        )
        stub = ModelingGroupStub(self._server.channel)
        request = CreateModelingGroupRequest(collection_path=collection_path, name=name)
        reply = stub.Create(request)
        return ModelingGroup(resource_path=reply.info.resource_path.value, server=self._server)

    @property
    def modeling_groups(self) -> _Collection[ModelingGroup]:
        # TODO: maybe this 'type info' can be collected into e.g. a dataclass
        return _Collection.from_types(
            server=self._server,
            stub_class=ModelingGroupStub,
            parent_resource_path=ResourcePath(value=self._resource_path),
            list_attribute="modeling_groups",
            list_request_class=ListModelingGroupsRequest,
            delete_request_class=DeleteModelingGroupRequest,
            object_class=ModelingGroup,
        )

    # ------------------------------------------------
    # ROSETTE

    # Todo: implement helper functions which are independent of the object type.
    def create_rosette(self, name: str) -> Rosette:
        collection_path = CollectionPath(
            value=_rp_join(self._resource_path, Rosette.COLLECTION_LABEL)
        )
        stub = RosetteStub(self._server.channel)
        request = CreateRosetteRequest(collection_path=collection_path, name=name)
        reply = stub.Create(request)
        return Rosette(resource_path=reply.info.resource_path.value, server=self._server)

    @property
    def rosettes(self) -> _Collection[Rosette]:
        return _Collection.from_types(
            server=self._server,
            parent_resource_path=ResourcePath(value=self._resource_path),
            stub_class=RosetteStub,
            list_attribute="rosettes",
            list_request_class=ListRosettesRequest,
            delete_request_class=DeleteRosetteRequest,
            object_class=Rosette,
        )

    @property
    def element_sets(self) -> _Collection[ElementSet]:
        return _Collection.from_types(
            server=self._server,
            parent_resource_path=ResourcePath(value=self._resource_path),
            stub_class=ElementSetStub,
            list_attribute="element_sets",
            list_request_class=ListElementSetsRequest,
            delete_request_class=DeleteElementSetRequest,
            object_class=ElementSet,
        )

    def create_element_set(self, name: str) -> ElementSet:
        collection_path = CollectionPath(
            value=_rp_join(self._resource_path, Rosette.COLLECTION_LABEL)
        )
        stub = ElementSetStub(self._server.channel)
        request = CreateElementSetRequest(collection_path=collection_path, name=name)
        reply = stub.Create(request)
        return ElementSet(resource_path=reply.info.resource_path.value, server=self._server)
