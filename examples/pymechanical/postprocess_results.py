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
    Basic failure criteria evaluation. The evaluation expects that a DPF docker container with the
    composites plugin is running at port 50052.
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
