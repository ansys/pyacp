from constants import COMPOSITE_DEFINITIONS_H5, MATML_FILE

import ansys.acp.core as pyacp
from ansys.acp.core._tree_objects.material.property_sets import ConstantStrainLimits


def setup_and_update_acp_model(output_path, mesh_path, is_local=False):
    """
    Setup basic ACP layup based on mesh in mesh_path and export material and composite
    definition file to output_path.
    is_local specifies if ACP runs locally (True) or in a docker container.
    """
    pyacp_server = pyacp.launch_acp()
    pyacp_server.wait(timeout=30)
    pyacp_client = pyacp.Client(pyacp_server)

    if not is_local:
        mesh_path = pyacp_client.upload_file(mesh_path)

    model = pyacp_client.import_model(path=mesh_path, format="ansys:h5")

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

    mat.strain_limits = ConstantStrainLimits(
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
    model.update()

    # Todo: Distinction probably not needed
    if is_local:
        model.export_shell_composite_definitions(output_path / COMPOSITE_DEFINITIONS_H5)
        model.export_materials(output_path / MATML_FILE)
    else:
        model.export_shell_composite_definitions(COMPOSITE_DEFINITIONS_H5)
        model.export_materials(MATML_FILE)
        pyacp_client.download_file(COMPOSITE_DEFINITIONS_H5, output_path / COMPOSITE_DEFINITIONS_H5)
        pyacp_client.download_file(MATML_FILE, output_path / MATML_FILE)

    return model
