PyACP
=====
|pyansys| |python| |pypi| |GH-CI| |codecov| |MIT| |black|

.. TODO: Replace `pyacp-private` with `pyacp` everywhere before release.

.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
    :target: https://docs.pyansys.com/
    :alt: PyAnsys

.. |python| image:: https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue.svg
    :target: https://pypi.org/project/ansys-acp-core
    :alt: Python

.. |pypi| image:: https://img.shields.io/pypi/v/pyacp.svg?logo=python&logoColor=white
    :target: https://pypi.org/project/ansys-acp-core
    :alt: PyPI

.. |codecov| image:: https://codecov.io/gh/pyansys/pyacp-private/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/pyansys/pyacp-private
    :alt: Codecov

.. |GH-CI| image:: https://github.com/pyansys/pyacp-private/actions/workflows/ci_cd.yml/badge.svg
    :target: https://github.com/pyansys/pyacp-private/actions/workflows/ci_cd.yml
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

.. code::

    pip install git+https://github.com/pyansys/pyacp-private

For installing PyACP in development mode, see the `Development Setup`_ instructions below.


Documentation
-------------

The PyACP documentation can be viewed online at https://dev.acp.docs.pyansys.com.


Getting Started
---------------

Launching ACP locally
'''''''''''''''''''''

You can launch the ACP server locally by using ``launch_acp``:

.. code:: python

    from ansys.acp.core import launch_acp

    server = launch_acp(server_bin="<PATH_TO_ACP_GRPCSERVER>")

The ``<PATH_TO_ACP_GRPCSERVER>`` is the location of the ``acp_grpcserver`` executable
in your Ansys installation. For example, ``r"C:\Program Files\ANSYS Inc\v231\ACP\acp_grpcserver.exe"``.


Launching ACP in a Docker container
'''''''''''''''''''''''''''''''''''

Alternatively, you can use Docker to run the ACP server. After installing Docker on your
machine, you can use ``launch_acp_docker``:

.. code:: python

    from ansys.acp.core import launch_acp_docker

    server = launch_acp_docker(license_server="<LICENSE_SERVER>")

Here, ``<LICENSE_SERVER>`` is the address of your license server, e.g. ``1055@my.licenseserver.com``

Optionally, you can mount a local directory in the Docker container. This will give the container
access to the files in this directory.

.. code:: python

    server = launch_acp_docker(
        license_server="<LICENSE_SERVER>",
        mount_directories={"<LOCAL_DIRECTORY>": "/home/container/mounted_data"}
    )

The ``<LOCAL_DIRECTORY>`` is the path to the mounted directory on your machine, and
``/home/container/mounted_data`` is the path under which the container will see these files.

Basic Usage
'''''''''''

Once the server is running, we can start working with PyACP. For example, to load an ACP
Model from an existing file:

.. code:: python

    >>> from ansys.acp.core import Model
    >>> model = Model.from_file(path="<MODEL_PATH>", server=server)
    >>> model.name
    'ACP Model'

Development Setup
-----------------

Installation
''''''''''''

Installing PyACP in developer mode allows you to modify the source and enhance it. Before contributing to the project,
please refer to the `PyAnsys Developer's guide`_.

You will need to follow these steps:

1. Start by cloning this repository, and entering the newly created directory:

    .. code:: bash

        git clone https://github.com/pyansys/pyacp-private
        cd pyacp-private

2. Make sure you have the latest version of poetry:

    .. code:: bash

        python -m pip install pipx
        pipx ensurepath
        pipx install poetry

3. Install the project and all its development dependencies using poetry. This also takes care of
   creating a new virtual environment:

    .. code:: bash

        poetry install --extras all

   This step installs pyACP in an editable mode (no build step is needed, no re-install when changing the code).

4. Activate your development virtual environment with:

    .. code:: bash

        poetry shell

.. TODO: If we add tox, add instructions on its use here.

.. 6. Verify your development installation by running:

..     .. code:: bash

..         tox

Testing
'''''''

.. TODO: If we add tox, add instructions on its use here.

The PyACP test suite uses `pytest`_. You can run it with

.. code:: bash

    pytest --license-server=<YOUR_LICENSE_SERVER>

Pre-commit hooks
''''''''''''''''

Style and linter checks are run through the `pre-commit`_ tool. You can run these checks with

.. code:: bash

    pre-commit run --all-files

We also recommend installing pre-commit into your repository:

.. code:: bash

    pre-commit install

This will run the pre-commit hooks on the changed files before every ``git commit``. If you ever
need to create a commit without running the hooks, you can skip them with ``git commit -n``.

Documentation
'''''''''''''

The documentation can be built locally using `Sphinx`_.

On Linux & MacOS:

.. code:: sh

    make -C doc html

On Windows:

.. code:: batch

    cd doc; .\make.bat html

The generated HTML files can be viewed with the browser of your choice.

Distribution
''''''''''''

The following commands can be used to build and check the PyACP package:

.. code:: bash

    poetry build
    twine check dist/*

This creates both a source distribution, and a wheel file. An alternative is

.. code:: bash

    pip install build
    python -m build --wheel

License
-------
``PyACP`` is licensed under the MIT license. Please see the `LICENSE <https://github.com/pyansys/pyacp-private/raw/main/LICENSE>`_ for more details.


.. _black: https://github.com/psf/black
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _isort: https://github.com/PyCQA/isort
.. _PyAnsys Developer's guide: https://dev.docs.pyansys.com/
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/stable/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _tox: https://tox.wiki/
