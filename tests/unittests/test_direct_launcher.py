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

import pytest

import ansys.acp.core as pyacp
from ansys.acp.core._server.direct import DirectLauncher


def test_inexistent_binary_error():
    """Check that the right error is raised when the binary does not exist."""
    with pytest.raises(FileNotFoundError) as exc:
        pyacp.launch_acp(
            launch_mode=pyacp.LaunchMode.DIRECT,
            config=pyacp.DirectLaunchConfig(binary_path="inexistent_path"),
        )
    assert "Binary not found" in str(exc.value)


def test_stop_after_failed_start():
    """Check that the .stop() method works after a failed start.

    This test is necessary because the '.stop()' method is called on teardown
    even if the '.start()' method fails.
    In the 'test_inexistent_binary_error' test, errors in '.stop()' are not
    captured because they happen after the test ends.
    """
    launcher = DirectLauncher(config=pyacp.DirectLaunchConfig(binary_path="inexistent_path"))
    with pytest.raises(FileNotFoundError):
        launcher.start()
    launcher.stop()
