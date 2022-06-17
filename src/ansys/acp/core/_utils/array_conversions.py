from typing import Any, Tuple, Union

from ansys.api.acp.v0.array_types_pb2 import DoubleArray, IntArray


def to_1D_double_array(data: Tuple[float, ...]) -> DoubleArray:
    return DoubleArray(shape=[len(data)], data=data)


def to_1D_int_array(data: Tuple[int, ...]) -> IntArray:
    return IntArray(shape=[len(data)], data=data)


def to_tuple_from_1D_array(array: Union[IntArray, DoubleArray]) -> Tuple[Any, ...]:
    if not len(array.shape) == 1:
        raise RuntimeError(f"Cannot convert {len(array.shape)}-dimensional array to tuple!")
    return tuple(array.data)
