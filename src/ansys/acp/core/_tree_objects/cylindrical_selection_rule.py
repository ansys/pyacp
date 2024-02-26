from __future__ import annotations

from collections.abc import Collection, Iterable
import dataclasses

from ansys.api.acp.v0 import cylindrical_selection_rule_pb2, cylindrical_selection_rule_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    grpc_link_property,
    mark_grpc_properties,
)
from ._mesh_data import (
    ElementalData,
    NodalData,
    VectorData,
    elemental_data_property,
    nodal_data_property,
)
from .base import CreatableTreeObject, IdTreeObject
from .enums import status_type_from_pb
from .object_registry import register
from .rosette import Rosette

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip
from ._mesh_data import ScalarData  # noqa: F401 isort:skip

__all__ = [
    "CylindricalSelectionRule",
    "CylindricalSelectionRuleElementalData",
    "CylindricalSelectionRuleNodalData",
]


@dataclasses.dataclass
class CylindricalSelectionRuleElementalData(ElementalData):
    """Represents elemental data for a Cylindrical Selection Rule."""

    normal: VectorData | None = None


@dataclasses.dataclass
class CylindricalSelectionRuleNodalData(NodalData):
    """Represents nodal data for a Cylindrical Selection Rule."""


@mark_grpc_properties
@register
class CylindricalSelectionRule(CreatableTreeObject, IdTreeObject):
    """Instantiate a Cylindrical Selection Rule.

    Parameters
    ----------
    name :
        Name of the Cylindrical Selection Rule.
    use_global_coordinate_system :
        Use global coordinate system for origin and direction.
    rosette :
        Rosette used for origin and direction. Only applies if
        ``use_global_coordinate_system`` is False.
    origin :
        Origin of the Cylindrical Selection Rule.
    direction :
        Direction of the Cylindrical Selection Rule.
    radius :
        Radius of the cylinder.
    relative_rule_type :
        If True, parameters are evaluated relative to size of the object.
    include_rule_type :
        Include or exclude area in rule. Setting this to ``False``
        inverts the selection.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "cylindrical_selection_rules"
    _OBJECT_INFO_TYPE = cylindrical_selection_rule_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = cylindrical_selection_rule_pb2.CreateRequest

    def __init__(
        self,
        *,
        name: str = "CylindricalSelectionrule",
        use_global_coordinate_system: bool = True,
        rosette: Rosette | None = None,
        origin: tuple[float, ...] = (0.0, 0.0, 0.0),
        direction: tuple[float, ...] = (0.0, 0.0, 1.0),
        radius: float = 0.0,
        relative_rule_type: bool = False,
        include_rule_type: bool = True,
    ):
        super().__init__(name=name)
        self.use_global_coordinate_system = use_global_coordinate_system
        self.rosette = rosette
        self.origin = origin
        self.direction = direction
        self.radius = radius
        self.relative_rule_type = relative_rule_type
        self.include_rule_type = include_rule_type

    def _create_stub(self) -> cylindrical_selection_rule_pb2_grpc.ObjectServiceStub:
        return cylindrical_selection_rule_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    use_global_coordinate_system: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_global_coordinate_system"
    )
    rosette = grpc_link_property("properties.rosette", allowed_types=Rosette)
    origin: ReadWriteProperty[tuple[float, float, float], Collection[float]] = grpc_data_property(
        "properties.origin", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    direction = grpc_data_property(
        "properties.direction", from_protobuf=to_tuple_from_1D_array, to_protobuf=to_1D_double_array
    )
    radius: ReadWriteProperty[float, float] = grpc_data_property("properties.radius")
    relative_rule_type: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.relative_rule_type"
    )
    include_rule_type: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.include_rule_type"
    )

    elemental_data = elemental_data_property(CylindricalSelectionRuleElementalData)
    nodal_data = nodal_data_property(CylindricalSelectionRuleNodalData)
