"""Pytest configuration file for ansys-acp-core tests."""
import os
import pathlib
import tempfile

import pytest
from ansys.acp.core import launch_acp_docker
from ansys.acp.core import shutdown_server
from ansys.acp.core import wait_for_server

__all__ = [
    "pytest_addoption",
    "grpc_server",
    "check_grpc_server_before_run",
    # "grpc_channel",
    # "model_data_dir",
    # "model_stub",
    "clear_models_before_run",  # TODO: add back
]

TEST_ROOT_DIR = pathlib.Path(__file__).parent

SERVER_BIN_OPTION_KEY = "--server-bin"
LICENSE_SERVER_OPTION_KEY = "--license-server"
NO_SERVER_LOGS_OPTION_KEY = "--no-server-log-files"

# Add pytest command-line options
def pytest_addoption(parser):
    """Add command-line options to pytest."""
    # parser.addoption(
    #     SERVER_BIN_OPTION_KEY,
    #     action="store",
    #     help="Path of the gRPC server executable",
    # )
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


@pytest.fixture(scope="session")
def _server_log_stdout(request):
    if request.config.getoption(NO_SERVER_LOGS_OPTION_KEY):
        return os.devnull
    return TEST_ROOT_DIR / "server_log_out.txt"


@pytest.fixture(scope="session")
def _server_log_stderr(request):
    if request.config.getoption(NO_SERVER_LOGS_OPTION_KEY):
        return os.devnull
    return TEST_ROOT_DIR / "server_log_err.txt"


def _get_option_required(request, option_name):
    option_value = request.config.getoption(option_name)
    assert option_value, f"The '{option_name}' option must be specified."
    return option_value


# gRPC server handling


@pytest.fixture
def grpc_server(_grpc_server_list):
    """Provide the currently active gRPC server."""
    yield _grpc_server_list[0]


@pytest.fixture(scope="session")
def _grpc_server_list(_start_grpc_server):
    """Start and terminate the grpc server.

    This fixture yields a one-element list containing the server resources.
    Tests may replace the resources, if they terminate the server.

    This is a performance optimization because starting a new server is
    expensive, mainly due to the license checkout.
    """
    res = [_start_grpc_server()]
    try:
        _wait_for_server(res[0])
        yield res
    finally:
        _stop_grpc_server(res[0])


@pytest.fixture(scope="session")
def _start_grpc_server(
    request,
    model_data_dir_external,
    model_data_dir,
    convert_temp_path,
    _server_log_stdout,
    _server_log_stderr,
):
    """Start the gRPC server."""

    def inner():
        tmp_dir = tempfile.gettempdir()
        return launch_acp_docker(
            license_server=_get_option_required(request, LICENSE_SERVER_OPTION_KEY),
            mount_directories={
                model_data_dir_external: model_data_dir,
                tmp_dir: convert_temp_path(tmp_dir),
            },
            stdout_file=_server_log_stdout,
            stderr_file=_server_log_stderr,
        )

    return inner


# @pytest.fixture(scope="session")
# def _grpc_server_exe(request):
#     """Provide the path to the grpc server executable."""
#     res_path = _get_option_required(request, SERVER_BIN_OPTION_KEY)
#     assert pathlib.Path(
#         res_path
#     ).is_file(), f"Could not find acp_grpcserver executable at '{res_path}'."
#     return res_path


def _stop_grpc_server(server):
    """Terminate the gRPC server."""
    shutdown_server(server)


def _wait_for_server(server, timeout=30.0):
    """Wait for the server to start, by calling the health-check endpoint."""
    wait_for_server(server, timeout=timeout)


@pytest.fixture
def _restart_grpc_server(_grpc_server_list, _start_grpc_server):
    def inner():
        _stop_grpc_server(_grpc_server_list[0])
        _grpc_server_list[0] = _start_grpc_server()
        _wait_for_server(_grpc_server_list[0])

    return inner


@pytest.fixture(autouse=True)
def check_grpc_server_before_run(grpc_server, _restart_grpc_server):
    """Check if the server still responds before running each test, otherwise restart it."""
    try:
        _wait_for_server(grpc_server, timeout=1)
    except RuntimeError:
        _restart_grpc_server()
    yield


@pytest.fixture(scope="session")
def model_data_dir_external(request):
    """Provides the path to the ACP test model data directory."""
    res_path = (TEST_ROOT_DIR / "acp_tests_common" / "data").resolve()
    assert res_path.is_dir(), f"Could not find data directory at '{res_path}'."
    return res_path


@pytest.fixture(scope="session")
def model_data_dir(request):
    """Provides the path to the ACP test model data directory."""
    return pathlib.PurePosixPath("/home/container/mounted_data")


@pytest.fixture(scope="session")
def convert_temp_path():
    def inner(external_path) -> str:
        base_tmp_path = pathlib.PurePosixPath("/tmp")
        relative_external_path = (
            pathlib.Path(external_path).relative_to(tempfile.gettempdir()).as_posix()
        )
        return str(base_tmp_path / relative_external_path)

    return inner


@pytest.fixture
def db_kwargs(grpc_server):
    return {"server": grpc_server}
