"""Pytest configuration file for ansys-acp-core tests."""
import pathlib
import socket
import subprocess
import time
from collections import namedtuple
from contextlib import closing

import grpc
import pytest
from ansys.api.acp.v0.base_pb2 import Empty as _pb_Empty
from ansys.api.acp.v0.model_pb2 import ModelRequest
from ansys.api.acp.v0.model_pb2_grpc import ModelStub
from grpc_health.v1.health_pb2 import HealthCheckRequest
from grpc_health.v1.health_pb2 import HealthCheckResponse
from grpc_health.v1.health_pb2_grpc import HealthStub

__all__ = [
    "pytest_addoption",
    "grpc_server",
    "check_grpc_server_before_run",
    "grpc_channel",
    "model_data_dir",
    "model_stub",
    "clear_models_before_run",
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
    yield _grpc_server_list[0].proc


@pytest.fixture(scope="session")
def _grpc_server_list(_grpc_server_exe, _grpc_server_port, _wait_for_server):
    """Start and terminate the grpc server.

    This fixture yields a one-element list containing the server resources.
    Tests may replace the resources, if they terminate the server.

    This is a performance optimization because starting a new server is
    expensive, mainly due to the license checkout.
    """
    res = [_start_grpc_server(_grpc_server_exe, _grpc_server_port, filemode="w")]
    try:
        _wait_for_server()
        yield res
    finally:
        _stop_grpc_server(res[0])


@pytest.fixture(scope="session")
def _grpc_server_exe(request):
    """Provide the path to the grpc server executable."""
    res_path = _get_option_required(request, SERVER_BIN_OPTION_KEY)
    assert pathlib.Path(
        res_path
    ).is_file(), f"Could not find acp_grpcserver executable at '{res_path}'."
    return res_path


@pytest.fixture(scope="session")
def _grpc_server_port():
    """Find a free port on localhost.

    Note that there is a race condition between finding the free port
    here, and binding to it from the gRPC server.
    """
    with closing(socket.socket()) as sock:
        sock.bind(("", 0))  # bind to a free port
        return sock.getsockname()[1]


_ServerResource = namedtuple("_ServerResource", ("proc", "stdout", "stderr"))


def _start_grpc_server(_grpc_server_exe, grpc_server_port, filemode="w"):
    """Start the gRPC server."""
    stdout = open(SERVER_LOG_FILE_STDOUT, mode=filemode, encoding="utf-8")
    stderr = open(SERVER_LOG_FILE_STDERR, mode=filemode, encoding="utf-8")
    sub_process = subprocess.Popen(
        [_grpc_server_exe, f"--server-address=0.0.0.0:{grpc_server_port}"],
        stdout=stdout,
        stderr=stderr,
    )
    return _ServerResource(proc=sub_process, stdout=stdout, stderr=stderr)


def _stop_grpc_server(server_resource):
    """Terminate the gRPC server."""
    server_resource.proc.terminate()
    server_resource.proc.wait()
    server_resource.stdout.write("\n====SERVER RESTART====\n")
    server_resource.stdout.close()
    server_resource.stderr.write("\n====SERVER RESTART====\n")
    server_resource.stderr.close()


@pytest.fixture(scope="session")
def _wait_for_server(_grpc_server_port):
    """Wait for the server to start, by calling the health-check endpoint."""

    def inner(timeout=20):
        start_time = time.time()
        channel = _get_grpc_channel(_grpc_server_port)
        while time.time() - start_time <= timeout:
            try:
                res = HealthStub(channel).Check(
                    # The empty HealthCheckRequest is served by the default health
                    # check service.
                    request=HealthCheckRequest(),
                    timeout=timeout / 3,
                )
                if res.status == HealthCheckResponse.ServingStatus.SERVING:
                    break
            except grpc.RpcError:
                # Try again until the timeout is reached. We add a small
                # delay s.t. the server isn't bombarded with requests.
                time.sleep(timeout / 100)
        else:
            raise RuntimeError(
                f"The gRPC server is not serving requests {timeout}s after starting."
            )

    return inner


def _get_grpc_channel(grpc_server_port):
    return grpc.insecure_channel(f"localhost:{grpc_server_port}")


@pytest.fixture
def _restart_grpc_server(_grpc_server_list, _grpc_server_exe, _grpc_server_port, _wait_for_server):
    def inner():
        _stop_grpc_server(_grpc_server_list[0])
        _grpc_server_list[0] = _start_grpc_server(_grpc_server_exe, _grpc_server_port)
        _wait_for_server()

    return inner


@pytest.fixture(autouse=True)
def check_grpc_server_before_run(_wait_for_server, _restart_grpc_server):
    """Check if the server still responds before running each test, otherwise restart it."""
    try:
        _wait_for_server(timeout=1)
    except RuntimeError:
        _restart_grpc_server()
    yield


@pytest.fixture
def grpc_channel(grpc_server, _grpc_server_port):
    """Provide a channel connecting to the grpc server."""
    yield _get_grpc_channel(_grpc_server_port)


@pytest.fixture(autouse=True)
def clear_models_before_run(grpc_channel):
    """Delete all existing models before the test is executed."""
    model_stub = ModelStub(grpc_channel)
    for model in model_stub.List(_pb_Empty()).models:
        model_stub.Delete(ModelRequest(resource_path=model.info.resource_path))
