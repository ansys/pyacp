import os

from ansys.acp.core import get_model_tree


def test_printed_model(acp_instance, model_data_dir):
    """
    Test that model tree looks correct.
    """
    input_file_path = model_data_dir / "minimal_complete_model.acph5"
    remote_path = acp_instance.upload_file(input_file_path)

    model = acp_instance.import_model(name="minimal_complete", path=remote_path)

    model.update()
    tree = get_model_tree(model)

    assert (
        os.linesep + str(tree)
        == """
Model
    Material Data
        Materials
            Structural Steel
        Fabrics
            Fabric.1
    Element Sets
        All_Elements
    Edge Sets
        ns_edge
    Geometry
    Rosettes
        Global Coordinate System
    Lookup Table
    Selection Rules
    Oriented Selection Sets
        OrientedSelectionSet.1
    Modeling Groups
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
    Material Data
        Materials
            Structural Steel
        Fabrics
            Fabric.1
        Stackups
            Stackup
        Sublaminates
            SubLaminate
    Element Sets
        All_Elements
    Edge Sets
        ns_edge
        EdgeSet
    Geometry
        Cad Geometries
            CADGeometry
        Virtual Geometries
            VirtualGeometry
    Rosettes
        Global Coordinate System
    Lookup Table
        Lookup Tables 1d
            LookUpTable1D
        Lookup Tables 3d
            LookUpTable3D
    Selection Rules
        Parallel Selection Rules
            ParallelSelectionrule
        Cylindrical Selection Rules
            CylindricalSelectionrule
        Tube Selection Rules
            TubeSelectionrule
        Cutoff Selection Rules
            CutoffSelectionrule
        Geometrical Selection Rules
            GeometricalSelectionrule
        Boolean Selection Rules
            BooleanSelectionrule
    Oriented Selection Sets
        OrientedSelectionSet.1
    Modeling Groups
        ModelingGroup.1
            ModelingPly.1
                ProductionPly
                    P1L1__ModelingPly.1
    Sensors
        Sensor
""".replace(
            "\n", os.linesep
        )
    )
