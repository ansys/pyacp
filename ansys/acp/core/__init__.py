"""This init file allows python to treat directories containing it as modules.

Import any methods you want exposed at your library level here.

For example, if you want to avoid this behavior:

.. code::

   >>> from ansys.acp.core.module import add

Then add the import within this module to enable:

.. code::

   >>> from ansys.product import library
   >>> library.add(1, 2)

.. note::
   The version should be defined here so it can be referenced at the
   library level. It is also used by the 'flit' packaging tool.

"""

__version__ = "0.1.0.dev0"

from .other_module import Complex

__all__ = ["Complex"]
