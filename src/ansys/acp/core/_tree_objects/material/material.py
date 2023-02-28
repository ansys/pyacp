from __future__ import annotations

from typing import Iterable

from ansys.api.acp.v0 import material_pb2, material_pb2_grpc

from .._grpc_helpers.property_helper import (
    grpc_data_property,
    grpc_data_property_read_only,
    mark_grpc_properties,
)
from ..base import CreatableTreeObject, IdTreeObject
from ..enums import PlyType, ply_type_from_pb, ply_type_to_pb, status_type_from_pb
from ..object_registry import register
from .property_set_base import _VariablePropertySet
from .property_sets import (
    ConstantDensity,
    ConstantEngineeringConstants,
    VariableDensity,
    VariableEngineeringConstants,
)


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
        if isinstance(self.density, _VariablePropertySet):
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
        if isinstance(self.engineering_constants, _VariablePropertySet):
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
