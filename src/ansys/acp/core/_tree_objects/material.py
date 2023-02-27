from __future__ import annotations

from abc import abstractproperty
from dataclasses import dataclass
from typing import Any, Iterable, cast

from google.protobuf.message import Message

from ansys.api.acp.v0 import material_pb2, material_pb2_grpc

from ._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from .base import (
    CreatableTreeObject,
    IdTreeObject,
    TreeObjectAttribute,
    TreeObjectAttributeReadOnly,
)
from .enums import PlyType, ply_type_from_pb, ply_type_to_pb, status_type_from_pb
from .object_registry import register

__all__ = ["Material"]


class MaterialPropertySetBase(TreeObjectAttribute):
    @abstractproperty
    def _pb_propset(self) -> Message:
        ...

    @property
    def _pb_object(self) -> Message:
        # self._get_if_stored()
        try:
            return self._pb_propset.values[0]  # type: ignore
        except IndexError:
            # set default
            pb_object_default = type(self._pb_propset).Data()  # type: ignore
            self._pb_object = pb_object_default
            return self._pb_object

    @_pb_object.setter
    def _pb_object(self, value: Message) -> None:
        # self._get_if_stored()
        del self._pb_propset.values[:]  # type: ignore
        self._pb_propset.values.append(value)  # type: ignore
        # self._put_if_stored()


@mark_grpc_properties
class InterpolationOptions(TreeObjectAttributeReadOnly):
    GRPC_PROPERTIES = tuple()

    @property
    def _pb_object(self) -> Any:
        return self._parent_object._pb_object.interpolation_options

    algorithm = grpc_data_property_read_only("algorithm")
    cached = grpc_data_property_read_only("cached")
    normalized = grpc_data_property_read_only("normalized")


@dataclass(frozen=True)
class FieldVariable:
    name: str
    values: list[float]
    default: float
    lower_limit: float
    upper_limit: float


@mark_grpc_properties
class MaterialPropertySetVariable(TreeObjectAttributeReadOnly):
    GRPC_PROPERTIES = (
        "interpolation_options",
    )  # TODO: doesn't seem to propagate to children.. but why?

    @abstractproperty
    def _pb_propset(self) -> Message:
        ...

    @property
    def _pb_object(self) -> Message:
        self._get_if_stored()
        return self._pb_propset

    field_variables = grpc_data_property_read_only(
        "field_variables",
        from_protobuf=lambda field_vars: tuple(
            FieldVariable(
                name=val.name,
                values=val.values,
                default=val.default,
                lower_limit=val.lower_limit,
                upper_limit=val.upper_limit,
            )
            for val in field_vars
        ),
    )

    @property
    def interpolation_options(self) -> InterpolationOptions:
        return InterpolationOptions(parent_object=self)


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
class EngineeringConstantsPropertySetVariable(MaterialPropertySetVariable):
    # GRPC_PROPERTIES = tuple()

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

    E = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.E for val in values)
    )
    nu = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.nu for val in values)
    )
    E1 = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.E1 for val in values)
    )
    E2 = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.E2 for val in values)
    )
    E3 = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.E3 for val in values)
    )
    G12 = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.G12 for val in values)
    )
    G23 = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.G23 for val in values)
    )
    G31 = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.G31 for val in values)
    )
    nu12 = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.nu12 for val in values)
    )
    nu23 = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.nu23 for val in values)
    )
    nu13 = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.nu13 for val in values)
    )


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
        # if
        self.density = DensityPropertySet(parent_object=self)
        self.engineering_constants = EngineeringConstantsPropertySet(parent_object=self)

    @property
    def density(self) -> DensityPropertySet | None:
        self._get_if_stored()
        if not self._pb_object.properties.property_sets.HasField("density"):
            return None
        return DensityPropertySet(parent_object=self)

    @density.setter
    def density(self, value: DensityPropertySet | None) -> None:
        self._get_if_stored()
        self._pb_object.properties.property_sets.ClearField("density")
        if value is not None:
            self._pb_object.properties.property_sets.density.CopyFrom(
                material_pb2.DensityPropertySet()
            )
            assert self.density is not None
            self.density._pb_object = value._pb_object
        self._put_if_stored()

    @property
    def engineering_constants(
        self,
    ) -> EngineeringConstantsPropertySet | EngineeringConstantsPropertySetVariable | None:
        self._get_if_stored()
        propset_name = self._pb_object.properties.property_sets.WhichOneof("engineering_constants")
        if propset_name is None:
            return None
        eng_constants_propset = getattr(
            self._pb_object.properties.property_sets,
            propset_name,
        )
        if (len(eng_constants_propset.values) > 1) or (
            len(eng_constants_propset.field_variables) > 0
        ):
            return EngineeringConstantsPropertySetVariable(parent_object=self)
        return EngineeringConstantsPropertySet(parent_object=self)

    @engineering_constants.setter
    def engineering_constants(self, value: EngineeringConstantsPropertySet | None) -> None:
        self._get_if_stored()
        self._pb_object.properties.property_sets.ClearField("engineering_constants")
        if isinstance(self.engineering_constants, EngineeringConstantsPropertySetVariable):
            raise ValueError("Cannot replace variable engineering constants.")
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
        self._put_if_stored()

    def _create_stub(self) -> material_pb2_grpc.ObjectServiceStub:
        return material_pb2_grpc.ObjectServiceStub(self._channel)

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    ply_type = grpc_data_property(
        "properties.ply_type",
        from_protobuf=ply_type_from_pb,
        to_protobuf=ply_type_to_pb,
    )
