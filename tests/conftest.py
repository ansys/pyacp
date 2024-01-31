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
import pytest

from ansys.acp.core import (
    ACP,
    DirectLaunchConfig,
    DockerComposeLaunchConfig,
    LaunchMode,
    launch_acp,
)
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
def acp_instance(_configure_launcher) -> Generator[ACP, None, None]:
    """Provide the currently active gRPC server."""
    yield launch_acp(timeout=SERVER_STARTUP_TIMEOUT)


@pytest.fixture(autouse=True)
def check_grpc_server_before_run(
    acp_instance: ACP,
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
    def inner(relative_file_path="minimal_complete_model.acph5", format="acp:h5"):
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
