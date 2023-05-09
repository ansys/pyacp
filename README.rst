PyACP
=====
|pyansys| |python| |pypi| |GH-CI| |codecov| |MIT| |black|

.. TODO: Replace `ansys-internal` with `ansys` everywhere before release.

.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
    :target: https://docs.pyansys.com/
    :alt: PyAnsys

.. |python| image:: https://img.shields.io/badge/Python-3.8%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue.svg
    :target: https://pypi.org/project/ansys-acp-core
    :alt: Python

.. |pypi| image:: https://img.shields.io/pypi/v/pyacp.svg?logo=python&logoColor=white
    :target: https://pypi.org/project/ansys-acp-core
    :alt: PyPI

.. |codecov| image:: https://codecov.io/gh/ansys-internal/pyacp/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/ansys-internal/pyacp
    :alt: Codecov

.. |GH-CI| image:: https://github.com/ansys-internal/pyacp/actions/workflows/ci_cd.yml/badge.svg
    :target: https://github.com/ansys-internal/pyacp/actions/workflows/ci_cd.yml
    :alt: GH-CI

.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
    :target: https://github.com/psf/black
    :alt: Black


A Python client for Ansys Composite PrepPost (ACP).

Overview
--------

.. TODO: Add a teaser for what can be done with PyACP.

Installation
------------

.. TODO: Update install instructions before release, to refer to the final package locations.

Install PyACP with:

.. code-block::

    pip install git+https://github.com/ansys-internal/pyacp

For installing PyACP in development mode, see the `Development Setup`_ instructions below.


Documentation
-------------

The PyACP documentation can be viewed online at https://acp.docs.pyansys.com.


.. _launching_server:

Getting Started
---------------

Launching ACP
^^^^^^^^^^^^^

Configure ACP using the `ansys-launcher <https://local-product-launcher.tools.docs.pyansys.com>`_ command line tool:

.. code-block:: bash

    ansys-launcher configure ACP <launch_mode>

where ``<launch_mode>`` is one of

* ``direct``: run ACP as a sub-process
* ``docker_compose``: run ACP in a docker container, using ``docker-compose`` and the `filetransfer service <https://github.com/ansys-internal/ansys-tools-filetransfer-server>`_ to manage files

The ``ansys-launcher`` prompts for the relevant options for each mode.

Having configured the launcher, the server can be started with ``launch_acp``:

.. code-block:: python

    import ansys.acp.core as pyacp

    server = pyacp.launch_acp()
    client = pyacp.Client(server)


Basic Usage
^^^^^^^^^^^

Once the server is running, we can start working with PyACP. For example, to load an ACP
Model from an existing file:

.. code-block:: pycon

    >>> remote_filename = client.upload_file(local_path="<MODEL_PATH>")
    >>> model = client.import_model(path=remote_filename)
    >>> model.name
    'ACP Model'

Development Setup
-----------------

Installation
^^^^^^^^^^^^

Installing PyACP in developer mode allows you to modify the source and enhance it. Before contributing to the project,
please refer to the `PyAnsys Developer's guide`_.

You will need to follow these steps:

1.  Start by cloning this repository, and entering the newly created directory:

    .. code-block:: bash

        git clone https://github.com/ansys-internal/pyacp
        cd pyacp

2.  Make sure you have the latest version of poetry:

    .. code-block:: bash

        python -m pip install pipx
        pipx ensurepath
        pipx install poetry
        poetry config installer.modern-installation false

    The ``poetry config`` call is a temporary workaround for https://github.com/pydata/pydata-sphinx-theme/issues/1253

3.  Install the project and all its development dependencies using poetry. This also takes care of
    creating a new virtual environment:

    .. code-block:: bash

        poetry install --with dev,test

   This step installs PyACP in an editable mode (no build step is needed, no re-install when changing the code).

4.  Activate your development virtual environment with:

    .. code-block:: bash

        poetry shell

.. TODO: If we add tox, add instructions on its use here.

.. 6. Verify your development installation by running:

..     .. code-block:: bash

..         tox

Testing
^^^^^^^

.. TODO: If we add tox, add instructions on its use here.

The PyACP test suite uses `pytest`_. You can run it with

.. code-block:: bash

    pytest --license-server=<YOUR_LICENSE_SERVER>

Pre-commit hooks
^^^^^^^^^^^^^^^^

Style and linter checks are run through the `pre-commit`_ tool. You can run these checks with

.. code-block:: bash

    pre-commit run --all-files

We also recommend installing pre-commit into your repository:

.. code-block:: bash

    pre-commit install

This will run the pre-commit hooks on the changed files before every ``git commit``. If you ever
need to create a commit without running the hooks, you can skip them with ``git commit -n``.

Documentation
^^^^^^^^^^^^^

To build the documentation, DPF Composites and MAPDL servers need to be running:

.. code-block:: bash

    docker-compose -f docker-compose/docker-compose-extras.yaml up -d

In addition, the PyACP server needs to be configured via ``ansys-launcher``, see `Launching ACP <launching_server>`_ above.

It can then be built using `Sphinx`_.

On Linux & MacOS:

.. code-block:: sh

    make -C doc html

On Windows:

.. code-block:: batch

    cd doc; .\make.bat html

The generated HTML files can be viewed with the browser of your choice.

Distribution
^^^^^^^^^^^^

The following commands can be used to build and check the PyACP package:

.. code-block:: bash

    poetry build
    twine check dist/*

This creates both a source distribution, and a wheel file. An alternative is

.. code-block:: bash

    pip install build
    python -m build --wheel

License
-------
``PyACP`` is licensed under the MIT license. Please see the `LICENSE <https://github.com/ansys-internal/pyacp/raw/main/LICENSE>`_ for more details.


.. _black: https://github.com/psf/black
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _isort: https://github.com/PyCQA/isort
.. _PyAnsys Developer's guide: https://dev.docs.pyansys.com/
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/stable/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _tox: https://tox.wiki/
