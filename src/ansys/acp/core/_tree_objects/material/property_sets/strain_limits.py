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

from typing_extensions import Self

from ansys.api.acp.v0 import material_pb2

from ..._grpc_helpers.property_helper import mark_grpc_properties
from .base import (
    _ISOTROPIC_PROPERTY_UNAVAILABLE_MSG,
    _ORTHOTROPIC_PROPERTY_UNAVAILABLE_MSG,
    _ConstantPropertySet,
    _PolymorphicMixin,
    _PolymorphicPropertyKwargs,
    _VariablePropertySet,
)
from .property_helper import (
    constant_material_grpc_data_property,
    variable_material_grpc_data_property,
)

__all__ = [
    "ConstantStrainLimits",
    "VariableStrainLimits",
]


class _StrainLimitsMixin(_PolymorphicMixin):
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.OrthotropicStrainLimitsPropertySet
    _FIELD_NAME_SUFFIX_DEFAULT = "_orthotropic"
    _FIELD_NAME_SUFFIX_BY_PB_DATATYPE = {
        material_pb2.IsotropicStrainLimitsPropertySet: "_isotropic",
        material_pb2.OrthotropicStrainLimitsPropertySet: "_orthotropic",
    }


_ISOTROPIC_KWARGS: _PolymorphicPropertyKwargs = {
    "available_on_pb_type": material_pb2.IsotropicStrainLimitsPropertySet,
    "unavailable_msg": _ISOTROPIC_PROPERTY_UNAVAILABLE_MSG,
}
_ORTHOTROPIC_KWARGS: _PolymorphicPropertyKwargs = {
    "available_on_pb_type": material_pb2.OrthotropicStrainLimitsPropertySet,
    "unavailable_msg": _ORTHOTROPIC_PROPERTY_UNAVAILABLE_MSG,
}


@mark_grpc_properties
class ConstantStrainLimits(_StrainLimitsMixin, _ConstantPropertySet):
    """Constant strain limits material property set."""

    _GRPC_PROPERTIES = tuple()
    _SUPPORTED_SINCE = "24.2"

    @classmethod
    def from_isotropic_constants(
        cls,
        *,
        effective_strain: float = 0.0,
    ) -> Self:
        """Create an isotropic strain limits property set.

        Parameters
        ----------
        effective_strain:
            Effective strain limit.

        Returns
        -------
        :
            An isotropic strain limits property set.
        """
        obj = cls(
            _pb_object=cls._create_pb_object_from_propertyset_type(
                material_pb2.IsotropicStrainLimitsPropertySet
            )
        )
        obj.effective_strain = effective_strain
        return obj

    @classmethod
    def from_orthotropic_constants(
        cls,
        *,
        eXc: float = 0.0,
        eYc: float = 0.0,
        eZc: float = 0.0,
        eXt: float = 0.0,
        eYt: float = 0.0,
        eZt: float = 0.0,
        eSxy: float = 0.0,
        eSyz: float = 0.0,
        eSxz: float = 0.0,
    ) -> Self:
        """Create an orthotropic strain limits property set.

        Parameters
        ----------
        eXc:
            Compressive strain limit in material 1 direction.
        eYc:
            Compressive strain limit in material 2 direction.
        eZc:
            Compressive strain limit in out-of-plane direction.
        eXt:
            Tensile strain limit in material 1 direction.
        eYt:
            Tensile strain limit in material 2 direction.
        eZt:
            Tensile strain limit in out-of-plane direction.
        eSxy:
            Shear strain limit in-plane (:math:`e_{12}`).
        eSyz:
            Shear strain limit out-of-plane (:math:`e_{23}`).
        eSxz:
            Shear strain limit out-of-plane (:math:`e_{13}`).

        Returns
        -------
        :
            An orthotropic strain limits property set.
        """
        obj = cls(
            _pb_object=cls._create_pb_object_from_propertyset_type(
                material_pb2.OrthotropicStrainLimitsPropertySet
            )
        )
        obj.eXc = eXc
        obj.eYc = eYc
        obj.eZc = eZc
        obj.eXt = eXt
        obj.eYt = eYt
        obj.eZt = eZt
        obj.eSxy = eSxy
        obj.eSyz = eSyz
        obj.eSxz = eSxz
        return obj

    effective_strain = constant_material_grpc_data_property("effective_strain", **_ISOTROPIC_KWARGS)
    eXc = constant_material_grpc_data_property("eXc", **_ORTHOTROPIC_KWARGS)
    eYc = constant_material_grpc_data_property("eYc", **_ORTHOTROPIC_KWARGS)
    eZc = constant_material_grpc_data_property("eZc", **_ORTHOTROPIC_KWARGS)
    eXt = constant_material_grpc_data_property("eXt", **_ORTHOTROPIC_KWARGS)
    eYt = constant_material_grpc_data_property("eYt", **_ORTHOTROPIC_KWARGS)
    eZt = constant_material_grpc_data_property("eZt", **_ORTHOTROPIC_KWARGS)
    eSxy = constant_material_grpc_data_property("eSxy", **_ORTHOTROPIC_KWARGS)
    eSyz = constant_material_grpc_data_property("eSyz", **_ORTHOTROPIC_KWARGS)
    eSxz = constant_material_grpc_data_property("eSxz", **_ORTHOTROPIC_KWARGS)


@mark_grpc_properties
class VariableStrainLimits(_StrainLimitsMixin, _VariablePropertySet):
    """Variable strain limits material property set."""

    _GRPC_PROPERTIES = tuple()
    _SUPPORTED_SINCE = "24.2"

    effective_strain = variable_material_grpc_data_property("effective_strain", **_ISOTROPIC_KWARGS)
    eXc = variable_material_grpc_data_property("eXc", **_ORTHOTROPIC_KWARGS)
    eYc = variable_material_grpc_data_property("eYc", **_ORTHOTROPIC_KWARGS)
    eZc = variable_material_grpc_data_property("eZc", **_ORTHOTROPIC_KWARGS)
    eXt = variable_material_grpc_data_property("eXt", **_ORTHOTROPIC_KWARGS)
    eYt = variable_material_grpc_data_property("eYt", **_ORTHOTROPIC_KWARGS)
    eZt = variable_material_grpc_data_property("eZt", **_ORTHOTROPIC_KWARGS)
    eSxy = variable_material_grpc_data_property("eSxy", **_ORTHOTROPIC_KWARGS)
    eSyz = variable_material_grpc_data_property("eSyz", **_ORTHOTROPIC_KWARGS)
    eSxz = variable_material_grpc_data_property("eSxz", **_ORTHOTROPIC_KWARGS)
