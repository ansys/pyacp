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

import os
import textwrap

import pytest

from ansys.acp.core.extras.feature_tree import get_feature_tree


@pytest.mark.parametrize(
    "show_lines,expected",
    [
        (
            False,
            textwrap.dedent(
                """\
                Model
                    Material
                    Fabric
                    Stackup
                    SubLaminate
                    ElementSet
                    EdgeSet
                    CADGeometry
                        CADComponent (read-only)
                    VirtualGeometry
                    Rosette
                    LookUpTable1D
                        LookUpTable1DColumn
                    LookUpTable3D
                        LookUpTable3DColumn
                    ParallelSelectionRule
                    CylindricalSelectionRule
                    SphericalSelectionRule
                    TubeSelectionRule
                    CutOffSelectionRule
                    GeometricalSelectionRule
                    VariableOffsetSelectionRule
                    BooleanSelectionRule
                    OrientedSelectionSet
                    ModelingGroup
                        ModelingPly
                            ProductionPly (read-only)
                                AnalysisPly (read-only)
                        InterfaceLayer
                        ButtJointSequence
                    ImportedModelingGroup
                        ImportedModelingPly
                            ImportedProductionPly (read-only)
                                ImportedAnalysisPly (read-only)
                    SamplingPoint
                    SectionCut
                    SolidModel
                        ExtrusionGuide
                        SnapToGeometry
                        SolidElementSet (read-only)
                        CutOffGeometry
                        AnalysisPly (read-only)
                        InterfaceLayer (read-only)
                    ImportedSolidModel
                        SolidElementSet (read-only)
                        CutOffGeometry
                        LayupMappingObject
                            AnalysisPly (read-only)
                            ImportedAnalysisPly (read-only)
                        AnalysisPly (read-only)
                        ImportedAnalysisPly (read-only)
                    Sensor
                    FieldDefinition
                """
            ),
        ),
        (
            True,
            textwrap.dedent(
                """\
                Model
                ├── Material
                ├── Fabric
                ├── Stackup
                ├── SubLaminate
                ├── ElementSet
                ├── EdgeSet
                ├── CADGeometry
                │   └── CADComponent (read-only)
                ├── VirtualGeometry
                ├── Rosette
                ├── LookUpTable1D
                │   └── LookUpTable1DColumn
                ├── LookUpTable3D
                │   └── LookUpTable3DColumn
                ├── ParallelSelectionRule
                ├── CylindricalSelectionRule
                ├── SphericalSelectionRule
                ├── TubeSelectionRule
                ├── CutOffSelectionRule
                ├── GeometricalSelectionRule
                ├── VariableOffsetSelectionRule
                ├── BooleanSelectionRule
                ├── OrientedSelectionSet
                ├── ModelingGroup
                │   ├── ModelingPly
                │   │   └── ProductionPly (read-only)
                │   │       └── AnalysisPly (read-only)
                │   ├── InterfaceLayer
                │   └── ButtJointSequence
                ├── ImportedModelingGroup
                │   └── ImportedModelingPly
                │       └── ImportedProductionPly (read-only)
                │           └── ImportedAnalysisPly (read-only)
                ├── SamplingPoint
                ├── SectionCut
                ├── SolidModel
                │   ├── ExtrusionGuide
                │   ├── SnapToGeometry
                │   ├── SolidElementSet (read-only)
                │   ├── CutOffGeometry
                │   ├── AnalysisPly (read-only)
                │   └── InterfaceLayer (read-only)
                ├── ImportedSolidModel
                │   ├── SolidElementSet (read-only)
                │   ├── CutOffGeometry
                │   ├── LayupMappingObject
                │   │   ├── AnalysisPly (read-only)
                │   │   └── ImportedAnalysisPly (read-only)
                │   ├── AnalysisPly (read-only)
                │   └── ImportedAnalysisPly (read-only)
                ├── Sensor
                └── FieldDefinition
                """
            ),
        ),
    ],
)
def test_feature_tree(show_lines, expected):
    """Test that the feature tree is correct."""
    tree = get_feature_tree()
    assert tree.to_string(show_lines=show_lines) == expected.replace("\n", os.linesep)
