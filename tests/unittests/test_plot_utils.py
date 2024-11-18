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

import pytest
from pytest_cases import parametrize_with_cases

from ansys.acp.core._plotter import get_directions_plotter
from ansys.acp.core._utils.visualization import _replace_underscores_and_capitalize


@pytest.fixture
def model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


def case_mesh_none_valid():
    return None


def case_model_mesh_valid(model):
    return model.mesh


def case_other_mesh_valid(model):
    return model.element_sets["All_Elements"].mesh


def case_empty_mesh_invalid(model):
    return model.create_element_set().mesh


@parametrize_with_cases("mesh", cases=".", glob="*_valid")
def test_direction_plotter_valid_cases(model, mesh, load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        modeling_ply = model.modeling_groups["ModelingGroup.1"].modeling_plies["ModelingPly.1"]
        analysis_ply = modeling_ply.production_plies["ProductionPly"].analysis_plies[
            "P1L1__ModelingPly.1"
        ]
        components = [
            analysis_ply.elemental_data.orientation,
            analysis_ply.elemental_data.normal,
            analysis_ply.elemental_data.reference_direction,
            analysis_ply.elemental_data.fiber_direction,
            analysis_ply.elemental_data.transverse_direction,
            analysis_ply.elemental_data.draped_fiber_direction,
            analysis_ply.elemental_data.draped_transverse_direction,
            analysis_ply.elemental_data.material_1_direction,
        ]
        plotter = get_directions_plotter(
            model=model,
            mesh=mesh,
            components=components,
        )

        for idx, data in enumerate(components):
            assert plotter.legend.GetEntryString(idx) == _replace_underscores_and_capitalize(
                data.component_name
            )


@parametrize_with_cases("mesh", cases=".", glob="*_invalid")
def test_direction_plotter_invalid_cases(model, mesh, load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        modeling_ply = model.modeling_groups["ModelingGroup.1"].modeling_plies["ModelingPly.1"]
        analysis_ply = modeling_ply.production_plies["ProductionPly"].analysis_plies[
            "P1L1__ModelingPly.1"
        ]
        components = [
            analysis_ply.elemental_data.orientation,
            analysis_ply.elemental_data.normal,
            analysis_ply.elemental_data.reference_direction,
            analysis_ply.elemental_data.fiber_direction,
            analysis_ply.elemental_data.transverse_direction,
            analysis_ply.elemental_data.draped_fiber_direction,
            analysis_ply.elemental_data.draped_transverse_direction,
            analysis_ply.elemental_data.material_1_direction,
        ]
        with pytest.raises(KeyError):
            get_directions_plotter(
                model=model,
                mesh=mesh,
                components=components,
            )
