from typing import Optional

import numpy as np
from typing_extensions import assert_type

from ansys.acp.core import Model, ScalarData, VectorData
from ansys.acp.core._tree_objects.modeling_ply import ModelingPlyElementalData

model = Model()  # type: ignore

modeling_ply = model.modeling_groups["key"].plies["key"]
assert_type(modeling_ply.elemental_data, ModelingPlyElementalData)
assert_type(modeling_ply.elemental_data.normal, Optional[VectorData])
assert_type(modeling_ply.elemental_data.thickness, Optional[ScalarData[np.float64]])
assert_type(modeling_ply.elemental_data.element_labels, ScalarData[np.int32])
assert_type(modeling_ply.nodal_data.node_labels, ScalarData[np.int32])
assert_type(modeling_ply.nodal_data.ply_offset, Optional[VectorData])
