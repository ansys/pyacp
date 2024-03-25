Material property sets
----------------------

Material property sets define certain aspects of the properties
of a material.
The attributes described in the following subsections explain how
you may use material property sets within PyACP.


Constant versus variable property sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Material property sets can either be constant or variable. Constant property
sets are defined by a single value per property. Variable property
sets depend on field variables such as temperature, fiber volume content, etc.

Currently, only the constant property sets can be modified with PyACP. Variable
property sets can be inspected, but not modified.


Isotropic versus orthotropic property sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following material property sets can be defined as either isotropic or orthotropic:

- Engineering constants, defined in the :class:`.ConstantEngineeringConstants` and :class:`.VariableEngineeringConstants` classes.
- Stress limits, defined in the  :class:`.ConstantStressLimits` and :class:`.VariableStressLimits` classes.
- Strain limits, defined in the :class:`.ConstantStrainLimits` and :class:`.VariableStrainLimits` classes.

Whether a material has isotropic or orthotropic properties is determined by its
ply type. The isotropic ply types are:

- :attr:`.PlyType.ISOTROPIC`
- :attr:`.PlyType.ADHESIVE`

The :attr:`.PlyType.ISOTROPIC_HOMOGENEOUS_CORE` ply type has isotropic Engineering Constants,
but orthotropic stress and strain limits.

.. note::

    While a material is unstored (see :ref:`stored_vs_unstored`), the property set does not
    automatically change from orthotropic to isotropic or vice versa. When storing the
    material, then the backend will ensure that its definition is consistent.

Available attributes
''''''''''''''''''''

The available attributes for a given property set type change depending on whether
the material is isotropic or orthotropic.
The following table lists the available attributes for the different property sets in
isotropic and orthotropic materials.

+-----------------------------+-----------------------+------------------------------------------------------------------------------------+
| Property set                | Isotropic attributes  | Orthotropic attributes                                                             |
+=============================+=======================+====================================================================================+
| Engineering constants       | ``E``, ``nu``         | ``E1``, ``E2``, ``E3``, ``nu12``, ``nu13``, ``nu23``, ``G12``, ``G13``, ``G23``    |
+-----------------------------+-----------------------+------------------------------------------------------------------------------------+
| Stress limits               | ``effective_stress``  | ``Xc``, ``Yc``, ``Zc``, ``Xt``, ``Yt``, ``Zt``, ``Sxy``, ``Syz``, ``Sxz``          |
+-----------------------------+-----------------------+------------------------------------------------------------------------------------+
| Strain limits               | ``effective_strain``  | ``eXc``, ``eYc``, ``eZc``, ``eXt``, ``eYt``, ``eZt``, ``eSxy``, ``eSyz``, ``eSxz`` |
+-----------------------------+-----------------------+------------------------------------------------------------------------------------+

Relation between isotropic and orthotropic property sets
''''''''''''''''''''''''''''''''''''''''''''''''''''''''

For stress and strain limits, the isotropic and orthotropic attributes are
independently defined. This means that when you change the ply type of a material,
you must redefine the stress and strain limits.

For engineering constants, however, the orthotropic and isotropic definitions
are interlinked. Therefore, when you change the ply type of a material, the
engineering constants are automatically converted.
To avoid accidental use of incorrect engineering constants, PyACP enforces 
conversion and assignment rules, as described later on this page.

Conversion rules
^^^^^^^^^^^^^^^^

The following rules apply when changing the ply type of a material:

- The ply type can always be changed from an isotropic to an orthotropic type.
- When changing from an orthotropic to an isotropic type, the engineering constants must
  be *consistent* with their isotropic counterpart. In particular, the
  following relations must hold:

  .. math::

      E_1 &= E_2 = E_3 \\
      \nu_{12} &= \nu_{13} = \nu_{23} \\
      G_{12} &= G_{13} = G_{23} = \frac{E_1}{2 \cdot (1 + \nu_{12})}

.. doctest::
    :hide:

    >>> import ansys.acp.core as pyacp
    >>> acp = pyacp.launch_acp()
    >>> path = acp.upload_file("../tests/data/minimal_complete_model_no_matml_link.acph5")
    >>> model = acp.import_model(path=path)

Consider the following example:

.. doctest::

    >>> material = model.create_material(name="New Material")
    >>> material
    <Material with id 'New Material'>

First, convert to an isotropic ply type. This is allowed since the engineering constants are
consistent with an isotropic material.

.. doctest::

    >>> material.ply_type = pyacp.PlyType.ISOTROPIC
    >>> material.engineering_constants.E = 1e9
    >>> material.engineering_constants.nu = 0.3

Then convert to an orthotropic material. This is always allowed.

.. doctest::

    >>> material.ply_type = pyacp.PlyType.WOVEN
    >>> material.engineering_constants.E1 = 2e9

Now, the engineering constants are no longer consistent with an isotropic material, so converting
back to an isotropic ply type is not allowed.

.. doctest::

    >>> material.ply_type = pyacp.PlyType.ISOTROPIC
    Traceback (most recent call last):
    ...
    ValueError: Invalid argument: Cannot set an isotropic ply type, since the given engineering constants are orthotropic: The G12 value does not match 'E1 / (2. * (1. + nu12))'.

Assignment rules
^^^^^^^^^^^^^^^^

Similar rules apply when assigning engineering constants to a material:

- Isotropic engineering constants can be assigned to both isotropic and orthotropic materials.
- Orthotropic engineering constants can be assigned:

  - to orthotropic materials.
  - to isotropic materials, if their values are consistent with an isotropic material.

Continuing from the preceding example, you can assign either orthotropic or isotropic engineering constants to the orthotropic material:

.. doctest::

    >>> material.ply_type
    <PlyType.WOVEN: 'woven'>

.. doctest::

    >>> from ansys.acp.core.material_property_sets import ConstantEngineeringConstants
    >>> material.engineering_constants = (
    ...     ConstantEngineeringConstants.from_orthotropic_constants(
    ...         E1=1e9,
    ...         E2=1.1e9,
    ...         E3=8e8,
    ...     )
    ... )
    >>> material.engineering_constants = ConstantEngineeringConstants.from_isotropic_constants(
    ...     E=1e9, nu=0.3
    ... )

Now you can switch back to an isotropic ply type.

.. doctest::

    >>> material.ply_type = pyacp.PlyType.ISOTROPIC

Isotropic engineering constants can always be assigned to an isotropic material.

.. doctest::

    >>> material.engineering_constants = ConstantEngineeringConstants.from_isotropic_constants(
    ...     E=1.3e9, nu=0.5
    ... )

Orthotropic engineering constants can be assigned only if the values are consistent with an isotropic material.

.. doctest::

    >>> material.engineering_constants = (
    ...     ConstantEngineeringConstants.from_orthotropic_constants(
    ...         E1=1e9,
    ...         E2=1e9,
    ...         E3=1e9,
    ...         G12=5e8,
    ...         G23=5e8,
    ...         G31=5e8,
    ...     )
    ... )
    >>> material.engineering_constants = (
    ...     ConstantEngineeringConstants.from_orthotropic_constants(
    ...         E1=1e9,
    ...         E2=1.1e9,
    ...         E3=1.2e9,
    ...     )
    ... )
    Traceback (most recent call last):
    ...
    ValueError: Invalid argument: Cannot set an isotropic ply type, since the given engineering constants are orthotropic: The G12 value does not match 'E1 / (2. * (1. + nu12))'.
