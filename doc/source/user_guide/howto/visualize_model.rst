Visualizing the model
---------------------

For this how-to guide, we will use an example model of a race car front wing.

.. pyvista-plot::
    :nofigs:
    :context:

    >>> import ansys.acp.core as pyacp
    >>> acp = pyacp.launch_acp()
    >>> path = acp.upload_file('/home/dgresch/tmp/race_car_nose.acph5')
    >>> model = acp.import_model(path=path)

Showing the mesh
~~~~~~~~~~~~~~~~

The mesh data can be accessed using the :attr:`.Model.mesh` attribute. This attribute is an instance of the :class:`.MeshData` class, and can be converted to a PyVista mesh using the :meth:`.MeshData.to_pyvista` method.

.. pyvista-plot::
    :context:

    >>> model.mesh.to_pyvista().plot()


Showing the directions
~~~~~~~~~~~~~~~~~~~~~~

To show the directions (for example normals, fiber directions, orientations, etc.) of the model, we can use the :func:`.get_directions_plotter` helper function. This function takes the model, the components to visualize, and some optional parameters.

The following example shows the orientation and fiber direction of a modeling ply.

.. pyvista-plot::
    :context:

    >>> modeling_ply = model.modeling_groups['nose'].modeling_plies['mp.nose.4']
    >>> elemental_data = modeling_ply.elemental_data
    >>> directions_plotter = pyacp.get_directions_plotter(
    ...     model=model,
    ...     components=[
    ...         elemental_data.orientation,
    ...         elemental_data.fiber_direction
    ...     ],
    ...     length_factor=10.,
    ...     culling_factor=10,
    ... )
    >>> directions_plotter.show()

The color scheme used in this plot for the various components matches the ACP GUI.

Showing mesh data
~~~~~~~~~~~~~~~~~

In general, the mesh data relating to a specific ACP object can be accessed using the ``elemental_data`` and ``nodal_data`` attributes. These attributes represent either scalar or vector data.

Scalar data
'''''''''''

Scalar data can be converted to a PyVista mesh using the :meth:`get_pyvista_mesh <.ScalarData.get_pyvista_mesh>` method. The base model mesh needs to be passed to this method.

For example, we can plot the total thickness of the model using the following code:


.. pyvista-plot::
    :context:

    >>> thickness_data = model.elemental_data.thickness
    >>> pyvista_mesh = thickness_data.get_pyvista_mesh(mesh=model.mesh)
    >>> pyvista_mesh.plot()

Vector data
'''''''''''

Vector data can be converted to PyVista glyphs using the :meth:`get_pyvista_glyphs <.VectorData.get_pyvista_glyphs>` method. Again, the base model mesh needs to be passed to this method.

We can also choose a scaling factor to change the size of the vector glyphs, and a culling factor to reduce the number of glyphs plotted.


.. pyvista-plot::
    :context:

    >>> production_ply = model.modeling_groups['nose'].modeling_plies['mp.nose.6'].production_plies['ProductionPly.20']
    >>> ply_offset = production_ply.nodal_data.ply_offset
    >>> ply_offset.get_pyvista_glyphs(mesh=model.mesh, scaling_factor=6., culling_factor=5).plot()


When plotting vector data in this way, the base mesh is not shown. To additionally show the mesh, we can combine the mesh and the glyphs using a PyVista plotter.

.. pyvista-plot::
    :context:

    >>> import pyvista
    >>> plotter = pyvista.Plotter()
    >>> _ = plotter.add_mesh(model.mesh.to_pyvista(), color="white", opacity=0.5)
    >>> _ = plotter.add_mesh(
    ...     ply_offset.get_pyvista_glyphs(mesh=model.mesh, scaling_factor=6., culling_factor=5),
    ...     color="blue"
    ... )
    >>> plotter.show()

.. note::

    The preceding plot may not render correctly as a static scene. See the interactive scene instead.

.. pyvista-plot::
    :context:
    :include-source: false

    >>> acp.stop(timeout=0)