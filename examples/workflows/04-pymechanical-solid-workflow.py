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

.. _pymechanical_solid_example:

PyMechanical solid workflow
===========================

This example shows how to set up a simple solid model with PyACP and
PyMechanical:

- The geometry is imported into Mechanical and meshed.
- The mesh is exported to ACP.
- A simple lay-up and solid model is defined in ACP.
- The solid model is exported, to a CDB file and a composite definition file.
- In a separate Mechanical instance, the solid model is imported.
- Materials and plies are imported.
- Boundary conditions are set.
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

# sphinx_gallery_thumbnail_path = '_static/gallery_thumbnails/sphx_glr_04-pymechanical-solid-workflow_thumb.png'

# %%
# Start the ACP, Mechanical, and DPF servers. We use a ``ThreadPoolExecutor``
# to start them in parallel.
with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(pymechanical.launch_mechanical, batch=True),
        executor.submit(pymechanical.launch_mechanical, batch=True),
        executor.submit(pyacp.launch_acp),
        executor.submit(pydpf_composites.server_helpers.connect_to_or_start_server),
    ]
    mechanical_shell_geometry, mechanical_solid_model, acp, dpf = (fut.result() for fut in futures)

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
mechanical_shell_geometry.run_python_script(
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

        hull = Model.AddNamedSelection()
        hull.Name = "hull"
        hull.ScopingMethod = GeometryDefineByType.Worksheet
        # Add all faces with Z location < 0.9 m
        hull.GenerationCriteria.Add(None)
        hull.GenerationCriteria[0].EntityType = SelectionType.GeoFace
        hull.GenerationCriteria[0].Operator = SelectionOperatorType.LessThan
        hull.GenerationCriteria[0].Criterion = SelectionCriterionType.LocationZ
        hull.GenerationCriteria[0].Value = Quantity('0.9 [m]')
        # Remove keeltower
        hull.GenerationCriteria.Add(None)
        hull.GenerationCriteria[1].Action = SelectionActionType.Remove
        hull.GenerationCriteria[1].Criterion = SelectionCriterionType.LocationX
        hull.GenerationCriteria[1].Operator = SelectionOperatorType.RangeInclude
        hull.GenerationCriteria[1].LowerBound = Quantity('-6.7 [m]')
        hull.GenerationCriteria[1].UpperBound = Quantity('-5.9 [m]')
        # Add back keeltower bottom
        hull.GenerationCriteria.Add(None)
        hull.GenerationCriteria[2].Criterion = SelectionCriterionType.LocationZ
        hull.GenerationCriteria[2].Operator = SelectionOperatorType.LessThan
        hull.GenerationCriteria[2].Value = Quantity('-0.25 [m]')
        # Remove bulkhead
        hull.GenerationCriteria.Add(None)
        hull.GenerationCriteria[3].Action = SelectionActionType.Remove
        hull.GenerationCriteria[3].Criterion = SelectionCriterionType.LocationX
        hull.GenerationCriteria[3].Operator = SelectionOperatorType.RangeInclude
        hull.GenerationCriteria[3].LowerBound = Quantity('-5.7 [m]')
        hull.GenerationCriteria[3].UpperBound = Quantity('-5.6 [m]')
        hull.Generate()

        Model.Mesh.GenerateMesh()
        """
    )
)
pyacp.mechanical_integration_helpers.export_mesh_for_acp(
    mechanical=mechanical_shell_geometry, path=mesh_path
)


# %%
# Set up the ACP model
# --------------------
#
# Setup basic ACP lay-up based on the mesh in ``mesh_path``, and export the following
# files to ``output_path``:
#
# - Materials XML file
# - Composite definitions HDF5 file
# - Solid model composite definitions HDF5 file
# - Solid model CDB file

matml_file = "materials.xml"  # TODO: load an example materials XML file instead of defining the materials in ACP
solid_model_cdb_file = "SolidModel.cdb"
solid_model_composite_definitions_h5 = "SolidModel.h5"


mesh_path = acp.upload_file(mesh_path)

model = acp.import_model(path=mesh_path, format="ansys:h5")

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

solid_model = model.create_solid_model(
    element_sets=[model.element_sets["hull"]],
)

# %%
# Update and Save the ACP model
# -----------------------------

model.update()

if acp.is_remote:
    export_path = pathlib.PurePosixPath(".")

else:
    export_path = working_dir_path  # type: ignore

model.export_materials(export_path / matml_file)
solid_model.export(export_path / solid_model_cdb_file, format="ansys:cdb")
solid_model.export(export_path / solid_model_composite_definitions_h5, format="ansys:h5")

for filename in [
    matml_file,
    solid_model_cdb_file,
    solid_model_composite_definitions_h5,
]:
    acp.download_file(export_path / filename, working_dir_path / filename)


# %%
# Import mesh, materials and plies into Mechanical
# ------------------------------------------------
#
# Import geometry, mesh, and named selections into Mechanical

pyacp.mechanical_integration_helpers.import_acp_solid_mesh(
    mechanical=mechanical_solid_model, cdb_path=working_dir_path / solid_model_cdb_file
)


# %%
# Import materials into Mechanical

mechanical_solid_model.run_python_script(
    f"Model.Materials.Import({str(working_dir_path / matml_file)!r})"
)

# %%
# Import plies into Mechanical

pyacp.mechanical_integration_helpers.import_acp_composite_definitions(
    mechanical=mechanical_solid_model, path=working_dir_path / solid_model_composite_definitions_h5
)


# %%
# Set boundary condition and solve
# ---------------------------------
#
# Set boundary condition and solve

mechanical_solid_model.run_python_script(
    textwrap.dedent(
        """\
        analysis = Model.AddStaticStructuralAnalysis()

        front_face = Model.AddNamedSelection()
        front_face.Name = "front_face"
        front_face.ScopingMethod = GeometryDefineByType.Worksheet
        front_face.GenerationCriteria.Add(None)
        front_face.GenerationCriteria[0].EntityType = SelectionType.GeoFace
        front_face.GenerationCriteria[0].Criterion = SelectionCriterionType.LocationX
        front_face.GenerationCriteria[0].Operator = SelectionOperatorType.Largest
        front_face.Generate()

        back_face = Model.AddNamedSelection()
        back_face.Name = "back_face"
        back_face.ScopingMethod = GeometryDefineByType.Worksheet
        back_face.GenerationCriteria.Add(None)
        back_face.GenerationCriteria[0].EntityType = SelectionType.GeoFace
        back_face.GenerationCriteria[0].Criterion = SelectionCriterionType.LocationX
        back_face.GenerationCriteria[0].Operator = SelectionOperatorType.Smallest
        back_face.Generate()

        fixed_support = analysis.AddFixedSupport()
        fixed_support.Location = back_face

        force = analysis.AddForce()
        force.DefineBy = LoadDefineBy.Components
        force.XComponent.Output.SetDiscreteValue(0, Quantity(1e5, "N"))
        force.Location = front_face

        analysis.Solve(True)
        """
    )
)

rst_file = [
    filename for filename in mechanical_solid_model.list_files() if filename.endswith(".rst")
][0]
matml_out = [
    filename for filename in mechanical_solid_model.list_files() if filename.endswith("MatML.xml")
][0]

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
            "solid": pydpf_composites.data_sources.CompositeDefinitionFiles(
                definition=working_dir_path / solid_model_composite_definitions_h5
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
