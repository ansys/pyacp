

.. toctree::
    :hidden:
    :maxdepth: 3

    PyACP home<self>
    intro
    user_guide/index
    examples/index
    api/index
    contributing


PyACP
-----

PyACP enables modelling continuous-fiber composite structures from within your
Python environment. It provides access to the features of Ansys Composite
PrepPost (ACP) through a Python interface.

This makes PyACP a powerful tool for automating the design, analysis and
optimization of composite structures.

.. jinja:: conditional_skip

    .. grid:: 1 1 2 2
        :gutter: 2

        .. grid-item-card:: :octicon:`rocket` Getting started
            :link: getting_started
            :link-type: ref

            Contains installation instructions and a simple example to get you
            started with PyACP.

        .. grid-item-card:: :octicon:`tools` How-to guides
            :link: howto
            :link-type: ref

            Guides on how to achieve specific tasks with PyACP.

        .. grid-item-card:: :octicon:`light-bulb` Concepts
            :link: concepts
            :link-type: ref

            Explains the concepts and terminology used in PyACP.

        .. grid-item-card:: :octicon:`play` Examples
            :link: ref_examples
            :link-type: ref

            A collection of examples demonstrating the capabilities of PyACP.

        .. grid-item-card:: :octicon:`file-code` API reference
            :link: api_reference
            :link-type: ref

            Describes the public Python classes, methods, and functions.

        .. grid-item-card:: :octicon:`code` Contributing
            :link: contributing
            :link-type: ref

            Information on how to contribute to PyACP.

        .. grid-item-card:: :octicon:`mortar-board` ACP documentation
            :link: https://ansyshelp.ansys.com/public/?returnurl=/Views/Secured/prod_page.html?pn=Composites&pid=CompositePrepPost
            :columns: 12

            Describes the modeling features and techniques of Ansys Composite PrepPost.


.. _limitations:

Limitations
^^^^^^^^^^^

* Field definitions are currently only supported through (Py)Mechanical.
  The workflow from PyACP to (Py)MADL ignores field definitions.
* The PyACP to PyMADL workflow does not fully support variable materials.
* The PyACP to PyMechanical workflow is experimental and has the following limitations:

  * It only works on Windows, with a remote (not embedded) PyMechanical session.
  * Only one ACP shell or solid model is supported at a time.
  * Named selections defined in ACP are not transferred to PyMechanical.
  * The ``ansys.acp.core.mechanical_integration_helpers`` module may be
    changed or removed in future versions, when the corresponding features
    are available in PyMechanical directly.
  * Post-processing with the Composite Failure Tool inside Mechanical is not
    yet supported.

* Visualization and mesh data of imported plies are not supported yet.
* Section cuts cannot be visualized.
* Sampling point analysis data is not available.
* Imported solid model mapping statistics are not available.
