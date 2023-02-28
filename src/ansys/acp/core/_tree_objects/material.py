from __future__ import annotations

from abc import abstractproperty
from dataclasses import dataclass
from typing import Iterable, cast

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

__all__ = [
    "Material",
    "InterpolationOptions",
    "FieldVariable",
    "ConstantDensity",
    "VariableDensity",
    "ConstantEngineeringConstants",
    "VariableEngineeringConstants",
]


class _ConstantMaterialPropertySet(TreeObjectAttribute):
    @abstractproperty
    def _pb_propset_impl(self) -> Message:
        pass

    @property
    def _pb_object_impl(self) -> Message:
        try:
            return self._pb_propset_impl.values[0]  # type: ignore
        except IndexError:
            raise RuntimeError("The property set has either been deleted or changed type.")


@dataclass(frozen=True)
class InterpolationOptions:
    algorithm: str
    cached: bool
    normalized: bool


@dataclass(frozen=True)
class FieldVariable:
    name: str
    values: tuple[float, ...]
    default: float
    lower_limit: float
    upper_limit: float


@mark_grpc_properties
class _VariableMaterialPropertySet(TreeObjectAttributeReadOnly):
    @abstractproperty
    def _pb_propset(self) -> Message:
        pass

    @property
    def _pb_object(self) -> Message:
        # self._get_if_stored()
        return self._pb_propset

    field_variables = grpc_data_property_read_only(
        "field_variables",
        from_protobuf=lambda field_vars: tuple(
            FieldVariable(
                name=val.name,
                values=tuple(float(v) for v in val.values),
                default=val.default,
                lower_limit=val.lower_limit,
                upper_limit=val.upper_limit,
            )
            for val in field_vars
        ),
    )

    interpolation_options = grpc_data_property_read_only(
        "interpolation_options",
        from_protobuf=lambda val: InterpolationOptions(
            algorithm=val.algorithm, cached=val.cached, normalized=val.normalized
        ),
    )


@mark_grpc_properties
class ConstantDensity(_ConstantMaterialPropertySet):
    GRPC_PROPERTIES = tuple()
    _DEFAULT_PB_OBJECT_CONSTRUCTOR = material_pb2.DensityPropertySet.Data
    _pb_object: material_pb2.DensityPropertySet.Data

    def __init__(self, *, rho: float = 0.0, _parent_object: Material | None = None):
        super().__init__(_parent_object=_parent_object)
        if _parent_object is not None:
            return
        self.rho = rho

    @property
    def _pb_propset_impl(self) -> material_pb2.DensityPropertySet:
        assert self._parent_object is not None
        return cast(
            material_pb2.DensityPropertySet,
            self._parent_object._pb_object.properties.property_sets.density,
        )

    rho = grpc_data_property("rho")


@mark_grpc_properties
class VariableDensity(_VariableMaterialPropertySet):
    GRPC_PROPERTIES = tuple()

    @property
    def _pb_propset(
        self,
    ) -> material_pb2.DensityPropertySet:
        assert self._parent_object is not None
        return self._parent_object._pb_object.properties.property_sets.density  # type: ignore

    rho = grpc_data_property_read_only(
        "values", from_protobuf=lambda values: tuple(val.rho for val in values)
    )


@mark_grpc_properties
class VariableEngineeringConstants(_VariableMaterialPropertySet):
    GRPC_PROPERTIES = tuple()

    @property
    def _pb_propset(
        self,
    ) -> (
        material_pb2.OrthotropicEngineeringConstantsPropertySet
        | material_pb2.IsotropicEngineeringConstantsPropertySet
    ):
        assert self._parent_object is not None
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
class ConstantEngineeringConstants(_ConstantMaterialPropertySet):
    GRPC_PROPERTIES = tuple()
    _DEFAULT_PB_OBJECT_CONSTRUCTOR = material_pb2.OrthotropicEngineeringConstantsPropertySet.Data
    _pb_object: (
        material_pb2.IsotropicEngineeringConstantsPropertySet.Data
        | material_pb2.OrthotropicEngineeringConstantsPropertySet.Data
    )

    def __init__(
        self,
        *,
        E1: float = 0.0,
        E2: float = 0.0,
        E3: float = 0.0,
        nu12: float = 0.0,
        nu23: float = 0.0,
        nu13: float = 0.0,
        G12: float = 0.0,
        G23: float = 0.0,
        G31: float = 0.0,
        _parent_object: Material | None = None,
    ):
        super().__init__(_parent_object=_parent_object)
        if _parent_object is not None:
            return
        self.E1 = E1
        self.E2 = E2
        self.E3 = E3
        self.nu12 = nu12
        self.nu23 = nu23
        self.nu13 = nu13
        self.G12 = G12
        self.G23 = G23
        self.G31 = G31

    @property
    def _pb_propset_impl(
        self,
    ) -> (
        material_pb2.OrthotropicEngineeringConstantsPropertySet
        | material_pb2.IsotropicEngineeringConstantsPropertySet
    ):
        assert self._parent_object is not None
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

    def __init__(
        self,
        name: str = "Material",
        ply_type: PlyType = "undefined",
        density: ConstantDensity | None = None,
        engineering_constants: ConstantEngineeringConstants | None = None,
    ):
        super().__init__(name=name)

        self.ply_type = ply_type
        self.density = density or ConstantDensity()
        self.engineering_constants = engineering_constants or ConstantEngineeringConstants()

    @property
    def density(self) -> VariableDensity | ConstantDensity | None:
        self._get_if_stored()
        if not self._pb_object.properties.property_sets.HasField("density"):
            return None
        density_propset = self._pb_object.properties.property_sets.density
        if len(density_propset.values) == 0:
            return None
        if (len(density_propset.values) > 1) or (len(density_propset.field_variables) > 0):
            return VariableDensity(_parent_object=self)
        return ConstantDensity(_parent_object=self)

    @density.setter
    def density(self, value: ConstantDensity | None) -> None:
        self._get_if_stored()
        if isinstance(self.density, _VariableMaterialPropertySet):
            raise AttributeError("Cannot replace variable property sets.")
        self._pb_object.properties.property_sets.ClearField("density")
        if value is not None:
            self._pb_object.properties.property_sets.density.CopyFrom(
                material_pb2.DensityPropertySet(values=[value._pb_object])
            )
        self._put_if_stored()

    @density.deleter
    def density(self) -> None:
        self.density = None

    @property
    def engineering_constants(
        self,
    ) -> ConstantEngineeringConstants | VariableEngineeringConstants | None:
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
            return VariableEngineeringConstants(_parent_object=self)
        if len(eng_constants_propset.values) == 0:
            return None
        return ConstantEngineeringConstants(_parent_object=self)

    @engineering_constants.setter
    def engineering_constants(self, value: ConstantEngineeringConstants | None) -> None:
        self._get_if_stored()
        if isinstance(self.engineering_constants, _VariableMaterialPropertySet):
            raise AttributeError("Cannot replace variable engineering constants.")
        self._pb_object.properties.property_sets.ClearField("engineering_constants_isotropic")
        self._pb_object.properties.property_sets.ClearField("engineering_constants_orthotropic")
        if value is not None:
            if isinstance(
                value._pb_object, material_pb2.OrthotropicEngineeringConstantsPropertySet.Data
            ):
                self._pb_object.properties.property_sets.engineering_constants_orthotropic.CopyFrom(
                    material_pb2.OrthotropicEngineeringConstantsPropertySet(
                        values=[value._pb_object]
                    )
                )
            else:
                self._pb_object.properties.property_sets.engineering_constants_isotropic.CopyFrom(
                    material_pb2.IsotropicEngineeringConstantsPropertySet(values=[value._pb_object])
                )
        self._put_if_stored()

    @engineering_constants.deleter
    def engineering_constants(self) -> None:
        self.engineering_constants = None

    def _create_stub(self) -> material_pb2_grpc.ObjectServiceStub:
        return material_pb2_grpc.ObjectServiceStub(self._channel)

    locked = grpc_data_property_read_only("properties.locked")
    status = grpc_data_property_read_only("properties.status", from_protobuf=status_type_from_pb)

    ply_type = grpc_data_property(
        "properties.ply_type",
        from_protobuf=ply_type_from_pb,
        to_protobuf=ply_type_to_pb,
    )
