Visualize model
---------------

.. jinja:: conditional_skip

    {% if not skip_gallery %}
    This guide uses a model of a race car's front wing.

    .. pyvista-plot::
        :nofigs:
        :context:

        >>> import tempfile
        >>> import pathlib
        >>> import ansys.acp.core as pyacp
        >>> from ansys.acp.core import example_helpers

        >>> acp = pyacp.launch_acp()
        >>> tempdir = tempfile.TemporaryDirectory()
        >>> input_file = example_helpers.get_example_file(
        ...     example_helpers.ExampleKeys.RACE_CAR_NOSE_ACPH5, pathlib.Path(tempdir.name)
        ... )
        >>> path = acp.upload_file(input_file)
        >>> model = acp.import_model(path=path)

        >>> input_file_geometry = example_helpers.get_example_file(
        ...     example_helpers.ExampleKeys.RACE_CAR_NOSE_STEP, pathlib.Path(tempdir.name)
        ... )
        >>> path_geometry = acp.upload_file(input_file_geometry)
        >>> model.create_cad_geometry(name="nose_geometry", external_path=path_geometry)

        >>> model.update()

    Show the mesh
    ~~~~~~~~~~~~~

    Access the mesh data using the :attr:`.Model.mesh` attribute. This attribute, an instance of the :class:`.MeshData` class, can be converted to a PyVista mesh using the :meth:`.MeshData.to_pyvista` method.

    .. pyvista-plot::
        :context:

        >>> model.mesh.to_pyvista().plot()


    .. _directions_plotter:

    Showing the directions
    ~~~~~~~~~~~~~~~~~~~~~~

    Show the directions (such as normals, fiber directions, and orientations) of the model by using the :func:`.get_directions_plotter` helper function. This function takes the model, the components to visualize, and some optional parameters.

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

    Showing the mesh data
    ~~~~~~~~~~~~~~~~~~~~~

    Access the mesh data related to a specific ACP object using the ``elemental_data`` and ``nodal_data`` attributes. These attributes represent either scalar or vector data.

    Scalar data
    '''''''''''

    You can convert scalar data to a PyVista mesh using the :meth:`get_pyvista_mesh <.ScalarData.get_pyvista_mesh>` method. This method requires the base model mesh.

    For example, you can plot the total thickness of the model using this code:


    .. pyvista-plot::
        :context:

        >>> thickness_data = model.elemental_data.thickness
        >>> pyvista_mesh = thickness_data.get_pyvista_mesh(mesh=model.mesh)
        >>> pyvista_mesh.plot()

    Vector data
    '''''''''''

    Visualize vector data using the :func:`.get_directions_plotter` function shown in the preceding section :ref:`directions_plotter`. If you need more fine-grained control over the visualization, you can use the method shown in this section instead.

    Vector data can be converted to PyVista glyphs using the :meth:`get_pyvista_glyphs <.VectorData.get_pyvista_glyphs>` method. This method requires the base model mesh.

    You can also choose a scaling factor to change the size of the vector glyphs and a culling factor to reduce the number of glyphs plotted.


    .. pyvista-plot::
        :context:

        >>> production_ply = model.modeling_groups['nose'].modeling_plies['mp.nose.6'].production_plies['ProductionPly.20']
        >>> ply_offset = production_ply.nodal_data.ply_offset
        >>> ply_offset.get_pyvista_glyphs(mesh=model.mesh, scaling_factor=6., culling_factor=5).plot()


    The base mesh is not shown when plotting vector data using PyVista glyphs. To visualize the mesh, you can combine the mesh and glyphs together using a PyVista plotter.

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


    Showing geometries
    ~~~~~~~~~~~~~~~~~~

    You can view CAD geometries using their :attr:`visualization_mesh <.CADGeometry.visualization_mesh>` attribute. This attribute contains a tessellated (triangular) mesh that represents the geometry.

    For plotting, the tessellated mesh has a :meth:`.to_pyvista <.TriangleMesh.to_pyvista>` method that returns a PyVista :class:`PolyData <pyvista.PolyData>` object. To see its triangular nature, plot the mesh with the ``show_edges`` option set to ``True``.

    .. pyvista-plot::
        :context:

        >>> cad_geometry = model.cad_geometries['nose_geometry']
        >>> tessellated_mesh = cad_geometry.visualization_mesh
        >>> tessellated_mesh.to_pyvista().plot(show_edges=True)


    .. pyvista-plot::
        :context:
        :include-source: false

        >>> acp.stop(timeout=0)


    {% else %}
    .. note::

        This how-to is not built when building the gallery is disabled.
    {% endif %}
