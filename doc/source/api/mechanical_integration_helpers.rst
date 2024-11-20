Mechanical integration helpers
------------------------------

.. warning::

    The PyACP / PyMechanical integration is still experimental and will change
    in future releases.

    It is also limited in the following ways:

    - Only remote Mechanical sessions on Windows are supported.
    - Only one ACP shell or solid model can be imported into Mechanical.

    PyACP currently provides helper functions for integrating with PyMechanical.
    These functions will be replaced with native PyMechanical functions in the future.

.. currentmodule:: ansys.acp.core.mechanical_integration_helpers

.. autosummary::
    :toctree: _autosummary
    :template: autosummary/internal/base.rst.jinja2

    export_mesh_for_acp
    import_acp_composite_definitions
    import_acp_solid_model
