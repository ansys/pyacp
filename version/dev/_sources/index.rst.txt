..
    Just reuse the root readme to avoid duplicating the documentation.
    Provide any documentation specific to your online documentation
    here.

=============================
PyACP documentation |version|
=============================

.. include:: ../../README.rst

.. jinja:: main_toctree

    .. toctree::
        :hidden:
        :maxdepth: 3

        PyACP <self>
        {% if not skip_gallery %}
        examples/index
        {% endif %}
        {% if not skip_api %}
        api/index
        {% endif %}
