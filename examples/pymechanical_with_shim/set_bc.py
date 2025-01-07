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

# type: ignore
"""
Generate a structural analysis and set the boundary conditions. Used in remote_workflow.py.
"""

analysis = Model.AddStaticStructuralAnalysis()

# Geometry has 4 named selections the
# NS2 is xmin and NS3 is xmax
NS2 = Model.NamedSelections.Children[1]
NS3 = Model.NamedSelections.Children[2]

fixed_support_48 = analysis.AddFixedSupport()
fixed_support_48.Location = NS2

force_37 = analysis.AddForce()
force_37.DefineBy = LoadDefineBy.Components
force_37.XComponent.Output.SetDiscreteValue(0, Quantity(1000, "N"))
force_37.Location = NS3
