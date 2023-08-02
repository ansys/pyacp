from typing import Any, Tuple, Type, Union, overload

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0.array_types_pb2 import DoubleArray, Int32Array, IntArray
from ansys.api.acp.v0.mesh_query_pb2 import DataArray


def to_1D_double_array(data: Tuple[float, ...]) -> DoubleArray:
    return DoubleArray(shape=[len(data)], data=data)


def to_1D_int_array(data: Tuple[int, ...]) -> IntArray:
    return IntArray(shape=[len(data)], data=data)


def to_tuple_from_1D_array(array: Union[IntArray, DoubleArray]) -> Tuple[Any, ...]:
    if not len(array.shape) == 1:
        raise RuntimeError(f"Cannot convert {len(array.shape)}-dimensional array to tuple!")
    return tuple(array.data)


@overload
def to_numpy(array_pb: IntArray) -> npt.NDArray[np.int64]:
    ...


@overload
def to_numpy(array_pb: Int32Array) -> npt.NDArray[np.int32]:
    ...


@overload
def to_numpy(array_pb: DoubleArray) -> npt.NDArray[np.float64]:
    ...


def to_numpy(
    array_pb: Union[IntArray, Int32Array, DoubleArray]
) -> Union[npt.NDArray[np.int64], npt.NDArray[np.int32], npt.NDArray[np.float64]]:
    dtype = {
        IntArray: np.int64,
        Int32Array: np.int32,
        DoubleArray: np.float64,
    }[type(array_pb)]
    return np.array(array_pb.data, dtype=dtype).reshape(array_pb.shape)


def dataarray_to_numpy(
    array_pb: DataArray,
    dtype: Union[Type[np.int32], Type[np.int64], Type[np.float64]],
) -> Union[npt.NDArray[np.int64], npt.NDArray[np.int32], npt.NDArray[np.float64]]:
    data_array_attribute = array_pb.WhichOneof("data")
    if data_array_attribute is None:
        raise RuntimeError("None of the 'DataArray' data attributes are set!")
    expected_data_array_attribute = {
        np.int64: "int_array",
        np.int32: "int32_array",
        np.float64: "double_array",
    }[dtype]
    if data_array_attribute != expected_data_array_attribute:
        raise RuntimeError(
            f"Wrong data attribute is set: expected '{expected_data_array_attribute}', "
            f"got '{data_array_attribute}'!"
        )
    return to_numpy(getattr(array_pb, data_array_attribute))
