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

from __future__ import annotations

from typing import Protocol

import grpc

from .._utils.typing_helper import StrEnum

__all__ = ["LaunchMode"]


class ServerKey(StrEnum):
    MAIN = "main"
    FILE_TRANSFER = "file_transfer"


class LaunchMode(StrEnum):
    """Available launch modes for ACP."""

    DIRECT = "direct"
    DOCKER_COMPOSE = "docker_compose"
    CONNECT = "connect"


class ServerProtocol(Protocol):
    """Interface definition for ACP gRPC servers."""

    @property
    def channels(self) -> dict[str, grpc.Channel]: ...

    def check(self, timeout: float | None = None) -> bool: ...

    def wait(self, timeout: float) -> None: ...


class ControllableServerProtocol(ServerProtocol, Protocol):
    """Interface definition for ACP servers which can be remotely started / stopped."""

    def start(self) -> None: ...

    def stop(self, *, timeout: float | None = None) -> None: ...

    def restart(self, *, stop_timeout: float | None = None) -> None: ...
