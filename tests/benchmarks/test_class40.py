import pytest

import ansys.acp.core as pyacp
from ansys.acp.core import Fabric, ModelingGroup, ModelingPly, OrientedSelectionSet, Rosette

from ..conftest import SOURCE_ROOT_DIR


@pytest.mark.benchmark(
    min_rounds=1,
)
def test_class40(benchmark, grpc_server):
    """Benchmark for creating a composite lay-up for the Class40 model."""
    pyacp_client = pyacp.Client(grpc_server)
    benchmark(create_class40, pyacp_client)


def create_class40(pyacp_client):
    """
    Create a composite lay-up for the Class40 model.
    """
    examples_data_dir = SOURCE_ROOT_DIR / "examples" / "data" / "class40"

    cdb_file_path = pyacp_client.upload_file(local_path=str(examples_data_dir / "class40.cdb"))

    model = pyacp_client.import_model(
        path=cdb_file_path, format="ansys:cdb", unit_system=pyacp.UnitSystemType.MPA
    )

    # Materials
    mat_corecell_81kg = model.materials["1"]
    mat_corecell_81kg.name = "Core Cell 81kg"
    mat_corecell_81kg.ply_type = "isotropic_homogeneous_core"

    mat_corecell_103kg = model.materials["2"]
    mat_corecell_103kg.name = "Core Cell 103kg"
    mat_corecell_103kg.ply_type = "isotropic_homogeneous_core"

    mat_eglass_ud = model.materials["3"]
    mat_eglass_ud.name = "E-Glass (uni-directional)"
    mat_eglass_ud.ply_type = "regular"

    # Fabrics
    corecell_81kg_5mm = Fabric(name="Corecell 81kg", thickness=0.005, material=mat_corecell_81kg)
    model.add_fabric(corecell_81kg_5mm)
    corecell_103kg_10mm = Fabric(name="Corecell 103kg", thickness=0.01, material=mat_corecell_103kg)
    model.add_fabric(corecell_103kg_10mm)
    eglass_ud_02mm = Fabric(name="eglass UD", thickness=0.0002, material=mat_eglass_ud)
    model.add_fabric(eglass_ud_02mm)

    # Rosettes
    ros_deck = Rosette(name="ros_deck", origin=(-5.9334, -0.0481, 1.693))
    model.add_rosette(ros_deck)
    ros_hull = Rosette(name="ros_hull", origin=(-5.3711, -0.0506, -0.2551))
    model.add_rosette(ros_hull)
    ros_bulkhead = Rosette(
        name="ros_bulkhead",
        origin=(-5.622, 0.0022, 0.0847),
        dir1=(0.0, 1.0, 0.0),
        dir2=(0.0, 0.0, 1.0),
    )
    model.add_rosette(ros_bulkhead)
    ros_keeltower = Rosette(
        name="ros_keeltower", origin=(-6.0699, -0.0502, 0.623), dir1=(0.0, 0.0, 1.0)
    )
    model.add_rosette(ros_keeltower)

    # Element Sets
    esets = [
        model.element_sets["KEELTOWER_AFT"],
        model.element_sets["KEELTOWER_FRONT"],
        model.element_sets["KEELTOWER_PORT"],
        model.element_sets["KEELTOWER_STB"],
    ]

    # Oriented Selection Sets
    model.add_oriented_selection_set(
        OrientedSelectionSet(
            name="oss_deck",
            orientation_point=(-5.3806, -0.0016, 1.6449),
            orientation_direction=(0.0, 0.0, -1.0),
            element_sets=[model.element_sets["DECK"]],
            rosettes=[ros_deck],
        )
    )
    model.add_oriented_selection_set(
        OrientedSelectionSet(
            name="oss_hull",
            orientation_point=(-5.12, 0.1949, -0.2487),
            orientation_direction=(0.0, 0.0, 1.0),
            element_sets=[model.element_sets["HULL_ALL"]],
            rosettes=[ros_hull],
        )
    )
    model.add_oriented_selection_set(
        OrientedSelectionSet(
            name="oss_bulkhead",
            orientation_point=(-5.622, -0.0465, -0.094),
            orientation_direction=(1.0, 0.0, 0.0),
            element_sets=[model.element_sets["BULKHEAD_ALL"]],
            rosettes=[ros_bulkhead],
        )
    )
    model.add_oriented_selection_set(
        OrientedSelectionSet(
            name="oss_keeltower",
            orientation_point=(-6.1019, 0.0001, 1.162),
            orientation_direction=(-1.0, 0.0, 0.0),
            element_sets=esets,
            rosettes=[ros_keeltower],
        )
    )

    # Modeling Plies

    # Define plies for the HULL, DECK and BULKHEAD
    angles = [-90.0, -60.0, -45.0 - 30.0, 0.0, 0.0, 30.0, 45.0, 60.0, 90.0]
    for mg_name in ["hull", "deck", "bulkhead"]:
        mg = ModelingGroup(name=mg_name)
        model.add_modeling_group(mg)
        oss_list = [model.oriented_selection_sets["oss_" + mg_name]]
        for angle in angles:
            add_ply(mg, "eglass_ud_02mm_" + str(angle), eglass_ud_02mm, angle, oss_list)
        add_ply(mg, "corecell_103kg_10mm", corecell_103kg_10mm, 0.0, oss_list)
        for angle in angles:
            add_ply(mg, "eglass_ud_02mm_" + str(angle), eglass_ud_02mm, angle, oss_list)

    # Add plies to the keeltower
    mg = ModelingGroup(name="keeltower")
    model.add_modeling_group(mg)
    oss_list = [model.oriented_selection_sets["oss_keeltower"]]
    for angle in angles:
        add_ply(mg, "eglass_ud_02mm_" + str(angle), eglass_ud_02mm, angle, oss_list)

    add_ply(mg, "corecell_81kg_5mm", corecell_81kg_5mm, 0.0, oss_list)

    for angle in angles:
        add_ply(mg, "eglass_ud_02mm_" + str(angle), eglass_ud_02mm, angle, oss_list)

    pyacp_client.clear()


def add_ply(mg, name, ply_material, angle, oss):
    ply = ModelingPly(
        name=name,
        ply_material=ply_material,
        oriented_selection_sets=oss,
        ply_angle=angle,
        number_of_layers=1,
        global_ply_nr=0,  # add at the end
    )
    mg.add_modeling_ply(ply)
    return ply
