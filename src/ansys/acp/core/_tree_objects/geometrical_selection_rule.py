from __future__ import annotations

from collections.abc import Iterable
import dataclasses

from ansys.api.acp.v0 import geometrical_selection_rule_pb2, geometrical_selection_rule_pb2_grpc

from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.linked_object_list import define_linked_object_list
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
from .element_set import ElementSet
from .enums import (
    GeometricalRuleType,
    geometrical_rule_type_from_pb,
    geometrical_rule_type_to_pb,
    status_type_from_pb,
)
from .object_registry import register
from .virtual_geometry import VirtualGeometry

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip
from ._mesh_data import ScalarData  # noqa: F401 isort:skip

__all__ = [
    "GeometricalSelectionRule",
    "GeometricalSelectionRuleElementalData",
    "GeometricalSelectionRuleNodalData",
]


@dataclasses.dataclass
class GeometricalSelectionRuleElementalData(ElementalData):
    """Represents elemental data for a Geometrical Selection Rule."""

    normal: VectorData


@dataclasses.dataclass
class GeometricalSelectionRuleNodalData(NodalData):
    """Represents nodal data for a Geometrical Selection Rule."""


@mark_grpc_properties
@register
class GeometricalSelectionRule(CreatableTreeObject, IdTreeObject):
    """Instantiate a Geometrical Selection Rule.

    Parameters
    ----------
    name :
        Name of the Geometrical Selection Rule.
    geometrical_rule_type :
        Rule type. Can be either :attr:`.GeometricalRuleType.GEOMETRY` or
        :attr:`.GeometricalRuleType.ELEMENT_SETS`.
    geometry :
        Virtual geometry to use for the rule.
    element_sets :
        Element sets to use for the rule.
    include_rule_type :
        Include or exclude area in rule. Setting this to ``False``
        inverts the selection.
    use_default_tolerances :
        Whether to use default tolerances.
    in_plane_capture_tolerance :
        In-plane capture tolerance around the outline.
    negative_capture_tolerance :
        Capture tolerance along the surface or projection normal.
    positive_capture_tolerance :
        Capture tolerance along the opposite surface or projection normal.
    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "geometrical_selection_rules"
    OBJECT_INFO_TYPE = geometrical_selection_rule_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = geometrical_selection_rule_pb2.CreateRequest

    def __init__(
        self,
        *,
        name: str = "GeometricalSelectionrule",
        geometrical_rule_type: GeometricalRuleType = GeometricalRuleType.GEOMETRY,
        geometry: VirtualGeometry | None = None,
        element_sets: Iterable[ElementSet] = (),
        include_rule_type: bool = True,
        use_default_tolerances: bool = True,
        in_plane_capture_tolerance: float = 0.0,
        negative_capture_tolerance: float = 0.0,
        positive_capture_tolerance: float = 0.0,
    ):
        super().__init__(name=name)
        self.geometrical_rule_type = geometrical_rule_type
        self.geometry = geometry
        self.element_sets = element_sets
        self.include_rule_type = include_rule_type
        self.use_default_tolerances = use_default_tolerances
        self.in_plane_capture_tolerance = in_plane_capture_tolerance
        self.negative_capture_tolerance = negative_capture_tolerance
        self.positive_capture_tolerance = positive_capture_tolerance

    def _create_stub(self) -> geometrical_selection_rule_pb2_grpc.ObjectServiceStub:
        return geometrical_selection_rule_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    geometrical_rule_type = grpc_data_property(
        "properties.geometrical_rule_type",
        from_protobuf=geometrical_rule_type_from_pb,
        to_protobuf=geometrical_rule_type_to_pb,
    )
    geometry = grpc_link_property("properties.geometry")
    element_sets = define_linked_object_list("properties.element_sets", object_class=ElementSet)
    include_rule_type: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.include_rule_type"
    )
    use_default_tolerances: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_default_tolerances"
    )
    in_plane_capture_tolerance: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.in_plane_capture_tolerance"
    )
    negative_capture_tolerance: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.negative_capture_tolerance"
    )
    positive_capture_tolerance: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.positive_capture_tolerance"
    )

    elemental_data = elemental_data_property(GeometricalSelectionRuleElementalData)
    nodal_data = nodal_data_property(GeometricalSelectionRuleNodalData)
