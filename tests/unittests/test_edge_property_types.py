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

from pytest_cases import parametrize_with_cases

from ansys.acp.core import (
    BooleanOperationType,
    FabricWithAngle,
    Lamina,
    LinkedSelectionRule,
    SubShape,
    TaperEdge,
)


def case_fabric_with_angle(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        fabric = model.create_fabric()
        yield FabricWithAngle(fabric=fabric, angle=12.3), ("fabric", "angle")


def case_linked_selection_rule(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        selection_rule = model.create_parallel_selection_rule()
        yield LinkedSelectionRule(
            selection_rule=selection_rule,
            operation_type=BooleanOperationType.ADD,
            template_rule=False,
            parameter_1=1.0,
            parameter_2=2.0,
        ), ("selection_rule", "operation_type", "template_rule", "parameter_1", "parameter_2")


def case_taper_edge(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        edge_set = model.create_edge_set()
        yield TaperEdge(edge_set=edge_set, angle=11.2, offset=0.6), ("edge_set", "angle", "offset")


def case_subshape(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        cad_geometry = model.create_cad_geometry()
        yield SubShape(cad_geometry=cad_geometry, path="path/to/subshape"), ("cad_geometry", "path")


def case_lamina_fabric(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        material = model.create_fabric()
        yield Lamina(material=material, angle=7.5), ("material", "angle")


def case_lamina_stackup(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        material = model.create_stackup()
        yield Lamina(material=material, angle=7.5), ("material", "angle")


@parametrize_with_cases("edge_property_type_instance,attribute_names", cases=".", glob="*")
def test_clone(edge_property_type_instance, attribute_names):
    cloned_instance = edge_property_type_instance.clone()
    for attr_name in attribute_names:
        assert getattr(cloned_instance, attr_name) == getattr(
            edge_property_type_instance, attr_name
        )
