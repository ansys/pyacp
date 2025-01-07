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
from typing import Union, get_args

from ansys.api.acp.v0 import sensor_pb2, sensor_pb2_grpc

from .._utils.array_conversions import to_tuple_from_1D_array
from .._utils.property_protocols import ReadOnlyProperty, ReadWriteProperty
from ._grpc_helpers.linked_object_list import define_polymorphic_linked_object_list
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject
from .element_set import ElementSet
from .enums import SensorType, sensor_type_from_pb, sensor_type_to_pb, status_type_from_pb
from .fabric import Fabric
from .modeling_ply import ModelingPly
from .object_registry import register
from .oriented_selection_set import OrientedSelectionSet
from .stackup import Stackup
from .sublaminate import SubLaminate

__all__ = ["Sensor"]


_LINKABLE_ENTITY_TYPES = Union[
    Fabric, Stackup, SubLaminate, ElementSet, OrientedSelectionSet, ModelingPly
]


@mark_grpc_properties
@register
class Sensor(CreatableTreeObject, IdTreeObject):
    """Instantiate a Sensor.

    Parameters
    ----------
    name :
        Name of the sensor.
    sensor_type :
        Type of sensor: The sensor can be scoped by area, material, plies,
        or solid model.
    active :
        Inactive sensors are not evaluated.
    entities :
        List of entities which define the sensor's scope.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "sensors"
    _OBJECT_INFO_TYPE = sensor_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = sensor_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "Sensor",
        sensor_type: SensorType = SensorType.SENSOR_BY_AREA,
        active: bool = True,
        entities: Sequence[_LINKABLE_ENTITY_TYPES] = (),
    ):
        super().__init__(name=name)
        self.active = active
        self.entities = entities
        self.sensor_type = sensor_type

    def _create_stub(self) -> sensor_pb2_grpc.ObjectServiceStub:
        return sensor_pb2_grpc.ObjectServiceStub(self._channel)

    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    sensor_type = grpc_data_property(
        "properties.sensor_type", from_protobuf=sensor_type_from_pb, to_protobuf=sensor_type_to_pb
    )
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    active: ReadWriteProperty[bool, bool] = grpc_data_property("properties.active")
    entities = define_polymorphic_linked_object_list(
        "properties.entities", allowed_types=get_args(_LINKABLE_ENTITY_TYPES)
    )

    covered_area: ReadOnlyProperty[float | None] = grpc_data_property_read_only(
        "properties.covered_area",
        check_optional=True,
        doc=(
            "The surface area of a selected Element Set / Oriented Selection Set, "
            "or the tooling surface area that is covered by the composite layup of "
            "the selected Material or Modeling Ply."
        ),
    )
    modeling_ply_area: ReadOnlyProperty[float | None] = grpc_data_property_read_only(
        "properties.modeling_ply_area",
        check_optional=True,
        doc="The surface area of all Modeling Plies of the selected entity.",
    )
    production_ply_area: ReadOnlyProperty[float | None] = grpc_data_property_read_only(
        "properties.production_ply_area",
        check_optional=True,
        doc="The surface area of all production plies of the selected entity.",
    )
    price: ReadOnlyProperty[float | None] = grpc_data_property_read_only(
        "properties.price",
        check_optional=True,
        doc=(
            "The price for the composite layup of the selected entity. The price "
            "per area is defined on the Fabrics or Stackups."
        ),
    )
    weight: ReadOnlyProperty[float | None] = grpc_data_property_read_only(
        "properties.weight", check_optional=True, doc="The mass of the selected entity."
    )
    center_of_gravity = grpc_data_property_read_only(
        "properties.center_of_gravity",
        from_protobuf=to_tuple_from_1D_array,
        check_optional=True,
        doc="The center of gravity of the selected entity in the global coordinate system.",
    )
