Input file for PyACP
--------------------

To start working with PyACP, an input file that contains the mesh is required. PyACP supports reading
the mesh from \*.cdb and \*.dat files with :meth:`.ACPWorkflow.from_cdb_file`. PyACP will read the mesh including - if they exist - coordinate systems, element, edge sets, and materials from the
input file. After the layup has been created with PyACP a \*.cdb file can be exported with :meth:`.ACPWorkflow.get_local_cdb_file`. This file
contains all the information contained in the initial input file plus the layup information and
materials added by PyACP. An attempt is made to preserve the original input file as much as possible.
This includes the original mesh, materials and boundary conditions.


Create an input file with Ansys Mechanical
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One way to create an input file for PyACP is to create a static structural setup and export the solver input file. To do this, follow these steps:

* Open Ansys workbench
* Add a "Static Structural" system
* Create or import a geometry in the geometry part of the static structural system (A3). Note: PyACP only supports shell geometries
* Open the Mechanical Model (A4)
* Assign a thickness and a material to the geometry (will be later overwritten by PyACP)
* Optional: Define boundary conditions
* Click on Static Structural (A5) in the tree and click on "Environment/Write Input File.." in the navigation bar.
* Save the input file in \*.dat format in the desired location.


The created input file can be read with :meth:`.ACPWorkflow.from_cdb_file`. See
:ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py` for a complete example.

.. note::

    The imported model will always contain the dummy material that was assigned to the geometry with the name "1".


Create an input file with Ansys Mechanical APDL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Open Ansys Mechanical APDL
* Load or create a model with APDL commands
* Write the \*.cdb file with the the ``CDWRITE`` command:

    .. code-block:: apdl

        CDWRITE,ALL,FILE,cdbfile.cdb

The created input file can be read with :meth:`.ACPWorkflow.from_cdb_file`. See
:ref:`sphx_glr_examples_gallery_examples_001_basic_flat_plate.py` for a complete example.

Notes on material handling
~~~~~~~~~~~~~~~~~~~~~~~~~~

Materials present in the input file (\*.cdb or \*.dat) are read into PyACP. The following rules apply:

* If the material has defined a UVID, the material is imported as locked. This means the material cannot be edited in PyACP. This is the case if the input file was created with Ansys Mechanical (see above). A UVID can be defined with the ``MP,UVID`` or ``MPDATAT,UNBL,16,UVID`` command.
* If the material has no UVID, the material is copied on import. Only the copied material appears in PyACP. The original material is not changed and will appear unmodified in the output file.


