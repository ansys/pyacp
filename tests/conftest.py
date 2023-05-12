"""Pytest configuration file for ansys-acp-core tests."""
from contextlib import contextmanager
import logging
import os
import pathlib
import tempfile
from typing import Generator, cast

import docker
from hypothesis import settings
import pytest

from ansys.acp.core import Client, launch_acp
from ansys.acp.core._server import (
    ControllableServerProtocol,
    DirectLaunchConfig,
    DockerComposeLaunchConfig,
    LaunchMode,
)
from ansys.acp.core._typing_helper import PATH
from ansys.tools.local_product_launcher.config import set_config_for

__all__ = [
    "pytest_addoption",
    "model_data_dir",
    # "convert_temp_path",
    "grpc_server",
    "check_grpc_server_before_run",
    "clear_models_before_run",
    "load_model_from_tempfile",
]


settings.register_profile("fast", max_examples=10)
settings.load_profile("fast")

logging.getLogger("ansys.acp.core").setLevel(logging.DEBUG)

TEST_ROOT_DIR = pathlib.Path(__file__).parent
SOURCE_ROOT_DIR = TEST_ROOT_DIR.parent

SERVER_BIN_OPTION_KEY = "--server-bin"
LICENSE_SERVER_OPTION_KEY = "--license-server"
DOCKER_IMAGENAME_OPTION_KEY = "--docker-image"
NO_SERVER_LOGS_OPTION_KEY = "--no-server-log-files"
BUILD_BENCHMARK_IMAGE_OPTION_KEY = "--build-benchmark-image"
SERVER_STARTUP_TIMEOUT = 30.0

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
            f"'{SERVER_BIN_OPTION_KEY}' is not set."
        ),
        default="ghcr.io/ansys-internal/pyacp:latest",
    )
    parser.addoption(
        LICENSE_SERVER_OPTION_KEY,
        action="store",
        help="Value of the ANSYSLMD_LICENSE_FILE for the gRPC server.",
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


@pytest.fixture(scope="session")
def _configure_launcher(request: pytest.FixtureRequest) -> None:
    """Parse test options and set up server handling."""
    server_bin = request.config.getoption(SERVER_BIN_OPTION_KEY)
    license_server = request.config.getoption(LICENSE_SERVER_OPTION_KEY)

    if bool(server_bin) == bool(license_server):
        raise ValueError(
            f"Exactly one of '{SERVER_BIN_OPTION_KEY}' or '{LICENSE_SERVER_OPTION_KEY}' must be specified."
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

    else:
        # If no binary is provided, use docker-compose for running
        # the ACP server.
        image_name = request.config.getoption(DOCKER_IMAGENAME_OPTION_KEY)
        image_name_filetransfer = "ghcr.io/ansys-internal/tools-filetransfer:latest"
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
def grpc_server(_configure_launcher) -> Generator[ControllableServerProtocol, None, None]:
    """Provide the currently active gRPC server."""
    server = cast(ControllableServerProtocol, launch_acp())
    server.wait(timeout=SERVER_STARTUP_TIMEOUT)
    yield server


@pytest.fixture(autouse=True)
def check_grpc_server_before_run(
    grpc_server: ControllableServerProtocol,
) -> Generator[None, None, None]:
    """Check if the server still responds before running each test, otherwise restart it."""
    try:
        grpc_server.wait(timeout=1.0)
    except RuntimeError:
        grpc_server.restart()
        grpc_server.wait(timeout=SERVER_STARTUP_TIMEOUT)
    yield


@pytest.fixture(autouse=True)
def clear_models_before_run(grpc_server):
    """Delete all existing models before the test is executed."""
    Client(server=grpc_server).clear()


@pytest.fixture
def load_model_from_tempfile(model_data_dir, grpc_server):
    @contextmanager
    def inner(relative_file_path="minimal_complete_model.acph5", format="acp:h5"):
        with tempfile.TemporaryDirectory() as tmp_dir:
            source_path = model_data_dir / relative_file_path
            client = Client(server=grpc_server)
            file_path = client.upload_file(source_path)
            yield client.import_model(path=file_path, format=format)

    return inner
