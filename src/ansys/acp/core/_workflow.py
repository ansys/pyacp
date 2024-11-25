# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
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

import pathlib
import typing

from . import UnitSystemType
from ._tree_objects import Model
from ._utils.typing_helper import PATH

# Avoid dependencies on pydpf-composites and dpf-core if it is not used
if typing.TYPE_CHECKING:  # pragma: no cover
    from ansys.dpf.composites.data_sources import ContinuousFiberCompositesFiles
    from ansys.dpf.core import UnitSystem

__all__ = ["get_shell_composite_post_processing_files", "get_dpf_unit_system"]


def get_shell_composite_post_processing_files(
    model: Model, local_rst_file_path: PATH, working_directory: PATH
) -> "ContinuousFiberCompositesFiles":
    """Get the files object needed for pydpf-composites from the workflow and the rst path.

    Only supports the shell workflow.

    Parameters
    ----------
    model:
        The ACP model.
    local_rst_file_path:
        Local path to the rst file.
    working_directory:
        Directory where the composite files will be saved.
    """
    working_directory = pathlib.Path(working_directory)

    # Only import here to avoid dependency on ansys.dpf.composites if it is not used
    try:
        from ansys.dpf.composites.data_sources import (
            CompositeDefinitionFiles,
            ContinuousFiberCompositesFiles,
        )
    except ImportError as e:
        raise ImportError(
            "The composite post processing files can only be retrieved if the "
            "ansys-dpf-composites package is installed."
        ) from e

    composite_definitions_file = working_directory / "ACPCompositeDefinitions.h5"
    model.export_shell_composite_definitions(composite_definitions_file)

    materials_file = working_directory / "materials.xml"
    model.export_materials(materials_file)

    composite_files = ContinuousFiberCompositesFiles(
        rst=local_rst_file_path,
        composite={
            "shell": CompositeDefinitionFiles(definition=composite_definitions_file),
        },
        engineering_data=materials_file,
    )
    return composite_files


# TODO: add 'get_solid_composite_post_processing_files' function


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
