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
.. _sensor_example:

Sensor
======

The :class:`.Sensor` capabilities to analyze the composite structure
is demonstrated in this example. A sensor is used to compute the weight,
area, cost, etc. of the model or specific entities such as ply material,
modeling ply, etc.
"""

# %%
# Import modules
# --------------
#
# Import the standard library and third-party dependencies.
import pathlib
import tempfile

import pyvista

# %%
# Import the PyACP dependencies.
from ansys.acp.core import SensorType, UnitSystemType, launch_acp
from ansys.acp.core.extras import RACE_CARE_NOSE_CAMERA_METER, ExampleKeys, get_example_file

# sphinx_gallery_thumbnail_number = 2


# %%
# Start ACP and load the model
# ----------------------------

# %%
# Get the example file from the server.
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
acph5_input_file = get_example_file(ExampleKeys.RACE_CAR_NOSE_ACPH5, WORKING_DIR)

# %%
# Launch the PyACP server and connect to it.
acp = launch_acp()

# %%
# Load the model from the input file which contains
# a formula 1 front wing with layup. The plot shows the total
# laminate thickness per element.
model = acp.import_model(acph5_input_file)
model.unit_system = UnitSystemType.SI
print(model.unit_system)
model.update()

thickness_data = model.elemental_data.thickness
if thickness_data is not None:
    plotter = pyvista.Plotter()
    plotter.add_mesh(thickness_data.get_pyvista_mesh(model.mesh), show_edges=False)
    plotter.camera_position = RACE_CARE_NOSE_CAMERA_METER
    plotter.show()

# %%
# Set price per area for all fabrics.
model.fabrics["UD"].area_price = 15  # $/m^2
model.fabrics["woven"].area_price = 23  # $/m^2
model.fabrics["core_4mm"].area_price = 7  # $/m^2

# %%
# Sensor by area
# --------------

# %%
# Entire Model
# ~~~~~~~~~~~~
# The first sensor is applied to the entire model to compute for example
# the total weight, area of production material, and material cost.
sensor_by_area = model.create_sensor(
    name="By Area",
    sensor_type=SensorType.SENSOR_BY_AREA,
    entities=[model.element_sets["All_Elements"]],
)
# %%
# Update the model to compute the sensor values.
model.update()


def print_measures(my_sensor):
    print(f"Price: {my_sensor.price:.2f} $")
    print(f"Weight: {my_sensor.weight:.2f} kg")
    print(f"Covered area: {my_sensor.covered_area:.2f} m²")
    print(f"Production ply area: {my_sensor.production_ply_area:.2f} m²")
    cog = my_sensor.center_of_gravity
    print(f"Center of gravity: ({cog[0]:.2f}, {cog[1]:.2f}, {cog[2]:.2f}) m")


# %%
# Print the values. The ``production ply area`` is the area of production material.
print_measures(sensor_by_area)

# %%
# Scope to a specific component
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Compute the measures for the nose only. Note that :class:`.OrientedSelectionSet`
# can also be used to scope the sensor.
eset_nose = model.element_sets["els_nose"]
sensor_by_area.entities = [eset_nose]
model.update()
print_measures(sensor_by_area)
plotter = pyvista.Plotter()
plotter.add_mesh(eset_nose.mesh.to_pyvista(), show_edges=False, opacity=1, color="turquoise")
plotter.add_mesh(model.mesh.to_pyvista(), show_edges=False, opacity=0.2)
plotter.camera_position = RACE_CARE_NOSE_CAMERA_METER
plotter.show()

# %%
# Sensor by material
# ------------------
#
# A sensor can also be used to compute the amount of a certain ply material
# (:class:`.Fabric`, :class:`.Stackup`, :class:`.SubLaminate`).
sensor_by_material = model.create_sensor(
    name="By Material",
    sensor_type=SensorType.SENSOR_BY_MATERIAL,
    entities=[model.fabrics["UD"]],
)
print_measures(sensor_by_area)

# %%
# Sensor by ply
# -------------
#
# A sensor can also be scoped to a specific ply or a list of plies. In this example,
# a ply of the suction side and a ply of the pressure side of wing 3 are selected.
mg = model.modeling_groups["wing_3"]
modeling_plies = [
    mg.modeling_plies["mp.wing_3.1_suction"],
    mg.modeling_plies["mp.wing_3.1_pressure.2"],
]
sensor_by_ply = model.create_sensor(
    name="By Ply",
    sensor_type=SensorType.SENSOR_BY_PLIES,
    entities=modeling_plies,
)
model.update()
print_measures(sensor_by_ply)
plotter = pyvista.Plotter()
for ply in modeling_plies:
    plotter.add_mesh(ply.mesh.to_pyvista(), show_edges=False, opacity=1, color="turquoise")
plotter.add_mesh(model.mesh.to_pyvista(), show_edges=False, opacity=0.2)
plotter.camera_position = RACE_CARE_NOSE_CAMERA_METER
plotter.show()
