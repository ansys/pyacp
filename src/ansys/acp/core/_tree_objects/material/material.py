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

from collections.abc import Iterable

from ansys.api.acp.v0 import material_pb2, material_pb2_grpc

from ..._utils.property_protocols import ReadOnlyProperty
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

    .. note::

        The active material property sets are determined by the ``ply_type``. For
        example, ``puck_constants`` are only active when the ``ply_type`` is either
        :attr:`.PlyType.REGULAR` or :attr:`.PlyType.WOVEN`.

        The inactive property sets can still be *set*, but may not be accessible:

        - For **stored** materials, inactive property sets always return ``None``.
        - For **unstored** materials, inactive property sets can be accessed. They
          return ``None`` after storing.

    Parameters
    ----------
    name :
        Name of the Material.
    ply_type :
        Define the type of material such as core, uni-directional (regular), woven, or isotropic.
    density :
        Define the density of the material.
    engineering_constants :
        Define the material stiffness (Young's moduli, Poisson ratios and shear moduli).
    stress_limits :
        Define the stress limits for the evaluation of failure criteria with ansys.dpf.composites.
    strain_limits :
        Define the strain limits for the evaluation of failure criteria with ansys.dpf.composites.
    puck_constants :
        Define the puck constants for the evaluation of the Puck criterion with ansys.dpf.composites.
    woven_characterization :
        Define the puck constants of woven fabrics for the evaluation of the Puck
        criterion with ansys.dpf.composites.
    woven_puck_constants_1 :
        Define the puck constants of woven fabrics for the evaluation of the Puck
        criterion with ansys.dpf.composites.
    woven_puck_constants_2 :
        Define the puck constants of woven fabrics for the evaluation of the Puck
        criterion with ansys.dpf.composites.
    woven_puck_constants_2 :
        Define the puck constants of woven fabrics for the evaluation of the Puck
        criterion with ansys.dpf.composites.
    woven_stress_limits_1 :
        Define the puck constants of woven fabrics for the evaluation of the Puck
        criterion with ansys.dpf.composites.
    woven_stress_limits_2 :
        Define the puck constants of woven fabrics for the evaluation of the Puck
        criterion with ansys.dpf.composites.
    tsai_wu_constants :
        Define the Tsai-Wu constants for the evaluation of the Tsai-Wu criterion
        with ansys.dpf.composites.
    larc_constants :
        Define the LaRC constants for the evaluation of the LaRC criterion with
        ansys.dpf.composites.
    fabric_fiber_angle :
        Define the rotation angle between the material coordinate system and the fiber direction.
        Only used for shear dependent material properties which are provided by Material Designer.
    """

    _pb_object: material_pb2.ObjectInfo
    __slots__: Iterable[str] = tuple()

    _COLLECTION_LABEL = "materials"
    _OBJECT_INFO_TYPE = material_pb2.ObjectInfo
    _CREATE_REQUEST_TYPE = material_pb2.CreateRequest
    _SUPPORTED_SINCE = "24.2"

    def __init__(
        self,
        *,
        name: str = "Material",
        ply_type: PlyType = "undefined",
        density: ConstantDensity | None = None,
        engineering_constants: ConstantEngineeringConstants | None = None,
        stress_limits: ConstantStressLimits | None = None,
        strain_limits: ConstantStrainLimits | None = None,
        puck_constants: ConstantPuckConstants | None = None,
        woven_characterization: ConstantWovenCharacterization | None = None,
        woven_puck_constants_1: ConstantPuckConstants | None = None,
        woven_puck_constants_2: ConstantPuckConstants | None = None,
        woven_stress_limits_1: ConstantWovenStressLimits | None = None,
        woven_stress_limits_2: ConstantWovenStressLimits | None = None,
        tsai_wu_constants: ConstantTsaiWuConstants | None = None,
        larc_constants: ConstantLaRCConstants | None = None,
        fabric_fiber_angle: ConstantFabricFiberAngle | None = None,
    ):
        super().__init__(name=name)

        self.ply_type = ply_type
        self.density = density or ConstantDensity()
        self.engineering_constants = engineering_constants or ConstantEngineeringConstants()
        self.stress_limits = stress_limits
        self.strain_limits = strain_limits
        self.puck_constants = puck_constants
        self.woven_characterization = woven_characterization
        self.woven_puck_constants_1 = woven_puck_constants_1
        self.woven_puck_constants_2 = woven_puck_constants_2
        self.woven_stress_limits_1 = woven_stress_limits_1
        self.woven_stress_limits_2 = woven_stress_limits_2
        self.tsai_wu_constants = tsai_wu_constants
        self.larc_constants = larc_constants
        self.fabric_fiber_angle = fabric_fiber_angle

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

    locked: ReadOnlyProperty[bool] = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)
    ext_id: ReadOnlyProperty[str] = grpc_data_property_read_only("properties.ext_id")

    ply_type = grpc_data_property(
        "properties.ply_type",
        from_protobuf=ply_type_from_pb,
        to_protobuf=ply_type_to_pb,
    )
