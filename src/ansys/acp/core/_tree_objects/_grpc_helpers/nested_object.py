from ..base import TreeObjectBase
from .protocols import ObjectInfo, ResourceStub


class NestedGrpcObject(TreeObjectBase):
    def __init__(self, parent_object: TreeObjectBase):
        self._parent_object: TreeObjectBase = parent_object

    @property
    def _pb_object(self) -> ObjectInfo:
        return self._parent_object._pb_object

    @_pb_object.setter
    def _pb_object(self, value: ObjectInfo) -> None:
        self._parent_object._pb_object = value

    def _get_stub(self) -> ResourceStub:
        return self._parent_object._get_stub()

    @property
    def _is_stored(self) -> bool:
        return self._parent_object._is_stored
