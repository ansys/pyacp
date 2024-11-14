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

.. warning::

    The PyACP / PyMechanical integration is still experimental:

    - Only the 'remote' PyMechanical mode on Windows is supported.
    - Only one ACP solid model can be loaded into Mechanical.


"""

from concurrent.futures import ThreadPoolExecutor
import os
import pathlib
import textwrap

import ansys.acp.core as pyacp
from ansys.acp.core.mechanical_integration_helpers import (
    export_mesh_for_acp,
    import_acp_composite_definitions,
    import_acp_solid_model,
)
from ansys.dpf.composites.composite_model import CompositeModel
from ansys.dpf.composites.constants import FailureOutput
from ansys.dpf.composites.data_sources import (
    CompositeDefinitionFiles,
    ContinuousFiberCompositesFiles,
)
from ansys.dpf.composites.failure_criteria import CombinedFailureCriterion, MaxStrainCriterion
from ansys.dpf.composites.server_helpers import connect_to_or_start_server
import ansys.mechanical.core as pymechanical

"""
 Full composites workflow that uses 'remote' PyMechanical.
 See embedded_workflow.py for more comments.
"""
BATCH_MECHANICAL = True
COMPOSITE_DEFINITIONS_H5 = "ACPCompositeDefinitions.h5"
MATML_FILE = "materials.xml"
SOLID_MODEL_CDB_FILE = "SolidModel.cdb"
SOLID_MODEL_COMPOSITE_DEFINITIONS_H5 = "SolidModel.h5"
ACPH5_FILE = "model.acph5"


def setup_and_update_acp_model(acp: pyacp.ACP, output_path, mesh_path):
    """
    Setup basic ACP lay-up based on mesh in mesh_path, and export material and composite
    definition file to output_path.
    is_local specifies if ACP runs locally (True) or in a docker container.
    """

    if acp.is_remote:
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

    mat.strain_limits = (
        pyacp.material_property_sets.ConstantStrainLimits.from_orthotropic_constants(
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
        element_sets=[model.element_sets["All_Elements"]],
    )

    # %%
    # Update and Save the ACP model
    model.update()

    # To-do: Distinction probably not needed
    if acp.is_remote:
        export_path = pathlib.PurePosixPath(".")

    else:
        export_path = output_path

    model.save(export_path / ACPH5_FILE)
    model.export_shell_composite_definitions(export_path / COMPOSITE_DEFINITIONS_H5)
    model.export_materials(export_path / MATML_FILE)
    solid_model.export(export_path / SOLID_MODEL_CDB_FILE, format="ansys:cdb")
    solid_model.export(export_path / SOLID_MODEL_COMPOSITE_DEFINITIONS_H5, format="ansys:h5")

    for filename in [
        ACPH5_FILE,
        COMPOSITE_DEFINITIONS_H5,
        MATML_FILE,
        SOLID_MODEL_CDB_FILE,
        SOLID_MODEL_COMPOSITE_DEFINITIONS_H5,
    ]:
        acp.download_file(export_path / filename, output_path / filename)

    return model


def postprocess_results(
    rst_file, matml_file, composite_definitions_path, solid_composite_definitions_path=None
):
    """
    Basic failure criteria evaluation. The evaluation expects that a DPF docker container with
    the Composites plugin is running at port 50052.
    """
    # dpf_server = connect_to_or_start_server(ip="127.0.0.1", port=50052)
    dpf_server = connect_to_or_start_server()

    max_strain = MaxStrainCriterion()
    cfc = CombinedFailureCriterion(
        name="Combined Failure Criterion",
        failure_criteria=[max_strain],
    )

    if solid_composite_definitions_path is not None:
        solid_kwargs = {
            "solid": CompositeDefinitionFiles(definition=solid_composite_definitions_path),
        }
    composite_model = CompositeModel(
        composite_files=ContinuousFiberCompositesFiles(
            rst=rst_file,
            composite={
                "shell": CompositeDefinitionFiles(definition=composite_definitions_path),
                **solid_kwargs,
            },
            engineering_data=matml_file,
        ),
        server=dpf_server,
    )

    # Evaluate the failure criteria
    output_all_elements = composite_model.evaluate_failure_criteria(cfc)

    # Query and plot the results
    irf_field = output_all_elements.get_field({"failure_label": FailureOutput.FAILURE_VALUE})

    irf_field.plot()


# The following lines show how to start the PyMechanical container, currently disabled because
# a local instance is used.
# Run the Mechanical Docker container: docker run
# -e ANSYSLMD_LICENSE_FILE=1055@example@example.com -p 50054:10000 ghcr.io/ansys/mechanical:24.1.0
# mechanical = pymechanical.launch_mechanical(batch=False, port=50054, start_instance=False)

with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(pyacp.launch_acp),
        executor.submit(pymechanical.launch_mechanical, batch=BATCH_MECHANICAL),
        executor.submit(pymechanical.launch_mechanical, batch=BATCH_MECHANICAL),
    ]
    acp, mechanical1, mechanical2 = (fut.result() for fut in futures)

script_dir = pathlib.Path(__file__).resolve().parent

mesh_path = script_dir / "pymechanical" / "output" / "mesh.h5"
mesh_path.unlink(missing_ok=True)

geometry_file = script_dir / "pymechanical" / "geometry" / "flat_plate.agdb"
mechanical1.run_python_script(
    textwrap.dedent(
        f"""\
        geometry_import = Model.GeometryImportGroup.AddGeometryImport()

        import_format = Ansys.Mechanical.DataModel.Enums.GeometryImportPreference.Format.Automatic
        import_preferences = Ansys.ACT.Mechanical.Utilities.GeometryImportPreferences()
        import_preferences.ProcessNamedSelections = True
        import_preferences.ProcessCoordinateSystems = True

        geometry_file = {str(geometry_file)!r}
        geometry_import.Import(
            geometry_file,
            import_format,
            import_preferences
        )

        body = Model.Geometry.GetChildren(
            Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body, True
        )[0]
        body.Thickness = Quantity(0.001, "m")

        Model.Mesh.GenerateMesh()
        """
    )
)
export_mesh_for_acp(mechanical=mechanical1, path=mesh_path)
assert mesh_path.exists()
mechanical1.exit(force=True)


SETUP_FOLDER_NAME = "Setup"
output_path = pathlib.Path(mechanical2.project_directory) / SETUP_FOLDER_NAME
os.mkdir(output_path)

acp_model = setup_and_update_acp_model(acp, output_path, mesh_path)

assert (output_path / MATML_FILE).exists()
assert (output_path / COMPOSITE_DEFINITIONS_H5).exists()
assert (output_path / SOLID_MODEL_COMPOSITE_DEFINITIONS_H5).exists()

cdb_path = output_path / SOLID_MODEL_CDB_FILE
h5_path = output_path / SOLID_MODEL_COMPOSITE_DEFINITIONS_H5

with open(cdb_path, "r+", encoding="utf-8") as f:
    cdb_content = f.read()
    cdb_content = cdb_content.replace(",_ACP_", ",ACP_")
    f.seek(0)
    f.write(cdb_content)

# Import geometry, mesh, and named selections into Mechanical
import_acp_solid_model(mechanical=mechanical2, cdb_path=cdb_path)

# Import materials into Mechanical
mechanical2.run_python_script(f"Model.Materials.Import({str(output_path / MATML_FILE)!r})")

# Import plies into Mechanical
import_acp_composite_definitions(
    mechanical=mechanical2, path=output_path / SOLID_MODEL_COMPOSITE_DEFINITIONS_H5
)

# Set boundary condition and solve
mechanical2.run_python_script(
    textwrap.dedent(
        """\
        analysis = Model.AddStaticStructuralAnalysis()

        ns_by_name = {ns.Name: ns for ns in Model.NamedSelections.Children}

        fixed_support = analysis.AddFixedSupport()
        fixed_support.Location = ns_by_name["ACP_SOLIDMODEL_4_WALL"]

        force = analysis.AddForce()
        force.DefineBy = LoadDefineBy.Components
        force.XComponent.Output.SetDiscreteValue(0, Quantity(1e5, "N"))
        force.Location = ns_by_name["ACP_SOLIDMODEL_2_WALL"]

        analysis.Solve(True)
        """
    )
)

rst_file = [filename for filename in mechanical2.list_files() if filename.endswith(".rst")][0]
matml_out = [filename for filename in mechanical2.list_files() if filename.endswith("MatML.xml")][0]

postprocess_results(
    rst_file=rst_file,
    matml_file=matml_out,
    composite_definitions_path=output_path / COMPOSITE_DEFINITIONS_H5,
    solid_composite_definitions_path=output_path / SOLID_MODEL_COMPOSITE_DEFINITIONS_H5,
)
