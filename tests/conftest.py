"""Pytest configuration file for ansys-acp-core tests."""
import pathlib
import time

import pytest
from ansys.acp.core import launch_acp

__all__ = [
    "pytest_addoption",
    "grpc_server",
    "check_grpc_server_before_run",
    # "grpc_channel",
    # "model_data_dir",
    # "model_stub",
    "clear_models_before_run",  # TODO: add back
]

SERVER_LOG_FILE_STDOUT = pathlib.Path(__file__).parent / "server_log_out.txt"
SERVER_LOG_FILE_STDERR = pathlib.Path(__file__).parent / "server_log_err.txt"

SERVER_BIN_OPTION_KEY = "--server-bin"

# Add pytest command-line options
def pytest_addoption(parser):
    """Add command-line options to pytest."""
    parser.addoption(
        SERVER_BIN_OPTION_KEY,
        action="store",
        help="Path of the gRPC server executable",
    )


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
def _grpc_server_list(_grpc_server_exe):
    """Start and terminate the grpc server.

    This fixture yields a one-element list containing the server resources.
    Tests may replace the resources, if they terminate the server.

    This is a performance optimization because starting a new server is
    expensive, mainly due to the license checkout.
    """
    res = [_start_grpc_server(_grpc_server_exe)]
    try:
        _wait_for_server(res[0])
        yield res
    finally:
        _stop_grpc_server(res[0])


def _start_grpc_server(_grpc_server_exe):
    """Start the gRPC server."""
    return launch_acp(
        _grpc_server_exe, stdout_file=SERVER_LOG_FILE_STDOUT, stderr_file=SERVER_LOG_FILE_STDERR
    )


@pytest.fixture(scope="session")
def _grpc_server_exe(request):
    """Provide the path to the grpc server executable."""
    res_path = _get_option_required(request, SERVER_BIN_OPTION_KEY)
    assert pathlib.Path(
        res_path
    ).is_file(), f"Could not find acp_grpcserver executable at '{res_path}'."
    return res_path


def _stop_grpc_server(server):
    """Terminate the gRPC server."""
    server.stdout.write("\n====SERVER RESTART====\n")
    server.stderr.write("\n====SERVER RESTART====\n")
    server.close()


def _wait_for_server(server, timeout=10.0):
    """Wait for the server to start, by calling the health-check endpoint."""
    start_time = time.time()
    while time.time() - start_time <= timeout:
        if server.check(timeout=timeout / 3.0):
            break
        else:
            # Try again until the timeout is reached. We add a small
            # delay s.t. the server isn't bombarded with requests.
            time.sleep(timeout / 100)
    else:
        raise RuntimeError(f"The gRPC server is not serving requests {timeout}s after starting.")


@pytest.fixture
def _restart_grpc_server(_grpc_server_list, _grpc_server_exe):
    def inner():
        _stop_grpc_server(_grpc_server_list[0])
        _grpc_server_list[0] = _start_grpc_server(_grpc_server_exe)
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
