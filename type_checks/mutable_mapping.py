from typing_extensions import assert_type

from ansys.acp.core import Model, ModelingGroup

model = Model()

# Test that the type checker understands the mutable mapping defined
# via 'define_mutable_mapping'.

assert_type(model.modeling_groups["key"], ModelingGroup)
