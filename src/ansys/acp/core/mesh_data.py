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
"""Move mesh_data into separate namespace.

Remove classes and function which are not used by the public API
into a separate namespace.
"""

from ._tree_objects import (
    AnalysisPlyElementalData,
    AnalysisPlyNodalData,
    BooleanSelectionRuleElementalData,
    BooleanSelectionRuleNodalData,
    CutOffSelectionRuleElementalData,
    CutOffSelectionRuleNodalData,
    CylindricalSelectionRuleElementalData,
    CylindricalSelectionRuleNodalData,
    ElementSetElementalData,
    ElementSetNodalData,
    GeometricalSelectionRuleElementalData,
    GeometricalSelectionRuleNodalData,
    ImportedSolidModelElementalData,
    ImportedSolidModelNodalData,
    MeshData,
    ModelElementalData,
    ModelingPlyElementalData,
    ModelingPlyNodalData,
    ModelNodalData,
    OrientedSelectionSetElementalData,
    OrientedSelectionSetNodalData,
    ParallelSelectionRuleElementalData,
    ParallelSelectionRuleNodalData,
    ProductionPlyElementalData,
    ProductionPlyNodalData,
    ScalarData,
    SolidElementSetElementalData,
    SolidElementSetNodalData,
    SolidModelElementalData,
    SolidModelNodalData,
    SphericalSelectionRuleElementalData,
    SphericalSelectionRuleNodalData,
    TriangleMesh,
    TubeSelectionRuleElementalData,
    TubeSelectionRuleNodalData,
    VariableOffsetSelectionRuleElementalData,
    VariableOffsetSelectionRuleNodalData,
    VectorData,
)

__all__ = [
    "AnalysisPlyElementalData",
    "AnalysisPlyNodalData",
    "BooleanSelectionRuleElementalData",
    "BooleanSelectionRuleNodalData",
    "CutOffSelectionRuleElementalData",
    "CutOffSelectionRuleNodalData",
    "CylindricalSelectionRuleElementalData",
    "CylindricalSelectionRuleNodalData",
    "ElementSetElementalData",
    "ElementSetNodalData",
    "GeometricalSelectionRuleElementalData",
    "GeometricalSelectionRuleNodalData",
    "ImportedSolidModelElementalData",
    "ImportedSolidModelNodalData",
    "MeshData",
    "ModelElementalData",
    "ModelingPlyElementalData",
    "ModelingPlyNodalData",
    "ModelNodalData",
    "OrientedSelectionSetElementalData",
    "OrientedSelectionSetNodalData",
    "ParallelSelectionRuleElementalData",
    "ParallelSelectionRuleNodalData",
    "ProductionPlyElementalData",
    "ProductionPlyNodalData",
    "ScalarData",
    "SolidElementSetElementalData",
    "SolidElementSetNodalData",
    "SolidModelElementalData",
    "SolidModelNodalData",
    "SphericalSelectionRuleElementalData",
    "SphericalSelectionRuleNodalData",
    "TriangleMesh",
    "TubeSelectionRuleElementalData",
    "TubeSelectionRuleNodalData",
    "VariableOffsetSelectionRuleElementalData",
    "VariableOffsetSelectionRuleNodalData",
    "VectorData",
]
