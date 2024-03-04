from typing_extensions import assert_type

from ansys.acp.core import Fabric, Rosette

rosette = Rosette()
fabric = Fabric()

# Test that the type checker understands the grpc properties.

assert_type(rosette.locked, bool)  # read-only property
assert_type(fabric.thickness, float)  # read-write property
