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


"""

.. _cdb_to_pymechanical_example:

CDB to PyMechanical shell workflow
==================================

This example shows how to define a composite lay-up in PyACP based on a mesh
from a CDB file, import the model into PyMechanical for defining the load and
boundary conditions, and run a failure analysis with PyDPF - Composites.

.. warning::

    The PyACP / PyMechanical integration is still experimental. Refer to the
    :ref:`limitations section <limitations>` for more information.

"""


# %%
# Import modules and start the Ansys products
# -------------------------------------------


# %%
# Import the standard library and third-party dependencies.

from concurrent.futures import ThreadPoolExecutor
import pathlib
import tempfile
import textwrap

# %%
# Import PyACP, PyMechanical, and PyDPF - Composites.

# isort: off
import ansys.acp.core as pyacp
from ansys.acp.core.extras import example_helpers
import ansys.dpf.composites as pydpf_composites
import ansys.mechanical.core as pymechanical

# sphinx_gallery_thumbnail_path = '_static/gallery_thumbnails/sphx_glr_06-cdb-to-pymechanical-workflow_thumb.png'

# %%
# Start the ACP, Mechanical, and DPF servers. We use a ``ThreadPoolExecutor``
# to start them in parallel.
with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(pyacp.launch_acp),
        executor.submit(pymechanical.launch_mechanical, batch=True),
        executor.submit(pydpf_composites.server_helpers.connect_to_or_start_server),
    ]
    acp, mechanical, dpf = (fut.result() for fut in futures)

# %%
# Get example input files
# -----------------------
#
# Create a temporary working directory, and download the example input files
# to this directory.

working_dir = tempfile.TemporaryDirectory()
working_dir_path = pathlib.Path(working_dir.name)
input_file = example_helpers.get_example_file(
    example_helpers.ExampleKeys.BASIC_FLAT_PLATE_DAT, working_dir_path
)

# %%
# Set up the ACP model
# --------------------
#
# Setup basic ACP lay-up based on the CDB file.


model = acp.import_model(path=input_file, format="ansys:cdb")
model.unit_system

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
    pyacp.material_property_sets.ConstantEngineeringConstants.from_orthotropic_constants(
        E1=5e10, E2=1e10, E3=1e10, nu12=0.28, nu13=0.28, nu23=0.3, G12=5e9, G23=4e9, G31=4e9
    )
)

strain_limit = 0.01
strain_limits = pyacp.material_property_sets.ConstantStrainLimits.from_orthotropic_constants(
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
    ply_type=pyacp.PlyType.REGULAR,
    engineering_constants=engineering_constants,
    strain_limits=strain_limits,
)

fabric = model.create_fabric(name="UD", material=ud_material, thickness=1e-4)


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

plotter = pyacp.get_directions_plotter(model=model, components=[oss.elemental_data.orientation])
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
plotter = pyacp.get_directions_plotter(
    model=model,
    components=[fiber_direction],
)

plotter.show()


# %%
# For a quick overview, print the model tree. Note that
# the model can also be opened in the ACP GUI. For more
# information, see :ref:`view_the_model_in_the_acp_gui`.
pyacp.print_model(model)

# %%
# Save the ACP model
# ------------------

cdb_filename = "model.cdb"
composite_definitions_h5_filename = "ACPCompositeDefinitions.h5"
matml_filename = "materials.xml"

model.export_analysis_model(working_dir_path / cdb_filename)
model.export_shell_composite_definitions(working_dir_path / composite_definitions_h5_filename)
model.export_materials(working_dir_path / matml_filename)


# %%
# Import mesh, materials and plies into Mechanical
# ------------------------------------------------
#
# Import geometry, mesh, and named selections into Mechanical


pyacp.mechanical_integration_helpers.import_acp_mesh_from_cdb(
    mechanical=mechanical, cdb_path=working_dir_path / cdb_filename
)


# %%
# Import materials into Mechanical

mechanical.run_python_script(f"Model.Materials.Import({str(working_dir_path / matml_filename)!r})")

# %%
# Import plies into Mechanical

pyacp.mechanical_integration_helpers.import_acp_composite_definitions(
    mechanical=mechanical, path=working_dir_path / composite_definitions_h5_filename
)

# %%
# Set boundary condition and solve
# ---------------------------------
#

mechanical.run_python_script(
    textwrap.dedent(
        """\
        front_edge = Model.AddNamedSelection()
        front_edge.Name = "Front Edge"
        front_edge.ScopingMethod = GeometryDefineByType.Worksheet

        front_edge.GenerationCriteria.Add(None)
        front_edge.GenerationCriteria[0].EntityType = SelectionType.GeoEdge
        front_edge.GenerationCriteria[0].Criterion = SelectionCriterionType.LocationX
        front_edge.GenerationCriteria[0].Operator = SelectionOperatorType.Largest
        front_edge.Generate()

        back_edge = Model.AddNamedSelection()
        back_edge.Name = "Back Edge"
        back_edge.ScopingMethod = GeometryDefineByType.Worksheet

        back_edge.GenerationCriteria.Add(None)
        back_edge.GenerationCriteria[0].EntityType = SelectionType.GeoEdge
        back_edge.GenerationCriteria[0].Criterion = SelectionCriterionType.LocationX
        back_edge.GenerationCriteria[0].Operator = SelectionOperatorType.Smallest
        back_edge.Generate()

        analysis = Model.AddStaticStructuralAnalysis()

        fixed_support = analysis.AddFixedSupport()
        fixed_support.Location = back_edge

        force = analysis.AddForce()
        force.DefineBy = LoadDefineBy.Components
        force.XComponent.Output.SetDiscreteValue(0, Quantity(100, "N"))
        force.Location = front_edge

        analysis.Solution.Solve(True)
        """
    )
)


rst_file = [filename for filename in mechanical.list_files() if filename.endswith(".rst")][0]
matml_out = [filename for filename in mechanical.list_files() if filename.endswith("MatML.xml")][0]

# %%
# Postprocess results
# -------------------
#
# Evaluate the failure criteria using the PyDPF - Composites.


max_strain = pydpf_composites.failure_criteria.MaxStrainCriterion()
cfc = pydpf_composites.failure_criteria.CombinedFailureCriterion(
    name="Combined Failure Criterion",
    failure_criteria=[max_strain],
)

composite_model = pydpf_composites.composite_model.CompositeModel(
    composite_files=pydpf_composites.data_sources.ContinuousFiberCompositesFiles(
        rst=rst_file,
        composite={
            "shell": pydpf_composites.data_sources.CompositeDefinitionFiles(
                definition=working_dir_path / composite_definitions_h5_filename
            ),
        },
        engineering_data=working_dir_path / matml_out,
    ),
    server=dpf,
)

# Evaluate the failure criteria
output_all_elements = composite_model.evaluate_failure_criteria(cfc)

# Query and plot the results
irf_field = output_all_elements.get_field(
    {"failure_label": pydpf_composites.constants.FailureOutput.FAILURE_VALUE}
)

irf_field.plot()
