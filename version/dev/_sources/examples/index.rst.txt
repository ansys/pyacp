.. _ref_examples:

..
   Add links to the gallery examples which would otherwise cause a warning due
   to missing references

.. jinja:: conditional_skip

   {% if skip_gallery %}
   .. _sphx_glr_examples_gallery_examples_001_basic_flat_plate.py:

   {% endif %}

   ========
   Examples
   ========

   {% if not skip_gallery %}
   .. include:: gallery_examples/index.rst
      :start-line: 2
   {% else %}
   .. note::

      The gallery examples are not included in this build of the documentation.
   {% endif %}
