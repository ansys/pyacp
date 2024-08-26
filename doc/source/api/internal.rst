Internal objects
----------------

.. warning::

    The following objects are used internally by PyACP. They should not be used directly by the user, and
    are subject to change without notice.

.. currentmodule:: ansys.acp.core

.. autosummary::
    :toctree: _autosummary
    :template: autosummary/internal/base.rst.jinja2

    _model_printer.Node
    _server.common.ControllableServerProtocol
    _server.common.ServerProtocol
    _tree_objects._grpc_helpers.edge_property_list.EdgePropertyList
    _tree_objects._grpc_helpers.edge_property_list.GenericEdgePropertyType
    _tree_objects._grpc_helpers.linked_object_list.ChildT
    _tree_objects._grpc_helpers.linked_object_list.LinkedObjectList
    _tree_objects._grpc_helpers.mapping.CreatableValueT
    _tree_objects._grpc_helpers.mapping.Mapping
    _tree_objects._grpc_helpers.mapping.MutableMapping
    _tree_objects._grpc_helpers.mapping.ValueT
    _tree_objects._grpc_helpers.polymorphic_from_pb.CreatableFromResourcePath
    _tree_objects._grpc_helpers.protocols.CreateRequest
    _tree_objects._grpc_helpers.protocols.ObjectInfo
    _tree_objects._mesh_data.MeshDataT
    _tree_objects._mesh_data.ScalarDataT
    _tree_objects.base.CreatableTreeObject
    _tree_objects.base.TreeObject
    _tree_objects.base.TreeObjectBase
    _tree_objects.base.ServerWrapper
    _tree_objects.material.property_sets.wrapper.TC
    _tree_objects.material.property_sets.wrapper.TV
    _workflow._LocalWorkingDir
