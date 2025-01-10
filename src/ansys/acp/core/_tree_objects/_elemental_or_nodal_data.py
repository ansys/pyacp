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

from __future__ import annotations

import dataclasses
import typing
from typing import Any, ClassVar, Literal, cast

import numpy as np
import numpy.typing as npt
from typing_extensions import Self

if typing.TYPE_CHECKING:  # pragma: no cover
    from pyvista.core.pointset import PolyData, UnstructuredGrid

from ansys.acp.core._utils.array_conversions import dataarray_to_numpy, to_numpy
from ansys.api.acp.v0 import mesh_query_pb2, mesh_query_pb2_grpc

from .._utils.property_protocols import ReadOnlyProperty
from .._utils.typing_helper import StrEnum
from ._mesh_data import MeshData
from .base import TreeObject
from .enums import (
    elemental_data_type_from_pb,
    elemental_data_type_to_pb,
    nodal_data_type_from_pb,
    nodal_data_type_to_pb,
)

__all__ = [
    "ElementalData",
    "NodalData",
    "elemental_data_property",
    "nodal_data_property",
    "ScalarData",
    "VectorData",
]


@dataclasses.dataclass
class _LabelInfo:
    mesh_labels: npt.NDArray[np.int32]
    data_labels: npt.NDArray[np.int32]
    mesh_label_to_index_map: dict[np.int32, int]


def _get_labels(
    *,
    field_names: _LabelAndPyvistaFieldNames,
    labels: npt.NDArray[np.int32],
    mesh: MeshData,
) -> _LabelInfo:
    mesh_labels = getattr(mesh, field_names.LABEL_FIELD_NAME)
    mesh_label_to_index_map = {label: idx for idx, label in enumerate(mesh_labels)}
    return _LabelInfo(
        mesh_labels=mesh_labels, data_labels=labels, mesh_label_to_index_map=mesh_label_to_index_map
    )


def _expand_array(
    *,
    array: npt.NDArray[ScalarDataT],
    labels: _LabelInfo,
    culling_factor: int = 1,
) -> npt.NDArray[np.float64]:
    """Expand the array to the size of the mesh."""
    target_shape = tuple([labels.mesh_labels.size] + list(array.shape[1:]))
    target_array = np.full(target_shape, np.nan, dtype=np.float64)
    for idx, (label, value) in enumerate(zip(labels.data_labels, array)):
        if idx % culling_factor == 0:
            try:
                target_array[labels.mesh_label_to_index_map[label]] = value
            except KeyError:
                pass
    return target_array


def _get_pyvista_mesh_with_all_data(
    *,
    mesh_data_base: ElementalOrNodalDataBase,
    mesh: MeshData,
) -> UnstructuredGrid:
    pv_mesh = mesh.to_pyvista()

    mesh_data_field = getattr(
        pv_mesh, mesh_data_base._LABEL_AND_PYVISTA_FIELD_NAMES.PYVISTA_FIELD_NAME
    )
    field_labels = getattr(
        mesh_data_base, mesh_data_base._LABEL_AND_PYVISTA_FIELD_NAMES.LABEL_FIELD_NAME
    ).values
    labels = _get_labels(
        field_names=mesh_data_base._LABEL_AND_PYVISTA_FIELD_NAMES, mesh=mesh, labels=field_labels
    )

    for name in mesh_data_base._field_names():
        values = getattr(mesh_data_base, name).values
        target_array = _expand_array(array=values, labels=labels)
        mesh_data_field[name] = target_array
    return pv_mesh


def _get_mesh_with_scalar_pyvista_data(
    *,
    labels: npt.NDArray[np.int32],
    field_names: _LabelAndPyvistaFieldNames,
    mesh: MeshData,
    values: npt.NDArray[ScalarDataT],
    component_name: str,
) -> UnstructuredGrid:
    all_labels = _get_labels(field_names=field_names, labels=labels, mesh=mesh)

    pv_mesh = mesh.to_pyvista()
    mesh_data_field = getattr(pv_mesh, field_names.PYVISTA_FIELD_NAME)

    target_array = _expand_array(array=values, labels=all_labels)
    component_label = component_name
    mesh_data_field[component_label] = target_array
    return pv_mesh


def _get_pyvista_glyphs(
    *,
    labels: npt.NDArray[np.int32],
    field_names: _LabelAndPyvistaFieldNames,
    mesh: MeshData,
    values: npt.NDArray[np.float64],
    component_name: str,
    culling_factor: int = 1,
    scaling_factor: float = 1.0,
    **kwargs: Any,
) -> PolyData:
    all_labels = _get_labels(field_names=field_names, labels=labels, mesh=mesh)

    pv_mesh = mesh.to_pyvista()
    mesh_data_field = getattr(pv_mesh, field_names.PYVISTA_FIELD_NAME)

    target_array = _expand_array(array=values, labels=all_labels, culling_factor=culling_factor)
    component_label = component_name
    mesh_data_field[component_label] = target_array

    magnitude_name = f"{component_label}_magnitude"
    mesh_data_field[magnitude_name] = np.linalg.norm(target_array, axis=-1) * scaling_factor
    return pv_mesh.glyph(orient=component_label, scale=magnitude_name, **kwargs)  # type: ignore


ScalarDataT = typing.TypeVar("ScalarDataT", np.float64, np.int32)


class ScalarData(typing.Generic[ScalarDataT]):
    """Class that encapsulates scalar data."""

    def __init__(
        self,
        field_names: _LabelAndPyvistaFieldNames,
        labels: npt.NDArray[np.int32],
        values: npt.NDArray[ScalarDataT],
        component_name: str,
    ):
        self._field_names = field_names
        self._labels = labels
        self._values: npt.NDArray[ScalarDataT] = values
        self._component_name = component_name

    @property
    def values(self) -> npt.NDArray[ScalarDataT]:
        """Scalar data values as a numpy array."""
        return self._values

    @property
    def component_name(self) -> str:
        """Name of the component."""
        return self._component_name

    def get_pyvista_mesh(
        self,
        mesh: MeshData,
    ) -> UnstructuredGrid:
        """Convert the mesh data to a PyVista object.

        Parameters
        ----------
        mesh :
            The mesh to which the data is associated.
        """
        return _get_mesh_with_scalar_pyvista_data(
            labels=self._labels,
            field_names=self._field_names,
            mesh=mesh,
            values=self._values,
            component_name=self._component_name,
        )


class VectorData:
    """Class that encapsulates vector data."""

    def __init__(
        self,
        field_names: _LabelAndPyvistaFieldNames,
        labels: npt.NDArray[np.int32],
        values: npt.NDArray[np.float64],
        component_name: str,
    ):
        self._field_names = field_names
        self._labels = labels
        self._values = values
        self._component_name = component_name

    @property
    def values(self) -> npt.NDArray[np.float64]:
        """Vector data values as a numpy array."""
        return self._values

    @property
    def component_name(self) -> str:
        """Name of the component."""
        return self._component_name

    def get_pyvista_glyphs(
        self,
        *,
        mesh: MeshData,
        culling_factor: int = 1,
        scaling_factor: float = 1.0,
        **kwargs: Any,
    ) -> PolyData:
        """Get a pyvista glyph object from the vector data.

        Parameters
        ----------
        mesh :
            The mesh to which the data is associated.
        culling_factor :
            If set to a value other than ``1``, add only every n-th data
            point to the PyVista object. This is useful especially for
            vector data, where the arrows can be too dense.
        scaling_factor :
            Factor to scale the length of the arrows.
        kwargs :
            Keyword arguments passed to the PyVista object constructor.
        """
        return _get_pyvista_glyphs(
            labels=self._labels,
            field_names=self._field_names,
            mesh=mesh,
            values=self._values,
            component_name=self._component_name,
            culling_factor=culling_factor,
            scaling_factor=scaling_factor,
            **kwargs,
        )


def _check_field_type(klass: Any, field_name: str, actual_field_type: str) -> None:
    """Check that the type declared in the dataclass (klass) matches the actual type."""
    declared_field_types: typing.Sequence[str] = cast(
        typing.Sequence[str],
        [field.type for field in dataclasses.fields(klass) if field.name == field_name],
    )
    if len(declared_field_types) != 1:
        raise RuntimeError("Failed to find field in dataclass.")
    declared_field_type = declared_field_types[0].removesuffix(" | None")
    if declared_field_type != actual_field_type:
        raise RuntimeError(
            f"Declared type does not match actual data type. "
            f"Declared type: {declared_field_type}, actual type: {actual_field_type}. "
            f"Field name: {field_name}"
        )


@dataclasses.dataclass
class _LabelAndPyvistaFieldNames:
    LABEL_FIELD_NAME: str
    PYVISTA_FIELD_NAME: str


@dataclasses.dataclass
class ElementalOrNodalDataBase:
    """Base class for nodal or elemental mesh data.

    Implements the construction from a protobuf response and the conversion
    to a PyVista object.
    """

    _LABEL_AND_PYVISTA_FIELD_NAMES: ClassVar[_LabelAndPyvistaFieldNames]
    _FIELD_NAME_FROM_PB_VALUE: ClassVar[typing.Callable[[int], StrEnum]]
    _PB_VALUE_FROM_FIELD_NAME: ClassVar[typing.Callable[[StrEnum], int]]

    @classmethod
    def _field_names(cls) -> list[str]:
        return [
            field.name
            for field in dataclasses.fields(cls)
            if field.name != cls._LABEL_AND_PYVISTA_FIELD_NAMES.LABEL_FIELD_NAME
        ]

    @classmethod
    def _from_pb(cls, response: mesh_query_pb2.ElementalData | mesh_query_pb2.NodalData) -> Self:
        """Construct a mesh data object from a protobuf response."""
        labels = to_numpy(response.labels)
        kwargs: dict[str, Any] = {
            cls._LABEL_AND_PYVISTA_FIELD_NAMES.LABEL_FIELD_NAME: ScalarData(
                field_names=cls._LABEL_AND_PYVISTA_FIELD_NAMES,
                labels=labels,
                values=labels,
                component_name=cls._LABEL_AND_PYVISTA_FIELD_NAMES.LABEL_FIELD_NAME,
            )
        }
        for data_type, array in zip(response.data_types, response.data_arrays):
            field_name = cls._FIELD_NAME_FROM_PB_VALUE(data_type).value
            values = cast(
                npt.NDArray[np.float64], dataarray_to_numpy(array, dtype=np.float64)
            )  # todo: handle other dtypes
            kwargs[field_name] = values
            data_wrapper: VectorData | ScalarData[np.float64]
            if len(values.shape) == 2 and values.shape[1] == 3:
                data_wrapper = VectorData(
                    field_names=cls._LABEL_AND_PYVISTA_FIELD_NAMES,
                    labels=labels,
                    values=values,
                    component_name=field_name,
                )
                _check_field_type(klass=cls, field_name=field_name, actual_field_type="VectorData")

            else:
                data_wrapper = ScalarData(
                    field_names=cls._LABEL_AND_PYVISTA_FIELD_NAMES,
                    labels=labels,
                    values=values,
                    component_name=field_name,
                )
                _check_field_type(
                    klass=cls, field_name=field_name, actual_field_type="ScalarData[np.float64]"
                )
            kwargs[field_name] = data_wrapper

        instance = cls(**kwargs)
        return instance

    def get_pyvista_mesh(
        self,
        mesh: MeshData,
    ) -> UnstructuredGrid:
        """Get a pyvista mesh with all data.

        Parameters
        ----------
        mesh :
            The mesh to which the data is associated.
        """
        return _get_pyvista_mesh_with_all_data(mesh_data_base=self, mesh=mesh)


_NODE_FIELD_NAMES = _LabelAndPyvistaFieldNames(
    LABEL_FIELD_NAME="node_labels",
    PYVISTA_FIELD_NAME="point_data",
)

_ELEMENT_FIELD_NAMES = _LabelAndPyvistaFieldNames(
    LABEL_FIELD_NAME="element_labels",
    PYVISTA_FIELD_NAME="cell_data",
)


@dataclasses.dataclass
class NodalData(ElementalOrNodalDataBase):
    """Base class for nodal data."""

    node_labels: ScalarData[np.int32]
    _LABEL_AND_PYVISTA_FIELD_NAMES = _NODE_FIELD_NAMES
    _PB_VALUE_FROM_FIELD_NAME = nodal_data_type_to_pb
    _FIELD_NAME_FROM_PB_VALUE = nodal_data_type_from_pb


@dataclasses.dataclass
class ElementalData(ElementalOrNodalDataBase):
    """Base class for elemental data."""

    element_labels: ScalarData[np.int32]
    _LABEL_AND_PYVISTA_FIELD_NAMES = _ELEMENT_FIELD_NAMES
    _PB_VALUE_FROM_FIELD_NAME = elemental_data_type_to_pb
    _FIELD_NAME_FROM_PB_VALUE = elemental_data_type_from_pb


T = typing.TypeVar("T", bound=ElementalOrNodalDataBase)


ElementalDataT = typing.TypeVar("ElementalDataT", bound=ElementalData)


def elemental_data_property(
    wrapped_cls: type[ElementalDataT],
) -> ReadOnlyProperty[ElementalDataT]:
    """Create a property to get elemental data from a tree object."""
    return _mesh_data_property_impl(
        wrapped_cls=wrapped_cls,
        request_name="GetElementalData",
        request_type=mesh_query_pb2.GetElementalDataRequest,
    )


NodalDataT = typing.TypeVar("NodalDataT", bound=NodalData)


def nodal_data_property(
    wrapped_cls: type[NodalDataT],
) -> ReadOnlyProperty[NodalDataT]:
    """Create a property to get nodal data from a tree object."""
    return _mesh_data_property_impl(
        wrapped_cls=wrapped_cls,
        request_name="GetNodalData",
        request_type=mesh_query_pb2.GetNodalDataRequest,
    )


MeshDataT = typing.TypeVar("MeshDataT", bound=ElementalOrNodalDataBase)


def _mesh_data_property_impl(
    wrapped_cls: type[MeshDataT],
    request_name: Literal["GetNodalData", "GetElementalData"],
    request_type: (
        type[mesh_query_pb2.GetNodalDataRequest] | type[mesh_query_pb2.GetElementalDataRequest]
    ),
) -> ReadOnlyProperty[MeshDataT]:
    """Create a mesh data property.

    Implementation of the mesh data property helpers ``nodal_data_property``
    and ``elemental_data_property``.
    """

    def getter(self: TreeObject) -> MeshDataT:
        if not self._is_stored:
            raise RuntimeError("Cannot get mesh data from an unstored object")
        stub = mesh_query_pb2_grpc.MeshQueryServiceStub(self._channel)
        request_func = getattr(stub, request_name)
        response = request_func(
            request=request_type(
                resource_path=self._resource_path,
                data_types=[
                    wrapped_cls._PB_VALUE_FROM_FIELD_NAME(name)  # type: ignore
                    for name in wrapped_cls._field_names()
                ],
            ),
        )
        return wrapped_cls._from_pb(response)

    return property(getter)
