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

.. _pymechanical_shell_example:

PyMechanical shell workflow
===========================

This example shows how to set up a simple shell model with PyACP and
PyMechanical:

- The geometry is imported into Mechanical and meshed.
- The mesh is exported to ACP.
- A simple lay-up is defined in ACP.
- Plies and materials are exported from ACP, and imported into Mechanical.
- Boundary conditions are set in Mechanical.
- The model is solved.
- The results are post-processed in PyDPF Composites.

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
# Import PyACP, PyMechanical, and PyDPF Composites.

# isort: off
import ansys.acp.core as pyacp
import ansys.dpf.composites as pydpf_composites
import ansys.mechanical.core as pymechanical

# sphinx_gallery_thumbnail_path = '_static/gallery_thumbnails/sphx_glr_03-pymechanical-shell-workflow_thumb.png'

# %%
# Start the ACP, Mechanical, and DPF servers. We use a ``ThreadPoolExecutor``
# to start them in parallel.
with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(pymechanical.launch_mechanical, batch=True),
        executor.submit(pyacp.launch_acp),
        executor.submit(pydpf_composites.server_helpers.connect_to_or_start_server),
    ]
    mechanical, acp, dpf = (fut.result() for fut in futures)

# %%
# Get example input files
# -----------------------
#
# Create a temporary working directory, and download the example input files
# to this directory.

working_dir = tempfile.TemporaryDirectory()
working_dir_path = pathlib.Path(working_dir.name)
input_geometry = pyacp.extras.example_helpers.get_example_file(
    pyacp.extras.example_helpers.ExampleKeys.CLASS40_AGDB, working_dir_path
)

# %%
# Generate the mesh in PyMechanical
# ---------------------------------
#
# Load the geometry into Mechanical, generate the mesh, and export it to the
# appropriate transfer format for ACP.

mesh_path = working_dir_path / "mesh.h5"
mechanical.run_python_script(
    # This script runs in the Mechanical Python environment, which uses IronPython 2.7.
    textwrap.dedent(
        f"""\
        geometry_import = Model.GeometryImportGroup.AddGeometryImport()

        import_format = Ansys.Mechanical.DataModel.Enums.GeometryImportPreference.Format.Automatic
        import_preferences = Ansys.ACT.Mechanical.Utilities.GeometryImportPreferences()
        import_preferences.ProcessNamedSelections = True
        import_preferences.ProcessCoordinateSystems = True

        geometry_file = {str(input_geometry)!r}
        geometry_import.Import(
            geometry_file,
            import_format,
            import_preferences
        )

        for body in Model.Geometry.GetChildren(
            Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body, True
        ):
            body.Thickness = Quantity(1e-6, "m")

        Model.Mesh.GenerateMesh()
        """
    )
)
pyacp.mechanical_integration_helpers.export_mesh_for_acp(mechanical=mechanical, path=mesh_path)

# %%
# Set up the ACP model
# --------------------
#
# Setup basic ACP lay-up based on the mesh in ``mesh_path``, and export material and composite
# definition file to output_path.

composite_definitions_h5 = "ACPCompositeDefinitions.h5"
matml_file = "materials.xml"  # TODO: load an example materials XML file instead of defining the materials in ACP


model = acp.import_model(mesh_path, format="ansys:h5")

mat = model.create_material(name="mat")

mat.ply_type = "regular"
mat.engineering_constants.E1 = 1e12
mat.engineering_constants.E2 = 1e11
mat.engineering_constants.E3 = 1e11
mat.engineering_constants.G12 = 1e10
mat.engineering_constants.G23 = 1e10
mat.engineering_constants.G31 = 1e10
mat.engineering_constants.nu12 = 0.3
mat.engineering_constants.nu13 = 0.3
mat.engineering_constants.nu23 = 0.3

mat.strain_limits = pyacp.material_property_sets.ConstantStrainLimits.from_orthotropic_constants(
    eXc=-0.01,
    eYc=-0.01,
    eZc=-0.01,
    eXt=0.01,
    eYt=0.01,
    eZt=0.01,
    eSxy=0.01,
    eSyz=0.01,
    eSxz=0.01,
)

corecell_81kg_5mm = model.create_fabric(name="Corecell 81kg", thickness=0.005, material=mat)

ros = model.create_rosette(name="ros", origin=(0, 0, 0))

oss = model.create_oriented_selection_set(
    name="oss",
    orientation_point=(-0, 0, 0),
    orientation_direction=(0.0, 1, 0.0),
    element_sets=[model.element_sets["All_Elements"]],
    rosettes=[ros],
)

mg = model.create_modeling_group(name="group")
mg.create_modeling_ply(
    name="ply",
    ply_material=corecell_81kg_5mm,
    oriented_selection_sets=[oss],
    ply_angle=45,
    number_of_layers=1,
    global_ply_nr=0,  # add at the end
)
mg.create_modeling_ply(
    name="ply2",
    ply_material=corecell_81kg_5mm,
    oriented_selection_sets=[oss],
    ply_angle=0,
    number_of_layers=2,
    global_ply_nr=0,  # add at the end
)

# %%
# Update and Save the ACP model
# -----------------------------

model.update()

model.export_shell_composite_definitions(working_dir_path / composite_definitions_h5)
model.export_materials(working_dir_path / matml_file)

# %%
# Import materials and plies into Mechanical
# ------------------------------------------
#
# Import materials into Mechanical

mechanical.run_python_script(f"Model.Materials.Import({str(working_dir_path / matml_file)!r})")

# %%
# Import plies into Mechanical

pyacp.mechanical_integration_helpers.import_acp_composite_definitions(
    mechanical=mechanical,
    path=working_dir_path / composite_definitions_h5,
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
        front_edge.GenerationCriteria[0].Operator = SelectionOperatorType.GreaterThan
        front_edge.GenerationCriteria[0].Value = Quantity('-4.6 [m]')
        front_edge.Generate()

        back_edge = Model.AddNamedSelection()
        back_edge.Name = "Back Edge"
        back_edge.ScopingMethod = GeometryDefineByType.Worksheet

        back_edge.GenerationCriteria.Add(None)
        back_edge.GenerationCriteria[0].EntityType = SelectionType.GeoEdge
        back_edge.GenerationCriteria[0].Criterion = SelectionCriterionType.LocationX
        back_edge.GenerationCriteria[0].Operator = SelectionOperatorType.LessThan
        back_edge.GenerationCriteria[0].Value = Quantity('-7.8 [m]')
        back_edge.Generate()

        analysis = Model.AddStaticStructuralAnalysis()

        fixed_support = analysis.AddFixedSupport()
        fixed_support.Location = back_edge

        force = analysis.AddForce()
        force.DefineBy = LoadDefineBy.Components
        force.XComponent.Output.SetDiscreteValue(0, Quantity(1e6, "N"))
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
# Evaluate the failure criteria using the PyDPF Composites.


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
                definition=working_dir_path / composite_definitions_h5
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
