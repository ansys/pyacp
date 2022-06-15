from typing import Tuple

from ansys.api.acp.v0.array_types_pb2 import DoubleArray


def to_1D_double_array(data: Tuple[float, ...]) -> DoubleArray:
    return DoubleArray(shape=[len(data)], data=data)


def to_tuple_from_1D_array(double_array: DoubleArray) -> Tuple[float, ...]:
    if not len(double_array.shape) == 1:
        raise RuntimeError(f"Cannot convert {len(double_array.shape)}-dimensional array to tuple!")
    res = tuple(double_array.data)
    if len(res) != 3:
        raise RuntimeError("bli")
    return res
