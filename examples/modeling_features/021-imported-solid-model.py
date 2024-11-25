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
.. _imported_solid_model_example:

Imported Solid model
====================

This example guides you through the definition of an :class:`.ImportedSolidModel`
which allows to map the layup onto an external solid mesh.
In contrast to the :class:`.SolidModel`, the raw solid mesh of
:class:`.ImportedSolidModel` is loaded from an external source, such as a CDB file.
In this example, the layup is applied onto a t-joint which consists of different
parts such as shell, stringer, and bonding skins.
The example only shows the PyACP part of the setup. For a complete composite analysis,
see :ref:`pymapdl_workflow_example`.

This example starts from an ACP model with layup. It shows how to:

- Create an :class:`.ImportedSolidModel` from an external mesh.
- Define the :class:`.LayupMappingObject` to apply the layup onto the solid mesh.
- Scope plies to specific parts of the solid mesh.
- Visualize the mapped layup.

It is recommended to look at the Ansys help for all the details. This example shows the
basic setup only.
"""

# %%
# Import the standard library and third-party dependencies.
import pathlib
import tempfile

import pyvista

# %%
# Import the PyACP dependencies.
from ansys.acp.core import (
    ACPWorkflow,
    ElementTechnology,
    LayupMappingRosetteSelectionMethod,
    launch_acp,
)
from ansys.acp.core.extras import ExampleKeys, get_example_file

# sphinx_gallery_thumbnail_number = 3


# %%
# Start ACP and load the model
# ----------------------------
# %%
# Get the example file from the server.
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_file = get_example_file(ExampleKeys.IMPORTED_SOLID_MODEL_ACPH5, WORKING_DIR)

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
# Import external solid model
# ---------------------------
#
# Get the solid mesh file and create an ImportedSolidModel and
# load the initial mesh.

solid_mesh_file = get_example_file(ExampleKeys.IMPORTED_SOLID_MODEL_SOLID_MESH, WORKING_DIR)
imported_solid_model = model.create_imported_solid_model(
    name="Imported Solid Model",
    external_path=solid_mesh_file,
    format="ansys:h5",
)

# Load the initial mesh and show the raw mesh without any mapping.
imported_solid_model.refresh()
imported_solid_model.import_initial_mesh()
model.solid_mesh.to_pyvista().plot(show_edges=True)

# %%
# The solid element sets can be used as target for the mapping.
print(imported_solid_model.solid_element_sets)

# %%
# Add mapping objects
# -------------------
#
# Link the layup (plies) of the top skin of the sandwich
# with the corresponding named selections of the solid mesh
# and show the updated solid model.
solid_esets = imported_solid_model.solid_element_sets

_ = imported_solid_model.create_layup_mapping_object(
    name="sandwich skin top",
    element_technology=ElementTechnology.LAYERED_ELEMENT,
    shell_element_sets=[model.element_sets["els_sandwich_skin_top"]],
    entire_solid_mesh=False,
    solid_element_sets=[solid_esets["mapping_target sandwich skin top"]],
)

model.update()
model.solid_mesh.to_pyvista().plot(show_edges=True)

# %%
# Add other mapping objects
_ = imported_solid_model.create_layup_mapping_object(
    name="sandwich skin bottom",
    element_technology=ElementTechnology.LAYERED_ELEMENT,
    shell_element_sets=[model.element_sets["els_sandwich_skin_bottom"]],
    entire_solid_mesh=False,
    solid_element_sets=[
        imported_solid_model.solid_element_sets["mapping_target sandwich skin bottom"]
    ],
)

_ = imported_solid_model.create_layup_mapping_object(
    name="stringer",
    element_technology=ElementTechnology.LAYERED_ELEMENT,
    shell_element_sets=[model.element_sets["els_stringer_skin_left"]],
    entire_solid_mesh=False,
    solid_element_sets=[
        solid_esets[v]
        for v in [
            "mapping_target stringer honeycomb",
            "mapping_target stringer skin left",
            "mapping_target stringer skin right",
        ]
    ],
)

_ = imported_solid_model.create_layup_mapping_object(
    name="bonding skin",
    element_technology=ElementTechnology.LAYERED_ELEMENT,
    shell_element_sets=[
        model.element_sets[v] for v in ["els_bonding_skin_left", "els_bonding_skin_right"]
    ],
    entire_solid_mesh=False,
    solid_element_sets=[
        solid_esets[v]
        for v in ["mapping_target bonding skin left", "mapping_target bonding skin right"]
    ],
)

# %%
# Show intermediate result
model.update()
model.solid_mesh.to_pyvista().plot(show_edges=True)

# %%
# The mapping can also be done for specific plies
# as shown for the core materials.
_ = imported_solid_model.create_layup_mapping_object(
    name="foam",
    element_technology=ElementTechnology.LAYERED_ELEMENT,
    shell_element_sets=[
        model.element_sets[v] for v in ["els_foam_core_left", "els_foam_core_right"]
    ],
    select_all_plies=False,
    sequences=[model.modeling_groups["MG foam_core"]],
    entire_solid_mesh=False,
    solid_element_sets=[solid_esets["mapping_target foam core"]],
    delete_lost_elements=False,
    filler_material=model.materials["SAN Foam (81 kg m^-3)"],
    rosettes=[model.rosettes["Global Coordinate System"]],
    rosette_selection_method=LayupMappingRosetteSelectionMethod.MINIMUM_DISTANCE,
)

_ = imported_solid_model.create_layup_mapping_object(
    name="honeycomb",
    element_technology=ElementTechnology.LAYERED_ELEMENT,
    shell_element_sets=[
        model.element_sets[v] for v in ["els_honeycomb_left", "els_honeycomb_right"]
    ],
    select_all_plies=False,
    sequences=[model.modeling_groups["MG honeycomb_core"]],
    entire_solid_mesh=False,
    solid_element_sets=[solid_esets["mapping_target sandwich honeycomb"]],
    delete_lost_elements=False,
    filler_material=model.materials["Honeycomb"],
    rosettes=[model.rosettes["Global Coordinate System"]],
    rosette_selection_method=LayupMappingRosetteSelectionMethod.MINIMUM_DISTANCE,
)
model.update()
model.solid_mesh.to_pyvista().plot(show_edges=True)

# %%
# Add filler mapping objects where the solid mesh is "filled"
# with a single material. No plies from the layup are used here.

_ = imported_solid_model.create_layup_mapping_object(
    name="resin",
    element_technology=ElementTechnology.LAYERED_ELEMENT,
    shell_element_sets=[],
    entire_solid_mesh=False,
    solid_element_sets=[
        solid_esets[v] for v in ["mapping_target adhesive", "mapping_target adhesive stringer root"]
    ],
    delete_lost_elements=False,
    filler_material=model.materials["Resin Epoxy"],
    rosettes=[model.rosettes["Global Coordinate System"]],
    rosette_selection_method=LayupMappingRosetteSelectionMethod.MINIMUM_DISTANCE,
)

# %%
# Show final solid mesh with mapped layup
model.update()
model.solid_mesh.to_pyvista().plot(show_edges=True)


# %%
# Show extent and thickness of mapped plies
# -----------------------------------------
#
# Use :meth:`.print_model` to get the list of plies.
ap = (
    model.modeling_groups["MG bonding_skin_right"]
    .modeling_plies["ModelingPly.26"]
    .production_plies["ProductionPly.33"]
    .analysis_plies["P1L1__ModelingPly.26"]
)
thickness_data = ap.elemental_data.thickness
thickness_pyvista_mesh = thickness_data.get_pyvista_mesh(mesh=ap.solid_mesh)  # type: ignore
plotter = pyvista.Plotter()
plotter.add_mesh(thickness_pyvista_mesh)
plotter.add_mesh(model.solid_mesh.to_pyvista(), opacity=0.2, show_edges=True)
plotter.show()


# %%
# Other features
# --------------
#
# The :class:`.CutOffGeometry` can be used in combination witt the :class:`.ImportedSolidModel`
# as well. See example :ref:`solid_model_example` for more details.
# More plotting capabilities are shown in the example :ref:`solid_model_example` as well.
#
# The solid mesh can be exported as CDB for MAPDL or to PyMechanical for further analysis.
# These workflows are shown in :ref:`pymapdl_workflow_example` and
# :ref:`pymechanical_solid_example`.
