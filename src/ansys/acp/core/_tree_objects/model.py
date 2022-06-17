from __future__ import annotations

from enum import Enum
from functools import lru_cache
from typing import Any, Iterable, Union

from grpc import Channel

from ansys.api.acp.v0 import (
    element_set_pb2_grpc,
    model_pb2,
    model_pb2_grpc,
    modeling_group_pb2_grpc,
    oriented_selection_set_pb2_grpc,
    rosette_pb2_grpc,
)
from ansys.api.acp.v0.model_pb2 import Format as _pb_Format

from .._grpc_helpers.collection import define_collection
from .._grpc_helpers.property_helper import grpc_data_property
from .._typing_helper import PATH as _PATH
from .base import TreeObject
from .element_set import ElementSet
from .modeling_group import ModelingGroup
from .oriented_selection_set import OrientedSelectionSet
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
    OBJECT_INFO_TYPE = model_pb2.ObjectInfo

    def __init__(self, name: str = "ACP Model", **kwargs: Any) -> None:
        super().__init__(name=name)

        for key, value in kwargs.items():
            setattr(self, key, value)

    @lru_cache(maxsize=1)
    def _get_stub(self) -> model_pb2_grpc.ObjectServiceStub:
        return model_pb2_grpc.ObjectServiceStub(self._channel)

    # # TODO: document further properties, or autogenerate docstring from .proto files.

    use_nodal_thicknesses = grpc_data_property("properties.use_nodal_thicknesses")
    draping_offset_correction = grpc_data_property("properties.draping_offset_correction")
    angle_tolerance = grpc_data_property("properties.angle_tolerance")
    relative_thickness_tolerance = grpc_data_property("properties.relative_thickness_tolerance")
    minimum_analysis_ply_thickness = grpc_data_property("properties.minimum_analysis_ply_thickness")
    use_default_section_tolerances = grpc_data_property("properties.use_default_section_tolerances")

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

        request_type = model_pb2.LoadFromFEFileRequest
        ignored_mapping = {
            _IgnorableEntity.MESH: request_type.IgnorableEntity.MESH,
            _IgnorableEntity.ELEMENT_SETS: request_type.IgnorableEntity.ELEMENT_SETS,
            _IgnorableEntity.MATERIALS: request_type.IgnorableEntity.MATERIALS,
            _IgnorableEntity.COORDINATE_SYSTEMS: request_type.IgnorableEntity.COORDINATE_SYSTEMS,
            _IgnorableEntity.SHELL_SECTIONS: request_type.IgnorableEntity.SHELL_SECTIONS,
        }
        ignored_entities_pb = [ignored_mapping[_IgnorableEntity(val)] for val in ignored_entities]

        request = request_type(
            path=str(path),
            format=format_pb,
            ignored_entities=ignored_entities_pb,
            convert_section_data=convert_section_data,
        )
        reply = model_pb2_grpc.ObjectServiceStub(channel).LoadFromFEFile(request)
        return cls._from_object_info(object_info=reply, channel=channel)

    def update(self, *, relations_only: bool = False) -> None:
        self._get_stub().Update(
            model_pb2.UpdateRequest(
                resource_path=self._resource_path, relations_only=relations_only
            )
        )

    def save(self, path: _PATH, *, save_cache: bool = False) -> None:
        self._get_stub().SaveToFile(
            model_pb2.SaveToFileRequest(
                resource_path=self._resource_path,
                path=str(path),
                save_cache=save_cache,
            )
        )

    create_element_set, element_sets = define_collection(
        ElementSet, element_set_pb2_grpc.ObjectServiceStub
    )
    create_rosette, rosettes = define_collection(Rosette, rosette_pb2_grpc.ObjectServiceStub)
    create_oriented_selection_set, oriented_selection_sets = define_collection(
        OrientedSelectionSet, oriented_selection_set_pb2_grpc.ObjectServiceStub
    )
    create_modeling_group, modeling_groups = define_collection(
        ModelingGroup, modeling_group_pb2_grpc.ObjectServiceStub
    )
