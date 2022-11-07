from __future__ import annotations

from typing import Iterable, cast

from grpc import Channel

from ansys.api.acp.v0 import (
    element_set_pb2_grpc,
    fabric_pb2_grpc,
    material_pb2_grpc,
    model_pb2,
    model_pb2_grpc,
    modeling_group_pb2_grpc,
    oriented_selection_set_pb2_grpc,
    rosette_pb2_grpc,
)

from .._grpc_helpers.enum_wrapper import wrap_to_string_enum
from .._grpc_helpers.mapping import define_mapping
from .._grpc_helpers.property_helper import grpc_data_property, mark_grpc_properties
from .._typing_helper import PATH as _PATH
from .base import TreeObject
from .element_set import ElementSet
from .fabric import Fabric
from .material import Material
from .modeling_group import ModelingGroup
from .oriented_selection_set import OrientedSelectionSet
from .rosette import Rosette

__all__ = ["Model"]


_FeFormat, _fe_format_to_pb, _ = wrap_to_string_enum(
    "_FeFormat",
    model_pb2.Format,
    module=__name__,
    value_converter=lambda val: val.lower().replace("_", ":"),
)
_IgnorableEntity, _ignorable_entity_to_pb, _ = wrap_to_string_enum(
    "_IgnorableEntity", model_pb2.LoadFromFEFileRequest.IgnorableEntity, module=__name__
)


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

    COLLECTION_LABEL = "models"
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
    ) -> Model:
        format_pb = _fe_format_to_pb(format)
        ignored_entities_pb = [_ignorable_entity_to_pb(val) for val in ignored_entities]

        request = model_pb2.LoadFromFEFileRequest(
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

    def save_analysis_model(self, path: _PATH) -> None:
        self._get_stub().SaveAnalysisModel(
            model_pb2.SaveAnalysisModelRequest(
                resource_path=self._resource_path,
                path=str(path),
            )
        )

    create_element_set, element_sets = define_mapping(
        ElementSet, element_set_pb2_grpc.ObjectServiceStub
    )
    create_fabric, fabrics = define_mapping(Fabric, fabric_pb2_grpc.ObjectServiceStub)
    create_material, materials = define_mapping(Material, material_pb2_grpc.ObjectServiceStub)
    create_rosette, rosettes = define_mapping(Rosette, rosette_pb2_grpc.ObjectServiceStub)
    create_oriented_selection_set, oriented_selection_sets = define_mapping(
        OrientedSelectionSet, oriented_selection_set_pb2_grpc.ObjectServiceStub
    )
    create_modeling_group, modeling_groups = define_mapping(
        ModelingGroup, modeling_group_pb2_grpc.ObjectServiceStub
    )
