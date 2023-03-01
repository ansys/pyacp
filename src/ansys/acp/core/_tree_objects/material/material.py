from __future__ import annotations

from typing import Iterable

from ansys.api.acp.v0 import material_pb2, material_pb2_grpc

from .._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ..base import CreatableTreeObject, IdTreeObject
from ..enums import PlyType, ply_type_from_pb, ply_type_to_pb, status_type_from_pb
from ..object_registry import register
from .property_set_wrapper import wrap_property_set
from .property_sets import (
    ConstantDensity,
    ConstantEngineeringConstants,
    VariableDensity,
    VariableEngineeringConstants,
)


@mark_grpc_properties
@register
class Material(CreatableTreeObject, IdTreeObject):
    """Instantiate a Material.

    Parameters
    ----------
    name :
        Name of the Material.
    ply_type :
        Define the type of material such as core, uni-directional (regular), woven, or isotropic.
    """

    _pb_object: material_pb2.ObjectInfo
    __slots__: Iterable[str] = tuple()

    COLLECTION_LABEL = "materials"
    OBJECT_INFO_TYPE = material_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = material_pb2.CreateRequest

    def __init__(
        self,
        name: str = "Material",
        ply_type: PlyType = "undefined",
        density: ConstantDensity | None = None,
        engineering_constants: ConstantEngineeringConstants | None = None,
    ):
        super().__init__(name=name)

        self.ply_type = ply_type
        self.density = density or ConstantDensity()
        self.engineering_constants = engineering_constants or ConstantEngineeringConstants()

    density = wrap_property_set("density", ConstantDensity, VariableDensity)
    engineering_constants = wrap_property_set(
        "engineering_constants", ConstantEngineeringConstants, VariableEngineeringConstants
    )

    def _create_stub(self) -> material_pb2_grpc.ObjectServiceStub:
        return material_pb2_grpc.ObjectServiceStub(self._channel)

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    ply_type = grpc_data_property(
        "properties.ply_type",
        from_protobuf=ply_type_from_pb,
        to_protobuf=ply_type_to_pb,
    )
