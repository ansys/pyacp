.. _api_reference:

API reference
=============

.. jinja:: conditional_skip

    {% if not skip_api %}
    This section describes the API of the public PyACP classes, functions,
    and attributes.

    .. currentmodule:: ansys.acp.core

    .. toctree::
        :maxdepth: 2

        server
        tree_objects
        mesh_data
        linked_object_definitions
        material_property_sets
        enum_types
        other_types
        plot_utils
        other_utils
        workflow
        example_helpers
        mechanical_integration_helpers
        internal
    {% else %}
    The API reference is not available in this documentation build.
    {% endif %}
