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
    "ConstantEngineeringConstants",
    "VariableEngineeringConstants",
]


class _EngineeringConstantsMixin(_PolymorphicMixin):
    _DEFAULT_PB_PROPERTYSET_TYPE = material_pb2.OrthotropicEngineeringConstantsPropertySet
    _FIELD_NAME_DEFAULT = "_orthotropic"
    _FIELD_NAME_SUFFIX_BY_PB_DATATYPE = {
        material_pb2.IsotropicEngineeringConstantsPropertySet: "_isotropic",
        material_pb2.OrthotropicEngineeringConstantsPropertySet: "_orthotropic",
    }


_ISOTROPIC_KWARGS: _PolymorphicPropertyKwargs = {
    "available_on_pb_type": material_pb2.IsotropicEngineeringConstantsPropertySet,
    "unavailable_msg": _ISOTROPIC_PROPERTY_UNAVAILABLE_MSG,
}
_ORTHOTROPIC_KWARGS: _PolymorphicPropertyKwargs = {
    "available_on_pb_type": material_pb2.OrthotropicEngineeringConstantsPropertySet,
    "unavailable_msg": _ORTHOTROPIC_PROPERTY_UNAVAILABLE_MSG,
}


@mark_grpc_properties
class ConstantEngineeringConstants(_EngineeringConstantsMixin, _ConstantPropertySet):
    """Constant engineering constants material property set."""

    _GRPC_PROPERTIES = tuple()
    _SUPPORTED_SINCE = "24.2"

    @classmethod
    def from_isotropic_constants(
        cls,
        *,
        E: float = 0.0,
        nu: float = 0.0,  # correct??
    ) -> Self:
        """Create an isotropic engineering constants property set.

        Parameters
        ----------
        E :
            Young's modulus.
        nu :
            Poisson's ratio.

        Returns
        -------
        :
            An isotropic engineering constants property set.
        """
        obj = cls(
            _pb_object=cls._create_pb_object_from_propertyset_type(
                material_pb2.IsotropicEngineeringConstantsPropertySet
            )
        )
        obj.E = E
        obj.nu = nu
        return obj

    @classmethod
    def from_orthotropic_constants(
        cls,
        *,
        E1: float = 0.0,
        E2: float = 0.0,
        E3: float = 0.0,
        nu12: float = 0.0,
        nu23: float = 0.0,
        nu13: float = 0.0,
        G12: float = 0.0,
        G23: float = 0.0,
        G31: float = 0.0,
    ) -> Self:
        r"""Create an orthotropic engineering constants property set.

        Parameters
        ----------
        E1 :
            Young's modulus in material 1 direction.
        E2 :
            Young's modulus in material 2 direction.
        E3 :
            Young's modulus in out-of-plane direction.
        nu12 :
            Poisson's ratio :math:`\nu_{12}`.
        nu23 :
            Poisson's ratio :math:`\nu_{23}`.
        nu13 :
            Poisson's ratio :math:`\nu_{13}`.
        G12 :
            Shear modulus :math:`G_{12}`.
        G23 :
            Shear modulus :math:`G_{23}`.
        G31 :
            Shear modulus :math:`G_{31}`.

        Returns
        -------
        :
            An orthotropic engineering constants property set.
        """
        obj = cls()
        obj.E1 = E1
        obj.E2 = E2
        obj.E3 = E3
        obj.nu12 = nu12
        obj.nu23 = nu23
        obj.nu13 = nu13
        obj.G12 = G12
        obj.G23 = G23
        obj.G31 = G31
        return obj

    E = constant_material_grpc_data_property("E", **_ISOTROPIC_KWARGS)
    nu = constant_material_grpc_data_property("nu", **_ISOTROPIC_KWARGS)
    E1 = constant_material_grpc_data_property("E1", **_ORTHOTROPIC_KWARGS)
    E2 = constant_material_grpc_data_property("E2", **_ORTHOTROPIC_KWARGS)
    E3 = constant_material_grpc_data_property("E3", **_ORTHOTROPIC_KWARGS)
    G12 = constant_material_grpc_data_property("G12", **_ORTHOTROPIC_KWARGS)
    G23 = constant_material_grpc_data_property("G23", **_ORTHOTROPIC_KWARGS)
    G31 = constant_material_grpc_data_property("G31", **_ORTHOTROPIC_KWARGS)
    nu12 = constant_material_grpc_data_property("nu12", **_ORTHOTROPIC_KWARGS)
    nu23 = constant_material_grpc_data_property("nu23", **_ORTHOTROPIC_KWARGS)
    nu13 = constant_material_grpc_data_property("nu13", **_ORTHOTROPIC_KWARGS)


@mark_grpc_properties
class VariableEngineeringConstants(_EngineeringConstantsMixin, _VariablePropertySet):
    """Variable engineering constants material property set."""

    _GRPC_PROPERTIES = tuple()
    _SUPPORTED_SINCE = "24.2"

    E = variable_material_grpc_data_property("E", **_ISOTROPIC_KWARGS)
    nu = variable_material_grpc_data_property("nu", **_ISOTROPIC_KWARGS)
    E1 = variable_material_grpc_data_property("E1", **_ORTHOTROPIC_KWARGS)
    E2 = variable_material_grpc_data_property("E2", **_ORTHOTROPIC_KWARGS)
    E3 = variable_material_grpc_data_property("E3", **_ORTHOTROPIC_KWARGS)
    G12 = variable_material_grpc_data_property("G12", **_ORTHOTROPIC_KWARGS)
    G23 = variable_material_grpc_data_property("G23", **_ORTHOTROPIC_KWARGS)
    G31 = variable_material_grpc_data_property("G31", **_ORTHOTROPIC_KWARGS)
    nu12 = variable_material_grpc_data_property("nu12", **_ORTHOTROPIC_KWARGS)
    nu23 = variable_material_grpc_data_property("nu23", **_ORTHOTROPIC_KWARGS)
    nu13 = variable_material_grpc_data_property("nu13", **_ORTHOTROPIC_KWARGS)
