.. jinja:: conditional_skip

    .. toctree::
        :hidden:
        :maxdepth: 3

        intro
        user_guide/index
        examples/index
        {% if not skip_api %}
        api/index
        {% endif %}
        contributing


PyACP
-----

.. note::

    PyACP is currently released as a beta version. This means that the API may
    change in future releases. We encourage you to try PyACP and provide us with
    feedback.

PyACP enables modelling continuous-fiber composite structures from within your
Python environment. It provides access to the features of Ansys Composite
PrepPost (ACP) through a Python interface.

This makes PyACP a powerful tool for automating the design, analysis and
optimization of composite structures.

.. jinja:: conditional_skip

    .. grid:: 1 1 2 2
        :gutter: 2

        .. grid-item-card:: :octicon:`rocket` Getting started
            :link: intro
            :link-type: doc

            Contains installation instructions and a simple example to get you
            started with PyACP.

        .. grid-item-card:: :octicon:`tools` How-to guides
            :link: user_guide/howto/index
            :link-type: doc

            Guides on how to achieve specific tasks with PyACP.

        .. grid-item-card:: :octicon:`light-bulb` Concepts
            :link: user_guide/concepts/index
            :link-type: doc

            Explains the concepts and terminology used in PyACP.

        .. grid-item-card:: :octicon:`play` Examples
            :link: examples/index
            :link-type: doc

            A collection of examples demonstrating the capabilities of PyACP.

        .. grid-item-card:: :octicon:`file-code` API reference
            {% if not skip_api %}:link: api/index
            :link-type: doc
            {% endif %}

            Describes the public Python classes, methods, and functions.

        .. grid-item-card:: :octicon:`code` Contributing
            :link: contributing
            :link-type: doc

            Information on how to contribute to PyACP.


Limitations
^^^^^^^^^^^

* Only shell workflows are supported, solid models can not yet be defined using PyACP
* FieldDefinitions for variable material properties are not supported
* Section cuts cannot be visualized
* Sampling point analysis data is not available
