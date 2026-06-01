# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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

from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor
import copy
import os
import subprocess
import sys

import docker
import pytest

import ansys.acp.core as pyacp

from ..conftest import (
    BUILD_BENCHMARK_IMAGE_OPTION_KEY,
    DOCKER_IMAGENAME_OPTION_KEY,
    LICENSE_SERVER_OPTION_KEY,
    SERVER_STARTUP_TIMEOUT,
    SERVER_STOP_TIMEOUT,
    SOURCE_ROOT_DIR,
    TEST_ROOT_DIR,
    VALIDATE_BENCHMARKS_ONLY_OPTION_KEY,
)

BENCHMARK_IMAGE_NAME = "pyacp-benchmark-runner"


def pytest_ignore_collect(collection_path, config):
    # The benchmarks can only be run on Linux, since the 'tc-netem' tool
    # used for manipulating network speeds is not available on Docker for
    # Windows / Mac.
    if sys.platform != "linux":
        return True
    # The benchmarks make use of the 'ConnectionTest.Dockerfile' and
    # 'docker-compose-benchmark.yaml', so can only be used with the
    # docker-compose launcher.
    if not config.getoption(LICENSE_SERVER_OPTION_KEY):
        return True
    return False


@pytest.fixture(scope="session")
def launcher_configuration(request):
    if request.config.getoption(BUILD_BENCHMARK_IMAGE_OPTION_KEY):
        base_image_name = request.config.getoption(DOCKER_IMAGENAME_OPTION_KEY)

        docker.from_env().images.pull(base_image_name)

        dockerfiles_dir = SOURCE_ROOT_DIR / "dockerfiles"
        benchmark_dockerfile = dockerfiles_dir / "ConnectionTest.Dockerfile"

        build_env = copy.deepcopy(os.environ)
        build_env.update({"DOCKER_BUILDKIT": "1"})
        # Currently the Python Docker SDK does not support using BuildKit, so we need
        # to use the command line. See https://github.com/docker/docker-py/issues/2230
        subprocess.check_output(
            [
                "docker",
                "build",
                "--tag",
                BENCHMARK_IMAGE_NAME,
                "-f",
                benchmark_dockerfile,
                dockerfiles_dir,
            ],
            env=build_env,
        )

    # check that the benchmark image exists
    docker.from_env().images.get(name=BENCHMARK_IMAGE_NAME)

    image_name_filetransfer = "ghcr.io/ansys/tools-filetransfer:latest"
    docker.from_env().images.pull(image_name_filetransfer)

    license_server = request.config.getoption(LICENSE_SERVER_OPTION_KEY)

    return pyacp.DockerComposeLaunchConfig(
        image_name_acp=BENCHMARK_IMAGE_NAME,
        image_name_filetransfer=image_name_filetransfer,
        compose_file=SOURCE_ROOT_DIR / "docker-compose" / "docker-compose-benchmark.yaml",
        license_server=license_server,
        keep_volume=False,
        certs_dir=TEST_ROOT_DIR / "insecure_certs",
    )


ServerNetworkOptions = namedtuple("ServerNetworkOptions", ["delay_ms", "rate_kbit"])

VALIDATE_BENCHMARK_NETWORK_OPTION = ServerNetworkOptions(delay_ms=0, rate_kbit=1e6)

NETWORK_OPTIONS = [
    ServerNetworkOptions(delay_ms=0, rate_kbit=1e6),
    ServerNetworkOptions(delay_ms=1, rate_kbit=1e6),
    ServerNetworkOptions(delay_ms=10, rate_kbit=1e6),
    ServerNetworkOptions(delay_ms=100, rate_kbit=1e6),
    ServerNetworkOptions(delay_ms=0, rate_kbit=1e4),
    ServerNetworkOptions(delay_ms=0, rate_kbit=1e3),
    ServerNetworkOptions(delay_ms=0, rate_kbit=1e2),
]


@pytest.fixture(scope="session")
def _benchmark_servers(launcher_configuration):
    # Use a ThreadPoolExecutor to start and stop all servers simultaneously
    executor = ThreadPoolExecutor(max_workers=len(NETWORK_OPTIONS))

    def launch_benchmark_server(network_options):
        conf = copy.deepcopy(launcher_configuration)
        conf.environment_variables = {
            "PYACP_DELAY": f"{network_options.delay_ms}ms",
            "PYACP_RATE": f"{network_options.rate_kbit}kbit",
        }
        for num_retries in reversed(range(2)):
            try:
                acp = pyacp.launch_acp(config=conf, launch_mode=pyacp.LaunchMode.DOCKER_COMPOSE)
                acp.wait(SERVER_STARTUP_TIMEOUT)
                break
            except subprocess.CalledProcessError as e:
                if num_retries == 0:
                    raise e
        return acp

    servers_list = list(executor.map(launch_benchmark_server, NETWORK_OPTIONS))

    yield {
        network_options: server for (network_options, server) in zip(NETWORK_OPTIONS, servers_list)
    }

    # convert to list to wait until all servers are stopped
    list(executor.map(lambda server: server.stop(timeout=SERVER_STOP_TIMEOUT), servers_list))


@pytest.fixture(
    params=NETWORK_OPTIONS,
    ids=lambda options: f"delay={options.delay_ms}ms, rate={options.rate_kbit}kbit",
)
def network_options(request):
    options = request.param
    if request.config.getoption(VALIDATE_BENCHMARKS_ONLY_OPTION_KEY):
        if options != VALIDATE_BENCHMARK_NETWORK_OPTION:
            pytest.skip(
                "Skipping benchmarks for slower network options since "
                f"'{VALIDATE_BENCHMARKS_ONLY_OPTION_KEY}' is specified."
            )
    return request.param


@pytest.fixture
def acp_instance(_benchmark_servers, network_options):
    return _benchmark_servers[network_options]
