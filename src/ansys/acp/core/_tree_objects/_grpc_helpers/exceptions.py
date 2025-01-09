# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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

from collections.abc import Iterator
from contextlib import contextmanager

from grpc import RpcError, StatusCode

STATUS_CODE_TO_EXCEPTION_TYPE = {
    StatusCode.INVALID_ARGUMENT: ValueError,
    StatusCode.NOT_FOUND: LookupError,
    StatusCode.ALREADY_EXISTS: RuntimeError,
    StatusCode.DEADLINE_EXCEEDED: TimeoutError,
    StatusCode.PERMISSION_DENIED: PermissionError,
    StatusCode.UNAUTHENTICATED: PermissionError,
    StatusCode.FAILED_PRECONDITION: RuntimeError,
    StatusCode.OUT_OF_RANGE: LookupError,
    StatusCode.UNIMPLEMENTED: NotImplementedError,
    StatusCode.UNAVAILABLE: ConnectionError,
    StatusCode.DATA_LOSS: RuntimeError,
    StatusCode.ABORTED: RuntimeError,
    StatusCode.INTERNAL: RuntimeError,
    StatusCode.UNKNOWN: RuntimeError,
}


@contextmanager
def wrap_grpc_errors() -> Iterator[None]:
    """Wrap gRPC errors in Python exceptions.

    This context manager will catch gRPC errors and re-raise them as Python
    exceptions with simpler error messages. The original error message will
    still be available in the traceback.
    """
    try:
        yield
    except RpcError as exc:
        details = exc.details().split("\n", 1)[0].strip()
        exception_type = STATUS_CODE_TO_EXCEPTION_TYPE.get(exc.code(), RuntimeError)
        raise exception_type(details) from exc
