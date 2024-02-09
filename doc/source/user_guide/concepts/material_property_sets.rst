Material property sets
----------------------

Material property sets are used to define a certain aspect of the properties
of a material.
The attributes described in the following subsections determine how the
material property set can be used within PyACP.


Constant versus variable property sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Material property sets can either be constant or variable. Constant property
sets are defined by a single value for each property, while variable property
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

- :attr:`.PlyType.ISOTROPIC_HOMOGENEOUS_CORE`
- :attr:`.PlyType.ISOTROPIC`
- :attr:`.PlyType.ADHESIVE`

.. note::

    While a material is unstored (see :ref:`stored_vs_unstored`), the property set does not
    automatically change from orthotropic to isotropic or vice versa. While storing the
    material, the backend will check that the material definition is consistent.

Available attributes
''''''''''''''''''''

The available attributes for a given property set type changes depending on whether
the material is isotropic or orthotropic. For example, the :class:`.ConstantEngineeringConstants`
provides the following attributes for isotropic materials:

- ``E``, ``nu``

whereas for the orthotropic case, the following attributes are available:

- ``E1``, ``E2``, ``E3``, ``nu12``, ``nu13``, ``nu23``, ``G12``, ``G13``, ``G23``

Conversion rules
''''''''''''''''

To avoid accidentally using the wrong property set for a given material, PyACP
restricts how the ply type of a material can be changed. The following rules apply:

- The ply type can always be changed from an isotropic to an orthotropic type.
- When changing from an orthotropic to an isotropic type, the property sets must
  be *consistent* with their isotropic counterpart. For example, the
  ``E1``, ``E2``, and ``E3`` values must all be the same.

.. doctest::
    :hide:

    >>> import ansys.acp.core as pyacp
    >>> acp = pyacp.launch_acp()
    >>> path = acp.upload_file("../tests/data/minimal_complete_model.acph5")
    >>> model = acp.import_model(path=path)

Consider the following example:

.. doctest::

    >>> material = model.create_material(name="New Material")
    >>> material
    <Material with id 'New Material'>

First, convert to an isotropic ply type. This is allowed since the properties values are
consistent with an isotropic material.

.. doctest::

    >>> material.ply_type = pyacp.PlyType.ISOTROPIC
    >>> material.engineering_constants.E = 1e9
    >>> material.engineering_constants.nu = 0.3

Then convert to an orthotropic material. This is always allowed.

.. doctest::

    >>> material.ply_type = pyacp.PlyType.WOVEN
    >>> material.engineering_constants.E1 = 2e9

Now, the properties are no longer consistent with an isotropic material, so converting
back to an isotropic ply type is not allowed.

.. doctest::

    >>> material.ply_type = pyacp.PlyType.ISOTROPIC
    Traceback (most recent call last):
    ...
    ValueError: Invalid argument: Cannot set an isotropic ply type, since the given engineering constants are orthotropic: The G12 value does not match 'E1 / (2. * (1. + nu12))'.

Assignment rules
''''''''''''''''

Similar rules apply when assigning a new property set to a material:

- isotropic property sets can be assigned to both isotropic and orthotropic materials.
- orthotropic property can be assigned:

  - to orthotropic materials.
  - to isotropic materials, if their values are consistent with an isotropic material.

Continuing from the preceding example, we can assign either an orthotropic or isotropic property set to the orthotropic material:

.. doctest::

    >>> from ansys.acp.core.material_property_sets import ConstantEngineeringConstants
    >>> material.ply_type
    <PlyType.WOVEN: 'woven'>

.. doctest::

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

Now we can switch back to an isotropic ply type.

.. doctest::

    >>> material.ply_type = pyacp.PlyType.ISOTROPIC

An isotropic material property set can always be assigned to an isotropic material.

.. doctest::

    >>> material.engineering_constants = ConstantEngineeringConstants.from_isotropic_constants(
    ...     E=1.3e9, nu=0.5
    ... )

An orthotropic material property set can be assigned only if the values are consistent with an isotropic material.

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
