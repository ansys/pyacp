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

"""
.. _solid_model_example:

Materials
=========

This example shows how to create and shape a solid model.

The solid model implements an extrusion algorithm which creates
a solid model based on the shell mesh and layup definition.
This solid model can be further processed by :class:`.ExtrusionGuide`,
:class:`.SnapToGeometry`, and :class:`.CutOffGeometry`.
"""
import os

# %%
# Import the standard library and third-party dependencies.
import pathlib
import tempfile

# %%
# Import the PyACP dependencies.
from ansys.acp.core import ACPWorkflow, launch_acp, SnapToGeometryOrientationType, Model, VirtualGeometry, CutOffGeometryOrientationType, ExtrusionGuideType, EdgeSetType
from ansys.acp.core.extras import ExampleKeys, get_example_file


# %%
# Load a minimal model
# ----------------------------
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_file = get_example_file(ExampleKeys.MINIMAL_FLAT_PLATE, WORKING_DIR)

# %%
# Launch the PyACP server and connect to it.
acp = launch_acp()

# %%
# Define the input file and instantiate an ``ACPWorkflow`` instance.
workflow = ACPWorkflow.from_acph5_file(
    acp=acp,
    acph5_file_path=input_file,
    local_working_directory=WORKING_DIR,
)

model = workflow.model

# %%
# Create a simple layup
# ---------------------
# %%
# Add more layers to the modeling ply so that it is easier to see the effects of the selection rules. Plot the thickness of all the plies without any rules.
modeling_ply = model.modeling_groups["modeling_group"].modeling_plies["ply"]
modeling_ply.number_of_layers = 3

# %%
# Create an initial solid model
# -----------------------------
#
# By default, the layup is extruded along the normal direction of the shell mesh.
solid_model = model.create_solid_model(
    name="Solid Model",
    element_sets=[model.element_sets["All_Elements"]],
)

model.update()
model.solid_mesh.to_pyvista().plot(show_edges=True)


def create_virtual_geometry_from_file(example_key: ExampleKeys) -> VirtualGeometry:
    geometry_file = get_example_file(example_key, WORKING_DIR)
    geometry_obj = workflow.add_cad_geometry_from_local_file(geometry_file)
    workflow.model.update()
    virtual_geometry = model.create_virtual_geometry(
        name="thickness_virtual_geometry", cad_components=geometry_obj.root_shapes.values()
    )
    return virtual_geometry


# %%
# Snap the top to a geometry
# --------------------------
#
# The :class:`.SnapToGeometry` allows to shape the bottom or top of the solid model.
# First, import the geometry and then add the snap-to feature to the solid model.
snap_to_virtual_geom = create_virtual_geometry_from_file(ExampleKeys.SNAP_TO_GEOMETRY)
solid_model.create_snap_to_geometry(
    name="Snap-to Geometry",
    cad_geometry=snap_to_virtual_geom,
    orientation_type=SnapToGeometryOrientationType.TOP,
    oriented_selection_set=model.oriented_selection_sets["oss"],
)

model.update()
model.solid_mesh.to_pyvista().plot(show_edges=True)

# %%
# Shape the walls
# ---------------
#
# The :class:`.ExtrusionGuide` is used to shape the side walls of the solid model.
# The feature can be defined by a direction as shown here or through a geometry.
edge_set = model.create_edge_set(
    name="Edge Set",
    edge_set_type=EdgeSetType.BY_REFERENCE,
    element_set=model.element_sets["All_Elements"],
    limit_angle=30,
    origin=(0.05, 0, 0),
)
solid_model.create_extrusion_guide(
    name="Extrusion Guide",
    edge_set=edge_set,
    extrusion_guide_type=ExtrusionGuideType.BY_DIRECTION,
    direction=(-0.5, 1, 0),
    radius=0.005,
    depth=0.6,
)
model.update()
model.solid_mesh.to_pyvista().plot(show_edges=True)

# %%
# Cut-off an edge
# ---------------
#
# The :class:`.CutOffGeometry` is used to crop elements from the solid model.
cutoff_virtual_geom = create_virtual_geometry_from_file(ExampleKeys.CUT_OFF_GEOMETRY_SOLID_MODEL)
solid_model.create_cut_off_geometry(
    name="Cut-off Geometry",
    cad_geometry=cutoff_virtual_geom,
    orientation_type=CutOffGeometryOrientationType.UP,
)

model.update()
model.solid_mesh.to_pyvista().plot(show_edges=True)
