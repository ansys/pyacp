from typing import Collection, List, Tuple

from ansys.api.acp.v0.array_types_pb2 import DoubleArray, IntArray


def to_1D_double_array(data: Tuple[float, ...]) -> DoubleArray:
    return DoubleArray(shape=[len(data)], data=data)


def to_1D_int_array(data: Collection[int]) -> IntArray:
    return IntArray(shape=[len(data)], data=data)


def to_tuple_from_1D_array(double_array: DoubleArray) -> Tuple[float, ...]:
    if not len(double_array.shape) == 1:
        raise RuntimeError(f"Cannot convert {len(double_array.shape)}-dimensional array to tuple!")
    return tuple(double_array.data)


def to_list_from_int_array(int_array: IntArray) -> List[int]:
    if not len(int_array.shape) == 1:
        raise RuntimeError(f"Cannot convert {len(int_array.shape)}-dimensional array to list!")
    return list(int_array.data)
