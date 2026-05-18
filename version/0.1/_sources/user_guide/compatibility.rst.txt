Compatibility
=============

Server version compatibility
----------------------------

PyACP is compatible with all versions of the ACP gRPC server since version 2024R2.

However, some features are not available when using older versions of the server.
Version 2025R1 is the first full release of the ACP gRPC server, which makes
almost all features of ACP available through PyACP.

Added in 2025R1
~~~~~~~~~~~~~~~

The following features were added in version 2025R1 of the ACP gRPC server.

Tree objects
''''''''''''

- :class:`.ButtJointSequence`
- :class:`.CutOffGeometry`
- :class:`.ExtrusionGuide`
- :class:`.FieldDefinition`
- :class:`.ImportedAnalysisPly`
- :class:`.ImportedModelingPly`
- :class:`.ImportedProductionPly`
- :class:`.ImportedSolidModel`
- :class:`.InterfaceLayer`
- :class:`.LayupMappingObject`
- :class:`.SamplingPoint`
- :class:`.SectionCut`
- :class:`.SnapToGeometry`
- :class:`.SolidElementSet`
- :class:`.SolidModel`

Methods
'''''''

- :meth:`.Model.import_hdf5_composite_cae`
- :meth:`.Model.export_hdf5_composite_cae`
- :meth:`.Model.import_materials`
- :meth:`.Model.export_modeling_ply_geometries`

Other features
''''''''''''''

- Mesh attributes for classes other than the :class:`.Model` class.
- The ``.shell_mesh`` and ``.solid_mesh`` attributes.


Upgrading PyACP
---------------

The following section describes how to upgrade to newer versions of PyACP.

Upgrading from the beta version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The beta version of PyACP did not yet provide a stable API. Consequently, some
backwards-incompatible changes were made in the first stable release to improve
the API.

If you encounter any difficulties upgrading from the beta version, feel free to
open an `issue <https://github.com/ansys/pyacp/issues>`_ on the PyACP GitHub
repository.

Removed features
''''''''''''''''

- The ``ACPWorkflow`` class for managing file up- and download was removed. Instead,
  file up- and download is now managed automatically by default. You can directly
  use the :meth:`.ACPInstance.import_model` method for importing models, and methods
  such as :meth:`.Model.save`, :meth:`.Model.export_analysis_model`, or
  :meth:`.Model.export_hdf5_composite_cae` for saving / exporting data.
  See the :ref:`file management section <file_management>` for more information.
- The ``get_composite_post_processing_files`` function was removed, since it only
  covered the shell workflow. Instead, you can directly use the ``ansys.dpf.composites``
  API, as shown in the :ref:`workflow examples <workflow_examples>`.

New submodules
''''''''''''''

Some features were moved into submodules instead of being exposed at the top level
``ansys.acp.core`` module:

- Elemental, nodal, and mesh data types were moved to the ``ansys.acp.core.mesh_data`` submodule.
- The ``example_helpers`` submodule was moved to the ``ansys.acp.core.extras`` submodule.
- The ``get_dpf_unit_system`` function was moved to the ``ansys.acp.core.dpf_integration_helpers`` submodule.


Renamed classes
'''''''''''''''

The following classes were renamed:

- ``ACP`` renamed to ``ACPInstance``.
- ``DrapingMaterialType`` renamed to ``DrapingMaterialModel``.
- ``StatusType`` renamed to ``Status``.
- ``DimensionType`` renamed to ``PhysicalDimension``.
- ``CutoffMaterialType`` renamed to ``CutOffMaterialType``.
- ``CutoffRuleType`` renamed to ``CutOffRuleType``.
- ``CutoffSelectionRule`` renamed to ``CutOffSelectionRule``.
- ``CutoffSelectionRuleElementalData`` renamed to ``CutOffSelectionRuleElementalData`` and moved to  ``ansys.acp.core.mesh_data``.
- ``CutoffSelectionRuleNodalData`` renamed to ``CutOffSelectionRuleNodalData`` and moved to  ``ansys.acp.core.mesh_data``.
- ``PlyCutoffType`` renamed to ``PlyCutOffType``.
- ``DropoffMaterialType`` renamed to ``DropOffMaterialType``.


Renamed attributes
''''''''''''''''''

The following attributes were renamed:

- ``dimension_type`` renamed to ``physical_dimension`` on the ``LookUpTable1DColumn`` and ``LookUpTable3DColumn`` classes.
- ``draping_type`` renamed to ``draping`` on the ``ModelingPly`` class.
- ``include_rule_type`` renamed to ``include_rule`` on all selection rule classes.
- ``relative_rule_type`` renamed to ``relative_rule`` on all selection rule classes.
