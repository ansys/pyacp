"""Pytest configuration file for ansys-acp-core tests."""
from contextlib import contextmanager
from dataclasses import dataclass
import os
import pathlib
import shutil
import tempfile
from typing import Callable, Generator, List

import pytest

from ansys.acp.core import Client, launch_acp, launch_acp_docker, shutdown_server, wait_for_server
from ansys.acp.core._server import ServerProtocol
from ansys.acp.core._typing_helper import PATH

__all__ = [
    "pytest_addoption",
    "model_data_dir_server",
    "model_data_dir_host",
    "convert_temp_path",
    "grpc_server",
    "check_grpc_server_before_run",
    "clear_models_before_run",
    "load_model_from_tempfile",
]

TEST_ROOT_DIR = pathlib.Path(__file__).parent

SERVER_BIN_OPTION_KEY = "--server-bin"
LICENSE_SERVER_OPTION_KEY = "--license-server"
NO_SERVER_LOGS_OPTION_KEY = "--no-server-log-files"
SERVER_STARTUP_TIMEOUT = 30.0

# Add pytest command-line options
def pytest_addoption(parser: pytest.Parser) -> None:
    """Add command-line options to pytest."""
    parser.addoption(
        SERVER_BIN_OPTION_KEY,
        action="store",
        help="Path of the gRPC server executable",
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


@dataclass
class _Config:
    server_launcher: Callable[[], ServerProtocol]
    temp_path_converter: Callable[[PATH], str]
    model_data_dir_server: pathlib.PurePath


@pytest.fixture(scope="session")
def _test_config(request: pytest.FixtureRequest, model_data_dir_host: PATH) -> _Config:
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

        _model_data_dir_server: pathlib.PurePath = pathlib.Path(model_data_dir_host)

        def _convert_temp_path(external_path: PATH) -> str:
            return str(external_path)

        def _launch_server() -> ServerProtocol:
            return launch_acp(
                binary_path=server_bin,
                stdout_file=server_log_stdout,
                stderr_file=server_log_stderr,
            )

    else:
        # If no binary is provided, use the Docker container for running
        # the ACP server.
        _model_data_dir_server = pathlib.PurePosixPath("/home/container/mounted_data")

        def _convert_temp_path(external_path: PATH) -> str:
            base_tmp_path = pathlib.PurePosixPath("/tmp")
            relative_external_path = (
                pathlib.Path(external_path).relative_to(tempfile.gettempdir()).as_posix()
            )
            return str(base_tmp_path / relative_external_path)

        def _launch_server() -> ServerProtocol:
            tmp_dir = tempfile.gettempdir()
            return launch_acp_docker(
                license_server=license_server,
                mount_directories={
                    str(model_data_dir_host): str(_model_data_dir_server),
                    tmp_dir: _convert_temp_path(tmp_dir),
                },
                stdout_file=server_log_stdout,
                stderr_file=server_log_stderr,
            )

    return _Config(
        server_launcher=_launch_server,
        temp_path_converter=_convert_temp_path,
        model_data_dir_server=_model_data_dir_server,
    )


@pytest.fixture(scope="session")
def model_data_dir_host() -> pathlib.Path:
    """Test data path, in the host filesystem."""
    res_path = (TEST_ROOT_DIR / "data").resolve()
    assert res_path.is_dir(), f"Could not find data directory at '{res_path}'."
    return res_path


@pytest.fixture(scope="session")
def model_data_dir_server(_test_config: _Config) -> pathlib.PurePath:
    """Test data path, in the server filesystem."""
    return _test_config.model_data_dir_server


@pytest.fixture(scope="session")
def convert_temp_path(_test_config: _Config) -> Callable[[PATH], str]:
    """Convert temporary paths from the host to the server filesystem."""
    return _test_config.temp_path_converter


@pytest.fixture
def grpc_server(_grpc_server_list: List[ServerProtocol]) -> Generator[ServerProtocol, None, None]:
    """Provide the currently active gRPC server."""
    yield _grpc_server_list[0]


@pytest.fixture(scope="session")
def _grpc_server_list(
    _start_grpc_server: Callable[[], ServerProtocol]
) -> Generator[List[ServerProtocol], None, None]:
    """Start and terminate the grpc server.

    This fixture yields a one-element list containing the server resources.
    Tests may replace the resources, if they terminate the server.

    This is a performance optimization because starting a new server is
    expensive, mainly due to the license checkout.
    """
    res = [_start_grpc_server()]
    try:
        wait_for_server(res[0], timeout=SERVER_STARTUP_TIMEOUT)
        yield res
    finally:
        shutdown_server(res[0])


@pytest.fixture(scope="session")
def _start_grpc_server(_test_config: _Config) -> Callable[[], ServerProtocol]:
    """Start the gRPC server."""
    return _test_config.server_launcher


@pytest.fixture
def _restart_grpc_server(
    _grpc_server_list: List[ServerProtocol], _start_grpc_server: Callable[[], ServerProtocol]
) -> Callable[[], None]:
    def inner() -> None:
        shutdown_server(_grpc_server_list[0])
        _grpc_server_list[0] = _start_grpc_server()
        wait_for_server(_grpc_server_list[0], timeout=SERVER_STARTUP_TIMEOUT)

    return inner


@pytest.fixture(autouse=True)
def check_grpc_server_before_run(
    grpc_server: ServerProtocol, _restart_grpc_server: Callable[[], None]
) -> Generator[None, None, None]:
    """Check if the server still responds before running each test, otherwise restart it."""
    try:
        wait_for_server(grpc_server, timeout=1.0)
    except RuntimeError:
        _restart_grpc_server()
    yield


@pytest.fixture(autouse=True)
def clear_models_before_run(grpc_server):
    """Delete all existing models before the test is executed."""
    Client(server=grpc_server).clear()


@pytest.fixture
def load_model_from_tempfile(model_data_dir_host, grpc_server, convert_temp_path):
    @contextmanager
    def inner(relative_file_path="minimal_complete_model.acph5", format="acp:h5"):
        with tempfile.TemporaryDirectory() as tmp_dir:
            dest_path = pathlib.Path(tmp_dir) / os.path.basename(relative_file_path)
            source_path = model_data_dir_host / relative_file_path
            shutil.copyfile(source_path, dest_path)

            client = Client(server=grpc_server)
            yield client.import_model(path=convert_temp_path(dest_path), format=format)

    return inner
