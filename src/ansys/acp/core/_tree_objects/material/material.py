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
from .property_sets import (
    ConstantDensity,
    ConstantEngineeringConstants,
    ConstantFabricFiberAngle,
    ConstantLaRCConstants,
    ConstantPuckConstants,
    ConstantStrainLimits,
    ConstantStressLimits,
    ConstantTsaiWuConstants,
    ConstantWovenCharacterization,
    ConstantWovenStressLimits,
    VariableDensity,
    VariableEngineeringConstants,
    VariableFabricFiberAngle,
    VariableLaRCConstants,
    VariablePuckConstants,
    VariableStrainLimits,
    VariableStressLimits,
    VariableTsaiWuConstants,
    VariableWovenCharacterization,
    VariableWovenStressLimits,
    wrap_property_set,
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
    stress_limits = wrap_property_set("stress_limits", ConstantStressLimits, VariableStressLimits)
    strain_limits = wrap_property_set("strain_limits", ConstantStrainLimits, VariableStrainLimits)
    puck_constants = wrap_property_set(
        "puck_constants", ConstantPuckConstants, VariablePuckConstants
    )
    woven_characterization = wrap_property_set(
        "woven_characterization", ConstantWovenCharacterization, VariableWovenCharacterization
    )
    woven_puck_constants_1 = wrap_property_set(
        "woven_puck_constants_1", ConstantPuckConstants, VariablePuckConstants
    )
    woven_puck_constants_2 = wrap_property_set(
        "woven_puck_constants_2", ConstantPuckConstants, VariablePuckConstants
    )
    woven_stress_limits_1 = wrap_property_set(
        "woven_stress_limits_1", ConstantWovenStressLimits, VariableWovenStressLimits
    )
    woven_stress_limits_2 = wrap_property_set(
        "woven_stress_limits_2", ConstantWovenStressLimits, VariableWovenStressLimits
    )
    tsai_wu_constants = wrap_property_set(
        "tsai_wu_constants", ConstantTsaiWuConstants, VariableTsaiWuConstants
    )
    larc_constants = wrap_property_set(
        "larc_constants", ConstantLaRCConstants, VariableLaRCConstants
    )
    fabric_fiber_angle = wrap_property_set(
        "fabric_fiber_angle", ConstantFabricFiberAngle, VariableFabricFiberAngle
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
