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
.. _pymapdl_workflow_example:

PyMAPDL workflow
================

This example shows how to define a composite lay-up with PyACP, solve the resulting model with PyMAPDL, and
run a failure analysis with PyDPF Composites.
"""

# %%
# Description
# -----------
#
# In a basic PyACP workflow, you begin with an MAPDL DAT file containing the mesh, material data, and
# boundary conditions. For more information on creating input files, see :ref:`input_file_for_pyacp`.
# Then, you import the DAT file into PyACP to define the composite lay-up. Finally, you export the
# resulting model from PyACP to PyMAPDL. Once the results are available, the RST file is loaded in
# PyDPF Composites for analysis. The additional input files (``material.xml`` and
# ``ACPCompositeDefinitions.h5``) can also be stored with PyACP and passed to PyDPF Composites.

# %%
# Import modules
# --------------
#
# Import the standard library and third-party dependencies.
import pathlib
import tempfile

# %%
# Import the PyACP dependencies.
from ansys.acp.core import (
    PlyType,
    dpf_integration_helpers,
    get_directions_plotter,
    launch_acp,
    material_property_sets,
    print_model,
)
from ansys.acp.core.extras import ExampleKeys, get_example_file

# sphinx_gallery_thumbnail_number = 3


# %%
# Launch PyACP
# ------------
#
# Download the example input file.
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_DAT, WORKING_DIR)

# %%
# Launch the PyACP server and connect to it.
acp = launch_acp()

# %%
# Create an ACP workflow instance and load the model
# --------------------------------------------------
#
# Import the model from the input file.

model = acp.import_model(input_file, format="ansys:dat")
print(model.unit_system)

# %%
# Visualize the loaded mesh.
mesh = model.mesh.to_pyvista()
mesh.plot(show_edges=True)


# %%
# Define the composite lay-up
# ---------------------------
#
# Create an orthotropic material and fabric including strain limits, which are later
# used to postprocess the simulation.
engineering_constants = (
    material_property_sets.ConstantEngineeringConstants.from_orthotropic_constants(
        E1=5e10, E2=1e10, E3=1e10, nu12=0.28, nu13=0.28, nu23=0.3, G12=5e9, G23=4e9, G31=4e9
    )
)

strain_limit = 0.01
strain_limits = material_property_sets.ConstantStrainLimits.from_orthotropic_constants(
    eXc=-strain_limit,
    eYc=-strain_limit,
    eZc=-strain_limit,
    eXt=strain_limit,
    eYt=strain_limit,
    eZt=strain_limit,
    eSxy=strain_limit,
    eSyz=strain_limit,
    eSxz=strain_limit,
)

ud_material = model.create_material(
    name="UD",
    ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants,
    strain_limits=strain_limits,
)

fabric = model.create_fabric(name="UD", material=ud_material, thickness=0.1)


# %%
# Define a rosette and oriented selection set. Plot the orientation.
rosette = model.create_rosette(origin=(0.0, 0.0, 0.0), dir1=(1.0, 0.0, 0.0), dir2=(0.0, 0.0, 1.0))

oss = model.create_oriented_selection_set(
    name="oss",
    orientation_point=(0.0, 0.0, 0.0),
    orientation_direction=(0.0, 1.0, 0),
    element_sets=[model.element_sets["All_Elements"]],
    rosettes=[rosette],
)

model.update()

plotter = get_directions_plotter(model=model, components=[oss.elemental_data.orientation])
plotter.show()


# %%
# Create various plies with different angles and add them to a modeling group.
modeling_group = model.create_modeling_group(name="modeling_group")
angles = [0, 45, -45, 45, -45, 0]
for idx, angle in enumerate(angles):
    modeling_group.create_modeling_ply(
        name=f"ply_{idx}_{angle}_{fabric.name}",
        ply_angle=angle,
        ply_material=fabric,
        oriented_selection_sets=[oss],
    )

model.update()


# %%
# Show the fiber directions of a specific ply.
modeling_ply = model.modeling_groups["modeling_group"].modeling_plies["ply_4_-45_UD"]


fiber_direction = modeling_ply.elemental_data.fiber_direction
assert fiber_direction is not None
plotter = get_directions_plotter(
    model=model,
    components=[fiber_direction],
)

plotter.show()


# %%
# For a quick overview, print the model tree. Note that
# the model can also be opened in the ACP GUI. For more
# information, see :ref:`view_the_model_in_the_acp_gui`.
print_model(model)

# %%
# Solve the model with PyMAPDL
# ----------------------------
#
# Launch the PyMAPDL instance.
from ansys.mapdl.core import launch_mapdl

mapdl = launch_mapdl()
mapdl.clear()

# %%
# Load the CDB file into PyMAPDL.
analysis_model_path = WORKING_DIR / "analysis_model.cdb"
model.export_analysis_model(analysis_model_path)
mapdl.input(str(analysis_model_path))

# %%
# Solve the model.
mapdl.allsel()
mapdl.slashsolu()
mapdl.solve()

# %%
# Show the displacements in postprocessing.
mapdl.post1()
mapdl.set("last")
mapdl.post_processing.plot_nodal_displacement(component="NORM")

# %%
# Download the RST file for composite-specific postprocessing.
rstfile_name = f"{mapdl.jobname}.rst"
rst_file_local_path = WORKING_DIR / rstfile_name
mapdl.download(rstfile_name, str(WORKING_DIR))

# %%
# Postprocessing with PyDPF Composites
# ------------------------------------
#
# To postprocess the results, you must configure the imports, connect to the
# PyDPF Composites server, and load its plugin.

from ansys.dpf.composites.composite_model import CompositeModel
from ansys.dpf.composites.constants import FailureOutput
from ansys.dpf.composites.data_sources import (
    CompositeDefinitionFiles,
    ContinuousFiberCompositesFiles,
)
from ansys.dpf.composites.failure_criteria import CombinedFailureCriterion, MaxStrainCriterion
from ansys.dpf.composites.server_helpers import connect_to_or_start_server

# %%
# Connect to the server. The ``connect_to_or_start_server`` function
# automatically loads the composites plugin.
dpf_server = connect_to_or_start_server()

# %%
# Specify the combined failure criterion.
max_strain = MaxStrainCriterion()

cfc = CombinedFailureCriterion(
    name="Combined Failure Criterion",
    failure_criteria=[max_strain],
)

# %%
# Create the composite model and configure its input.
composite_definitions_file = WORKING_DIR / "ACPCompositeDefinitions.h5"
model.export_shell_composite_definitions(composite_definitions_file)
materials_file = WORKING_DIR / "materials.xml"
model.export_materials(materials_file)
composite_model = CompositeModel(
    composite_files=ContinuousFiberCompositesFiles(
        rst=rst_file_local_path,
        composite={"shell": CompositeDefinitionFiles(composite_definitions_file)},
        engineering_data=materials_file,
    ),
    default_unit_system=dpf_integration_helpers.get_dpf_unit_system(model.unit_system),
    server=dpf_server,
)

# %%
# Evaluate and plot the failure criteria.
output_all_elements = composite_model.evaluate_failure_criteria(cfc)
irf_field = output_all_elements.get_field({"failure_label": FailureOutput.FAILURE_VALUE})
irf_field.plot()

# %%
# Release the composite model to close the open streams to the result file.
composite_model = None  # type: ignore
