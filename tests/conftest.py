# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Pytest configuration file for ansys-acp-core tests."""
from collections.abc import Generator
from contextlib import contextmanager
import logging
import os
import pathlib
import shutil
import tempfile

import docker
from hypothesis import settings
from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import (
    ACPInstance,
    ConnectLaunchConfig,
    DirectLaunchConfig,
    DockerComposeLaunchConfig,
    LaunchMode,
    launch_acp,
)
from ansys.acp.core._server.common import ServerProtocol
from ansys.acp.core._typing_helper import PATH
from ansys.tools.local_product_launcher.config import set_config_for

__all__ = [
    "pytest_addoption",
    "model_data_dir",
    "acp_instance",
    "check_grpc_server_before_run",
    "clear_models_before_run",
    "load_model_from_tempfile",
    "TEST_ROOT_DIR",
    "SOURCE_ROOT_DIR",
    "SERVER_BIN_OPTION_KEY",
    "SERVER_URLS_OPTION_KEY",
    "LICENSE_SERVER_OPTION_KEY",
    "DOCKER_IMAGENAME_OPTION_KEY",
    "NO_SERVER_LOGS_OPTION_KEY",
    "BUILD_BENCHMARK_IMAGE_OPTION_KEY",
    "VALIDATE_BENCHMARKS_ONLY_OPTION_KEY",
    "SERVER_STARTUP_TIMEOUT",
]


settings.register_profile("fast", max_examples=10)
settings.load_profile("fast")

logging.getLogger("ansys.acp.core").setLevel(logging.DEBUG)

TEST_ROOT_DIR = pathlib.Path(__file__).parent
SOURCE_ROOT_DIR = TEST_ROOT_DIR.parent

SERVER_BIN_OPTION_KEY = "--server-bin"
LICENSE_SERVER_OPTION_KEY = "--license-server"
SERVER_URLS_OPTION_KEY = "--server-urls"
DOCKER_IMAGENAME_OPTION_KEY = "--docker-image"
NO_SERVER_LOGS_OPTION_KEY = "--no-server-log-files"
BUILD_BENCHMARK_IMAGE_OPTION_KEY = "--build-benchmark-image"
VALIDATE_BENCHMARKS_ONLY_OPTION_KEY = "--validate-benchmarks-only"
SERVER_STARTUP_TIMEOUT = 30.0
SERVER_STOP_TIMEOUT = 1.0

pytest.register_assert_rewrite("common")


# Add pytest command-line options
def pytest_addoption(parser: pytest.Parser) -> None:
    """Add command-line options to pytest."""
    parser.addoption(
        SERVER_BIN_OPTION_KEY,
        action="store",
        help="Path of the gRPC server executable",
    )
    parser.addoption(
        DOCKER_IMAGENAME_OPTION_KEY,
        action="store",
        help=(
            "Docker image to be used for running the test. Only used if "
            f"'{SERVER_BIN_OPTION_KEY}' and '{SERVER_URLS_OPTION_KEY}' are not set."
        ),
        default="ghcr.io/ansys/acp:latest",
    )
    parser.addoption(
        LICENSE_SERVER_OPTION_KEY,
        action="store",
        help="Value of the ANSYSLMD_LICENSE_FILE for the gRPC server.",
    )
    parser.addoption(
        SERVER_URLS_OPTION_KEY,
        action="store",
        help="URLs of the gRPC server and file transfer server, separated by a comma.",
    )
    parser.addoption(
        NO_SERVER_LOGS_OPTION_KEY,
        action="store_true",
        help="If set, the server log is ignored instead of written to a file.",
    )
    parser.addoption(
        BUILD_BENCHMARK_IMAGE_OPTION_KEY,
        action="store_true",
        help="Build the 'pyacp-benchmark-runner' image.",
    )
    parser.addoption(
        VALIDATE_BENCHMARKS_ONLY_OPTION_KEY,
        action="store_true",
        help="Run the benchmarks only for the fastest network configuration.",
    )


@pytest.fixture(scope="session")
def _configure_launcher(request: pytest.FixtureRequest) -> None:
    """Parse test options and set up server handling."""
    server_bin = request.config.getoption(SERVER_BIN_OPTION_KEY)
    license_server = request.config.getoption(LICENSE_SERVER_OPTION_KEY)
    server_urls = request.config.getoption(SERVER_URLS_OPTION_KEY)

    if sum(bool(option) for option in (server_bin, server_urls, license_server)) != 1:
        raise ValueError(
            f"Exactly one of '{SERVER_BIN_OPTION_KEY}', '{LICENSE_SERVER_OPTION_KEY}' and "
            f"'{SERVER_URLS_OPTION_KEY}' must be specified."
        )

    if request.config.getoption(NO_SERVER_LOGS_OPTION_KEY):
        server_log_stdout: PATH = os.devnull
        server_log_stderr: PATH = os.devnull
    else:
        server_log_stdout = TEST_ROOT_DIR / "server_log_out.txt"
        server_log_stderr = TEST_ROOT_DIR / "server_log_err.txt"

    if server_bin:
        # Run the ACP server directly, with the provided binary.
        # This assumes that licensing is already configured on the host.
        set_config_for(
            product_name="ACP",
            launch_mode=LaunchMode.DIRECT,
            config=DirectLaunchConfig(
                binary_path=server_bin,
                stdout_file=str(server_log_stdout),
                stderr_file=str(server_log_stderr),
            ),
            overwrite_default=True,
        )
    elif server_urls:
        # Connect to an existing ACP server.
        acp_url, filetransfer_url = server_urls.split(",")
        set_config_for(
            product_name="ACP",
            launch_mode=LaunchMode.CONNECT,
            config=ConnectLaunchConfig(url_acp=acp_url, url_filetransfer=filetransfer_url),
            overwrite_default=True,
        )

    else:
        # If no binary is provided, use docker compose for running
        # the ACP server.
        image_name = request.config.getoption(DOCKER_IMAGENAME_OPTION_KEY)
        image_name_filetransfer = "ghcr.io/ansys/tools-filetransfer:latest"
        # We distinguish between local and remote images by checking if
        # the image name contains a slash. This is somewhat crude, but works
        # for now.
        if "/" in image_name:
            docker.from_env().images.pull(image_name)
        docker.from_env().images.pull(image_name_filetransfer)

        set_config_for(
            product_name="ACP",
            launch_mode=LaunchMode.DOCKER_COMPOSE,
            config=DockerComposeLaunchConfig(
                image_name_pyacp=image_name,
                image_name_filetransfer=image_name_filetransfer,
                license_server=license_server,
                keep_volume=False,
            ),
            overwrite_default=True,
        )


@pytest.fixture(scope="session")
def model_data_dir() -> pathlib.Path:
    """Test data path, in the host filesystem."""
    res_path = (TEST_ROOT_DIR / "data").resolve()
    assert res_path.is_dir(), f"Could not find data directory at '{res_path}'."
    return res_path


@pytest.fixture(scope="session")
def acp_instance(_configure_launcher) -> Generator[ACPInstance[ServerProtocol], None, None]:
    """Provide the currently active gRPC server."""
    yield launch_acp(timeout=SERVER_STARTUP_TIMEOUT)


@pytest.fixture(autouse=True)
def check_grpc_server_before_run(
    acp_instance: ACPInstance[ServerProtocol],
) -> Generator[None, None, None]:
    """Check if the server still responds before running each test, otherwise restart it."""
    try:
        acp_instance.wait(timeout=1.0)
    except RuntimeError:
        acp_instance.restart(stop_timeout=SERVER_STOP_TIMEOUT)
        acp_instance.wait(timeout=SERVER_STARTUP_TIMEOUT)
    yield


@pytest.fixture(autouse=True)
def clear_models_before_run(acp_instance):
    """Delete all existing models before the test is executed."""
    acp_instance.clear()


@pytest.fixture
def load_model_from_tempfile(model_data_dir, acp_instance):
    @contextmanager
    def inner(relative_file_path="minimal_complete_model_no_matml_link.acph5", format="acp:h5"):
        with tempfile.TemporaryDirectory() as tmp_dir:
            source_path = model_data_dir / relative_file_path

            if acp_instance.is_remote:
                file_path = acp_instance.upload_file(source_path)
            else:
                # Copy the file to a temporary directory, so the original file is never
                # modified. This can happen for example when a geometry reload happens.
                file_path = shutil.copy(source_path, tmp_dir)

            yield acp_instance.import_model(path=file_path, format=format)

    return inner


@pytest.fixture
def load_model_imported_plies_from_tempfile(model_data_dir, acp_instance):
    @contextmanager
    def inner(relative_file_path="minimal_model_imported_plies.acph5", format="acp:h5"):
        with tempfile.TemporaryDirectory() as tmp_dir:
            source_path = model_data_dir / relative_file_path

            if acp_instance.is_remote:
                file_path = acp_instance.upload_file(source_path)
            else:
                # Copy the file to a temporary directory, so the original file is never
                # modified. This can happen for example when a geometry reload happens.
                file_path = shutil.copy(source_path, tmp_dir)

            yield acp_instance.import_model(path=file_path, format=format)

    return inner


@pytest.fixture
def load_cad_geometry(model_data_dir, acp_instance):
    @contextmanager
    def inner(model, relative_file_path="square_and_solid.stp"):
        cad_file_path = acp_instance.upload_file(model_data_dir / relative_file_path)
        yield model.create_cad_geometry(
            external_path=cad_file_path,
        )

    return inner


@pytest.fixture
def raises_before_version(acp_instance):
    """Mark a test as expected to fail before a certain server version."""

    @contextmanager
    def inner(version: str):
        if parse_version(acp_instance.server_version) < parse_version(version):
            with pytest.raises(RuntimeError):
                yield
        else:
            yield

    return inner


@pytest.fixture
def skip_before_version(acp_instance):
    """Skip a test before a certain server version."""

    def inner(version: str):
        if parse_version(acp_instance.server_version) < parse_version(version):
            pytest.skip(f"Test is not supported before version {version}")

    return inner


@pytest.fixture
def tempdir_if_local_acp(acp_instance):
    """
    Context manager which provides a temporary directory if the ACP server is local.
    Otherwise, an empty path is provided.
    """

    @contextmanager
    def inner():
        if acp_instance.is_remote:
            yield pathlib.PurePosixPath(".")
        else:
            with tempfile.TemporaryDirectory() as tmp_dir:
                yield pathlib.Path(tmp_dir)

    return inner
