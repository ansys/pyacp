.. _input_file_for_pyacp:

Create input file for PyACP
---------------------------

To start working with PyACP, an input file that contains the mesh is required. PyACP supports reading
the mesh from \*.cdb and \*.dat files with :meth:`.ACPWorkflow.from_cdb_or_dat_file`. PyACP will read the mesh including - if they exist - coordinate systems, element sets,
edge sets and materials from the input file. Once the layup has been created with PyACP, you can export its CDB file with the :meth:`.ACPWorkflow.get_local_cdb_file` method. This file
contains all the data from the initial input file along with the layup information and
materials added by PyACP. An attempt is made to preserve the original input file as much as possible.
This includes the original mesh, materials, and boundary conditions. Therefore, you may directly use the exported CDB file
for an analysis through PyMAPDL. For more information, see :ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py`.

.. _input_file_from_mechanical:

Create an input file with Ansys Mechanical
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One way to create an input file for PyACP is to create a static structural setup and export the solver input file. To do this, follow these steps:

* Open Ansys Workbench.
* Add a "Static Structural" system.
* Create or import a geometry in the geometry cell of the static structural system (A3). Note that PyACP only supports shell geometries.
* Open the Mechanical Model (A4).
* Assign a thickness and a material to the geometry. (These are later overwritten by PyACP.)
* Optional: Define the boundary conditions.
* Select "Static Structural (A5)" in the tree and then click **Environment/Write Input File** in the navigation bar.
* Save the input file to a DAT file in the desired location.


The created input file can be read with the :meth:`.ACPWorkflow.from_cdb_or_dat_file` method.
For a complete example, see :ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py`.

.. note::

    The imported model always contains the dummy material named ``1`` that was assigned to the geometry.


Create an input file with Ansys Mechanical APDL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also create an input file for PyACP by performing these steps:

* Open Ansys Mechanical APDL
* Load or create a model with APDL commands
* Write the \*.cdb file with the ``CDWRITE`` command:

    .. code-block:: apdl

        CDWRITE,ALL,FILE,cdbfile.cdb

The created input file can be read with :meth:`.ACPWorkflow.from_cdb_or_dat_file`. See
:ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py` for a complete example.

Notes on material handling
~~~~~~~~~~~~~~~~~~~~~~~~~~

Materials present in the input file (\*.cdb or \*.dat) are read into PyACP. The following rules apply:

* If the material has defined a UVID, then the material is imported as locked. This means the material cannot be edited in PyACP. If the input file was created with Ansys Mechanical (see :ref:`input_file_from_mechanical`), this is always the case. In Mechanical APDL, you can define a UVID with the ``MP,UVID`` or ``MPDATAT,UNBL,16,UVID`` command.
* If the material has no UVID, then the material is copied on import. Only the copied material appears in PyACP. The original material is not changed and appears unmodified in the output file.
