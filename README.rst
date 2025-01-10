.. image:: https://github.com/ansys/pyacp/blob/feat/pyacp_logo/doc/source/_static/pyacp.svg
    :width: 400
    :alt: PyACP Logo
    :align: center

|pyansys| |python| |pypi| |GH-CI| |codecov| |MIT| |black|

.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
    :target: https://docs.pyansys.com/
    :alt: PyAnsys

.. |python| image:: https://img.shields.io/pypi/pyversions/ansys-acp-core?logo=pypi
    :target: https://pypi.org/project/ansys-acp-core
    :alt: Python

.. |pypi| image:: https://img.shields.io/pypi/v/ansys-acp-core.svg?logo=python&logoColor=white
    :target: https://pypi.org/project/ansys-acp-core
    :alt: PyPI

.. |codecov| image:: https://codecov.io/gh/ansys/pyacp/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/ansys/pyacp
    :alt: Codecov

.. |GH-CI| image:: https://github.com/ansys/pyacp/actions/workflows/ci_cd.yml/badge.svg
    :target: https://github.com/ansys/pyacp/actions/workflows/ci_cd.yml
    :alt: GH-CI

.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
    :target: https://github.com/psf/black
    :alt: Black


A Python client for Ansys Composite PrepPost (ACP).

Installation
------------

Install PyACP with:

.. code-block::

    pip install ansys-acp-core[all]


For installing PyACP in development mode, see the `Development Setup`_ instructions below.

Documentation
-------------

The PyACP documentation can be viewed online at https://acp.docs.pyansys.com.

.. _launching_server:

Getting Started
---------------

Launching ACP
^^^^^^^^^^^^^

The ACP server can be started with ``launch_acp``:

.. code-block:: python

    import ansys.acp.core as pyacp

    acp = pyacp.launch_acp()


Basic Usage
^^^^^^^^^^^

Once the server is running, we can start working with PyACP. For example, to load an ACP
Model from an existing file:

.. code-block:: pycon

    >>> remote_path = acp.upload_file(local_path="<MODEL_PATH>")
    >>> model = acp.import_model(path=remote_path)
    >>> model.name
    'ACP Model'

.. START_MARKER_FOR_SPHINX_DOCS

Development Setup
-----------------

Installation
^^^^^^^^^^^^

Installing PyACP in developer mode allows you to modify the source and enhance it. Before contributing to the project,
please refer to the `PyAnsys Developer's guide`_.

You will need to follow these steps:

1.  Start by cloning this repository, and entering the newly created directory:

    .. code-block:: bash

        git clone https://github.com/ansys/pyacp
        cd pyacp

2.  Make sure you have the latest version of poetry:

    .. code-block:: bash

        python -m pip install pipx
        pipx ensurepath
        pipx install poetry

    .. note::

        At this point, you may need to restart your shell or editor to ensure that the new ``poetry`` command is available.

4.  Install the project and all its development dependencies using poetry. This also takes care of
    creating a new virtual environment:

    .. code-block:: bash

        poetry install --with dev,test --all-extras

    This step installs PyACP in an editable mode (no build step is needed, no re-install when changing the code).

5.  Activate your development virtual environment with:

    .. code-block:: bash

        poetry shell

Testing
^^^^^^^

The PyACP test suite uses `pytest`_. You can run it with

.. code-block:: bash

    pytest --license-server=<YOUR_LICENSE_SERVER> tests/unittests

Benchmarking
^^^^^^^^^^^^

As part of the test suite, we run some performance benchmarks. These can be run with

.. code-block:: bash

    pytest --license-server=<YOUR_LICENSE_SERVER> tests/benchmarks


Additional options can be found in the `pytest-benchmark documentation <https://pytest-benchmark.readthedocs.io/en/latest/usage.html>`_.

**NOTE:** The benchmarks use the ``tc-netem`` Linux kernel module to simulate a slow network
connection within a Docker container. This is available only on Linux, not on Docker for MacOS
or Windows.

The benchmark results from the ``main`` branch are uploaded to https://acp.docs.pyansys.com/benchmarks.

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
Before generating the documentation, configure the PyACP server via the
``ansys-launcher``, see `Launching ACP <launching_server>`_ above.
If Ansys is installed the examples can directly built with `Sphinx`_.

On Linux & MacOS:

.. code-block:: sh

    make -C doc html

On Windows:

.. code-block:: batch

    cd doc; .\make.bat html

The generated HTML files can be viewed with the browser of your choice.

Alternatively you can build the documentation by starting a mapdl and pydpf-composites docker
container. First ensure that you have accepted the DPF Preview License Agreement by setting the
ANSYS_DPF_ACCEPT_LA environment variable to Y
(see `DPF Preview License Agreement <https://dpf.docs.pyansys.com/version/stable/user_guide/getting_started_with_dpf_server.html#dpf-preview-license-agreement>`_
). In addition the  ANSYSLMD_LICENSE_FILE environment variable needs be set to a
valid license server (e.g ``1055@mylicenseserver.com``). Then start the docker containers with:

.. code-block:: bash

    docker compose -f docker-compose/docker-compose-extras.yaml up -d

Then build the documentation with the `Sphinx`_ commands mentioned above.

On Windows, you can use the shipped shell script:

.. code-block:: batch

    .\doc\create_doc_windows.ps1

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

.. END_MARKER_FOR_SPHINX_DOCS

License
-------

``PyACP`` is licensed under the MIT license. Please see the `LICENSE <https://github.com/ansys/pyacp/raw/main/LICENSE>`_ for more details.

.. _black: https://github.com/psf/black
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _isort: https://github.com/PyCQA/isort
.. _PyAnsys Developer's guide: https://dev.docs.pyansys.com/
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/stable/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
