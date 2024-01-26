from typing_extensions import assert_type

from ansys.acp.core import Model, ScalarData, VectorData
from ansys.acp.core._tree_objects.modeling_ply import ModelingPlyElementalData

model = Model()  # type: ignore

modeling_ply = model.modeling_groups["key"].modeling_plies["key"]
assert_type(modeling_ply.elemental_data, ModelingPlyElementalData)
assert_type(modeling_ply.elemental_data.normal, VectorData)
assert_type(modeling_ply.elemental_data.thickness, ScalarData)
assert_type(modeling_ply.nodal_data.ply_offset, VectorData)
