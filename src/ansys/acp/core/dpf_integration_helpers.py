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

"""Helper functions for exchanging data between PyACP and PyDPF or PyDPF - Composites."""

import typing

from ._tree_objects.enums import UnitSystemType

# Avoid dependencies on pydpf-composites and dpf-core if it is not used
if typing.TYPE_CHECKING:  # pragma: no cover
    from ansys.dpf.core import UnitSystem

__all__ = ["get_dpf_unit_system"]


def get_dpf_unit_system(unit_system: UnitSystemType) -> "UnitSystem":
    """Convert pyACP unit system to DPF unit system.

    Parameters
    ----------
    unit_system
        The pyACP unit system.
    """
    try:
        from ansys.dpf.core import unit_systems
    except ImportError as e:
        raise ImportError(
            "The pyACP unit system can only be converted to a DPF unit system if the "
            "ansys-dpf-core package is installed."
        ) from e

    unit_systems_map = {
        UnitSystemType.UNDEFINED: unit_systems.undefined,
        # looks like the only difference from MKS to SI is
        # that temperature is defined as Kelvin in SI and °C in MKS.
        # We should still force the user to use MKS in this case.
        UnitSystemType.SI: None,
        UnitSystemType.MKS: unit_systems.solver_mks,
        UnitSystemType.uMKS: unit_systems.solver_umks,
        UnitSystemType.CGS: unit_systems.solver_cgs,
        # MPA is equivalent to nmm
        UnitSystemType.MPA: unit_systems.solver_nmm,
        UnitSystemType.BFT: unit_systems.solver_bft,
        UnitSystemType.BIN: unit_systems.solver_bin,
    }

    if unit_systems_map[unit_system] is None:
        raise ValueError(f"Unit system {unit_system} not supported. Use MKS instead of SI.")
    if unit_system not in unit_systems_map:
        raise ValueError(f"Unit system {unit_system} not supported.")

    return unit_systems_map[unit_system]
