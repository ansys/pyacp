from __future__ import annotations

from collections.abc import Iterable, Sequence
import dataclasses
import typing

from ansys.api.acp.v0 import oriented_selection_set_pb2, oriented_selection_set_pb2_grpc

from .._utils.array_conversions import to_1D_double_array, to_tuple_from_1D_array
from .._utils.property_protocols import ReadWriteProperty
from ._grpc_helpers.linked_object_list import (
    define_linked_object_list,
    define_polymorphic_linked_object_list,
)
from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
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
from .boolean_selection_rule import BooleanSelectionRule
from .cylindrical_selection_rule import CylindricalSelectionRule
from .element_set import ElementSet
from .enums import (
    DrapingMaterialType,
    RosetteSelectionMethod,
    draping_material_type_from_pb,
    draping_material_type_to_pb,
    rosette_selection_method_from_pb,
    rosette_selection_method_to_pb,
    status_type_from_pb,
)
from .object_registry import register
from .parallel_selection_rule import ParallelSelectionRule
from .rosette import Rosette
from .spherical_selection_rule import SphericalSelectionRule
from .tube_selection_rule import TubeSelectionRule
from .variable_offset_selection_rule import VariableOffsetSelectionRule

# Workaround: these imports are needed to make sphinx_autodoc_typehints understand
# the inherited members of the Elemental- and NodalData classes.
import numpy as np  # noqa: F401 isort:skip
from ._mesh_data import ScalarData  # noqa: F401 isort:skip

__all__ = [
    "OrientedSelectionSet",
    "OrientedSelectionSetElementalData",
    "OrientedSelectionSetNodalData",
]

if typing.TYPE_CHECKING:
    # Since the 'LinkedSelectionRule' class is used by the boolean selection rule,
    # this would cause a circular import at run-time.
    from .. import BooleanSelectionRule, CutoffSelectionRule, GeometricalSelectionRule

    _LINKABLE_SELECTION_RULE_TYPES = typing.Union[
        ParallelSelectionRule,
        CylindricalSelectionRule,
        SphericalSelectionRule,
        TubeSelectionRule,
        GeometricalSelectionRule,
        VariableOffsetSelectionRule,
        CutoffSelectionRule,
        BooleanSelectionRule,
    ]


@dataclasses.dataclass
class OrientedSelectionSetElementalData(ElementalData):
    """Represents elemental data for an Oriented Selection Set."""

    normal: VectorData | None = None
    orientation: VectorData | None = None
    reference_direction: VectorData | None = None


@dataclasses.dataclass
class OrientedSelectionSetNodalData(NodalData):
    """Represents nodal data for an Oriented Selection Set."""


@mark_grpc_properties
@register
class OrientedSelectionSet(CreatableTreeObject, IdTreeObject):
    """Instantiate an Oriented Selection Set.

    Parameters
    ----------
    name :
        The name of the Oriented Selection Set.
    element_sets :
        Element Sets on which the Oriented Selection Set is defined.
    orientation_point :
        The Orientation Point of the Oriented Selection Set.
    orientation_direction :
        The Orientation Direction of the Oriented Element set.
    rosettes :
        Rosettes of the Oriented Selection Set.
    rosette_selection_method :
        Selection Method for Rosettes of the Oriented Selection Set.
    selection_rules :
        Selection Rules which may limit the extent of the Oriented Selection Set.
    draping :
        If ``True``, activate draping to adjust the reference directions.
    draping_seed_point :
        Starting point of the draping algorithm.
    auto_draping_direction :
        If ``True``, the reference direction of the Oriented Selection Set at
        the seed point is used as draping direction.
    draping_direction :
        Set the primary draping direction for the draping algorithm. Only used if
        ``auto_draping_direction`` is ``False``.
    draping_mesh_size :
        Defines the mesh size for the draping algorithm. If set to ``-1.``, the
        mesh size is automatically determined based on the average element size.
    draping_material_model :
        Chooses between different draping formulations.
    draping_ud_coefficient :
        Value between ``0`` and ``1`` which determines the amount of deformation
        in the transverse direction if the draping material model is set to
        :attr:`DrapingMaterialType.UD`.

    """

    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "oriented_selection_sets"
    OBJECT_INFO_TYPE = oriented_selection_set_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = oriented_selection_set_pb2.CreateRequest

    def __init__(
        self,
        *,
        name: str = "OrientedSelectionSet",
        element_sets: Sequence[ElementSet] = tuple(),
        orientation_point: tuple[float, float, float] = (0.0, 0.0, 0.0),
        orientation_direction: tuple[float, float, float] = (0.0, 0.0, 0.0),
        rosettes: Sequence[Rosette] = tuple(),
        rosette_selection_method: RosetteSelectionMethod = "minimum_angle",
        selection_rules: Sequence[_LINKABLE_SELECTION_RULE_TYPES] = tuple(),
        draping: bool = False,
        draping_seed_point: tuple[float, float, float] = (0.0, 0.0, 0.0),
        auto_draping_direction: bool = True,
        draping_direction: tuple[float, float, float] = (0.0, 0.0, 1.0),
        use_default_draping_mesh_size: bool = True,
        draping_mesh_size: float = 0.0,
        draping_material_model: DrapingMaterialType = DrapingMaterialType.WOVEN,
        draping_ud_coefficient: float = 0.0,
        rotation_angle: float = 0.0,
    ):
        super().__init__(name=name)
        self.element_sets = element_sets
        self.orientation_point = orientation_point
        self.orientation_direction = orientation_direction
        self.rosettes = rosettes
        self.rosette_selection_method = RosetteSelectionMethod(rosette_selection_method)
        self.selection_rules = selection_rules
        self.draping = draping
        self.draping_seed_point = draping_seed_point
        self.auto_draping_direction = auto_draping_direction
        self.draping_direction = draping_direction
        self.use_default_draping_mesh_size = use_default_draping_mesh_size
        self.draping_mesh_size = draping_mesh_size
        self.draping_material_model = DrapingMaterialType(draping_material_model)
        self.draping_ud_coefficient = draping_ud_coefficient
        self.rotation_angle = rotation_angle

    def _create_stub(self) -> oriented_selection_set_pb2_grpc.ObjectServiceStub:
        return oriented_selection_set_pb2_grpc.ObjectServiceStub(self._channel)

    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    element_sets = define_linked_object_list("properties.element_sets", ElementSet)

    orientation_point = grpc_data_property(
        "properties.orientation_point",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    orientation_direction = grpc_data_property(
        "properties.orientation_direction",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )

    rosettes = define_linked_object_list("properties.rosettes", Rosette)
    rosette_selection_method = grpc_data_property(
        "properties.rosette_selection_method",
        from_protobuf=rosette_selection_method_from_pb,
        to_protobuf=rosette_selection_method_to_pb,
    )

    draping: ReadWriteProperty[bool, bool] = grpc_data_property("properties.draping")
    draping_seed_point = grpc_data_property(
        "properties.draping_seed_point",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    auto_draping_direction: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.auto_draping_direction"
    )
    draping_direction = grpc_data_property(
        "properties.draping_direction",
        from_protobuf=to_tuple_from_1D_array,
        to_protobuf=to_1D_double_array,
    )
    use_default_draping_mesh_size: ReadWriteProperty[bool, bool] = grpc_data_property(
        "properties.use_default_draping_mesh_size"
    )
    draping_mesh_size: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.draping_mesh_size"
    )
    draping_material_model = grpc_data_property(
        "properties.draping_material_model",
        from_protobuf=draping_material_type_from_pb,
        to_protobuf=draping_material_type_to_pb,
    )
    draping_ud_coefficient: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.draping_ud_coefficient"
    )

    rotation_angle: ReadWriteProperty[float, float] = grpc_data_property(
        "properties.rotation_angle"
    )

    selection_rules = define_polymorphic_linked_object_list(
        "properties.selection_rules",
        allowed_types=(
            ParallelSelectionRule,
            CylindricalSelectionRule,
            SphericalSelectionRule,
            TubeSelectionRule,
            VariableOffsetSelectionRule,
            BooleanSelectionRule,
        ),
    )

    elemental_data = elemental_data_property(OrientedSelectionSetElementalData)
    nodal_data = nodal_data_property(OrientedSelectionSetNodalData)
