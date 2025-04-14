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

.. _pymechanical_to_cdb_example:

PyMechanical to CDB shell workflow
==================================

This example shows how to set up a workflow that uses PyMechanical to mesh the
geometry and define the load case, PyACP to define a layup, PyMAPDL to solve the
model, and PyDPF - Composites to post-process the results.

This workflow does *not* suffer from the limitations of the PyACP to
PyMechanical integration.

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
from ansys.acp.core.extras import set_plot_theme
import ansys.dpf.core as pydpf_core
import ansys.dpf.composites as pydpf_composites
import ansys.mapdl.core as pymapdl
import ansys.mechanical.core as pymechanical

# sphinx_gallery_thumbnail_path = '_static/gallery_thumbnails/sphx_glr_05-pymechanical-to-cdb-workflow_thumb.png'

# %%
# Set the plot theme for the example. This is optional, and ensures that you get the
# same plot style (theme, color map, etc.) as in the online documentation.
set_plot_theme()

# %%
# Start the ACP, Mechanical, and DPF servers. We use a ``ThreadPoolExecutor``
# to start them in parallel.
with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(pymechanical.launch_mechanical, batch=True),
        executor.submit(pyacp.launch_acp),
        executor.submit(pymapdl.launch_mapdl),
        executor.submit(pydpf_composites.server_helpers.connect_to_or_start_server),
    ]
    mechanical, acp, mapdl, dpf = (fut.result() for fut in futures)
    mapdl.clear()

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
# Load the geometry into Mechanical, generate the mesh, and define the
# load case.

cdb_path_initial = working_dir_path / "model_from_mechanical.cdb"
mechanical.run_python_script(
    # This script runs in the Mechanical Python environment, which uses IronPython 2.7.
    textwrap.dedent(
        f"""\
        # Import the geometry
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

        # The thickness will be overridden by the ACP model, but is required
        # for the model to be valid.
        for body in Model.Geometry.GetChildren(
            Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body, True
        ):
            body.Thickness = Quantity(1e-6, "m")

        Model.Mesh.GenerateMesh()

        # Define named selections at the front and back edges
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

        # Create a static structural analysis, and define the boundary
        # conditions (fixed support at the back edge, force at the front edge).
        analysis = Model.AddStaticStructuralAnalysis()

        fixed_support = analysis.AddFixedSupport()
        fixed_support.Location = back_edge

        force = analysis.AddForce()
        force.DefineBy = LoadDefineBy.Components
        force.XComponent.Output.SetDiscreteValue(0, Quantity(1e6, "N"))
        force.Location = front_edge

        # Export the model to a CDB file
        analysis.WriteInputFile({str(cdb_path_initial)!r})
        """
    )
)

# %%
# Set up the ACP model
# --------------------
#
# Setup basic ACP lay-up based on the CDB file.


model = acp.import_model(path=cdb_path_initial, format="ansys:cdb")

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

cdb_filename_out = "model_from_acp.cdb"
composite_definitions_h5_filename = "ACPCompositeDefinitions.h5"
matml_filename = "materials.xml"

model.export_analysis_model(working_dir_path / cdb_filename_out)
model.export_shell_composite_definitions(working_dir_path / composite_definitions_h5_filename)
model.export_materials(working_dir_path / matml_filename)

# %%
# Solve with PyMAPDL
# ------------------

mapdl.clear()
# %%
# Load the CDB file into PyMAPDL.
mapdl.input(str(working_dir_path / cdb_filename_out))

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
# Download the RST file for further postprocessing.
rstfile_name = f"{mapdl.jobname}.rst"
rst_file_local_path = working_dir_path / rstfile_name
mapdl.download(rstfile_name, working_dir_path)

# %%
# Postprocessing with PyDPF - Composites
# --------------------------------------
#
# Specify the combined failure criterion.
max_strain = pydpf_composites.failure_criteria.MaxStrainCriterion()

cfc = pydpf_composites.failure_criteria.CombinedFailureCriterion(
    name="Combined Failure Criterion",
    failure_criteria=[max_strain],
)

# %%
# Create the composite model and configure its input.
composite_model = pydpf_composites.composite_model.CompositeModel(
    composite_files=pydpf_composites.data_sources.ContinuousFiberCompositesFiles(
        rst=rst_file_local_path,
        composite={
            "shell": pydpf_composites.data_sources.CompositeDefinitionFiles(
                definition=working_dir_path / composite_definitions_h5_filename
            ),
        },
        engineering_data=working_dir_path / matml_filename,
    ),
    default_unit_system=pydpf_core.unit_system.unit_systems.solver_nmm,
    server=dpf,
)

# %%
# Evaluate the failure criteria.
output_all_elements = composite_model.evaluate_failure_criteria(cfc)

# %%
# Query and plot the results.
#
# Note that the maximum IRF is different when compared to :ref:`pymechanical_shell_example`
# because ACP sets the ``ERESX,NO`` option in the CDB file. This option disables interpolation
# of the results from the integration point to the nodes.

irf_field = output_all_elements.get_field(
    {"failure_label": pydpf_composites.constants.FailureOutput.FAILURE_VALUE}
)
irf_field.plot()

# Close MAPDL instance
mapdl.exit()
