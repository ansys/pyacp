from typing import Optional

import numpy as np
from typing_extensions import assert_type

from ansys.acp.core.mesh_data import ScalarData, VectorData, ModelingPlyElementalData
from ansys.acp.core import Model

model = Model()

modeling_ply = model.modeling_groups["key"].modeling_plies["key"]
assert_type(modeling_ply.elemental_data, ModelingPlyElementalData)
assert_type(modeling_ply.elemental_data.normal, Optional[VectorData])
assert_type(modeling_ply.elemental_data.thickness, Optional[ScalarData[np.float64]])
assert_type(modeling_ply.elemental_data.element_labels, ScalarData[np.int32])
assert_type(modeling_ply.nodal_data.node_labels, ScalarData[np.int32])
assert_type(modeling_ply.nodal_data.ply_offset, Optional[VectorData])
