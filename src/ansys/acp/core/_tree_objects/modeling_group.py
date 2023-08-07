from __future__ import annotations

import dataclasses
from typing import Any, Iterable

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0 import modeling_group_pb2, modeling_group_pb2_grpc, modeling_ply_pb2_grpc

from ._grpc_helpers.mapping import define_mutable_mapping
from ._grpc_helpers.property_helper import mark_grpc_properties
from ._mesh_data import ElementalData, NodalData, elemental_data_property, nodal_data_property
from .base import CreatableTreeObject, IdTreeObject
from .modeling_ply import ModelingPly
from .object_registry import register

__all__ = ["ModelingGroup"]


@dataclasses.dataclass
class ModelingGroupElementalData(ElementalData):
    """Represents elemental data for an Modeling Group."""

    normal: npt.NDArray[np.float64]


@dataclasses.dataclass
class ModelingGroupNodalData(NodalData):
    """Represents nodal data for an Modeling Group."""


@mark_grpc_properties
@register
class ModelingGroup(CreatableTreeObject, IdTreeObject):
    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "modeling_groups"
    OBJECT_INFO_TYPE = modeling_group_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = modeling_group_pb2.CreateRequest

    def __init__(self, name: str = "ModelingGroup", **kwargs: Any):
        super().__init__(name=name)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def _create_stub(self) -> modeling_group_pb2_grpc.ObjectServiceStub:
        return modeling_group_pb2_grpc.ObjectServiceStub(self._channel)

    create_modeling_ply, modeling_plies = define_mutable_mapping(
        ModelingPly, modeling_ply_pb2_grpc.ObjectServiceStub
    )

    elemental_data = elemental_data_property(ModelingGroupElementalData)
    nodal_data = nodal_data_property(ModelingGroupNodalData)
