from __future__ import annotations

from enum import Enum
from functools import lru_cache
from typing import Any, Iterable, Union

from grpc import Channel

from ansys.api.acp.v0.model_pb2 import (
    LoadFEModelRequest,
    LoadModelRequest,
    ModelInfo,
    SaveModelRequest,
    UpdateModelRequest,
)
from ansys.api.acp.v0.model_pb2 import Format as _pb_Format
from ansys.api.acp.v0.model_pb2_grpc import ModelStub

from .._grpc_helpers.collection import define_collection
from .._grpc_helpers.property_helper import grpc_data_property
from .._grpc_helpers.stub_info.element_set import ElementSetStubWrapper
from .._grpc_helpers.stub_info.modeling_group import ModelingGroupStubWrapper
from .._grpc_helpers.stub_info.rosette import RosetteStubWrapper
from .._typing_helper import PATH as _PATH
from .base import TreeObject
from .element_set import ElementSet
from .modeling_group import ModelingGroup
from .rosette import Rosette

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


class Model(TreeObject):
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
    OBJECT_INFO_TYPE = ModelInfo

    def __init__(self, name: str = "ACP Model", **kwargs: Any) -> None:
        super().__init__(name=name)

        for key, value in kwargs.items():
            setattr(self, key, value)

    # Mypy doesn't like this being a property, see https://github.com/python/mypy/issues/1362
    @lru_cache(maxsize=1)
    def _get_stub(self) -> ModelStub:
        return ModelStub(self._channel)

    # name = grpc_data_property("info.name")
    # """The name of the model"""

    # # TODO: document further properties, or autogenerate docstring from .proto files.

    use_nodal_thicknesses = grpc_data_property("modeling_properties.use_nodal_thicknesses")
    draping_offset_correction = grpc_data_property("modeling_properties.draping_offset_correction")
    angle_tolerance = grpc_data_property("modeling_properties.angle_tolerance")
    relative_thickness_tolerance = grpc_data_property(
        "modeling_properties.relative_thickness_tolerance"
    )
    minimum_analysis_ply_thickness = grpc_data_property(
        "modeling_properties.minimum_analysis_ply_thickness"
    )
    use_default_section_tolerances = grpc_data_property(
        "modeling_properties.use_default_section_tolerances"
    )

    @classmethod
    def from_file(cls, *, path: _PATH, channel: Channel) -> Model:
        # Send absolute paths to the server, since its CWD may not match
        # the Python CWD.
        request = LoadModelRequest(path=str(path))
        reply = ModelStub(channel).LoadFromFile(request)
        return cls.from_resource_path(resource_path=reply.info.resource_path.value, channel=channel)

    @classmethod
    def from_fe_file(
        cls,
        *,
        path: _PATH,
        channel: Channel,
        format: Union[str, _FeFormat],
        ignored_entities: Iterable[Union[str, _IgnorableEntity]] = (),
        convert_section_data: bool = False,
    ) -> Model:
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
        reply = ModelStub(channel).LoadFromFEFile(request)
        return cls.from_resource_path(resource_path=reply.info.resource_path.value, channel=channel)

    def update(self, *, relations_only: bool = False) -> None:
        self._get_stub().Update(
            UpdateModelRequest(
                resource_path=self._pb_object.info.resource_path, relations_only=relations_only
            )
        )

    def save(self, path: _PATH, *, save_cache: bool = False) -> None:
        self._get_stub().SaveToFile(
            SaveModelRequest(
                resource_path=self._pb_object.info.resource_path,
                path=str(path),
                save_cache=save_cache,
            )
        )

    create_modeling_group, modeling_groups = define_collection(
        ModelingGroup, ModelingGroupStubWrapper
    )
    create_rosette, rosettes = define_collection(Rosette, RosetteStubWrapper)
    create_element_set, element_sets = define_collection(ElementSet, ElementSetStubWrapper)
