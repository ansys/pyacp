# type: ignore
from ansys.dpf.composites.composite_model import CompositeModel
from ansys.dpf.composites.constants import FailureOutput
from ansys.dpf.composites.data_sources import (
    CompositeDefinitionFiles,
    ContinuousFiberCompositesFiles,
)
from ansys.dpf.composites.failure_criteria import CombinedFailureCriterion, MaxStrainCriterion
from ansys.dpf.composites.server_helpers import connect_to_or_start_server


def postprocess_results(rst_file, matml_file, composite_definitions_path):
    """
    Basic failure criteria evaluation. Expects that a dpf docker container with the
    composites plugin is running at port 50052
    """
    dpf_server = connect_to_or_start_server(ip="127.0.0.1", port=50052)

    max_strain = MaxStrainCriterion()
    cfc = CombinedFailureCriterion(
        name="Combined Failure Criterion",
        failure_criteria=[max_strain],
    )

    composite_model = CompositeModel(
        composite_files=ContinuousFiberCompositesFiles(
            rst=rst_file,
            composite={
                "shell": CompositeDefinitionFiles(definition=composite_definitions_path),
            },
            engineering_data=matml_file,
        ),
        server=dpf_server,
    )

    # Evaluate the failure criteria
    output_all_elements = composite_model.evaluate_failure_criteria(cfc)

    # Query and plot the results
    irf_field = output_all_elements.get_field({"failure_label": FailureOutput.FAILURE_VALUE})

    assert composite_model.get_element_info(1).n_layers == 3
    irf_field.plot()
