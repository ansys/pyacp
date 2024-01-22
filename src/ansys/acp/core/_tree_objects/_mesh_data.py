from __future__ import annotations

import dataclasses
import typing
from typing import Any, ClassVar, Literal, cast

import numpy as np
import numpy.typing as npt
from pyvista.core.pointset import PolyData, UnstructuredGrid
from typing_extensions import Self

from ansys.acp.core._utils.array_conversions import dataarray_to_numpy, to_numpy
from ansys.api.acp.v0 import mesh_query_pb2, mesh_query_pb2_grpc

from .base import TreeObject
from .enums import (
    elemental_data_type_from_pb,
    elemental_data_type_to_pb,
    nodal_data_type_from_pb,
    nodal_data_type_to_pb,
)

if typing.TYPE_CHECKING:
    from .model import MeshData  # avoid circular import

__all__ = [
    "ElementalData",
    "NodalData",
    "elemental_data_property",
    "nodal_data_property",
]


def _expand_array(
        *,
        index_map: dict[int, int],
        array: npt.NDArray[np.float64],
        labels: npt.NDArray[np.int32],
        mesh_labels: npt.NDArray[np.int32],
        culling_factor: int,
) -> npt.NDArray[np.float64]:
    """Expand the array to the size of the mesh."""
    target_shape = tuple([mesh_labels.size] + list(array.shape[1:]))
    target_array = np.ones(target_shape, dtype=np.float64) * np.nan
    for idx, (label, value) in enumerate(zip(labels, array)):
        if idx % culling_factor == 0:
            target_array[index_map[label]] = value
    return target_array


def _to_pyvista(
        mesh_data_base: MeshDataBase,
        *,
        mesh: MeshData,
        values: npt.NDArray[np.float64] | None = None,
        culling_factor: int = 1,
        **kwargs: Any,
) -> PolyData | UnstructuredGrid:
    current_labels = getattr(mesh_data_base, mesh_data_base._LABEL_FIELD_NAME).values
    mesh_labels = getattr(mesh, mesh_data_base._LABEL_FIELD_NAME)
    idx_map = {label: idx for idx, label in enumerate(mesh_labels)}
    pv_mesh = mesh.to_pyvista()

    mesh_data_field = getattr(pv_mesh, mesh_data_base._PYVISTA_FIELD_NAME)

    if values is None:
        for name in mesh_data_base._field_names():
            values = getattr(mesh_data_base, name)
            target_array = _expand_array(
                index_map=idx_map,
                array=values,
                labels=current_labels,
                mesh_labels=mesh_labels,
                culling_factor=culling_factor,
            )
            mesh_data_field[name] = target_array
    else:
        target_array = _expand_array(
            index_map=idx_map,
            array=values,
            labels=current_labels,
            mesh_labels=mesh_labels,
            culling_factor=culling_factor,
        )
        component = "component"
        mesh_data_field[component] = target_array
        if len(target_array.shape) == 2 and target_array.shape[1] == 3:
            # handle vector data
            magnitude_name = f"{component}_magnitude"
            mesh_data_field[magnitude_name] = np.linalg.norm(target_array, axis=-1)
            return pv_mesh.glyph(orient=component, scale=magnitude_name, **kwargs)  # type: ignore
    if kwargs:
        raise TypeError(
            "The following keyword arguments were not used: " + ", ".join(kwargs.keys())
        )
    return pv_mesh

class PlotDataWrapper:
    def __init__(self, wrapping_class: MeshDataBase, values: npt.NDArray[np.float64]):
        self._wrapping_class = wrapping_class
        self._values = values

    @property
    def values(self) -> npt.NDArray[np.float64]:
        return self._values

    def to_pyvista(self,
        mesh: MeshData,
        culling_factor: int = 1,
        **kwargs: Any,):
        """Convert the mesh data to a PyVista object.

        Parameters
        ----------
        mesh :
            The mesh to which the data is associated.
        culling_factor :
            If set to a value other than ``1``, add only every n-th data
            point to the PyVista object. This is useful especially for
            vector data, where the arrows can be too dense.
        kwargs :
            Keyword arguments passed to the PyVista object constructor.
        """
        return _to_pyvista(
            self._wrapping_class,
            mesh=mesh,
            values=self._values,
            culling_factor=culling_factor,
            **kwargs,
        )


@dataclasses.dataclass
class MeshDataBase:
    """
    Base class for nodal or elemental mesh data. Implements the construction
    from a protobuf response and the conversion to a PyVista object.
    """

    _LABEL_FIELD_NAME: ClassVar[str]
    _PYVISTA_FIELD_NAME: ClassVar[str]
    _FIELD_NAME_FROM_PB_VALUE: ClassVar[typing.Callable[[int], str]]
    _PB_VALUE_FROM_FIELD_NAME: ClassVar[typing.Callable[[str], int]]

    @classmethod
    def _field_names(cls) -> list[str]:
        return [
            field.name for field in dataclasses.fields(cls) if field.name != cls._LABEL_FIELD_NAME
        ]

    @classmethod
    def _from_pb(cls, response: mesh_query_pb2.ElementalData | mesh_query_pb2.NodalData) -> Self:
        """Construct a mesh data object from a protobuf response."""
        kwargs: dict[str, Any] = {
            cls._LABEL_FIELD_NAME: to_numpy(response.labels),
        }
        for data_type, array in zip(response.data_types, response.data_arrays):
            field_name = cls._FIELD_NAME_FROM_PB_VALUE(data_type)
            kwargs[field_name] = cast(
                npt.NDArray[np.float64], dataarray_to_numpy(array, dtype=np.float64)
            )  # todo: handle other dtypes


        instance = cls(**kwargs)
        for key, value in kwargs.items():
            setattr(instance, key, PlotDataWrapper(instance, value))
        return instance

    def to_pyvista(self,
        mesh: MeshData,
        culling_factor: int = 1,
        **kwargs: Any,):
        """Convert the mesh data to a PyVista object.

        Parameters
        ----------
        mesh :
            The mesh to which the data is associated.
        culling_factor :
            If set to a value other than ``1``, add only every n-th data
            point to the PyVista object. This is useful especially for
            vector data, where the arrows can be too dense.
        kwargs :
            Keyword arguments passed to the PyVista object constructor.
        """
        return _to_pyvista(
            self,
            mesh=mesh,
            culling_factor=culling_factor
            **kwargs,
        )




@dataclasses.dataclass
class NodalData(MeshDataBase):
    """Base class for nodal data."""

    node_labels: npt.NDArray[np.int32]
    _LABEL_FIELD_NAME: ClassVar[str] = "node_labels"
    _PYVISTA_FIELD_NAME: ClassVar[str] = "point_data"
    _PB_VALUE_FROM_FIELD_NAME = nodal_data_type_to_pb
    _FIELD_NAME_FROM_PB_VALUE = nodal_data_type_from_pb


@dataclasses.dataclass
class ElementalData(MeshDataBase):
    """Base class for elemental data."""

    element_labels: npt.NDArray[np.int32]
    _LABEL_FIELD_NAME: ClassVar[str] = "element_labels"
    _PYVISTA_FIELD_NAME: ClassVar[str] = "cell_data"
    _PB_VALUE_FROM_FIELD_NAME = elemental_data_type_to_pb
    _FIELD_NAME_FROM_PB_VALUE = elemental_data_type_from_pb


T = typing.TypeVar("T", bound=MeshDataBase)


ElementalDataT = typing.TypeVar("ElementalDataT", bound=ElementalData)


def elemental_data_property(
    wrapped_cls: type[ElementalDataT],
) -> property:
    """Create a property to get elemental data from a tree object."""
    return _mesh_data_property_impl(
        wrapped_cls=wrapped_cls,
        request_name="GetElementalData",
        request_type=mesh_query_pb2.GetElementalDataRequest,
    )


NodalDataT = typing.TypeVar("NodalDataT", bound=NodalData)


def nodal_data_property(
    wrapped_cls: type[NodalDataT],
) -> property:
    """Create a property to get nodal data from a tree object."""
    return _mesh_data_property_impl(
        wrapped_cls=wrapped_cls,
        request_name="GetNodalData",
        request_type=mesh_query_pb2.GetNodalDataRequest,
    )


MeshDataT = typing.TypeVar("MeshDataT", bound=MeshDataBase)


def _mesh_data_property_impl(
    wrapped_cls: type[MeshDataT],
    request_name: Literal["GetNodalData", "GetElementalData"],
    request_type: type[mesh_query_pb2.GetNodalDataRequest]
    | type[mesh_query_pb2.GetElementalDataRequest],
) -> property:
    """Implementation of the mesh data property helpers."""

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
