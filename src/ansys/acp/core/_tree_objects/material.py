from __future__ import annotations

from abc import abstractproperty
from typing import Iterable, cast

from google.protobuf.message import Message

from ansys.api.acp.v0 import material_pb2, material_pb2_grpc

from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import CreatableTreeObject, IdTreeObject, TreeObjectAttribute
from .enums import PlyType, ply_type_from_pb, ply_type_to_pb, status_type_from_pb
from .object_registry import register

__all__ = ["Material"]


class MaterialPropertySetBase(TreeObjectAttribute):
    @abstractproperty
    def _pb_propset(self) -> Message:
        ...

    @property
    def _pb_object(self) -> Message:
        if self._is_stored:
            self._get()
        try:
            return self._pb_propset.values[0]  # type: ignore
        except IndexError:
            # set default
            pb_object_default = type(self._pb_propset).Data()  # type: ignore
            self._pb_object = pb_object_default
            return self._pb_object

    @_pb_object.setter
    def _pb_object(self, value: Message) -> None:
        if self._is_stored:
            self._get()
        del self._pb_propset.values[:]  # type: ignore
        self._pb_propset.values.append(value)  # type: ignore
        if self._is_stored:
            self._put()


@mark_grpc_properties
class DensityPropertySet(MaterialPropertySetBase):
    GRPC_PROPERTIES = tuple()

    @property
    def _pb_propset(self) -> material_pb2.DensityPropertySet:
        return cast(
            material_pb2.DensityPropertySet,
            self._parent_object._pb_object.properties.property_sets.density,
        )

    rho = grpc_data_property("rho")


@mark_grpc_properties
class EngineeringConstantsPropertySet(MaterialPropertySetBase):
    GRPC_PROPERTIES = tuple()

    @property
    def _pb_propset(
        self,
    ) -> (
        material_pb2.OrthotropicEngineeringConstantsPropertySet
        | material_pb2.IsotropicEngineeringConstantsPropertySet
    ):
        propset_name = "engineering_constants"
        field_name_default = "engineering_constants_orthotropic"
        field_name = (
            self._parent_object._pb_object.properties.property_sets.WhichOneof(propset_name)
            or field_name_default
        )
        return getattr(self._parent_object._pb_object.properties.property_sets, field_name)  # type: ignore

    E = grpc_data_property("E")
    nu = grpc_data_property("nu")
    E1 = grpc_data_property("E1")
    E2 = grpc_data_property("E2")
    E3 = grpc_data_property("E3")
    G12 = grpc_data_property("G12")
    G23 = grpc_data_property("G23")
    G31 = grpc_data_property("G31")
    nu12 = grpc_data_property("nu12")
    nu23 = grpc_data_property("nu23")
    nu13 = grpc_data_property("nu13")


@mark_grpc_properties
@register
class Material(CreatableTreeObject, IdTreeObject):
    """Instantiate a Material.

    Parameters
    ----------
    name :
        Name of the Material.
    ply_type :
        Define the type of material such as core, uni-directional (regular), woven, or isotropic.
    """

    _pb_object: material_pb2.ObjectInfo
    __slots__: Iterable[str] = tuple()

    COLLECTION_LABEL = "materials"
    OBJECT_INFO_TYPE = material_pb2.ObjectInfo
    CREATE_REQUEST_TYPE = material_pb2.CreateRequest

    def __init__(self, name: str = "Material", ply_type: PlyType = "undefined"):
        super().__init__(name=name)

        self.ply_type = ply_type
        self.density = DensityPropertySet(parent_object=self)
        self.engineering_constants = EngineeringConstantsPropertySet(parent_object=self)

    @property
    def density(self) -> DensityPropertySet | None:
        if self._is_stored:
            self._get()
        if not self._pb_object.properties.property_sets.HasField("density"):
            return None
        return DensityPropertySet(parent_object=self)

    @density.setter
    def density(self, value: DensityPropertySet | None) -> None:
        if self._is_stored:
            self._get()
        self._pb_object.properties.property_sets.ClearField("density")
        if value is not None:
            self._pb_object.properties.property_sets.density.CopyFrom(
                material_pb2.DensityPropertySet()
            )
            assert self.density is not None
            self.density._pb_object = value._pb_object
        if self._is_stored:
            self._put()

    @property
    def engineering_constants(self) -> EngineeringConstantsPropertySet | None:
        if self._is_stored:
            self._get()
        if not self._pb_object.properties.property_sets.HasField("engineering_constants"):
            return None
        return EngineeringConstantsPropertySet(parent_object=self)

    @engineering_constants.setter
    def engineering_constants(self, value: EngineeringConstantsPropertySet | None) -> None:
        if self._is_stored:
            self._get()
        self._pb_object.properties.property_sets.ClearField("engineering_constants")
        if value is not None:
            if isinstance(
                value._pb_object, material_pb2.OrthotropicEngineeringConstantsPropertySet.Data
            ):
                self._pb_object.properties.property_sets.engineering_constants_orthotropic.CopyFrom(
                    material_pb2.OrthotropicEngineeringConstantsPropertySet()
                )
            else:
                self._pb_object.properties.property_sets.engineering_constants_isotropic.CopyFrom(
                    material_pb2.IsotropicEngineeringConstantsPropertySet()
                )
            assert self.engineering_constants is not None
            self.engineering_constants._pb_object = value._pb_object
        if self._is_stored:
            self._put()

    def _create_stub(self) -> material_pb2_grpc.ObjectServiceStub:
        return material_pb2_grpc.ObjectServiceStub(self._channel)

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    ply_type = grpc_data_property(
        "properties.ply_type",
        from_protobuf=ply_type_from_pb,
        to_protobuf=ply_type_to_pb,
    )
