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

from pytest_cases import parametrize_with_cases

from ansys.acp.core import get_model_tree


def case_simple_model(acp_instance, model_data_dir):
    input_file_path = model_data_dir / "minimal_complete_model_no_matml_link.acph5"
    model = acp_instance.import_model(name="minimal_complete", path=input_file_path)
    model.update()
    return (
        model,
        False,
        textwrap.dedent(
            """\
            'minimal_complete'
                Materials
                    'Structural Steel'
                Fabrics
                    'Fabric.1'
                Element Sets
                    'All_Elements'
                Edge Sets
                    'ns_edge'
                Rosettes
                    'Global Coordinate System'
                Oriented Selection Sets
                    'OrientedSelectionSet.1'
                Modeling Groups
                    'ModelingGroup.1'
                        Modeling Plies
                            'ModelingPly.1'
                                Production Plies
                                    'P1__ModelingPly.1'
                                        Analysis Plies
                                            'P1L1__ModelingPly.1'
            """
        ),
    )


def case_more_objects(acp_instance, model_data_dir):
    input_file_path = model_data_dir / "minimal_complete_model_no_matml_link.acph5"
    model = acp_instance.import_model(name="minimal_complete", path=input_file_path)

    model.update()

    model.create_edge_set()
    model.create_stackup()
    model.create_sublaminate()
    model.create_virtual_geometry()
    model.create_cad_geometry()
    model.create_parallel_selection_rule()
    model.create_cylindrical_selection_rule()
    model.create_tube_selection_rule()
    model.create_cut_off_selection_rule()
    model.create_geometrical_selection_rule()
    model.create_boolean_selection_rule()
    model.create_lookup_table_1d()
    model.create_lookup_table_3d()
    model.create_sensor()

    return (
        model,
        False,
        textwrap.dedent(
            """\
            'minimal_complete'
                Materials
                    'Structural Steel'
                Fabrics
                    'Fabric.1'
                Stackups
                    'Stackup'
                Sublaminates
                    'SubLaminate'
                Element Sets
                    'All_Elements'
                Edge Sets
                    'ns_edge'
                    'EdgeSet'
                Cad Geometries
                    'CADGeometry'
                Virtual Geometries
                    'VirtualGeometry'
                Rosettes
                    'Global Coordinate System'
                Lookup Tables 1d
                    'LookUpTable1D'
                        Columns
                            'Location'
                Lookup Tables 3d
                    'LookUpTable3D'
                        Columns
                            'Location'
                Parallel Selection Rules
                    'ParallelSelectionrule'
                Cylindrical Selection Rules
                    'CylindricalSelectionrule'
                Tube Selection Rules
                    'TubeSelectionrule'
                Cut Off Selection Rules
                    'CutOffSelectionrule'
                Geometrical Selection Rules
                    'GeometricalSelectionrule'
                Boolean Selection Rules
                    'BooleanSelectionrule'
                Oriented Selection Sets
                    'OrientedSelectionSet.1'
                Modeling Groups
                    'ModelingGroup.1'
                        Modeling Plies
                            'ModelingPly.1'
                                Production Plies
                                    'P1__ModelingPly.1'
                                        Analysis Plies
                                            'P1L1__ModelingPly.1'
                Sensors
                    'Sensor'
            """
        ),
    )


def case_more_objects_lines(acp_instance, model_data_dir):
    input_file_path = model_data_dir / "minimal_complete_model_no_matml_link.acph5"
    model = acp_instance.import_model(name="minimal_complete", path=input_file_path)

    model.update()

    model.create_edge_set()
    model.create_stackup()
    model.create_sublaminate()
    model.create_virtual_geometry()
    model.create_cad_geometry()
    model.create_parallel_selection_rule()
    model.create_cylindrical_selection_rule()
    model.create_tube_selection_rule()
    model.create_cut_off_selection_rule()
    model.create_geometrical_selection_rule()
    model.create_boolean_selection_rule()
    model.create_lookup_table_1d()
    model.create_lookup_table_3d()
    model.create_sensor()

    return (
        model,
        True,
        textwrap.dedent(
            """\
            'minimal_complete'
            ├── Materials
            │   └── 'Structural Steel'
            ├── Fabrics
            │   └── 'Fabric.1'
            ├── Stackups
            │   └── 'Stackup'
            ├── Sublaminates
            │   └── 'SubLaminate'
            ├── Element Sets
            │   └── 'All_Elements'
            ├── Edge Sets
            │   ├── 'ns_edge'
            │   └── 'EdgeSet'
            ├── Cad Geometries
            │   └── 'CADGeometry'
            ├── Virtual Geometries
            │   └── 'VirtualGeometry'
            ├── Rosettes
            │   └── 'Global Coordinate System'
            ├── Lookup Tables 1d
            │   └── 'LookUpTable1D'
            │       └── Columns
            │           └── 'Location'
            ├── Lookup Tables 3d
            │   └── 'LookUpTable3D'
            │       └── Columns
            │           └── 'Location'
            ├── Parallel Selection Rules
            │   └── 'ParallelSelectionrule'
            ├── Cylindrical Selection Rules
            │   └── 'CylindricalSelectionrule'
            ├── Tube Selection Rules
            │   └── 'TubeSelectionrule'
            ├── Cut Off Selection Rules
            │   └── 'CutOffSelectionrule'
            ├── Geometrical Selection Rules
            │   └── 'GeometricalSelectionrule'
            ├── Boolean Selection Rules
            │   └── 'BooleanSelectionrule'
            ├── Oriented Selection Sets
            │   └── 'OrientedSelectionSet.1'
            ├── Modeling Groups
            │   └── 'ModelingGroup.1'
            │       └── Modeling Plies
            │           └── 'ModelingPly.1'
            │               └── Production Plies
            │                   └── 'P1__ModelingPly.1'
            │                       └── Analysis Plies
            │                           └── 'P1L1__ModelingPly.1'
            └── Sensors
                └── 'Sensor'
            """
        ),
    )


@parametrize_with_cases("model,show_lines,expected", cases=".", glob="*")
def test_printed_model(model, show_lines, expected):
    """
    Test that model tree looks correct.
    """

    tree = get_model_tree(model)

    assert tree.to_string(show_lines=show_lines) == expected.replace("\n", os.linesep)
