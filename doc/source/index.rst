.. jinja:: main_toctree

    .. toctree::
        :hidden:
        :maxdepth: 3

        self
        intro
        {% if not skip_gallery %}
        examples/index
        {% endif %}
        howto/index
        {% if not skip_api %}
        api/index
        {% endif %}
        contribute


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

.. jinja:: main_toctree

    .. grid:: 1 1 2 2
        :gutter: 2

        .. grid-item-card:: :octicon:`rocket` Getting started
            :link: intro
            :link-type: doc

            Contains installation instructions and a simple example to get you
            started with PyACP.

        .. grid-item-card:: :octicon:`light-bulb` How-to guides
            :link: howto/index
            :link-type: doc

            Guides on how to achieve specific tasks with PyACP.

        .. grid-item-card:: :octicon:`play` Examples
            {% if not skip_gallery %}
            :link: examples/index
            :link-type: doc
            {% endif %}

            A collection of examples demonstrating the capabilities of PyACP.

        .. grid-item-card:: :octicon:`file-code` API reference
            {% if not skip_api %}
            :link: api/index
            :link-type: doc
            {% endif %}

            Describes the public Python classes, methods, and functions.

        .. grid-item-card:: :octicon:`code` Contribute
            :link: contribute
            :link-type: doc
            :columns: 12

            Information on how to contribute to PyACP.

Key features
^^^^^^^^^^^^

TODO

Limitations
^^^^^^^^^^^

TODO
