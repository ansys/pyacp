import os

from ansys.acp.core import Client, get_model_tree


def test_printed_model(grpc_server, model_data_dir):
    """
    Test that model tree looks correct.
    """
    client = Client(server=grpc_server)

    input_file_path = model_data_dir / "minimal_complete_model.acph5"
    remote_path = client.upload_file(input_file_path)

    model = client.import_model(name="minimal_complete", path=remote_path)

    model.update()
    tree = get_model_tree(model)

    assert (
        os.linesep + str(tree)
        == """
Model
    material_data
        materials
            Structural Steel
        fabrics
            Fabric.1
    element_sets
        All_Elements
    edge_sets
        ns_edge
    geometry
    rosettes
        Global Coordinate System
    lookup_table
    selection_rules
    oriented_selection_sets
        OrientedSelectionSet.1
    modeling Groups
        ModelingGroup.1
            ModelingPly.1
                ProductionPly
                    P1L1__ModelingPly.1
""".replace(
            "\n", os.linesep
        )
    )

    model.create_edge_set()
    model.create_stackup()
    model.create_sublaminate()
    model.create_virtual_geometry()
    model.create_cad_geometry()
    model.create_parallel_selection_rule()
    model.create_cylindrical_selection_rule()
    model.create_tube_selection_rule()
    model.create_cutoff_selection_rule()
    model.create_geometrical_selection_rule()
    model.create_boolean_selection_rule()
    model.create_lookup_table_1d()
    model.create_lookup_table_3d()
    model.create_sensor()

    tree = get_model_tree(model)

    assert (
        os.linesep + str(tree)
        == """
Model
    material_data
        materials
            Structural Steel
        fabrics
            Fabric.1
        stackups
            Stackup
        sublaminates
            SubLaminate
    element_sets
        All_Elements
    edge_sets
        ns_edge
        EdgeSet
    geometry
        cad_geometries
            CADGeometry
        virtual_geometries
            VirtualGeometry
    rosettes
        Global Coordinate System
    lookup_table
        lookup_tables_1d
            LookUpTable1D
        lookup_tables_3d
            LookUpTable3D
    selection_rules
        parallel_selection_rules
            ParallelSelectionrule
        cylindrical_selection_rules
            CylindricalSelectionrule
        tube_selection_rules
            TubeSelectionrule
        cutoff_selection_rules
            CutoffSelectionrule
        geometrical_selection_rules
            GeometricalSelectionrule
        boolean_selection_rules
            BooleanSelectionrule
    oriented_selection_sets
        OrientedSelectionSet.1
    modeling Groups
        ModelingGroup.1
            ModelingPly.1
                ProductionPly
                    P1L1__ModelingPly.1
    sensors
        Sensor
""".replace(
            "\n", os.linesep
        )
    )
