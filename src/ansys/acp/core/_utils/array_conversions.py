# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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

from collections.abc import Collection
from typing import Any, overload

import numpy as np
import numpy.typing as npt

from ansys.api.acp.v0.array_types_pb2 import DoubleArray, Int32Array, IntArray
from ansys.api.acp.v0.mesh_query_pb2 import DataArray


def to_1D_double_array(data: Collection[float]) -> DoubleArray:
    """Convert a 1D collection of floats to a DoubleArray protobuf message."""
    return DoubleArray(shape=[len(data)], data=tuple(data))


def to_1D_int_array(data: Collection[int]) -> IntArray:
    """Convert a 1D collection of ints to a IntArray protobuf message."""
    return IntArray(shape=[len(data)], data=tuple(data))


def to_tuple_from_1D_array(array: IntArray | DoubleArray) -> tuple[Any, ...]:
    """Convert a 1D IntArray or DoubleArray protobuf message to a tuple."""
    if not len(array.shape) == 1:
        raise RuntimeError(f"Cannot convert {len(array.shape)}-dimensional array to tuple!")
    return tuple(array.data)


def to_ND_double_array_from_numpy_or_list(data: npt.NDArray[np.float64]) -> DoubleArray:
    """Convert a list or numpy array to a DoubleArray protobuf message."""
    data_np = np.array(data)
    return DoubleArray(shape=list(data_np.shape), data=data_np.flatten())


@overload
def to_numpy(array_pb: IntArray) -> npt.NDArray[np.int64]: ...


@overload
def to_numpy(array_pb: Int32Array) -> npt.NDArray[np.int32]: ...


@overload
def to_numpy(array_pb: DoubleArray) -> npt.NDArray[np.float64]: ...


def to_numpy(
    array_pb: IntArray | Int32Array | DoubleArray,
) -> npt.NDArray[np.int64] | npt.NDArray[np.int32] | npt.NDArray[np.float64]:
    """Convert a protubuf array message to a numpy array."""
    dtype = {
        IntArray: np.int64,
        Int32Array: np.int32,
        DoubleArray: np.float64,
    }[type(array_pb)]
    return np.array(array_pb.data, dtype=dtype).reshape(array_pb.shape)


def dataarray_to_numpy(
    array_pb: DataArray,
    dtype: type[np.int32] | type[np.int64] | type[np.float64],
) -> npt.NDArray[np.int64] | npt.NDArray[np.int32] | npt.NDArray[np.float64]:
    """Convert a DataArray protobuf message to a numpy array."""
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
