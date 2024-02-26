from ansys.acp.core._plotter import get_directions_plotter
from ansys.acp.core._utils.visualization import _replace_underscores_and_capitalize


def test_direction_plotter(acp_instance, load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        modeling_ply = model.modeling_groups["ModelingGroup.1"].modeling_plies["ModelingPly.1"]
        analysis_ply = modeling_ply.production_plies["ProductionPly"].analysis_plies[
            "P1L1__ModelingPly.1"
        ]
        components = [
            analysis_ply.elemental_data.orientation,
            analysis_ply.elemental_data.normal,
            analysis_ply.elemental_data.reference_direction,
            analysis_ply.elemental_data.fiber_direction,
            analysis_ply.elemental_data.transverse_direction,
            analysis_ply.elemental_data.draped_fiber_direction,
            analysis_ply.elemental_data.draped_transverse_direction,
            analysis_ply.elemental_data.material_1_direction,
        ]
        plotter = get_directions_plotter(
            model=model,
            components=components,
        )

        for idx, data in enumerate(components):
            assert plotter.legend.GetEntryString(idx) == _replace_underscores_and_capitalize(
                data.component_name
            )
