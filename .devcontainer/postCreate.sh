#!/bin/bash

poetry config http-basic.pyansys_private_pypi TOKEN $PYANSYS_PYPI_PRIVATE_READ_PAT
poetry install --with=dev,test
poetry run pre-commit install --install-hooks
poetry run ansys-launcher configure ACP docker_compose --image_name_pyacp=ghcr.io/ansys-internal/pyacp:latest --image_name_filetransfer=ghcr.io/ansys-internal/tools-filetransfer:latest --keep_volume=false --license_server=1055@$LICENSE_SERVER
